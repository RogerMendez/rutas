from django.db import models

from asociaciones.models import Asociacion

class Linea(models.Model):
    nombre = models.CharField(max_length='10')

    asociacion = models.ForeignKey(Asociacion, null=True, blank=True)
    def __unicode__(self):
        return self.nombre
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Lineas'
        permissions = (
            ('detail_linea', 'Detalle De Linea'),
            ('rutas_linea', 'Rutas de Linea'),
        )


