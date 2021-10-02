# make a prediction for a new image.
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from keras_preprocessing import image
import os


def run_example2(image):

    # load the image
    img = img_to_array(image)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 224, 224, 3)
    # center pixel data
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    # load model
    model = load_model("./computerVision/final_model.h5")
    # predict the class
    result = model.predict(img)

    return result[0]
