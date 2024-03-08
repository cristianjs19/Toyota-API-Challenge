from rest_framework import mixins, viewsets
from rest_framework import filters
from drf_yasg.utils import swagger_auto_schema

from .models import Vehicle
from .serializers import VehicleListSerializer, VehicleDetailSerializer
from .filters import TypeFilterBackend


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

