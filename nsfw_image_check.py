from .models.tensor_to_other import tensor_to_pil
from .models.nsfw_check import nsfw_detect


class NsfwCheckNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            # Image input
            "required": {
                "image_requires_in": ("IMAGE",),
            },

            # Thresholds for all filtering modes
            "optional": {
                "threshold_r18": ("FLOAT", {"default": 0.5, "min": 0, "max": 1}),

                "threshold_hentai": ("FLOAT", {"default": 0.5, "min": 0, "max": 1}),

                "threshold_furry": ("FLOAT", {"default": 0.5, "min": 0, "max": 1}),

                "threshold_genitalia": ("FLOAT", {"default": 0.5, "min": 0, "max": 1}),

                "threshold_porn": ("FLOAT", {"default": 0.5, "min": 0, "max": 1}),

                "threshold_sexy": ("FLOAT", {"default": 0.5, "min": 0, "max": 1}),

                # Select the app type
                "filter_choose": (
                    ["r18_nsfw_check", "hentai_nsfw_check", "furry_nsfw_check", "genitalia_nsfw_check",
                     "porn_nsfw_check", "sexy_nsfw_check", "auto_nsfw_check"],

                    {"default": "r18_nsfw_check"},)

            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("image_requires_out", "corresponding_filter_entries")

    FUNCTION = "nsfw_image_check"

    CATEGORY = "image/processing"

    def nsfw_image_check(self, image_requires_in, threshold_r18, threshold_hentai, threshold_furry, threshold_genitalia, threshold_porn, threshold_sexy, filter_choose):
        pil_image_info = tensor_to_pil(image_requires_in)

        image_check_info, check_type = nsfw_detect(pil_image_info, threshold_r18, threshold_hentai, threshold_furry, threshold_genitalia, threshold_porn, threshold_sexy, filter_choose)

        if image_check_info is None:
            return image_requires_in, "None"

        if not image_check_info is None:

            return image_check_info, f"{check_type} is image-triggered filtering rule"
