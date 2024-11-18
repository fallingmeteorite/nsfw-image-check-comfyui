import numpy as np
from PIL import Image
from torchvision import transforms
import cv2


def tensor_to_pil(tensor):
    return Image.fromarray(np.uint8((tensor.numpy())[0] * 255))


def tensor_to_array(tensor):
    return tensor.numpy()


def pil_to_cv2(pil):
    return cv2.cvtColor(np.asarray(pil), cv2.COLOR_RGB2BGR)


def pil_to_tensor(pil):
    to_pil = transforms.ToTensor()(pil)
    to_pil = to_pil.squeeze(0).permute(1, 2, 0)
    to_pil = to_pil.unsqueeze(0)
    return to_pil
