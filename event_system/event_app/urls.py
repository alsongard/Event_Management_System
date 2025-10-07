from django.urls import path
from .views import EventCreateAPIView, EventReviewAPIView, EventViewAPIVIEW, EventDeleteAPIView, EventUpdateAPIView

urlpatterns = [
    path("createEvent/", EventCreateAPIView.as_view(), name="create_event"),
    path("reviewEvent/<int:pk>", EventReviewAPIView.as_view(), name="review"),
    path("getEvents/",EventViewAPIVIEW.as_view(), name="getEventDetails"),
    path("deleteEvent/<int:pk>", EventDeleteAPIView.as_view(), name="deleteEvent"),
    path("updateEvent/<int:pk>", EventUpdateAPIView.as_view(), name="updateEvent")
]