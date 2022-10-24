from django.db import models
import uuid
from django.core.validators import MinLengthValidator
from product.models import *
from django.dispatch import receiver
from MyInventory.utils import sendEmail


class customer(models.Model):
    custId = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    custFname = models.CharField(max_length = 100)
    custLname = models.CharField(max_length = 100)
    custEmail = models.EmailField(max_length=254)
    custPhone = models.CharField(max_length = 10,default = '0000000000',validators=[MinLengthValidator(10)])
    address = models.CharField(max_length = 255)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    productNumber = models.CharField(max_length = 100)
    expiryDate = models.DateField()
    amount = models.CharField(max_length = 100)
    technition = models.ForeignKey(employee,on_delete=models.CASCADE)
    message = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True,editable=False)
  

    def __str__(self):
        return self.custFname + " " + self.custLname


@receiver(post_save,sender=customer)
def createMail(sender,instance,created,**kwargs):
    to = str(instance.custEmail)
    fro='wppl.team@gmail.com'
    subject = "Chaoudhary Batteries"

    body = "Dear Customer,"+ \
            "\n\nThank you for choosing our shop to purchase " + str(instance.product.prodName) + "." + \
            "\nProduct Number: " + str(instance.productNumber) + \
            "\nAmount: " + str(instance.amount) + \
            "\nExpiry Date: " + str(instance.expiryDate) + \
            "\n\nThanks and regards\nChaudhary Batteries-Akola\nContact No-0000000000"

    sendEmail(to,subject,body)
    
