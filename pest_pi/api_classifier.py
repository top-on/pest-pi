""" API to classify images. """

from fastapi import FastAPI
from pest_pi.image import prepare_image, get_classifier, predict_classes

app = FastAPI()

model = get_classifier()  # pre-load classifier


@app.get("/")
async def read_root(fname: str):
    # load and pre-process image from file
    img_prep = prepare_image(fname)
    # make predictions
    prediction = predict_classes(img=img_prep, classifier=model)
    return prediction
