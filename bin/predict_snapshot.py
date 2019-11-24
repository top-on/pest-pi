#!/usr/bin/env python
"""
Take a snapshot from the webcam and classify it.
Log both the snapshot and the prediction.
"""

import imageio
import json
import time

from pest_pi.camera import take_picture
from pest_pi.image import get_classifier, predict_classes, preprocess_array

# load model
model = get_classifier()

# take picture
img_array = take_picture()

# make prediction
img_prep = preprocess_array(img_array)
prediction = predict_classes(img=img_prep, classifier=model)

# write image and prediction to file
now = time.strftime('%Y-%m-%dT%H:%M%Z', time.gmtime(time.time()))
imageio.imwrite(f"img/{now}.jpg", img_array)
with open(f"img/{now}.txt", "w") as json_file:
    prediction_json = json.dumps(prediction, indent=2)
    json_file.write(prediction_json)
