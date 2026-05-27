from django.urls import path
from .views import CategoryListAPIView, ProductDetailAPIView, ProductListAPIView, StoneListAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<slug:slug>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('stones/', StoneListAPIView.as_view(), name='stone-list'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list')
]

