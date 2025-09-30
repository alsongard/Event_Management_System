from django.urls import path

from .views import event_view


urlpatterns = [
    path('events/', event_view, name="events"),
]