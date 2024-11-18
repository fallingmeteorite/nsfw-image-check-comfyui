from typing import Tuple, Dict

from ..data import ImageTyping
from ..generic import classify_predict, classify_predict_score

__all__ = [
    'anime_furry_score',
    'anime_furry',
]

_DEFAULT_MODEL_NAME = 'mobilenetv3_v0.1_dist'
_REPO_ID = 'deepghs/anime_furry'


def anime_furry_score(image: ImageTyping, model_name: str = _DEFAULT_MODEL_NAME) -> Dict[str, float]:
    """
    Get the scores for different types in a furry anime image.

    :param image: The input image.
    :type image: ImageTyping
    :param model_name: The model name. Default is 'mobilenetv3_v0.1_dist'.
    :type model_name: str
    :return: A dictionary with type scores.
    :rtype: Dict[str, float]
    """
    return classify_predict_score(image, _REPO_ID, model_name)


def anime_furry(image: ImageTyping, model_name: str = _DEFAULT_MODEL_NAME) -> Tuple[str, float]:
    """
    Get the primary furry type and its score.

    :param image: The input image.
    :type image: ImageTyping
    :param model_name: The model name. Default is 'mobilenetv3_v0.1_dist'.
    :type model_name: str
    :return: A tuple with the primary type and its score.
    :rtype: Tuple[str, float]
    """
    return classify_predict(image, _REPO_ID, model_name)
