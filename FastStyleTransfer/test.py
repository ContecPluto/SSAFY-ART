from utils import tensor_to_image, load_batch_image
import tensorflow as tf
import time
import PIL.Image
import numpy as np
import os

from utils import tensor_to_image, load_batch_image
from models import TransformModel

if __name__ == "__main__":
    model_save_path = 'the_scream_models'
    model = TransformModel()
    transfer = TransformModel()
    ckpt = tf.train.Checkpoint(step=tf.Variable(0), net=model)
    manager = tf.train.CheckpointManager(ckpt, './'+model_save_path, max_to_keep=3)
    ckpt.restore(manager.latest_checkpoint)

    start = time.time()
    model = ckpt.net
    for image_name in os.listdir('./content'):
        test_image = PIL.Image.open('./content/' + image_name)
        test_image = np.array(test_image, dtype=np.float32)
        test_image = np.expand_dims(test_image, axis=0)

        with tf.device('/cpu:0'):
            image = tensor_to_image(model(test_image))
            image.save(image_name+'_transform.jpg')
    end = time.time()

    print(end-start)
