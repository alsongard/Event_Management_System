from rest_framework import serializers

from .models import UserRegModel, UserDetailsModel
# for adding user serializer
# for deleteing use serializer
# for updating user details : 

class UserCreate(serializers.ModelSerializer):
    class Meta:
        model = UserRegModel
        fields = '__all__'



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetailsModel
        fields = '__all__'