from rest_framework import filters
from .models import TYPES

class TypeFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        type_label = request.query_params.get('type')
        if type_label:
            type_mapping = dict(TYPES)
            type_value = [key for key, value in type_mapping.items() if type_label.lower() in value.lower()]
            if type_value:
                return queryset.filter(type__in=type_value)
            else:
                return queryset.none()
        return queryset
