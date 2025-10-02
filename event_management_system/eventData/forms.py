from django import forms


from .models import EventSchema
class EventForm(forms.Form):
    event_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Event Title','class':"w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"}))
    event_type = forms.CharField(widget=forms.Select(choices=EventSchema.EVENT_CHOICES, attrs={'placeholder':'Event Title','class':"w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"}))
    event_location = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Event Location','class':"w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"}))
    event_start_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder':'Event Start Time','class':"w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"}))
    event_end_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder':'Event End Time','class':"w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"}))
    event_attendees = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Number of Attendees','class':"w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"}))
    event_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Event Description','class':"w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"}))
