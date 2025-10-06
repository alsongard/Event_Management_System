from django.urls import path, include
from .views import about_view, contact_view, service_view
urlpatterns = [
    path('about/', about_view , name="about"),
    path('service/', service_view , name="service"),
    path('contact/', contact_view , name="contact"),
]