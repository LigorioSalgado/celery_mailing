from rest_framework import serializers
from django.contrib.auth.models import User
from .tasks import send_mail


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name') 
    

    def create(self,validated_data):
        send_mail.delay(validated_data['email'],
        validated_data['first_name'],
        validated_data['last_name'])
        return User.objects.create_user(**validated_data) 