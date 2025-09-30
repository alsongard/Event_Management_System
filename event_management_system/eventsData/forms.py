from django import forms
class EventForm(forms.Form):
    event_title =  forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Event title..."}))
    event_start_time = forms.DateField(widget=forms.DateTimeInput())
    event_end_time = forms.DateField(widget=forms.DateTimeInput())
    event_description = forms.CharField(widget=forms.Textarea())
    event_attendees = forms.IntegerField(widget=forms.NumberInput())
