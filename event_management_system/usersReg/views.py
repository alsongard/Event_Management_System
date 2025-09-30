from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .forms import UserRegistrationForm

def home_view(request, *args, **kwargs):
    return render(request, "base.html")


def user_registration_view(request, *args, **kwargs):
    myForm = UserRegistrationForm(request.POST)

    if myForm.is_valid():
        print("User has been successfully registered!")
        return redirect("Success")
    else:
        usersForm = UserRegistrationForm()
    return render(request, "user.html", {"form":usersForm})
