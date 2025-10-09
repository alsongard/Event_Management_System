from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EventSchema
from django.http import JsonResponse
from .serializers import EventCreateSerializer, UserEventViewSerializer

class EventCreateAPIView(generics.CreateAPIView):
    queryset = EventSchema.objects.all()
    serializer_class = EventCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventReviewAPIView(generics.RetrieveAPIView):
    queryset = EventSchema.objects.all()
    serializer_class = EventCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventViewAPIVIEW(generics.ListAPIView):
    queryset = EventSchema.objects.all()
    serializer_class  = EventCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = EventSchema.objects.all()
    serializer_class  = EventCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = EventSchema.objects.all()
    serializer_class  = EventCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(["GET"])
def get_all_events(request, *args, **kwargs):
    events = EventSchema.objects.all()
    serializer = UserEventViewSerializer(events, many=True)
    print(f'serializer response')
    print(f'{serializer.data}')
    # return JsonResponse(serializer.data, safe=False)
    return Response(serializer.data)