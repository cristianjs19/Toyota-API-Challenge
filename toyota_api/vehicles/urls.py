from rest_framework import routers

from .views import VehiclesListRetrieveView

router = routers.SimpleRouter()
router.register(r'vehicles', VehiclesListRetrieveView, basename="vehicles")

app_name = 'vehicles'
urlpatterns = router.urls