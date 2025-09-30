from django import forms

class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name"}))
    middle_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Middle Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Last Name"}))
    email  = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"password"}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"confirm password"}))
    phone_number = forms.IntegerField(widget=forms.NumberInput())




    def password_check(self):
        pass