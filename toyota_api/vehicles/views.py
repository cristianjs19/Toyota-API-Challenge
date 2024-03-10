from rest_framework import mixins, viewsets
from rest_framework import filters
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.decorators import method_decorator

from .models import Vehicle
from .serializers import VehicleListSerializer, VehicleDetailSerializer
from .filters import TypeFilterBackend


order_by = openapi.Parameter('order_by', openapi.IN_QUERY, description="price, -price, year, -year", type=openapi.TYPE_STRING)
type = openapi.Parameter('type', openapi.IN_QUERY, description="Autos, Pickup, SUV", type=openapi.TYPE_STRING)

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="List vehicles, filter, and order queryset",
    manual_parameters=[order_by, type]
))
class VehiclesListRetrieveView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    filter_backends = [TypeFilterBackend, filters.SearchFilter]
    search_fields = ['type']

    def get_queryset(self):
        order_qs = self.request.query_params.get('order_by', None)
        if order_qs:
            queryset = Vehicle.objects.filter(active=True).order_by(order_qs)
        else:
            queryset = Vehicle.objects.filter(active=True)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            serializer_class = VehicleListSerializer
        else:
            serializer_class = VehicleDetailSerializer
        return serializer_class

