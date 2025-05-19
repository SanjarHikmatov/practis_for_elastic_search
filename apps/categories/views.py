from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.categories.models import Category
from apps.categories.serializer import CategorySerializer
from apps.categories.filter import CategoryFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']
    filterset_class = CategoryFilter

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY, description="Filter by name contains", type=openapi.TYPE_STRING),
            openapi.Parameter('description', openapi.IN_QUERY, description="Filter by description contains", type=openapi.TYPE_STRING),
            openapi.Parameter('is_active', openapi.IN_QUERY, description="Filter by active status", type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('created_at_after', openapi.IN_QUERY, description="Created at after date", type=openapi.TYPE_STRING, format='date'),
            openapi.Parameter('created_at_before', openapi.IN_QUERY, description="Created at before date", type=openapi.TYPE_STRING, format='date'),
            openapi.Parameter('parent', openapi.IN_QUERY, description="Filter by parent category id", type=openapi.TYPE_INTEGER),
        ]
    )

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
