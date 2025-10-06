from django.db import models

# Create your models here.
class EventSchema(models.Model):
    EVENT_CHOICES = [
        ("wedding", "wedding"),
        ("conference", "conference"),
        ("birthday", "birthday")
    ]

    event_id = models.CharField(max_length=100, null=False, blank=False)
    event_title = models.CharField(max_length=50)
    event_type = models.CharField(choices=EVENT_CHOICES, max_length=100)
    event_location = models.CharField(max_length=100)
    event_start_time = models.DateTimeField()
    event_end_time = models.DateTimeField()
    event_attendees = models.IntegerField()
    event_description = models.CharField(max_length=800)
    event_price = models.IntegerField(max_length=10000000,null=False, blank=False, default=0)