from django.db import models


class Reserva(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=1, default='A')

    def __str__(self):
        return ('%s - %s' % (self.pk, self.descripcion))

class ReservaDetalle(models.Model):
    reserva = models.ForeignKey(Reserva)
    fecha = models.DateField()
    detalle = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField()
    precio = models.PositiveIntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)