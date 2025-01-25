from rest_framework import viewsets
from .models import Venue, EventSession
from .serializers import VenueSerializer, EventSessionSerializer
from .custom_permissons import IsEventOwner
from events.models import Event
from rest_framework import serializers

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

    def get_queryset(self):
        # Filter venues to only show venues of events owned by the current user
        return Venue.objects.filter(event__owner=self.request.user)

    def perform_create(self, serializer):
        # Ensure the venue is created only for the current user's event
        event = Event.objects.filter(
            owner=self.request.user, 
            id=serializer.validated_data['event'].id
        ).first()
        
        if not event:
            raise serializers.ValidationError(
                "You can only create venues for your own events"
            )
        
        serializer.save()

class EventSessionViewSet(viewsets.ModelViewSet):
    queryset = EventSession.objects.all()
    serializer_class = EventSessionSerializer

    def get_queryset(self):
        # Filter sessions to only show sessions of events owned by the current user
        return EventSession.objects.filter(event__owner=self.request.user)

    def perform_create(self, serializer):
        # Ensure the session is created only for the current user's event
        event = Event.objects.filter(
            owner=self.request.user, 
            id=serializer.validated_data['event'].id
        ).first()
        
        if not event:
            raise serializers.ValidationError(
                "You can only create sessions for your own events"
            )
        
        serializer.save()

