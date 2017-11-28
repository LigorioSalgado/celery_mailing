from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
# Create your views here.




class CreateUser(generics.CreateAPIView):

    serializer_class = UserSerializer
    queryset =User.objects.all()x