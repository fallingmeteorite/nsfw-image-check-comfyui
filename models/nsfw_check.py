import torch

from ..validate import anime_rating_score

from ..detect import detect_censors

from ..validate import nsfw_pred_score

from ..validate import anime_furry_score


# Tensor data that produces a black graph
def black_image_output():
    width, height = 128, 128
    black_tensor = torch.zeros(1, height, width)
    return black_tensor


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


# 05
def furry_check(pil, threshold_furry):
    result = anime_furry_score(pil)
    if float(result["furry"]) >= float(threshold_furry):
        return True
    return False


# 01
def genitalia_check(pil, threshold_genitalia):
    result = detect_censors(pil)
    if not result == []:
        if float(result[0][2]) >= float(threshold_genitalia):
            return True
    return False


# 03
def porn_check(pil, threshold_porn):
    result = nsfw_pred_score(pil)
    if float(result['porn']) >= float(threshold_porn):
        return True
    return False


# 06
def sexy_check(pil, threshold_sexy):
    result = nsfw_pred_score(pil)
    if float(result['sexy']) >= float(threshold_sexy):
        return True
    return False


def nsfw_detect(pil, threshold_r18, threshold_hentai, threshold_furry, threshold_genitalia, threshold_porn,
                threshold_sexy, filter_choose):
    if filter_choose == "r18_nsfw_check":
        if r18_check(pil, threshold_r18):
            return black_image_output(), "r18"

    if filter_choose == "hentai_nsfw_check":
        if hentai_check(pil, threshold_hentai):
            return black_image_output(), "hentai"

    if filter_choose == "furry_nsfw_check":
        if furry_check(pil, threshold_furry):
            return black_image_output(), "furry"

    if filter_choose == "genitalia_nsfw_check":
        if genitalia_check(pil, threshold_genitalia):
            return black_image_output(), "genitalia"

    if filter_choose == "porn_nsfw_check":
        if porn_check(pil, threshold_porn):
            return black_image_output(), "porn"

    if filter_choose == "sexy_nsfw_check":
        if sexy_check(pil, threshold_sexy):
            return black_image_output(), "sexy"

    # Automatic mode, from the most obvious to the least noticeable
    if filter_choose == "auto_nsfw_check":
        # 01
        if genitalia_check(pil, threshold_genitalia):
            return black_image_output(), "genitalia"

        # 02
        if r18_check(pil, threshold_r18):
            return black_image_output(), "r18"

        # 03
        if porn_check(pil, threshold_porn):
            return black_image_output(), "porn"

        # 04
        if hentai_check(pil, threshold_hentai):
            return black_image_output(), "hentai"

        # 05
        if furry_check(pil, threshold_furry):
            return black_image_output(), "furry"

        # 06
        if sexy_check(pil, threshold_sexy):
            return black_image_output(), "sexy"

    return None, None
