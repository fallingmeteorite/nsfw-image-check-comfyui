from .modules.tensor_to_other import tensor_to_pil
from .modules.nsfw_check import nsfw_detect


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
                "r18_threshold": ("FLOAT", {"default": 0.5, "min": 0, "max": 1}),

                "hentai_threshold": ("FLOAT", {"default": 0.5, "min": 0, "max": 1}),

                "furry_threshold": ("FLOAT", {"default": 0.5, "min": 0, "max": 1}),

                "genitalia_threshold": ("FLOAT", {"default": 0.5, "min": 0, "max": 1}),

                "porn_threshold": ("FLOAT", {"default": 0.5, "min": 0, "max": 1}),

                "sexy_threshold": ("FLOAT", {"default": 0.5, "min": 0, "max": 1}),

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

    def nsfw_image_check(self, image_requires_in, r18_threshold, hentai_threshold, furry_threshold, genitalia_threshold, porn_threshold, sexy_threshold, filter_choose):
        pil_image_info = tensor_to_pil(image_requires_in)

        image_check_info, check_type = nsfw_detect(pil_image_info, r18_threshold, hentai_threshold, furry_threshold, genitalia_threshold, porn_threshold, sexy_threshold, filter_choose)

        if image_check_info is None:
            return image_requires_in, "None"

        if not image_check_info is None:

            return image_check_info, f"{check_type} is image-triggered filtering rule"
