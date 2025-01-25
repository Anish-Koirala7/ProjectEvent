from django.db import models
from events.models import Event

class Venue(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='venues')
    name = models.CharField(max_length=200)
    address = models.TextField()
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.name

    
class EventSession(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='sessions', null=True, blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='sessions', null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    available_seats = models.IntegerField()
    
    def __str__(self):
        return f"{self.event.name} - Session"

