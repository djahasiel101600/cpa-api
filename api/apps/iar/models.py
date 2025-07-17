from django.db import models
from apps.core.models import Supplier, Employee, Office
from django.contrib.auth.models import User
from apps.core.uuid_generator import generate_custom_id

# Create your models here.
class InspectionAcceptanceReport(models.Model):
    id = models.CharField(primary_key=True, null=False, blank=False)
    iarNo = models.CharField(max_length=16, null=False, blank=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, related_name="IAR_Supplier")
    iarDate = models.DateField()
    salesInvoiceNo = models.CharField(max_length=100)
    dateInvoice = models.CharField(max_length=100)
    dateReceivedOfficer = models.CharField(max_length=100)
    dateAcceptance = models.CharField(max_length=100)
    dateInspection = models.CharField(max_length=100)
    dateReceivedCoa = models.DateField()
    receivedBy = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name="IARReceivedBy_Employee")
    submittedBy = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name="IARSubmittedBy_Employee")
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True, blank=True, related_name="IAR_Office")
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="IAR_User")
    
    def __str__(self):
        return f"{self.iarNo}"
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.id = generate_custom_id()
        super().save(*args, **kwargs)
    
    
     
class Particular(models.Model):
    id = models.CharField(max_length=12, primary_key=True, null=False, blank=False)
    iarId = models.ForeignKey(InspectionAcceptanceReport, on_delete=models.SET_NULL, null=True, blank=True, related_name="Particular_IarId")
    description = models.TextField()
    unit = models.CharField(max_length=12, null=True, blank=True)
    quantity = models.DecimalField(decimal_places=2, max_digits=9, default=0)
    unitPrice = models.DecimalField(decimal_places=2, max_digits=13, default=0)
    totalPrice = models.DecimalField(decimal_places=2, max_digits=13, default=0)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="Particular_User")
    
    def __str__(self):
        return f"{self.description}"
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.id = generate_custom_id()
            
        if not self.totalPrice:
            
            if not self.unitPrice:
                unitPrice = 0
            else:
                unitPrice = self.unitPrice
                
            if not self.unit:
                unit = 0
            else:
                unit = self.unit
                
            self.totalPrice = unit * unitPrice
            
        super().save(*args, **kwargs)