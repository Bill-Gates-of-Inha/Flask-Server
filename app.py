from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import tensorflow as tf
import numpy as np
app = Flask(__name__)


@app.route('/')
def hello_jiyong():
    return 'hello_jiyong'


@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    image = Image.open(file)
    image = image.resize((224, 224))
    img_batch = np.expand_dims(image, axis=0)
    img_preprocessed = tf.keras.applications.efficientnet.preprocess_input(img_batch)
    prediction = model.predict(img_preprocessed)
    idx = prediction[0].argmax()

    return labels[idx]

    """return jsonify(
        {'data': {
            'name': food_name
        }
    })"""


if __name__ == '__main__':
    model = load_model('./model/Food_Classifier.h5')
    labels = open("./model/labels.txt", 'r').read().split('\n')
    app.run(debug=True)
