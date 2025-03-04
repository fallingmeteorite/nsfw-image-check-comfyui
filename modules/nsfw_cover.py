from typing import Any, List, Tuple

from PIL import Image, ImageDraw

from .tensor_to_other import pil_to_tensor
from ..detect import detect_censors


def cover(pil: Image.Image, data: List[Tuple[Tuple[int, int, int, int], str, float]]):
    # Create an ImageDraw object
    draw = ImageDraw.Draw(pil)

    for bbox, label, confidence in data:
        x1, y1, x2, y2 = bbox
        draw.rectangle((x1, y1, x2, y2), fill="white")

    return pil


def nsfw_cover(pil: Image.Image,
               enabled_check: bool
               ) -> Any:
    """
    Detect NSFW content in the image based on the selected filter mode.

    Parameters:
    pil (Image.Image): Input PIL image.
    enabled_check (bool): Whether to enable NSFW checks.

    Returns:
    Any: Tensor.
    """

    if enabled_check:
        pil = cover(pil, detect_censors(pil))

    return pil_to_tensor(pil)
