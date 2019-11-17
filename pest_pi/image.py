""" Utils for images. """

import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    decode_predictions,
    preprocess_input,
)
from tensorflow.keras.preprocessing.image import img_to_array, load_img


def prepare_image(file_path: str) -> np.ndarray:
    """Read image from file and preprocess for MobileNetv2
    Args:
        file_path (str): Path to image file.
    Returns:
        np.ndarray: Preprocessed images.
    """
    img = load_img(file_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array_expanded_dims)


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
