import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    id__in = django_filters.BaseInFilter(field_name='id', lookup_expr='in')
    stones = django_filters.BaseInFilter(field_name='stones__slug', lookup_expr='in')
    categories = django_filters.BaseInFilter(field_name='category__slug', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['id']

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset).distinct()