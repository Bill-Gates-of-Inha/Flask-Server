from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import tensorflow as tf
import numpy as np
app = Flask(__name__)


@app.route('/')
def hello_jiyong():
    return 'hello_jiyong'

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
    idx = prediction[0].argmax()

    ### 결과값을 정의해서 리턴하면 댐 난 그냥 짜장면 나오게 햇삼
    return labels[idx]

    """return jsonify(
        {'data': {
            'name': food_name
        }
    })"""


if __name__ == '__main__':
    ### 모델 로드하는거
    model = load_model('./model/Food_Classifier.h5')
    ### 레이블화 된거를 list로 불러오기
    labels = open("./model/labels.txt", 'r').read().split('\n')
    app.run(debug=True)
