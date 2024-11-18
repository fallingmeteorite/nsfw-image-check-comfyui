from typing import Tuple, Dict

from ..data import ImageTyping
from ..generic import classify_predict, classify_predict_score

__all__ = [
    'anime_rating_score',
    'anime_rating',
]

_DEFAULT_MODEL_NAME = 'mobilenetv3_v1_pruned_ls0.1'
_REPO_ID = 'deepghs/anime_rating'


def anime_rating_score(image: ImageTyping, model_name: str = _DEFAULT_MODEL_NAME) -> Dict[str, float]:
    """
    Overview:
        Predict the rating of the given image, return the score with as a dict object.

    :param image: Image to rating.
    :param model_name: Model to use. Default is ``mobilenetv3_sce_dist``. All available models are listed
        on the benchmark plot above. If you need better accuracy, just set this to ``caformer_s36_plus``.
    :return: A dict with ratings and scores.
    """
    return classify_predict_score(image, _REPO_ID, model_name)


def anime_rating(image: ImageTyping, model_name: str = _DEFAULT_MODEL_NAME) -> Tuple[str, float]:
    """
    Overview:
        Predict the rating of the given image, return the class and its score.

    :param image: Image to rating.
    :param model_name: Model to use. Default is ``mobilenetv3_sce_dist``. All available models are listed
        on the benchmark plot above. If you need better accuracy, just set this to ``caformer_s36_plus``.
    :return: A tuple contains the rating and its score.
    """
    return classify_predict(image, _REPO_ID, model_name)
