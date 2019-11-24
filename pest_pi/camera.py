""" Utils for using camera on raspberry pi. """

from typing import Tuple

import numpy as np
import picamera


def take_picture(resolution: Tuple[int, int] = (224, 224)) -> np.ndarray:
    """Take picture from Raspberry Pi webcam.

    Args:
        resolution (Tuple[int, int], optional): Image resolution. Defaults to (224, 224).

    Returns:
        np.ndarray: Array of snapshot in RGB.
    """
    with picamera.PiCamera() as camera:
        camera.resolution = (224, 224)
        camera.framerate = 24
        # OPTIONAL: sleep for 2 seconds here
        img_array = np.empty((224, 224, 3), dtype=np.uint8)
        camera.capture(img_array, 'rgb')
    return img_array
