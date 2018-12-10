# -*- coding: utf-8 -*-
from django.db.models import (
    Avg,
    Count,
    Max,
    Min,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from classifier.models import Classification
from report.authorization import UserIsShotCaller


class CreateReport(APIView):
    # permission_classes = (UserIsShotCaller,)
    permission_classes = ()

    def get(self, request):
        top_ten_classifications = (
            Classification.objects.values('image_url')
            .annotate(classification_count=Count('image_url'))
            .annotate(processing_time_avg=Avg('processing_time'))
            .annotate(processing_time_max=Max('processing_time'))
            .annotate(processing_time_min=Min('processing_time'))
            .order_by('-classification_count')[:10]
        )
        return Response(top_ten_classifications, status=status.HTTP_200_OK)
