from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, default='None', unique=True)
    password = models.CharField(max_length=255, default='1234')
    email = models.EmailField(max_length = 255, unique=True)
    phone_number = models.CharField(max_length = 255, default='None')
    department = models.CharField(max_length = 255, default='None')
    year = models.CharField(max_length = 10, default='None')
    user_type = models.CharField(max_length= 100, choices=[('Student', 'Student'), ('Faculty', 'Faculty'), ('Admin', 'Admin')])
    unique_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username


class Complaint(models.Model):
    name = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length = 255)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    resolution = models.TextField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length = 100, choices=[('Resolved', 'Resolved'), ('Unresolved', 'Unresolved')], default='Unresolved')

    def __str__(self):
        return self.title



class Event(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length = 255)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

