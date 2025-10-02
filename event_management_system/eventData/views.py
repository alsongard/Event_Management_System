from django.shortcuts import render


from .forms import EventForm
# Create your views here.
def create_event(request, *args, **kwargs):
    myForm = EventForm()
    return render(request, 'event_trial.html',{"form":myForm} )