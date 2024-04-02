from django.shortcuts import render
from .models import Venta
from rest_framework import viewsets
from .serializers import VentaSerializer

# Create your views here.

class VentaViewApi(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer