from django.db import models
from datetime import datetime

class Customer(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to="customer_pics")
    address = models.TextField()

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"
    


