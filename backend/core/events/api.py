from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Event 
from .serializers import EventSer
from .custom_permissions import isOwnerOrReadOnly
from rest_framework import filters
from rest_framework import pagination

from .pagination import MyPagination

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly ,
        isOwnerOrReadOnly,    
    ]
    pagination_class = MyPagination
    filter_backends = [filters.OrderingFilter]
    ordering = ['-p_date']

    def perform_create(self ,serializer):
        serializer.save(owner = self.request.user)

    @action(detail = True, url_path='own-feed', url_name='own_feed')
    def get_user_events(self , request ,pk = None):
        owner = get_object_or_404(User , pk = pk)
        owner_events = Event.objects.filter(owner = owner.id)
        serializer = EventSer(owner_events , many = True)
        return Response(serializer.data)

