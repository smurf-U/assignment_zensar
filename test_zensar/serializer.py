from rest_framework import serializers
from .models import RouterManager

class RouterManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouterManager
        fields = "__all__"
        
