from django.shortcuts import render, redirect
from django.forms import ModelForm
from rest_framework import generics
# Create your views here.
from django.contrib.auth.hashers import make_password 
from .forms import UserRegistrationForm, UserLoginForm

def user_registration_view(request, *args, **kwargs):
    myForm = UserRegistrationForm()
    if request.method == 'POST':
        print('request method is POST')
        myForm = UserRegistrationForm(request.POST)
        if myForm.is_valid():
            myData = myForm.save()
            myData.password = make_password(myForm.cleaned_data.get("password"))
            myData.save()
            return redirect("home")
            # ALL FORM VALIDATION PROCESS SHOULD BE DONE IN MODELS.PY
            # # user_email = myForm.cleaned_data.get("email") # testing:working
            # # print(f'user_email: {user_email}') # testing:working
            # password = myForm.cleaned_data.get("password")
            # confirm_password = myForm.cleaned_data.get("confirm_password")
            # if password != confirm_password:
            #     form.raise
    return render(request, 'userreg.html', {'form':myForm})


def user_login_view(request, *args, **kwargs):
    myLoginForm = UserLoginForm()

    if request.method == 'POST':
        pass

    return render(request, 'login.html', {"form":myLoginForm})


def user_details_reg_view(request, *args, **kwargs):
    return render(request, 'userdetails.html', {})