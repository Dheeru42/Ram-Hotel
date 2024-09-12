from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    checkindate = models.DateField()
    checkoutdate = models.DateField()
    nguest = models.IntegerField()
    rtype = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    date = models.DateField()
    
    def __str__(self):
        return self.name