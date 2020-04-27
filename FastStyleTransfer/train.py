import tensorflow as tf
import numpy as np
import PIL.Image
import os

from utils import tensor_to_image, load_batch_image
from models import StyleContentModel, TransformModel, _gram_matrix, _get_total_variation_loss

# layer 설정
# Content layer where will pull our feature maps
content_layers = ['block4_conv2'] 

# Style layer of interest
style_layers = ['block1_conv1',
                'block2_conv1',
                'block3_conv1', 
                'block4_conv1', 
                'block5_conv1']

num_content_layers = len(content_layers)
num_style_layers = len(style_layers)


# loss function
def style_content_loss(content_output, style_output, transform_output, transform_image):
    content_image_features = content_output['content'] # content featur of content image
    transform_content_features = transform_output['content'] # content feature of transform image
    style_image_features = style_output['style'] # style feature of style image
    transform_style_features = transform_output['style'] # style feature of transform image
    
    # Content Loss
    L_content = 0
    for idx in content_layers:
        F = transform_content_features[idx]  # content feature of transform image
        P = content_image_features[idx]  # content feature of content image
        
        b, h, w, d = transform_content_features[idx].get_shape()
        N = h*w
        M = d
        
        w = 1.0
        
        L_content += w * 2 * tf.nn.l2_loss(F-P) / (b*N*M)
    
    # Style Loss
    L_style = 0
    for idx in style_layers:
        F = transform_style_features[idx] # style feature of transform image
        A = style_image_features[idx] # style feature of style image
        
        b, h, w, d = F.get_shape()
        N = h*w
        M = d
        
        w = 0.2
        G = _gram_matrix(F, (b,N,M))
        A = _gram_matrix(A)
        
        L_style += w * 2 * tf.nn.l2_loss(G-A) / (b * (M ** 2))
    
    # total variation loss
    L_tv = _get_total_variation_loss(transform_image)
    
    # Total Loss
    L_total = 7.5e0*L_content + 5e2*L_style + 2e2*L_tv
    
    return L_total, L_content, L_style, L_tv

def train_step(content_image, style_image, extractor, transfer_model, opt): 
    with tf.GradientTape() as tape:
        original_image = content_image / 255.  # [0, 1.]
        transform_image = transfer_model(original_image) # 이미지 생성 [0, 255.]
        
        transform_image_outputs = extractor(transform_image) # 생성된 이미지의 feature
        content_image_outputs = extractor(content_image) # content image의 feature
        style_image_outputs = extractor(style_image) # style image의 feature
        
        L_total, L_content, L_style, L_tv = style_content_loss(content_image_outputs, style_image_outputs, transform_image_outputs, transform_image)
    
    transformer_grad = tape.gradient(L_total, transfer_model.trainable_variables) # loss를 기반으로 image를 학습시킴
    opt.apply_gradients(zip(transformer_grad, transfer_model.trainable_variables))
    
    return L_total, L_content, L_style, L_tv

def train(content_image_path, style_image_path, model_save_path, extractor, model, opt):
    
    # model 저장 폴더 생성
    if not os.path.exists(model_save_path):
        os.mkdir(model_save_path)
    
    # 학습 중간과정 결과 이미지 저장 폴더 생성
    if not os.path.exists(model_save_path+'result'):
        os.mkdir(model_save_path+'result')

        
    ckpt = tf.train.Checkpoint(step=tf.Variable(0), optimizer=opt, net=model)
    manager = tf.train.CheckpointManager(ckpt, './'+model_save_path, max_to_keep=3)
    ckpt.restore(manager.latest_checkpoint)
    
    if manager.latest_checkpoint:
        transfer_model = ckpt.net  # ckpt 파일이 존재한다면 불러와서 사용
        opt = ckpt.optimizer
        print("Restored from {}".format(manager.latest_checkpoint))
    else:
        transfer_model = model  # ckpt 모델이 없으면 초기에 만든 모델 사용
        opt = opt
        print("Initializing from scratch.")
    
    # load style image
    style_image = PIL.Image.open(style_image_path)
    style_image = np.array(style_image, dtype=np.float32)
    style_image = np.expand_dims(style_image, axis=0)
    
    # Load test image
    test_image = PIL.Image.open(content_image_path)
    test_image = np.array(test_image, dtype=np.float32)
    test_image = np.expand_dims(test_image, axis=0)
    
    # Load train imageset
    coco_len = len(os.listdir('./train2014'))
    coco_len -= coco_len % BATCH_SIZE
    epoch_start = ckpt.step // coco_len
    
    
    for epoch in range(epoch_start, EPOCHS):
        while (ckpt.step - epoch * coco_len) + BATCH_SIZE <= coco_len:
            content_image = load_batch_image((ckpt.step - epoch * coco_len), BATCH_SIZE)
            L_total, L_content, L_style, L_tv = train_step(content_image, style_image, extractor, transfer_model, opt)
            
            ckpt.step.assign_add(BATCH_SIZE)    
            print('epoch : %d, iter : %4d, ' % (epoch, ckpt.step),'L_total : %g, L_content : %g, L_style : %g, L_tv : %g' % (L_total, L_content, L_style, L_tv))
            if ckpt.step % 1000 == 0:
                save_path = manager.save()
                print("Saved checkpoint for step {}: {}".format(int(ckpt.step), save_path))
            if ckpt.step % 2000 == 0:
                # save result image
                with tf.device('/cpu:0'):
                    image = transfer_model(test_image/255.)
                    image = tensor_to_image(image)
                    image.save('./'+model_save_path+'result/'+str(int(ckpt.step))+'.jpg')
                
        # 남은거 처리
        # content_image = load_batch_image((ckpt.step - epoch * coco_len), coco_len - (ckpt.step - epoch_start * coco_len))
        # L_total, L_content, L_style, L_tv = train_step(content_image, style_image, extractor, transfer_model, opt)
        # ckpt.step.assign_add(coco_len - (ckpt.step - epoch_start * coco_len))
        
        # print('epoch : %d, iter : %4d, ' % (epoch, ckpt.step),'L_total : %g, L_content : %g, L_style : %g, L_tv : %g' % (L_total, L_content, L_style, L_tv))
        # save_path = manager.save()
        # print("Saved checkpoint for step {}: {}".format(int(ckpt.step), save_path))


if __name__ == "__main__":
    # 파라미터 
    BATCH_SIZE = 4
    EPOCHS = 2  
    opt = tf.keras.optimizers.Adam(learning_rate=1e-3)

    # model
    extractor = StyleContentModel(style_layers, content_layers)
    transfer = TransformModel()

    # train(content image path, style image path, 저장할 모델 폴더 이름, Style과 Content feature를 뽑을 모델, 이미지 변환 모델, 최적화)
    train('./content/europe.jpg', './style/Kandinsky.jpg', 'Kandinsky_models', extractor, transfer, opt)