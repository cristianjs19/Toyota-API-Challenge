from rest_framework import mixins, viewsets
from rest_framework import filters
from drf_yasg.utils import swagger_auto_schema

from .models import Vehicle
from .serializers import VehicleListSerializer, VehicleDetailSerializer


class VehiclesListRetrieveView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Vehicle.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            serializer_class = VehicleListSerializer
        else:
            serializer_class = VehicleDetailSerializer
        return serializer_class

