from rest_framework import serializers
from . models import feed

class feedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = feed
        fields = '__all__'
