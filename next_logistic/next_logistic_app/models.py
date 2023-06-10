from django.db import models


# Create your models here.

class Employee(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    imageUrl = models.URLField(blank=True, null=True)
    contactNumber = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.firstName
