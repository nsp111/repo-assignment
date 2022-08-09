from django.shortcuts import render
from .serializers import userSerializer
from .models import *
from rest_framework import generics

class List_User(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=userSerializer

class Read_User(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=userSerializer

class Create_User(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=userSerializer

class Update_User(generics.UpdateAPIView):
    queryset=User.objects.all()
    serializer_class=userSerializer

class Delete_User(generics.DestroyAPIView):
    queryset=User.objects.all()
    serializer_class=userSerializer

