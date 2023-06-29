from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_manager=models.BooleanField('Is Manager', default=False)


class PurchaseRequisitions(models.Model):
    requested_by = models.CharField(max_length=255)
    requested_date = models.DateField(default=timezone.now)
    expected_date = models.DateField()
    manager_name = models.CharField(max_length=255)
    vendor_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='Draft')
    requisition_id = models.CharField(max_length=255, unique=True, null=True)

    
class PurchaseRequisitionLines(models.Model):
    product = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

