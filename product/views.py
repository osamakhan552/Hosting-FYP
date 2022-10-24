from django.shortcuts import render
from rest_framework import status,generics,filters
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class createProduct(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['^prodName','^prodNumber']

    queryset = product.objects.all()
    serializer_class = productSerializer




