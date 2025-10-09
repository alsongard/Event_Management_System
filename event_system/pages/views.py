from django.shortcuts import render
from event_app.models import EventSchema
from event_app.serializers import UserEventViewSerializer
# Create your views here.
def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def service_view(request):
    return render(request, 'service.html')

def home_view(request):
    return render(request, 'base.html')

def user_view_events(request):
    events_data = EventSchema.objects.all()
    print("events_data")    
    print(events_data)    


    return render(request, 'user_event.html', {'events_data':events_data})