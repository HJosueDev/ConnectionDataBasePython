from django.db import models

# Create your models here.
class Producto(models.Model):
	codigop = models.CharField(primary_key=True, max_length=12)
	nombre = models.CharField(max_length=60)
	alias = models.CharField(max_length=60)



class Estado(models.Model):
	codigoe = models.CharField(primary_key=True, max_length=12)
	nombre = models.CharField(max_length=60)
		


class Tienda(models.Model):
	numerot = models.CharField(primary_key=True, max_length=12)
	codigop = models.ManyToManyField(Producto)
	nombre = models.CharField(max_length=60)
	fechaapertura = models.DateField(auto_now_add=True);
	ciudad = models.CharField(max_length=60)
	alias = models.CharField(max_length=60)
	codigoe = models.ForeignKey(Estado, null=False, blank=True, on_delete=models.CASCADE)




"""
Type Relation
Relation 1 - 1 =OneToOneField   unique=true
Relation 1 - m =ForeignKey (OneToManyField)
Relation m - m =ManyToManyField   unique=true

"""

"""
class TiendaProducto(models.Model):
	tienda = models.ForeignKey(Tienda, max_length=12)
	nombre = models.CharField(max_length=60)
	imagen = models.ImageField(height_field=75, width_field=75)
	alias = models.CharField(max_length=60)"""


"""
class Tienda(models.Model):
	producto=models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
	sursal=models.ForeignKey(Sucursal, null=False, blank=True, on_delete=models.CASCADE)
	descripcion=models.CharField(max_length=60)
	cantidad=models.DecimalField(max_digits=10, decimal_places=2)
	precio=models.DecimalField(max_digits=10, decimal_places=2)
	estado=models.BooleanField()"""

