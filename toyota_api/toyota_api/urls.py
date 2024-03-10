from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

URL_API_BASE_V1 = 'api/v1/'

schema_view = get_schema_view(
    openapi.Info(
        title="Toyota challenge API",
        default_version='v1',
        description="Toyota challenge API"
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path(URL_API_BASE_V1 + 'vehicles/', include('vehicles.urls', namespace='vehicles')),

    # Docs
    re_path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

