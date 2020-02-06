from django.db import models

# Create your models here.
class Product(models.Model):
    nom = models.CharField(max_length=10)
    prix = models.DecimalField(max_digits=4, decimal_places=4)