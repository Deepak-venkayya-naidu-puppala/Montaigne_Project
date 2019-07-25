from rest_framework import serializers
from .models import JSONFileUpload, URLModel

class PostJSONDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = JSONFileUpload
        fields = "__all__"


class GetJsonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLModel
        fields = "__all__"