from django.db import models

# Create your models here.
class Agency(models.Model):
    agencyName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.agencyName
    

class Fund(models.Model):
    fundName = models.CharField(max_length=200)
    
    def __str__(self):
        return self.fundName
    
class Office(models.Model):
    officeName = models.CharField(max_length=100)
    officeAgency = models.ForeignKey(Agency, models.CASCADE, related_name="office_agency")

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.officeName} - {self.officeAgency}"


class Position(models.Model):
    positionName = models.CharField(max_length=100)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.positionName


class Employee(models.Model):
    firstName = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    position = models.ForeignKey(Position, models.CASCADE, related_name="employee_position")

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.firstName} - {self.position}"

class ExpenditureCode(models.Model):
    objectCode = models.IntegerField()
    description = models.CharField(255)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)