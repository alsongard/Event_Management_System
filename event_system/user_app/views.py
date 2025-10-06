from django.shortcuts import render

from rest_framework import generics
# Create your views here.

from .forms import UserRegistrationForm

def user_registration_view(request, *args, **kwargs):
    myForm = UserRegistrationForm()
    if request.method == 'POST':
        myFormData = UserRegistrationForm(request.POST)
        if myFormData.is_valid():
            myFormData.save()

    return render(request, 'userreg.html', {'form':myForm})




def user_details_reg_view(request, *args, **kwargs):
    
    return render(request, 'userdetails.html', {})