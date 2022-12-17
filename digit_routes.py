import io
from http import HTTPStatus

from PIL import Image
import numpy as np
from tensorflow import keras

from flask import Blueprint, request, jsonify
from uuid6 import uuid6

from helpers import ensure_dir

digits_blueprint = Blueprint('digit', __name__, url_prefix='/digit')


MODEL = keras.models.load_model('mnist_model')


@digits_blueprint.route('/determine', methods=['POST'])
def determine_the_digit():
    photo_bytes = request.get_data()

    photo = Image.open(io.BytesIO(photo_bytes)).convert('L')
    photo = photo.resize((28, 28))
    photo = (255.0 - np.array(photo).reshape(-1)) / 255
    X = np.expand_dims(photo, axis=0)

    prediction = MODEL.predict(X)
    prediction = np.argmax(prediction)

    return jsonify(
        {'prediction': int(prediction)}
    ), HTTPStatus.CREATED


@digits_blueprint.route('/save_photo_label/<int:label>', methods=['POST'])
def save_photo_with_label(label: int):
    photo_bytes = request.get_data()
    photo = Image.open(io.BytesIO(photo_bytes)).convert('RGB')

    path_to_label_dir = f'data/{label}'

    ensure_dir(path_to_label_dir)
    photo.save(f'{path_to_label_dir}/{str(uuid6())}.jpg')

    return 'Saved.', HTTPStatus.CREATED
