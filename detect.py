import numpy as np
from keras.models import model_from_json


class AccidentDetection(object):
    class_name = ['Accident', 'No Accident']

    def __init__(self):
        model_json_file = 'model.json'
        model_weight_file = 'model.h5'
        with open(model_json_file, "r") as json_file:
            loaded_json_model = json_file.read()
            self.loaded_model = model_from_json(loaded_json_model)
        self.loaded_model.load_weights(model_weight_file)
        self.loaded_model.make_predict_function()

    def predict_accident(self, img):
        self.pred = self.loaded_model.predict(img)
        return AccidentDetection.class_name[np.argmax(self.pred)], self.pred
