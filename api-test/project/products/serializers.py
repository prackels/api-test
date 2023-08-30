from .models import *
from rest_framework import serializers

class iphoneserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= iphone
        fields= '__all__'