import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    id__in = django_filters.BaseInFilter(field_name='id', lookup_expr='in')
    stones = django_filters.BaseInFilter(field_name='stones__slug', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['id', 'id__in', 'stones']

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        if 'stones' in self.form.cleaned_data and self.form.cleaned_data['stones']:
            return queryset.distinct()
        return queryset