from .nsfw_image_check import NsfwCheckNode, NsfwAreaCoverNode

NODE_CLASS_MAPPINGS = {
    "NsfwCheckNode": NsfwCheckNode, "NsfwAreaCoverNode": NsfwAreaCoverNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NsfwCheckNode": "Nsfw Image Check Node",
    "NsfwAreaCoverNode": "Nsfw area coverage",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
