from django.db import models
from django.db.models.deletion import CASCADE
import uuid
from employee.models import employee, roles
from product.models import product
from django.core.validators import MinLengthValidator
# Create your models here.

class VendorMaster(models.Model):
    vendorId = models.UUIDField(default = uuid.uuid4, primary_key=True, editable = False)
    vendorCode = models.CharField(max_length=255, default=0, unique=True)
    vendorName = models.CharField(max_length=255)
    vendorAddress = models.TextField()
    vendorPrimaryName = models.CharField(max_length=255, null=True, blank=True)
    vendorPrimaryEmail = models.CharField(max_length=255, null=True, blank=True)
    vendorPrimaryPhone = models.CharField(max_length=10,null=True, blank=True)
    vendorSecondaryEmail = models.CharField(max_length=255, null=True, blank=True)
    vendorSecondaryPhone = models.CharField(max_length=10, null=True, blank=True)
    products = models.ManyToManyField(product, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True,editable=False)
    def __str__(self):
        return self.vendorName


class Order(models.Model):
    orderId = models.UUIDField(default = uuid.uuid4, primary_key=True, editable = False)
    orderNumber = models.CharField(max_length=255, unique=True, null=False)
    prodNumber = models.ForeignKey(product, on_delete=models.CASCADE)
    orderQuantity = models.CharField(max_length=255)
    vendorCode = models.ForeignKey(VendorMaster, on_delete=models.CASCADE)
    orderDelivery = models.DateField()
    createdAt = models.DateTimeField(auto_now_add=True,editable=False)
   

    def __str__(self):
        return str(self.orderNumber)

class OrderReceived(models.Model):
    orderNumber = models.OneToOneField(Order, on_delete=models.CASCADE)
    quantityReceived = models.CharField(max_length=255)
    orderReceiveDate = models.DateField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.orderNumber.orderNumber)