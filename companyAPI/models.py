from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    website = models.CharField(max_length=80)

    def __str__(self):
        return self.name