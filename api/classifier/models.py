# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from classifier.services import classify_image


TYPES = (
    ('new', 'Image URL being processed for the first time'),
    ('cached', 'Image URL was previously processed'),
)


class Classification(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image_url = models.TextField()
    result = models.TextField(max_length=32)
    confidence = models.DecimalField(max_digits=16, decimal_places=4)
    processing_type = models.TextField(choices=TYPES)
    processing_time = models.DecimalField(max_digits=16, decimal_places=4)
