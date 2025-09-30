from django.db import models

# Create your models here.
# Create your views here.
class EventSchema(models.Model):
    event_title = models.CharField(max_length=20)
    event_start_time = models.DateField()
    event_end_time = models.DateField()
    event_description = models.TextField()
    event_attendees = models.IntegerField()


