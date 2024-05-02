from django.db import models

# Create your models here.
class Driver(models.Model):
    driver_name = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=13)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.driver_name
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=13)
    
    def __str__(self):
        return self.customer_name