from django.db import models

class Cliente(models.Model):
    nombre = models.CharField('Nombre', max_length=30)
    direccion = models.CharField('Dirección', max_length=50)
    email = models.EmailField()
    tfono = models.CharField('Teléfono', max_length=10)

class Articulo(models.Model):
    nombre = models.CharField('Nombre', max_length=30)
    seccion = models.CharField('Sección', max_length=20)
    precio = models.IntegerField()

class Pedido(models.Model):
    numPedido = models.IntegerField()
    fechaPedido = models.DateField()
    entregado = models.BooleanField()

