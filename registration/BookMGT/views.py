from django.shortcuts import render
from .serialisers import *
from .models import *
from rest_framework import generics

class list_Books(generics.ListAPIView):
    queryset=Books.objects.all()
    serializer_class=Books_Serialiser

class Read_Books(generics.RetrieveAPIView):
    queryset=Books.objects.all()
    serializer_class=Books_Serialiser

class Create_Books(generics.CreateAPIView):
    queryset=Books.objects.all()
    serializer_class=Books_Serialiser

class Update_Books(generics.UpdateAPIView):
    queryset=Books.objects.all()
    serializer_class=Books_Serialiser

class Delete_Books(generics.DestroyAPIView):
    queryset=Books.objects.all()
    serializer_class=Books_Serialiser

