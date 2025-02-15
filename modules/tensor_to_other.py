import cv2
import numpy as np
from PIL import Image
from torch import Tensor
from torchvision import transforms


def tensor_to_pil(tensor: Tensor) -> Image.Image:
    """
    Convert a tensor to a PIL image.

    Parameters:
    tensor (Tensor): Input tensor containing image data.

    Returns:
    Image.Image: Output PIL image.
    """
    # Convert tensor to numpy array and scale to [0, 255]
    array = (tensor.numpy()[0] * 255).astype(np.uint8)
    return Image.fromarray(array)


def tensor_to_array(tensor: Tensor) -> np.ndarray:
    """
    Convert a tensor to a numpy array.

    Parameters:
    tensor (Tensor): Input tensor containing image data.

    Returns:
    np.ndarray: Output numpy array.
    """
    return tensor.numpy()


def pil_to_cv2(pil: Image.Image) -> np.ndarray:
    """
    Convert a PIL image to a CV2 image.

    Parameters:
    pil (Image.Image): Input PIL image.

    Returns:
    np.ndarray: Output CV2 image in BGR format.
    """
    # Convert PIL image to numpy array and change color space to BGR
    return cv2.cvtColor(np.asarray(pil), cv2.COLOR_RGB2BGR)


def pil_to_tensor(pil: Image.Image) -> Tensor:
    """
    Convert a PIL image to a tensor.

    Parameters:
    pil (Image.Image): Input PIL image.

    Returns:
    Tensor: Output tensor containing image data.
    """
    # Convert PIL image to tensor
    to_tensor = transforms.ToTensor()(pil)
    # Squeeze the tensor to remove the batch dimension, permute channels, and unsqueeze to add the batch dimension back
    to_tensor = to_tensor.squeeze(0).permute(1, 2, 0).unsqueeze(0)
    return to_tensor
