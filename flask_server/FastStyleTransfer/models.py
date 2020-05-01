import tensorflow as tf
import tensorflow_addons as tfa
import numpy as np
import PIL.Image

# model function

def _instance_norm(net):
    batch, rows, cols, channels = net.get_shape()
    var_shape = [channels]
    mu, sigma_sq = tf.nn.moments(net, [1,2], keepdims=True)
    
    shift = tf.Variable(initial_value=tf.zeros(var_shape), dtype=tf.float32)
    scale = tf.Variable(initial_value=tf.ones(var_shape), dtype=tf.float32)
    epsilon = 1e-3
    normalized = (net-mu)/(sigma_sq + epsilon)**(.5)
    return scale * normalized + shift

def _conv_layer(inputs, num_filters, kernel_size, strides, padding='same', relu=True):
    net = tf.keras.layers.Conv2D(num_filters, kernel_size, strides=(strides, strides), padding=padding)(inputs)
    net = tfa.layers.InstanceNormalization()(net)
#     net = _instance_norm(net)
    if relu:
        net = tf.keras.layers.ReLU()(net)
    return net

def _conv_transpose_layer(inputs, num_filters, kernel_size, strides):
    net = tf.keras.layers.Conv2DTranspose(num_filters, kernel_size, strides=(strides, strides), padding='same')(inputs)
    net = tfa.layers.InstanceNormalization()(net)
#     net = _instance_norm(net)
    return tf.keras.layers.ReLU()(net)

def _residual_block(net, kernel_size=3):
    batch, rows, cols, channels = tf.shape(net)
    tmp = _conv_layer(net, 128, kernel_size, 1, padding='valid', relu=True)
    shape = tf.shape(net)
#     return _conv_layer(tmp, 128, kernel_size, 1, padding='valid', relu=False) + tf.slice(net, [0,2,2,0], [batch,rows-4,cols-4,channels])
    return _conv_layer(tmp, 128, kernel_size, 1, padding='valid', relu=False) + tf.slice(net, [0,2,2,0], [shape[0],shape[1]-4,shape[2]-4,shape[3]])

def _gram_matrix(tensor, shape=None):
    if shape is not None:
        B = shape[0]  # batch size
        HW = shape[1] # height x width
        C = shape[2]  # channels
        CHW = C*HW
    else:
        B, H, W, C = tensor.get_shape()
        HW = H*W
        CHW = W*H*C

    # reshape the tensor so it is a (B, 2-dim) matrix
    # so that 'B'th gram matrix can be computed
    feats = tf.reshape(tensor, (B, HW, C))

    # leave dimension of batch as it is
    feats_T = tf.transpose(feats, perm=[0, 2, 1])

    # paper suggests to normalize gram matrix by its number of elements
    gram = tf.matmul(feats_T, feats) / CHW

    return gram

def _get_total_variation_loss(img):
    b, h, w, d = img.get_shape()
    tv_y_size = (h-1) * w * d
    tv_x_size = h * (w-1) * d
    y_tv = tf.nn.l2_loss(img[:, 1:, :, :] - img[:, :img.shape[1] - 1, :, :])
    x_tv = tf.nn.l2_loss(img[:, :, 1:, :] - img[:, :, :img.shape[2] - 1, :])
    loss = 2. * (x_tv / tv_x_size + y_tv / tv_y_size) / b

    loss = tf.cast(loss, tf.float32)
    return loss


# vgg model
def vgg_layers(layer_names):
    vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
    vgg.trainable = False
    
    outputs = [vgg.get_layer(name).output for name in layer_names]
    
    model = tf.keras.Model(inputs=[vgg.input], outputs=outputs)
    return model

class StyleContentModel(tf.keras.models.Model):
    def __init__(self, style_layers, content_layers):
        super(StyleContentModel, self).__init__()
        self.vgg = vgg_layers(style_layers + content_layers)
        self.style_layers = style_layers # 5
        self.content_layers = content_layers # 1
        self.num_style_layers = len(style_layers)
        self.vgg.trainable = False
        
    def call(self, inputs):
        preprocessed_input = tf.keras.applications.vgg19.preprocess_input(inputs)
        outputs = self.vgg(preprocessed_input)
        style_outputs, content_outputs = outputs[:self.num_style_layers], outputs[self.num_style_layers:]
        
        content_dict = {content_name:value for content_name, value in zip(self.content_layers, content_outputs)}
        style_dict = {style_name:value for style_name, value in zip(self.style_layers, style_outputs)}
        
        return {'content': content_dict, 'style':style_dict}

# Transform model
def TransformModel():
    input_n = tf.keras.Input(shape=(None, None, 3), dtype=tf.float32)
    image_p = tf.pad(input_n,[[0, 0],[40, 40],[40, 40], [0, 0]], "REFLECT")
    conv1 = _conv_layer(image_p, 32, 9, 1)
    conv2 = _conv_layer(conv1, 64, 3, 2)
    conv3 = _conv_layer(conv2, 128, 3, 2)

    resid1 = _residual_block(conv3, 3)
    resid2 = _residual_block(resid1, 3)
    resid3 = _residual_block(resid2, 3)
    resid4 = _residual_block(resid3, 3)
    resid5 = _residual_block(resid4, 3)

    conv_t1 = _conv_transpose_layer(resid5, 64, 3, 2)
    conv_t2 = _conv_transpose_layer(conv_t1, 32, 3, 2)
    conv_t3 = _conv_layer(conv_t2, 3, 9, 1, relu=False)
    
    activ = tf.keras.activations.tanh(conv_t3)
    preds = (activ + 1) * (255. / 2)
    
    model = tf.keras.Model(inputs=input_n, outputs=preds)
    return model

