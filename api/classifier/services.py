# -*- coding: utf-8 -*-
import random

def classify_image(image_url):
    print("Classifying image from URL {}..".format(image_url))
    return {
        'classification': random.choice(
            ['cat', 'moose', 'house', 'car', 'phone', 'coffee']
        ),
        'confidence': random.uniform(0, 1.0),
        'processing_time': random.uniform(3, 10),
    }
