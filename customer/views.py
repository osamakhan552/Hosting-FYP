from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics,status,filters
from .models import *
from .serializer import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class createCustomer(generics.ListCreateAPIView):

    authorization_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = customerSerializer
    queryset = customer.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['^custFname','^custEmail','^custPhone']

    def post(self, request,format = None):
        request.data.update({'createdBy':request.user.empId})
        print(request.data)
        customer = customerSerializer(data = request.data)
        print(customer.is_valid())
        if customer.is_valid():
       
            customer.save()
        
            return Response(customer.data,status = status.HTTP_201_CREATED)
        return Response(customer.errors,status = status.HTTP_400_BAD_REQUEST)