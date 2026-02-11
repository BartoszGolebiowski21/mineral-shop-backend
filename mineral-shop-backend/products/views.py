from rest_framework import generics
from .models import Product, Stone, Category
from .serializers import ProductListSerializer, ProductDetailSerializer, StoneSerializer, \
    CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.prefetch_related("images")
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.select_related(
    "category",
    "size"
).prefetch_related(
    "stones",
    "images"
)
    serializer_class = ProductDetailSerializer
    lookup_field = "slug"


class StoneListAPIView(generics.ListAPIView):
    queryset = Stone.objects.all().order_by('name')
    serializer_class = StoneSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
