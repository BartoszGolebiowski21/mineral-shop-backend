from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
