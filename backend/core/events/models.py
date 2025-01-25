from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class Event(models.Model):
    cover_img = models.ImageField(upload_to="images/events" ,blank = True)
    title = models.CharField(max_length= 112)
    content = models.TextField()
    owner = models.ForeignKey(User ,on_delete = models.CASCADE)
    p_date = models.DateTimeField( editable=False ,null = True)
    event_date = models.DateTimeField( null = True)
    u_date = models.DateTimeField( null  = True)

    

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.p_date = timezone.now()
        self.u_date = timezone.now()
        return super(Event, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-p_date']  # Order by publish date descending


class Like(models.Model):
    owner = models.ForeignKey(User ,on_delete = models.CASCADE,related_name='likes')
    event = models.ForeignKey(Event ,on_delete = models.CASCADE,related_name='likes' )
    like = models.BooleanField()
    




