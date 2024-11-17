from .nsfw_image_check import NsfwCheckNode

NODE_CLASS_MAPPINGS = {
    "NsfwCheckNode": NsfwCheckNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NsfwCheckNode": "Nsfw Image Check Node"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
