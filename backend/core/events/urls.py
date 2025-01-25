from rest_framework import routers
from django.urls import path, include
from .api import EventViewSet

router = routers.DefaultRouter()

router.register(r'events', EventViewSet ,basename='events')

urlpatterns = [
    path('', include(router.urls)),
]