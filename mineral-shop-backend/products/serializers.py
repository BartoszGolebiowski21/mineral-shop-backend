from rest_framework import serializers
from .models import Product, Image


class ImageSerializer(serializers.ModelSerializer):
    upload = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = ['id', 'upload']

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'images']
