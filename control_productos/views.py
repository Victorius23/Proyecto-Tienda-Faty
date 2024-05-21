from django.shortcuts import render
from rest_framework import viewsets
import json
# Create your views here.

from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer
from django.http import JsonResponse




class ProductoViewApi(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# * get categorias
class CategoriaViewApi(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
# * recuperar los productos por categoria
class ProductoCategoriaViewApi(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        categoria = self.request.GET.get('categoria')
        return Producto.objects.filter(categoria=categoria)