#!/usr/bin/env python
""" Image classifier. """
# %%
import wget

from pest_pi.image import get_classifier, predict_classes, prepare_image

# %% download image
url = "https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png"
out = "img/cat.png"
wget.download(url=url, out=out)

# %% preprocess image
file_path = "img/cat.png"
img_prep = prepare_image(file_path)

# %% predict
model = get_classifier()
result = predict_classes(img=img_prep, classifier=model)
print(result)
