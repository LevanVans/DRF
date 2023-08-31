from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True, max_length=500)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    
    
    @property
    def sale_price(self):
        return self.price - 1
    
    def get_discount(self):
        try:
            return self.price + 100
        except:
            return None