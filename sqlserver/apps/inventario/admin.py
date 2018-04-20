from django.contrib import admin

#importando los modelos al admin y poderlos visualizar en html
from apps.inventario.models import Producto, Estado, Tienda 

# Register your models here.
admin.site.register(Producto)
admin.site.register(Estado)
admin.site.register(Tienda)