from django.db import models
from django.contrib.auth.models import User
from .uuid_generator import generate_custom_id

class Agency(models.Model):
    id = models.CharField(primary_key=True,max_length=12, editable=False)
    agencyName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="Agency_User")
    
    def __str__(self):
        return self.agencyName
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.id = generate_custom_id()
        super().save(*args, **kwargs)
    
class Fund(models.Model):
    id = models.CharField(primary_key=True, max_length=12, editable=False)
    fundName = models.CharField(max_length=200)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="Fund_User")
    
    def __str__(self):
        return self.fundName
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.id = generate_custom_id()
        super().save(*args, **kwargs)
    
class Office(models.Model):
    id = models.CharField(primary_key=True, max_length=12, editable=False)
    officeName = models.CharField(max_length=100)
    officeAgency = models.ForeignKey(Agency, models.CASCADE, related_name="office_agency")

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="Office_User")
    
    def __str__(self):
        return f"{self.officeName} - {self.officeAgency}"
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.id = generate_custom_id()
        super().save(*args, **kwargs)

class Position(models.Model):
    id = models.CharField(primary_key=True, max_length=12, editable=False)
    positionName = models.CharField(max_length=100)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="Position_User")
    
    def __str__(self):
        return self.positionName
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.id = generate_custom_id()
        super().save(*args, **kwargs)

class Employee(models.Model):
    id = models.CharField(primary_key=True, max_length=12, editable=False)
    firstName = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    position = models.ForeignKey(Position, models.CASCADE, related_name="employee_position")

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="Employee_User")
    
    def __str__(self):
        return f"{self.firstName} - {self.position}"
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.id = generate_custom_id()
        super().save(*args, **kwargs)
        
class ExpenditureCode(models.Model):
    id = models.CharField(primary_key=True, max_length=12, editable=False)
    objectCode = models.CharField(max_length=10)
    description = models.CharField(max_length=255, unique=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="ExpindetureCode_User")
    
    def __str__(self):
        return str(self.description)
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.id = generate_custom_id()
        super().save(*args, **kwargs)
        
class Supplier(models.Model):
    id = models.CharField(primary_key=True, max_length=12, null=False, blank=False, editable=False)
    supplierName = models.CharField(max_length=150)
    supplierAddress = models.CharField(max_length=255)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="Supplier_User")
    
    def __str__(self):
        return str(self.supplierName)
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.id = generate_custom_id()
        super().save(*args, **kwargs)