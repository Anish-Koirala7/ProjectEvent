from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    image = models.ImageField(upload_to="images/accounts" ,blank = True)
    sex = models.CharField(max_length = 112)
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    role = models.CharField(max_length=9, default='Attendee')

    def __str__(self):
        return self.user.username