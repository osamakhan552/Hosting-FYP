from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from employee.models import *


class employeeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ('username','email','password','is_active','empCbid','empId','empFname','empLname','empPhone','createdBy','roleId')
        read_only_fields = ['is_active']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4,'required': False},'username': {'required': False},'email': {'required': False}}
class employeeReadSerializer(serializers.ModelSerializer):
    class Meta(employeeWriteSerializer.Meta):
        depth = 1