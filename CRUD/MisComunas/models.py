from django.utils import timezone
from django.db import models

class comuna(models.Model):
 id = models.IntegerField(primary_key=True)
 nombre =models.CharField(max_length=50)
 cantidad_habitantes = models.IntegerField(null=True)
 tasa_de_vulneribilidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
 fecha_fundacion = models.DateField(default=timezone.now)
