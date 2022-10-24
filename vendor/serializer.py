from rest_framework import serializers
from .models import *

class vendorWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VendorMaster
        fields = '__all__'


class orderWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'


class orderReceivedWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderReceived
        fields = '__all__'
        dept = 2

class vendorReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VendorMaster
        fields = '__all__'
        dept = 2


class orderReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'
        dept = 1

class orderReceivedReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderReceived
        fields = '__all__'
        dept = 2