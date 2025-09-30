from django import forms


class EventForm(forms.Form):
    EventTitle = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Event Title','class':"w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"}))
    EventStartDate = forms.DateField()
    EventEndDate = forms.DateField()
    EventDescription = forms.CharField(widget=forms.Textarea())
    EventAttendeesNum = forms.IntegerField()

