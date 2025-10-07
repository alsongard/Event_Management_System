from django.urls import path, include


from .views import user_registration_view
urlpatterns = [
    path("registerUser/", user_registration_view, name="registerUser"),
]

"""

urls: user
- register accoutn
- login account
- reset password
- perfrom verification:accountVerified
"""