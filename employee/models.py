from django.db import models
from phone_field import PhoneField

# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    firstName = models.CharField(max_length=40)
    middleName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="male")
    dateBirth = models.DateField()
    contactNumber = PhoneField()
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.firstName
