""" Image classifier. """
# %%
import numpy as np
import wget
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input

# %% download image
url = "https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png"
out = "img/cat.png"
wget.download(url=url, out=out)

# %% download pre-trained network
mobile = MobileNetV2()


# %% preprocess image
def prepare_image(file_path):
    img = load_img(file_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array_expanded_dims)


file_path = "img/cat.png"
img = prepare_image(file_path)

# %% predict
predictions = mobile.predict(img)
results = decode_predictions(predictions)
print(results)
