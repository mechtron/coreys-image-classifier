# -*- coding: utf-8 -*-
import datetime
import hashlib
import json
import os
import uuid

import numpy
import keras
from keras.models import Model
from keras.preprocessing import image
from keras.applications import (
    imagenet_utils,
    mobilenet,
)
import redis
from requests import get


REDIS_CLIENT = redis.StrictRedis(host='classifier-dev-cache-master', port=6379)


def download_image(image_url):
    temp_file_path = "/tmp/{}".format(uuid.uuid4())
    with open(temp_file_path, 'wb') as f:
        f.write(get(image_url).content)
    return temp_file_path


def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = numpy.expand_dims(img_array, axis=0)
    preprocessed_img = mobilenet.preprocess_input(img_array)
    return preprocessed_img


def make_prediction(image):
    mobilenet_model = mobilenet.MobileNet()
    prediction = mobilenet_model.predict(image)
    results = imagenet_utils.decode_predictions(prediction)
    print('Decoded predictions: ', results)
    return {
        'prediction': results[0][0][1],
        'confidence': float(results[0][0][2]),
    }


def delete_temp_image(image_path):
    os.remove(image_path)


def process_new_image(image_url):
    keras.backend.clear_session()
    image_path = download_image(image_url)
    processed_image = preprocess_image(image_path)
    prediction = make_prediction(processed_image)
    delete_temp_image(image_path)
    return prediction


def string_sha1(input_string):
    return hashlib.sha1(input_string.encode('utf-8')).hexdigest()


def get_prediction_cached(image_url):
    image_url_hashed = string_sha1(image_url)
    current_cached_value = REDIS_CLIENT.get(image_url_hashed)
    if current_cached_value:
        print("Found a cached result for {}..".format(image_url))
        return (json.loads(current_cached_value.decode('utf-8')), True)
    else:
        print('New image URL detected, processing new image..')
        prediction = process_new_image(image_url)
        REDIS_CLIENT.set(
            image_url_hashed,
            json.dumps(prediction),
            ex=3600,
        )
        return (prediction, False)


def classify_image(image_url):
    print("Classifying image from URL {}..".format(image_url))
    start_time = datetime.datetime.now()
    prediction, was_cached = get_prediction_cached(image_url)
    end_time = datetime.datetime.now()
    processing_time_seconds = (end_time-start_time).total_seconds()
    print("Time to process {url}: {seconds}s".format(
        url=image_url,
        seconds=processing_time_seconds,
    ))
    return {
        'classification': prediction['prediction'],
        'confidence': prediction['confidence'],
        'processing_time': processing_time_seconds,
        'cached': was_cached,
    }
