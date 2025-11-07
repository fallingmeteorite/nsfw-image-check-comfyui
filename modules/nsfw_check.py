import os
import random
from typing import Tuple, Optional, List, Any

from PIL import Image
from torch import Tensor

from .tensor_to_other import pil_to_tensor
from ..detect import detect_censors
from ..validate import anime_furry_score
from ..validate import anime_rating_score
from ..validate import nsfw_pred_score


def get_value(data: List[Tuple[Tuple[int, int, int, int], str, float]]) -> Tuple[float, float, float]:
    """
    Extract values for 'nipple_f', 'pussy', and 'penis' from the input data.

    Parameters:
    data (List[Tuple[Tuple[int, int, int, int], str, float]]): List of tuples containing bounding box coordinates, label, and score.

    Returns:
    Tuple[float, float, float]: Values for 'nipple_f', 'pussy', and 'penis'.
    """
    # Initialize variables
    nipple_f_value = 0.0
    pussy_value = 0.0
    penis_value = 0.0

    # Traverse the list
    for item in data:
        if item[1] == 'nipple_f':
            nipple_f_value = float(item[2])
        elif item[1] == 'pussy':
            pussy_value = float(item[2])
        elif item[1] == 'penis':
            penis_value = float(item[2])

    return nipple_f_value, pussy_value, penis_value


def get_random_image(directory: str) -> str:
    """
    Get a random image file from the specified directory.

    Parameters:
    directory (str): Directory containing image files.

    Returns:
    str: Full path to a random image file.
    """
    # Get all the files in the directory
    files = os.listdir(directory)

    # Filter out image files (assuming the image file extension is .jpg)
    image_files = [f for f in files if f.lower().endswith('.jpg')]

    if not image_files:
        raise ValueError("No image files found in the directory.")

    # Choose a random image
    random_image_file = random.choice(image_files)

    # Returns the full path to the image
    return f"custom_nodes/nsfw-image-check-comfyui/img/{random_image_file}"


# Generate Tensor data for the warning graph
def warn_image_output() -> Optional[Any]:
    """
    Convert a random image from the specified directory to a tensor.

    Returns:
    Optional[Any]: Tensor containing the warning image.
    """
    img_path = get_random_image(f"custom_nodes/nsfw-image-check-comfyui/img")
    img = Image.open(img_path).convert('RGB')
    return pil_to_tensor(img)


# 02
def r18_check(pil: Image.Image, threshold_r18: float) -> bool:
    """
    Check if the 'r18' score meets or exceeds the threshold.

    Parameters:
    pil (Image.Image): Input PIL image.
    threshold_r18 (float): Threshold for 'r18' score.

    Returns:
    bool: True if the score meets or exceeds the threshold, False otherwise.
    """
    result = anime_rating_score(pil)
    return float(result['r18']) >= threshold_r18


# 04
def hentai_check(pil: Image.Image, threshold_hentai: float) -> bool:
    """
    Check if the 'hentai' score meets or exceeds the threshold.

    Parameters:
    pil (Image.Image): Input PIL image.
    threshold_hentai (float): Threshold for 'hentai' score.

    Returns:
    bool: True if the score meets or exceeds the threshold, False otherwise.
    """
    result = nsfw_pred_score(pil)
    return float(result['hentai']) >= threshold_hentai


# 06
def furry_check(pil: Image.Image, threshold_furry: float) -> bool:
    """
    Check if the 'furry' score meets or exceeds the threshold.

    Parameters:
    pil (Image.Image): Input PIL image.
    threshold_furry (float): Threshold for 'furry' score.

    Returns:
    bool: True if the score meets or exceeds the threshold, False otherwise.
    """
    result = anime_furry_score(pil)
    return float(result["furry"]) >= threshold_furry


# 01
def genitalia_check(pil: Image.Image, threshold_genitalia: float) -> bool:
    """
    Check if any of the 'nipple_f', 'pussy', or 'penis' scores meet or exceed the threshold.

    Parameters:
    pil (Image.Image): Input PIL image.
    threshold_genitalia (float): Threshold for genitalia scores.

    Returns:
    bool: True if any score meets or exceeds the threshold, False otherwise.
    """
    nipple_f_value, pussy_value, penis_value = get_value(detect_censors(pil))
    return nipple_f_value >= threshold_genitalia or pussy_value >= threshold_genitalia or penis_value >= threshold_genitalia


# 03
def porn_check(pil: Image.Image, threshold_porn: float) -> bool:
    """
    Check if the 'porn' score meets or exceeds the threshold.

    Parameters:
    pil (Image.Image): Input PIL image.
    threshold_porn (float): Threshold for 'porn' score.

    Returns:
    bool: True if the score meets or exceeds the threshold, False otherwise.
    """
    result = nsfw_pred_score(pil)
    return float(result['porn']) >= threshold_porn


# 05
def sexy_check(pil: Image.Image, threshold_sexy: float) -> bool:
    """
    Check if the 'sexy' score meets or exceeds the threshold.

    Parameters:
    pil (Image.Image): Input PIL image.
    threshold_sexy (float): Threshold for 'sexy' score.

    Returns:
    bool: True if the score meets or exceeds the threshold, False otherwise.
    """
    result = nsfw_pred_score(pil)
    return float(result['sexy']) >= threshold_sexy


def nsfw_detect(pil: Image.Image,
                custom_image_out: Tensor,
                enabled_check: bool,
                r18_threshold: float, r18_enabled: bool,
                hentai_threshold: float, hentai_enabled: bool,
                furry_threshold: float, furry_enabled: bool,
                genitalia_threshold: float, genitalia_enabled: bool,
                porn_threshold: float, porn_enabled: bool,
                sexy_threshold: float, sexy_enabled: bool,
                filter_choose: str) -> Tuple[Optional[Any], str]:
    """
    Detect NSFW content in the image based on the selected filter mode.

    Parameters:
    pil (Image.Image): Input PIL image.
    enabled_check (bool): Whether to enable NSFW checks.
    r18_threshold (float): Threshold for 'r18' score.
    r18_enabled (bool): Whether to enable 'r18' check.
    hentai_threshold (float): Threshold for 'hentai' score.
    hentai_enabled (bool): Whether to enable 'hentai' check.
    furry_threshold (float): Threshold for 'furry' score.
    furry_enabled (bool): Whether to enable 'furry' check.
    genitalia_threshold (float): Threshold for genitalia scores.
    genitalia_enabled (bool): Whether to enable genitalia check.
    porn_threshold (float): Threshold for 'porn' score.
    porn_enabled (bool): Whether to enable 'porn' check.
    sexy_threshold (float): Threshold for 'sexy' score.
    sexy_enabled (bool): Whether to enable 'sexy' check.
    filter_choose (str): Selected filter mode.

    Returns:
    Tuple[Optional[Any], str]: Tensor containing the warning image and the corresponding filter type if triggered, otherwise None and a safety message.
    """
    if custom_image_out == None:
        custom_image_out = warn_image_output()

    if enabled_check:
        if filter_choose == "r18_nsfw_check":
            if r18_check(pil, r18_threshold):
                return custom_image_out, "r18"

        if filter_choose == "hentai_nsfw_check":
            if hentai_check(pil, hentai_threshold):
                return custom_image_out, "hentai"

        if filter_choose == "furry_nsfw_check":
            if furry_check(pil, furry_threshold):
                return custom_image_out, "furry"

        if filter_choose == "genitalia_nsfw_check":
            if genitalia_check(pil, genitalia_threshold) and genitalia_enabled:
                return custom_image_out, "genitalia"

        if filter_choose == "porn_nsfw_check":
            if porn_check(pil, porn_threshold) and porn_enabled:
                return custom_image_out, "porn"

        if filter_choose == "sexy_nsfw_check":
            if sexy_check(pil, sexy_threshold) and sexy_enabled:
                return custom_image_out, "sexy"

        # Automatic mode, from the most obvious to the least noticeable
        if filter_choose == "auto_nsfw_check":
            checks = [
                ("genitalia", genitalia_check, genitalia_threshold, genitalia_enabled),
                ("r18", r18_check, r18_threshold, r18_enabled),
                ("porn", porn_check, porn_threshold, porn_enabled),
                ("hentai", hentai_check, hentai_threshold, hentai_enabled),
                ("sexy", sexy_check, sexy_threshold, sexy_enabled),
                ("furry", furry_check, furry_threshold, furry_enabled)
            ]

            for check_type, check_func, threshold, enabled in checks:
                if enabled and check_func(pil, threshold):
                    return custom_image_out, check_type

    return None, "The pictures are safe"