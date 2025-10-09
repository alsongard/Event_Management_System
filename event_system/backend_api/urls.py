"""
URL configuration for backend_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view, name='home' ),
    path("accounts/", include("django.contrib.auth.urls"), name="accounts"),
    path("api/", include('rest_framework.urls'), name="rest_api"),
    path("", include('pages.urls')),  # Include the pages app URLs
    path("", include("user_app.urls")),
    path("event/", include("event_app.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
