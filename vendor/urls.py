from django.urls import path
from .views import *

urlpatterns = [
    path('vendorMaster',createVendor.as_view()),
    path('order',createOrder.as_view()),
    path('orderReceived',createOrderReceived.as_view()),
    path('VendorMaster/<uuid:vendorId>',vendorApiView.as_view()),
    path('order/<uuid:orderId>',orderApiView.as_view()),
    path('orderReceived/<uuid:orderNumber>',orderReceivedApiView.as_view()),
    path('receivedOrder',onlyReceivedOrder),
]