from django.db import models

class Cliente(models.Model):
    nombre = models.CharField('Nombre', max_length=30)
    direccion = models.CharField('Dirección', max_length=50)
    email = models.EmailField(blank=True, null=True, verbose_name='El email')
    tfono = models.CharField('Teléfono', max_length=10)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    nombre = models.CharField('Nombre', max_length=30)
    seccion = models.CharField('Sección', max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return 'el nombre es %s la seccion es %s y el precio es %s' %(self.nombre, self.seccion, self.precio)

class Pedido(models.Model):
    numPedido = models.IntegerField()
    fechaPedido = models.DateField()
    entregado = models.BooleanField()



