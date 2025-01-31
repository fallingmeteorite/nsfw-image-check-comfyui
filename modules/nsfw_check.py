import os
import random
from PIL import Image

from .tensor_to_other import pil_to_tensor
from ..detect import detect_censors
from ..validate import anime_furry_score
from ..validate import anime_rating_score
from ..validate import nsfw_pred_score


def get_value(data):
    # Initialize variables
    nipple_f_value = 0
    pussy_value = 0
    penis_value = 0

    # Traverse the list
    for item in data:
        if item[1] == 'nipple_f':
            nipple_f_value = item[2]
        elif item[1] == 'pussy':
            pussy_value = item[2]
        elif item[1] == 'penis':
            penis_value = item[2]

    return nipple_f_value, pussy_value, penis_value


def get_random_image(directory):
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
def warn_image_output():
    img = Image.open(get_random_image(f"custom_nodes/nsfw-image-check-comfyui/img")).convert('RGB')
    return pil_to_tensor(img)


# 02
def r18_check(pil, threshold_r18):
    result = anime_rating_score(pil)
    if float(result['r18']) >= float(threshold_r18):
        return True
    return False


# 04
def hentai_check(pil, threshold_hentai):
    result = nsfw_pred_score(pil)
    if float(result['hentai']) >= float(threshold_hentai):
        return True
    return False


# 06
def furry_check(pil, threshold_furry):
    result = anime_furry_score(pil)
    if float(result["furry"]) >= float(threshold_furry):
        return True
    return False


# 01
def genitalia_check(pil, threshold_genitalia):
    nipple_f_value, pussy_value, penis_value = get_value(detect_censors(pil))
    if float(nipple_f_value) >= float(threshold_genitalia):
        return True

    if float(pussy_value) >= float(threshold_genitalia):
        return True

    if float(penis_value) >= float(threshold_genitalia):
        return True
    return False


# 03
def porn_check(pil, threshold_porn):
    result = nsfw_pred_score(pil)
    if float(result['porn']) >= float(threshold_porn):
        return True
    return False


# 05
def sexy_check(pil, threshold_sexy):
    result = nsfw_pred_score(pil)
    if float(result['sexy']) >= float(threshold_sexy):
        return True
    return False


def nsfw_detect(pil,
                enabled_check,
                r18_threshold, r18_enabled,
                hentai_threshold, hentai_enabled,
                furry_threshold, furry_enabled,
                genitalia_threshold, genitalia_enabled,
                porn_threshold, porn_enabled,
                sexy_threshold, sexy_enabled,
                filter_choose):
    if enabled_check:

        if filter_choose == "r18_nsfw_check":
            if r18_check(pil, r18_threshold):
                return warn_image_output(), "r18"

        if filter_choose == "hentai_nsfw_check":
            if hentai_check(pil, hentai_threshold):
                return warn_image_output(), "hentai"

        if filter_choose == "furry_nsfw_check":
            if furry_check(pil, furry_threshold):
                return warn_image_output(), "furry"

        if filter_choose == "genitalia_nsfw_check":
            if genitalia_check(pil, genitalia_threshold):
                return warn_image_output(), "genitalia"

        if filter_choose == "porn_nsfw_check":
            if porn_check(pil, porn_threshold):
                return warn_image_output(), "porn"

        if filter_choose == "sexy_nsfw_check":
            if sexy_check(pil, sexy_threshold):
                return warn_image_output(), "sexy"

        # Automatic mode, from the most obvious to the least noticeable
        if filter_choose == "auto_nsfw_check":
            # 01
            if genitalia_check(pil, genitalia_threshold) and genitalia_enabled:
                return warn_image_output(), "genitalia"

            # 02
            if r18_check(pil, r18_threshold) and r18_enabled:
                return warn_image_output(), "r18"

            # 03
            if porn_check(pil, porn_threshold) and porn_enabled:
                return warn_image_output(), "porn"

            # 04
            if hentai_check(pil, hentai_threshold) and hentai_enabled:
                return warn_image_output(), "hentai"

            # 05
            if sexy_check(pil, sexy_threshold) and sexy_enabled:
                return warn_image_output(), "sexy"

            # 06
            if furry_check(pil, furry_threshold) and furry_enabled:
                return warn_image_output(), "furry"

    return None, "The pictures are safe"
