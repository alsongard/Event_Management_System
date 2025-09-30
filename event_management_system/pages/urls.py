from django.urls import path
from .views import about_view, services_view, contact_view
urlpatterns = [
    path('about/', about_view, name="about"),
    path("services/", services_view, name="services"),
    path('contact/', contact_view, name="contact")
]