from rest_framework import serializers
from .models import EventSchema


class EventCreateSerializer(serializers.ModelSerializer): # serializer used when creating an event
    class Meta:
        myModel = EventSchema
        fields = '__all__'


class UserEventViewSerializer(serializers.ModelSerializer): # serializer will be used when the user views events
    class Meta: 
        myModel = EventSchema
        fields = [
            'event_id',
            'event_title',
            'event_type',
            'event_location',
            'event_start_time',
            'event_end_time',
            'event_description',
            'event_price'
        ]

class EventAmdinViewSerializer(serializers.ModelSerializer):
    class Meta:
        myModel = EventSchema
        fields = '__all__'