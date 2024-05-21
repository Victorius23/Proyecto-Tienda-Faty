from django.shortcuts import render
from .models import Venta
from rest_framework import viewsets
from .serializers import VentaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
#se importa date para poder obtener la fecha de hoy
from datetime import date
#importa sun
from django.db.models import Sum
from django.utils import timezone
from .bascula import obtener_peso_de_bascula

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
# Create your views here.


class VentaViewApi(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

# * api para conseguir el total de ventas de hoy
# * djangorestframework


class TotalVentasHoyApi(APIView):
    def get(self, request):
        total = Venta.objects.total_ventas_hoy()
        return Response({'total': total})


class ProductosMasVendidosApi(APIView):
    def get(self, request):
        # Obtener el primer y último día del mes actual
        today = timezone.now()
        first_day = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        last_day = (today.replace(day=1, month=today.month % 12 + 1, year=today.year)
                    - timezone.timedelta(days=1))

        # Consultar las ventas de productos del mes actual y obtener los 5 más vendidos
        productos = Venta.objects.filter(
            fecha__gte=first_day, fecha__lte=last_day
        ).values('detalles__producto__nombre').annotate(
            total=Sum('detalles__cantidad')
        ).order_by('-total')[:5]  # Obtener los 5 productos más vendidos del mes

        # Formatear los datos para la respuesta
        data = [{'name': producto['detalles__producto__nombre'], 'value': producto['total']} for producto in productos]
        return Response(data)

class VentasRealizadasHoy(APIView):
    def get(self, request):
        #cuenta las ventas realizadas hoy
        ventas = Venta.objects.filter(fecha__date=date.today()).count()
        return Response({'ventas': ventas})
    
class GananciasPorMes(APIView):
    def get(self, request):
        # Obtener el primer y último día del mes actual
        today = timezone.now()
        first_day = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        last_day = (today.replace(day=1, month=today.month % 12 + 1, year=today.year)
                    - timezone.timedelta(days=1))

        # Consultar las ventas del mes actual y obtener las ganancias
        ventas = Venta.objects.filter(
            fecha__gte=first_day, fecha__lte=last_day
        ).aggregate(ganancias=Sum('total'))['ganancias'] or 0

        return Response({'ganancias': ventas})        
    
 


@api_view(['GET'])
@permission_classes([AllowAny])
def obtener_peso_bascula(request):
    try:
        puerto_serial = "COM3"  # Puerto serial de la báscula
        baud_rate = 9600  # Velocidad de comunicación en baudios
        secuencia = "P"  # Secuencia de comandos para obtener el peso
        peso = obtener_peso_de_bascula(puerto_serial, baud_rate, secuencia)
        
        # Eliminar las unidades "kg" del peso
        peso_sin_unidades = peso.replace(' kg', '')
        
        return JsonResponse({'peso': peso_sin_unidades})
    except Exception as e:
        return JsonResponse({'error': str(e)})
