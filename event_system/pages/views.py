from django.shortcuts import render

# Create your views here.
def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def service_view(request):
    return render(request, 'service.html')

def home_view(request):
    return render(request, 'base.html')