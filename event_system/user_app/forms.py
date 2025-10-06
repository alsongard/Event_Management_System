from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name"}))
    email  = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"password"}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"confirm password"}))
    phone_number = forms.IntegerField(widget=forms.NumberInput())




    def password_check(self):
        pass




class UserDetailsRegistrationForm(forms.Form):
    age = forms.IntegerField(widget=forms.NumberInput)
    gender = forms.CharField(widget=forms.Select())
    organization = forms.CharField(widget=forms.Select())
    address = forms.Textarea()