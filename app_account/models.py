from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=30)
    phone_number= models.CharField(max_length=30)
    taxid_number= models.CharField(max_length=30)
    email= models.EmailField(max_length=254)
    address= models.CharField(max_length=30)

    def __str__(self):
        return self.name