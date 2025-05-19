from django_filters.rest_framework import (
    FilterSet, CharFilter,
    BooleanFilter, DateFromToRangeFilter, NumberFilter)

from apps.categories.models import Category


class CategoryFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')
    is_active = BooleanFilter()
    created_at = DateFromToRangeFilter()
    parent = NumberFilter(field_name='parent__id')

    class Meta:
        model = Category
        fields = ['name', 'description', 'is_active', 'created_at', 'parent']
