""" Utils for images. """

import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    decode_predictions,
    preprocess_input,
)
from tensorflow.keras.preprocessing.image import img_to_array, load_img


def preprocess_array(img_arr: np.ndarray) -> np.ndarray:
    """Preprocess array for MobileNetv2

    Args:
        img_arr (np.ndarray): Data input, assuming shape of (224, 224, 3)

    Returns:
        np.ndarray: Array of image, proprocessed for use with MobileNetv2.
    """
    assert img_arr.shape == (224, 224, 3), "Input has wrong shape for mobilenet_v2"
    img_exp = np.expand_dims(img_arr, axis=0)
    img_prep = preprocess_input(img_exp)
    return img_prep


def prepare_image(file_path: str) -> np.ndarray:
    """Read image from file and preprocess for MobileNetv2

    Args:
        file_path (str): Path to image file.

    Returns:
        np.ndarray: Preprocessed images.
    """
    img = load_img(file_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_prep = preprocess_array(img_array)
    return img_prep


def get_classifier() -> MobileNetV2:
    """Load MobileNetv2 as classifier model.

    Returns:
        MobileNetV2: Classifier.
    """
    mobile = MobileNetV2()
    return mobile


def predict_classes(img: np.ndarray, classifier: MobileNetV2) -> dict:
    """Predict classification of an image.

    Args:
        img (np.ndarray): Image, preprocessed for MobileNetv2
        classifier (MobileNetV2): Instance of classifier.

    Returns:
        dict: Predicted classes and their assigned probability.
    """
    predictions = classifier.predict(img)
    prediction = decode_predictions(predictions)
    classes = dict([(i[1], float(i[2])) for i in prediction[0]])
    return classes
