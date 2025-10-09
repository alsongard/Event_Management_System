from django import forms

from .models import UserRegModel, UserDetailsModel

class UserRegistrationForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={"background-color":"red", "class":"border-[1px] border-gray-300 rounded-md py-[5px] pl-[5px] w-full"}))
    # email  = forms.EmailField(widget=forms.EmailInput(attrs={"class":"border-[1px] border-gray-300 rounded-md py-[5px] pl-[5px] w-full"}))
    # password = forms.CharField(widget=forms.TextInput(attrs={"class":"border-[1px] border-gray-300 rounded-md py-[5px] pl-[5px] w-full"}))
    # confirm_password = forms.CharField(widget=forms.TextInput(attrs={"class":"border-[1px] border-gray-300 rounded-md py-[5px] pl-[5px] w-full"}))
    # phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"border-[1px] border-gray-300 rounded-md py-[5px] pl-[5px] w-full"}))
    class Meta:
        model = UserRegModel
        fields = [
            'email',
            'username',
            'password',
            'confirm_password',
            'password',
            'phoneNumber',
        ]
        widgets = {
            "email":forms.EmailInput(attrs={"background-color":"red", "class":"border-[1px] border-gray-300 rounded-md py-[5px] pl-[5px] w-full"}),
            "username":forms.TextInput(attrs={"class":"border-[1px] border-gray-300 rounded-md py-[5px] pl-[5px] w-full"}),
            "password":forms.TextInput(attrs={"class":"border-[1px] border-gray-300 rounded-md py-[5px] pl-[5px] w-full"}),
            "confirm_password":forms.TextInput(attrs={"class":"border-[1px] border-gray-300 rounded-md py-[5px] pl-[5px] w-full"}),
            "phoneNumber":forms.TextInput(attrs={"class":"border-[1px] border-gray-300 rounded-md py-[5px] pl-[5px] w-full"}),
        }


    def clean(self):
        cleaned_data = super().clean()
        print('cleaned_data')
        print(cleaned_data)

        if cleaned_data["password"] != cleaned_data['confirm_password']:
            self.add_error('confirm_password', 'Paswords do not match')
            # raise forms.ValidationError("Password do not match!")
        return cleaned_data






class UserDetailsRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserDetailsModel
        fields = [
            'user',
            'age',
            'gender',
            'organization',
            'address',
        ]
        widgets = {
            'user':forms.TextInput(attrs={}),
            'age':forms.NumberInput(attrs={}),
            'gender':forms.Select(),
            'organization':forms.Select(),
            'address':forms.TextInput(),
        }



class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserRegModel
        fields = [
            'email',
            'password',
        ]
        widgets = {
            "email":forms.TextInput(attrs={"background-color":"red", "class":"border-[1px] border-gray-300 rounded-md py-[5px] pl-[5px] w-full"}),
            "password":forms.TextInput(attrs={"class":"border-[1px] border-gray-300 rounded-md py-[5px] pl-[5px] w-full"}),
        }
    
