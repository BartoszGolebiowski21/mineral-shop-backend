from rest_framework import serializers
from .models import Category, Product, Image, Size, Stone


class ImageSerializer(serializers.ModelSerializer):
    upload = serializers.ImageField(use_url=True)

    class Meta:
        model = Image
        fields = ['id', 'upload']


class ProductListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'slug', 'name', 'price', 'images']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class StoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stone
        fields = ["id", "name"]


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["id", "name"]


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    stones = StoneSerializer(many=True, read_only=True)
    size = SizeSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'slug',
            'name',
            'price',
            'images',
            'category',
            'stones',
            'description',
            'size'
        ]
