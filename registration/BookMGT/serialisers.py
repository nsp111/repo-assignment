from rest_framework import serializers
from .models import *

class Books_Serialiser(serializers.ModelSerializer):
    class Meta:
        models=Books
        fields='__all__'

class feedback_Serialiser(serializers.ModelSerializer):
    class Meta:
        models=feedback
        fields='__all__'
        
class Fine_Serialiser(serializers.ModelSerializer):
    class Meta:
        models=Fine
        fields='__all__'