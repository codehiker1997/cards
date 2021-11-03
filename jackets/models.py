from django.db import models

# Create your models here.

class Jacket(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.brand



class Jacket_Detail(models.Model):
    color = models.CharField(max_length=100)
    priceS = models.DecimalField(max_digits=5, decimal_places=2)
    priceM = models.DecimalField(max_digits=5, decimal_places=2)
    priceL = models.DecimalField(max_digits=5, decimal_places=2)
    priceXL = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.URLField(blank=False, null=False)
    jacktet = models.ForeignKey(Jacket, on_delete= models.CASCADE)
