from django.db import models

# Create your models here.
class EventSchema(models.Model):
    EVENT_CHOICES = [
        ("Wedding", "wedding"),
        ("Conference", "conference"),
        ("Birthday Party", "birthday"),
        ("Corporate Retreat", "corporate_retreat"),
        ("Product Launch", "product_launch"),
        ("Seminar", "seminar"),
        ("Networking Event", "networking"),
        ("Charity Gala", "charity_gala"),
        ("Fundraiser", "fundraiser"),
        ("Trade Show", "trade_show"),
        ("Concert", "concert"),
        ("Festival", "festival"),
        ("Sports Event", "sports_event"),
        ("Workshop", "workshop"),
        ("Award Ceremony", "award_ceremony"),
        ("Team Building", "team_building")
    ]   

    event_id = models.CharField(max_length=100, null=False, blank=False)
    event_title = models.CharField(max_length=50)
    event_type = models.CharField(choices=EVENT_CHOICES, max_length=100)
    event_location = models.CharField(max_length=100)
    event_start_time = models.DateTimeField()
    event_end_time = models.DateTimeField()
    event_attendees = models.IntegerField()
    event_description = models.CharField(max_length=800)
    event_price = models.IntegerField(null=False, blank=False, default=0)