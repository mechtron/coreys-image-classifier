# -*- coding: utf-8 -*-

def classify_image(image_url):
    print("Classifying image from URL {}..".format(image_url))
    return {
        'classification': 'cat',
        'confidence': 0.123,
        'processing_time': 4.567,
    }
