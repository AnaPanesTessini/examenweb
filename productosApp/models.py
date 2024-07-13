from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator, MaxLengthValidator

class ProductosTiendita(models.Model):
    id_producto = models.AutoField(db_column='idProducto', primary_key=True)
    name_prod = models.CharField(max_length=200)
    desc_prod = models.CharField(max_length=500)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idcategoria', related_name='productos')
    activo = models.IntegerField()  #
    precio_prod = models.IntegerField(default=0)  

    def __str__(self):
        return f'{self.id_producto}: {self.name_prod}'  

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True)
    name_categoria = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name_categoria  

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)  
    password = models.CharField(
        max_length=12,
        validators=[
            MinLengthValidator(8),  # Mínimo 8 caracteres
            MaxLengthValidator(12)  # Máximo 12 caracteres
        ]
    )  
    

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    def save(self, *args, **kwargs):
        if not self.pk or self._state.adding or 'password' in self._get_changed_fields():
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
