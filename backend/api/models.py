from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=3,max_digits=10,default=9999990)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)
    
    def discount(self):
        return "122"