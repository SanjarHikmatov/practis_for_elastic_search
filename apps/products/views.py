from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializer import ProductSerializer
from apps.products.filter import ProductFilter
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'description', 'brand', 'color', 'sku']
    filterset_class = ProductFilter

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('price_min', openapi.IN_QUERY, description="Minimum price", type=openapi.TYPE_NUMBER),
        openapi.Parameter('price_max', openapi.IN_QUERY, description="Maximum price", type=openapi.TYPE_NUMBER),
        openapi.Parameter('discount_price_min', openapi.IN_QUERY, description="Minimum discount price", type=openapi.TYPE_NUMBER),
        openapi.Parameter('discount_price_max', openapi.IN_QUERY, description="Maximum discount price", type=openapi.TYPE_NUMBER),
        openapi.Parameter('created_at_after', openapi.IN_QUERY, description="Created at after (YYYY-MM-DD)", type=openapi.TYPE_STRING, format='date'),
        openapi.Parameter('created_at_before', openapi.IN_QUERY, description="Created at before (YYYY-MM-DD)", type=openapi.TYPE_STRING, format='date'),
        openapi.Parameter('is_active', openapi.IN_QUERY, description="Is active", type=openapi.TYPE_BOOLEAN),
        openapi.Parameter('is_featured', openapi.IN_QUERY, description="Is featured", type=openapi.TYPE_BOOLEAN),
        openapi.Parameter('category', openapi.IN_QUERY, description="Category ID", type=openapi.TYPE_INTEGER),
        openapi.Parameter('brand', openapi.IN_QUERY, description="Brand name contains", type=openapi.TYPE_STRING),
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
