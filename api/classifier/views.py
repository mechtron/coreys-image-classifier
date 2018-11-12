# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from classifier.models import Classification
from classifier.serializers import CreateClassificationSerializer
from classifier.services import classify_image


class CreateClassification(CreateAPIView):
    queryset = Classification.objects.all()
    serializer_class = CreateClassificationSerializer

    def post(self, request):
        serializer = CreateClassificationSerializer(data=request.data)
        if serializer.is_valid():
            classification = classify_image(serializer.validated_data['image_url'])
            serializer.save(
                result=classification['classification'],
                confidence=classification['confidence'],
                processing_time=classification['processing_time'],
                processing_type='new',
            )
            response_data = {
                'classification': classification['classification'],
                'confidence': classification['confidence'],
                'processing_time': classification['processing_time'],
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
