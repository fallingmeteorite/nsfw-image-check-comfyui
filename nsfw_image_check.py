from typing import Tuple, Optional, Any

from .modules.nsfw_check import nsfw_detect
from .modules.nsfw_cover import nsfw_cover
from .modules.tensor_to_other import tensor_to_pil


class NsfwCheckNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            # Image input
            "required": {
                "image_requires_in": ("IMAGE", {"default": "", "forceInput": True}),
            },

            # Thresholds for all filtering modes
            "optional": {
                "custom_image_out": ("IMAGE", {"default": "", "forceInput": True}),

                "enabled_check": ("BOOLEAN", {"default": True}),

                "r18_threshold": ("FLOAT", {"default": 0.5, "min": 0, "max": 1, "step": 0.01}),

                "hentai_threshold": ("FLOAT", {"default": 0.5, "min": 0, "max": 1, "step": 0.01}),

                "furry_threshold": ("FLOAT", {"default": 0.5, "min": 0, "max": 1, "step": 0.01}),

                "genitalia_threshold": ("FLOAT", {"default": 0.5, "min": 0, "max": 1, "step": 0.01}),

                "porn_threshold": ("FLOAT", {"default": 0.5, "min": 0, "max": 1, "step": 0.01}),

                "sexy_threshold": ("FLOAT", {"default": 0.5, "min": 0, "max": 1, "step": 0.01}),

                "r18_enabled": ("BOOLEAN", {"default": True}),

                "hentai_enabled": ("BOOLEAN", {"default": True}),

                "furry_enabled": ("BOOLEAN", {"default": True}),

                "genitalia_enabled": ("BOOLEAN", {"default": True}),

                "porn_enabled": ("BOOLEAN", {"default": True}),

                "sexy_enabled": ("BOOLEAN", {"default": True}),

                # Select the filter type
                "filter_choose": (
                    ["r18_nsfw_check",
                     "hentai_nsfw_check",
                     "furry_nsfw_check",
                     "genitalia_nsfw_check",
                     "porn_nsfw_check",
                     "sexy_nsfw_check",
                     "auto_nsfw_check"],
                    {"default": "r18_nsfw_check"},
                ),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("image_requires_out", "corresponding_filter_entries")

    FUNCTION = "nsfw_image_check"

    CATEGORY = "image/processing"

    def nsfw_image_check(self,
                         image_requires_in: Any,
                         enabled_check: bool,
                         r18_threshold: float,
                         r18_enabled: bool,
                         hentai_threshold: float,
                         hentai_enabled: bool,
                         furry_threshold: float,
                         furry_enabled: bool,
                         genitalia_threshold: float,
                         genitalia_enabled: bool,
                         porn_threshold: float,
                         porn_enabled: bool,
                         sexy_threshold: float,
                         sexy_enabled: bool,
                         filter_choose: str,
                         custom_image_out: Any = None) -> Tuple[Optional[Any], str]:
        """
        Perform NSFW checks on the input image based on the selected filter mode and thresholds.

        Parameters:
        image_requires_in (Any): Input image tensor.
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
        Tuple[Optional[Any], str]: Tensor containing the warning image and the corresponding filter type if triggered, otherwise the original image and a safety message.
        """
        pil_image_info = tensor_to_pil(image_requires_in)

        image_check_info, check_type = nsfw_detect(
            pil_image_info,
            custom_image_out,
            enabled_check,
            r18_threshold, r18_enabled,
            hentai_threshold, hentai_enabled,
            furry_threshold, furry_enabled,
            genitalia_threshold, genitalia_enabled,
            porn_threshold, porn_enabled,
            sexy_threshold, sexy_enabled,
            filter_choose
        )

        if image_check_info is None:
            return image_requires_in, check_type

        return image_check_info, f"|{check_type}| is a filtering rule that is triggered"


class NsfwAreaCoverNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            # Image input
            "required": {
                "image_requires_in": ("IMAGE", {"default": "", "forceInput": True}),
            },

            # Thresholds for all filtering modes
            "optional": {
                "enabled_check": ("BOOLEAN", {"default": True}),

            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_requires_out",)

    FUNCTION = "nsfw_area_coverage"

    CATEGORY = "image/processing"

    def nsfw_area_coverage(self,
                           image_requires_in: Any,
                           enabled_check: bool
                           ) -> Tuple[Optional[Any]]:
        """
        Perform NSFW checks on the input image based on the selected filter mode and thresholds.

        Parameters:
        image_requires_in (Any): Input image tensor.
        enabled_check (bool): Whether to enable NSFW checks.

        Returns:
        Any: Tensor.
        """
        pil_image_info = tensor_to_pil(image_requires_in)

        image_check_info = nsfw_cover(
            pil_image_info,
            enabled_check
        )

        return image_check_info,
