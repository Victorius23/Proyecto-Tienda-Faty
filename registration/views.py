from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

# * api para conseguir el empleado con mas ventas (Los empleados son usuarios con es_staff=True)

from django.contrib.auth.models import User

from django.db.models import Sum

from rest_framework.response import Response
# * count
from django.db.models import Count


from django.db.models import Count

class EmpleadoMasVentas(APIView):
    def get(self, request):
        # * obtener el empleado con mas ventas
        empleado = User.objects.filter(is_staff=True).annotate(total_ventas=Count('ventas')).order_by('-total_ventas').first()

        return Response({'empleado': empleado.username, 'ventas': empleado.total_ventas})

