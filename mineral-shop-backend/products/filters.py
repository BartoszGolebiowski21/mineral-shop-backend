import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    id__in = django_filters.BaseInFilter(field_name='id', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['id', 'id__in']