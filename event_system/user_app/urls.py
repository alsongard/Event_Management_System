from django.urls import path, include


from .views import user_registration_view, user_login_view
urlpatterns = [
    path("registerUser/", user_registration_view, name="registerUser"),
    path("loginUser/", user_login_view, name="loginUser",)
]

"""

urls: user
- register accoutn
- login account
- reset password
- perfrom verification:accountVerified
"""