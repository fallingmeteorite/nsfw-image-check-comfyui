import numpy as np

from .image import load_image, ImageTyping

__all__ = [
    'rgb_encode',
]

_DEFAULT_ORDER = 'HWC'


def _get_hwc_map(order_: str):
    return tuple(_DEFAULT_ORDER.index(c) for c in order_.upper())


def rgb_encode(image: ImageTyping, order_: str = 'CHW', use_float: bool = True) -> np.ndarray:
    """
    Overview:
        Encode image as rgb channels.

    :param image: Image to be encoded.
    :param order_: Order of encoding, default is ``CHW``.
    :param use_float: Use float to represent the channels, default is ``True``. ``np.uint8`` will be used when false.
    :return: Encoded rgb image.
    """
    image = load_image(image, mode='RGB')
    array = np.asarray(image)
    array = np.transpose(array, _get_hwc_map(order_))
    if use_float:
        array = (array / 255.0).astype(np.float32)
        assert array.dtype == np.float32
    else:
        assert array.dtype == np.uint8
    return array
