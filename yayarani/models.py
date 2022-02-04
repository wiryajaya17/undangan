from django.db import models
from django.utils import timezone

# Create your models here.

class Rsvp(models.Model):
    owner = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    num_of_rsvp = models.IntegerField()
    flag_attending = models.CharField(max_length=1)
    message_body = models.CharField(max_length=200)
    post_date = models.DateTimeField(default=timezone.now)
