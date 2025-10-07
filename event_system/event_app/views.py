from django.shortcuts import render
from rest_framework import generics

from .models import EventSchema
from .serializers import EventCreateSerializer

class EventCreateAPIView(generics.CreateAPIView):
    queryset = EventSchema.objects.all()
    serializer_class = EventCreateSerializer

class EventReviewAPIView(generics.RetrieveAPIView):
    queryset = EventSchema.objects.all()
    serializer_class = EventCreateSerializer


class EventViewAPIVIEW(generics.ListAPIView):
    queryset = EventSchema.objects.all()
    serializer_class  = EventCreateSerializer


class EventUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = EventSchema.objects.all()
    serializer_class  = EventCreateSerializer


class EventDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = EventSchema.objects.all()
    serializer_class  = EventCreateSerializer