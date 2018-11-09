from rest_framework import serializers

from classifier.models import Classification


class CreateClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ('image_url',)
