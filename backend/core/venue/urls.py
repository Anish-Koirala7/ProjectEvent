from rest_framework.routers import DefaultRouter
from .api import VenueViewSet, EventSessionViewSet
from django.urls import include, path

router = DefaultRouter()

router.register(r'venues', VenueViewSet)
router.register(r'sessions', EventSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
