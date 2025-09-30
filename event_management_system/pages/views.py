from django.shortcuts import render

# Create your views here.
def about_view(request, *args, **kwargs):
    return render(request, 'about.html')

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html')

def services_view(request, *args, **kwargs):
    return render(request, 'services.html')



