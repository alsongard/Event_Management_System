from django.urls import path, include
from .views import user_registration_view

urlpatterns = [
    path("", user_registration_view, name="userreg"),
]