from django.db import models

# Create your models here.
class Fund(models.Model):
    fundName = models.CharField(100)


class Office(models.Model):
    officeName = models.CharField(100)
    officeLocation = models.CharField(255)


class Position(models.Model):
    positionName = models.CharField(200)


class Employee(models.Model):
    firstName = models.CharField(255)
    lastname = models.CharField(255)
    position = models.ForeignKey(Position, models.CASCADE, related_name="employee_position")


class BankRecon(models.Model):
    accountNumber = models.CharField(max_length=24)
    asOf = models.DateField()
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    fund = models.ForeignKey(Fund, models.CASCADE, related_name="bankRecon_fund")
    office = models.ForeignKey(Office, models.CASCADE, related_name="bankRecon_office")
    dateReceived = models.DateTimeField()
    sender = models.ForeignKey(Employee, models.CASCADE, related_name="bankReconSender_employee")
    receiver = models.ForeignKey(Employee, models.CASCADE, related_name="bankReconReceived_employee")
    remarks = models.CharField(max_length=255)