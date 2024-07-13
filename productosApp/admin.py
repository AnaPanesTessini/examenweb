from django.contrib import admin
from .models import ProductosTiendita,Categoria, Usuario
# Register your models here.

# admin.py


admin.site.register(Usuario)
admin.site.register(ProductosTiendita)
admin.site.register(Categoria)