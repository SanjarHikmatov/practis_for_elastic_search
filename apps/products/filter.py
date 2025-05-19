from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter, BooleanFilter, CharFilter, DateFromToRangeFilter
from .models import Product


class ProductFilter(FilterSet):
    price_min = NumberFilter(field_name="price", lookup_expr='gte')
    price_max = NumberFilter(field_name="price", lookup_expr='lte')
    discount_price_min = NumberFilter(field_name="discount_price", lookup_expr='gte')
    discount_price_max = NumberFilter(field_name="discount_price", lookup_expr='lte')
    created_at = DateFromToRangeFilter()
    is_active = BooleanFilter()
    is_featured = BooleanFilter()
    category = NumberFilter(field_name='category__id')
    brand = CharFilter(field_name='brand', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['category', 'price', 'discount_price', 'is_active', 'is_featured', 'brand', 'created_at']
