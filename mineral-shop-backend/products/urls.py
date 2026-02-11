from django.urls import path
from .views import ProductDetailAPIView, ProductListAPIView, StoneListAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<slug:slug>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('stones/', StoneListAPIView.as_view(), name='stone-list'),
]

