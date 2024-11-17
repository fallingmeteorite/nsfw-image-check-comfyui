"""
Overview:
    Detect targets from the given anime image.

    For example, you can detect the heads with :func:`imgutils.head.detect_heads` and visualize it
    with :func:`imgutils.visual.detection_visualize` like this

    .. image:: head_detect_demo.plot.py.svg
        :align: center
"""
from .censor import detect_censors
