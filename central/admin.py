from django.contrib import admin
from .models import User,Requisition,PurchaseRequisition,PurchaseRequisitionLine

# Register your models here.
admin.site.register(User)
admin.site.register(Requisition)
admin.site.register(PurchaseRequisition)
admin.site.register(PurchaseRequisitionLine)