from rest_framework import serializers
from .models import Venue
from .models import EventSession

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'
        extra_kwargs = {
            'event': {'required': True}
        }

class EventSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSession
        fields = '__all__'
        extra_kwargs = {
            'event': {'required': True},
            'venue': {'required': True}
        }
