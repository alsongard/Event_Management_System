from django.db import models

# Create your models here.
class UserData(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(null=False, blank=False, max_length=20)
    password = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"