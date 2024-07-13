# Generated by Django 5.0.7 on 2024-07-11 03:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(db_column='idCategoria', primary_key=True, serialize=False)),
                ('name_categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductosTiendita',
            fields=[
                ('id_producto', models.AutoField(db_column='idProducto', primary_key=True, serialize=False)),
                ('name_prod', models.CharField(max_length=200)),
                ('desc_prod', models.CharField(max_length=500)),
                ('activo', models.IntegerField()),
                ('precio_prod', models.IntegerField(default=0)),
                ('id_categoria', models.ForeignKey(db_column='idcategoria', on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='productosApp.categoria')),
            ],
        ),
    ]
