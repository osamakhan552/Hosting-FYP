from django.urls import path,include
from .views import *


urlpatterns = [
    path('',usersListAPIView.as_view()),
]