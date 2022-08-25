from typing import Tuple
import numpy as np
from tensorflow import keras

seq_model = keras.models.load_model('src/app/model/cnn_model')
img_dimensions = 32, 32
seq_model.metrics_names


def translate_pred(prediction: np.array) -> Tuple[str, float]:
    """Input prediction's shape: array([[X]], dtype=float32).
    
    Output examples:
        - ("Dog", 70.8)
        - ("Cat", 90.2)
    """
    if prediction[0][0] > 0.5:
        return "Dog", prediction[0][0] * 100
    else:
        return "Cat", (1 - prediction[0][0]) * 100

def model_predict(image_uri: str) -> Tuple[str, float]:
    import numpy as np
    from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
    
    #load the image
    img_width, img_height = img_dimensions
    my_image = load_img(image_uri, target_size=(img_width, img_height))

    #preprocess the image
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    # img_arr = img_to_array(my_image)
    img_arr = np.expand_dims(img_to_array(my_image), axis=0)
    preprocessed_img = next(test_datagen.flow(img_arr, batch_size=1))

    prediction = seq_model.predict(preprocessed_img)
    return translate_pred(prediction)


def multiple_model_predict(file_paths):
    data = list()
    for fp in file_paths:
        pred = model_predict(fp)
        data.append(pred)
        
    return data