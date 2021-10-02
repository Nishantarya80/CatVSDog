# make a prediction for a new image.
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from keras_preprocessing import image
import os


 
# load and prepare the image
def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(224, 224))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 224, 224, 3)
    # center pixel data
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    return img

def run_example(image):

    # load the image
    img = load_image("./computerVision/"+image)
    # load model
    model = load_model("./computerVision/final_model.h5")
    # predict the class
    result = model.predict(img)
    
    os.remove("./computerVision/"+image)

    return result[0]

def run_example2(image):

    # load the image
    # img = load_image("./computerVision/"+image)
    # load model
    img = img_to_array(image)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 224, 224, 3)
    # center pixel data
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]

    model = load_model("./computerVision/final_model.h5")
    # predict the class
    result = model.predict(img)
    
    # os.remove("./computerVision/"+image)

    return result[0]
