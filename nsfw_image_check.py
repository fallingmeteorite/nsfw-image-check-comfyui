from .models.tensor_to_other import tensor_to_pil
from .models.check import nsfw_threshold


class NsfwCheckNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            },
            "optional": {
                "threshold": ("FLOAT", {"default": 0.5, "min": 0, "max": 1}),

                "type_choose": (
                    ["safe", "r16", "r18"],
                    {"default": "r18"},)

            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "nsfw_image_check"

    CATEGORY = "image/processing"

    def nsfw_image_check(self, image, threshold, type_choose):
        output_info = nsfw_threshold(tensor_to_pil(image), threshold, type_choose)
        if output_info is None:
            return (image,)
        else:
            return (output_info,)
