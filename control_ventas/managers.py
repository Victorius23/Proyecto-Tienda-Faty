from django.db import models
from django.db.models import Sum
from datetime import date


class VentaManager(models.Manager):

    # * conseguir el total general de ventas de hoy

    def total_ventas_hoy(self):
        return self.filter(fecha__date=date.today()).aggregate(total=Sum('total'))['total'] or 0

    # * conseguir los nombnres de los 5 productos mas vendidos
    def productos_mas_vendidos(self):
        return self.filter(fecha__date=date.today()).values('detalles__producto__nombre').annotate(
            total=Sum('detalles__cantidad')).order_by('-total')[:5]