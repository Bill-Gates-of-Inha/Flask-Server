from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import tensorflow as tf
import numpy as np
import logging

app = Flask(__name__)
model = None
labels = None
logging.basicConfig(filename='app.log', level=logging.DEBUG)

@app.route('/', methods=['GET'])
def hello_jiyong():
    return "hello jiyong"

##메소드는 post 로 사진을 body에 담을꺼임
@app.route('/predict', methods=['POST'])
def predict():
    ###body에 담긴 이미지를 가져오는것 multi-part/form-data
    file = request.files['file']
    ###file 이 FileStorage 타입이라 PIL 타입으로 변경해야함 그리구 리사이징도 함께
    image = Image.open(file)
    image = image.resize((224, 224))

    ### 이 밑에는 수피가 알려준거
    img_batch = np.expand_dims(image, axis=0)
    img_preprocessed = tf.keras.applications.efficientnet.preprocess_input(img_batch)
    prediction = model.predict(img_preprocessed)
    best_3 = np.argsort(prediction, axis=1)[:, -3:]

    result = [labels[y] for y in best_3[0]][::-1]

    logging.getLogger().info(result)

    return jsonify({'data': result})

def load_model_to_app():
    global model
    global labels

    model = load_model('./model/Food_Classifier.h5')
    labels = open("./model/labels.txt", 'r').read().split('\n')

if __name__ == '__main__':
    ### 모델 로드하는거

    ### 레이블화 된거를 list로 불러오기

    app.run(host='0.0.0.0', debug=True)