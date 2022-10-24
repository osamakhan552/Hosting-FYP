from django.urls import path,include
from .views import *

urlpatterns = [
    path('',createProduct.as_view()),
]

