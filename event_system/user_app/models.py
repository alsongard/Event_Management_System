from django.db import models

# Create your models here.
class UserRegModel(models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=50)
    isAccountVerified = models.BooleanField(default=False)
    # verifyOTP = models.CharField(max_length=6, blank=True, null=True, default='')


    # to create foreignKey we use
    # models.ForeignKey(ModelName, on_delete=behavior, related_name="")
    def __str__(self):
        return f"email:{self.email}\nusername:{self.username}\npassword:{self.password}\nphoneNumber:{self.phoneNumber}\nisAccountVerified:{self.isAccountVerified}"

class UserDetailsModel(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    ORGANIZATION_CHOICES = [
        ('Public', 'Public'),
        ('Private', 'Private'),
        ('International', 'International'),
        ('NGO', 'NGO'),
    ]
    user = models.ForeignKey(UserRegModel, on_delete=models.CASCADE, related_name='details') # instead of using UserDetailsModelInstance.UserRegModel_set.all() for reverse relation
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    organization = models.CharField(max_length=50, choices=ORGANIZATION_CHOICES)
    address = models.TextField()




