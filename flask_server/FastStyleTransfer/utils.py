import tensorflow as tf
import numpy as np
import PIL.Image
import os

def tensor_to_image(tensor):
  tensor = np.array(tensor, dtype=np.uint8)
  if np.ndim(tensor) > 3:
    assert tensor.shape[0] == 1
    tensor = tensor[0]
  return PIL.Image.fromarray(tensor)

# 데이터 로드
def load_batch_image(start_idx, batch_size):
    train_list = os.listdir('./train2014')
    batch_images = np.zeros([batch_size, 256, 256, 3], dtype=np.float32)
    for i in range(batch_size):
        img = PIL.Image.open('./train2014/' + train_list[start_idx+i])
        img = img.resize((256, 256))
        img = np.array(img, dtype=np.float32)
        if not (len(img.shape) == 3 and img.shape[2] == 3):
            img = np.dstack((img, img, img))
        batch_images[i] = np.array(img, dtype=np.float32)

    return batch_images