import tensorflow as tf
from .utils import tensor_to_image
from .models import TransformModel
import PIL
import numpy as np
import IPython.display as display
import time
from datetime import datetime
import os


def tensor_to_image(tensor):
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return PIL.Image.fromarray(tensor)


def FastStyleTransfer(image_type, image_path):
    opt = tf.keras.optimizers.Adam(learning_rate=1e-3)
    train = TransformModel()
    model_save_path = os.getcwd() + '/FastStyleTransfer/' + image_type
    ckpt = tf.train.Checkpoint(step=tf.Variable(0), optimizer=opt, net=train)
    manager = tf.train.CheckpointManager(
        ckpt, model_save_path, max_to_keep=3)
    ckpt.restore(manager.latest_checkpoint)
    net = ckpt.net
    image = PIL.Image.open(image_path)
    image = np.array(image, dtype=np.float32)
    image = np.expand_dims(image, axis=0)
    with tf.device('/cpu:0'):
        train = TransformModel()
        styles = net(image)
    image = tensor_to_image(styles)
    time = str(datetime.now().hour) + str(datetime.now().minute) + \
        str(datetime.now().second)
    result_name = f'result_{time}.jpg'
    UPLOAD_URL = os.getcwd() + '/static/faststyletransfer/result/' + result_name
    image.save(UPLOAD_URL)
    return result_name
