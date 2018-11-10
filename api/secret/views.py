# -*- coding: utf-8 -*-
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class Secret(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return HttpResponse(
            "Hi {}\n".format(request.user),
            status=status.HTTP_200_OK,
        )
