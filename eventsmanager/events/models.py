from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Events(models.Model):

    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    attendees = models.ManyToManyField(User, related_name='events_attendees')

    def __str__(self):
        return self.name
    
    
    