import torch
from ..validate import anime_rating_score


def nsfw_threshold(pil, threshold):
    if float(threshold) <= float(anime_rating_score(pil)["r18"]):
        # Create a black image
        width, height = 256, 256  # The width and height of the image
        black_tensor = torch.zeros(1, height, width)
        return black_tensor
    else:
        return None
