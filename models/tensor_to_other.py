import numpy as np
from PIL import Image
import cv2


def tensor_to_pil(tensor):
    return Image.fromarray(np.uint8((tensor.numpy())[0] * 255))


def tensor_to_array(tensor):
    return tensor.numpy()


def pil_to_cv2(pil):
    return cv2.cvtColor(numpy.asarray(pil), cv2.COLOR_RGB2BGR)
