""" API to classify images. """

import numpy as np
from fastapi import FastAPI
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    decode_predictions,
    preprocess_input,
)
from tensorflow.keras.preprocessing.image import img_to_array, load_img

app = FastAPI()

mobile = MobileNetV2()


def prepare_image(file_path):
    img = load_img("img/" + file_path, target_size=(224, 224))
    # print(img)
    img_array = img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array_expanded_dims)


@app.get("/")
async def read_root(fname: str):
    # load and pre-process image
    img = prepare_image(fname)
    # amke predictions
    predictions = mobile.predict(img)
    # process predictions
    results = decode_predictions(predictions)
    results_dict = dict([(i[1], float(i[2])) for i in results[0]])
    return results_dict
