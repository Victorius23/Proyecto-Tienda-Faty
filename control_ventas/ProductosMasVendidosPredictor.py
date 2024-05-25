import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from django.db.models import Count
from .models import Venta

class ProductosMasVendidosPredictor:
    def __init__(self):
        self.model = None

    def entrenar_modelo(self):
        # Consulta las ventas de productos y cuenta la cantidad de ventas por producto
        ventas = Venta.objects.values('detalles__producto').annotate(
            total_ventas=Count('detalles__producto')
        )
        
        # Crear un DataFrame con los datos de ventas
        df = pd.DataFrame(list(ventas))
        
        # Entrenar el modelo ARIMA con los datos de ventas
        self.model = ARIMA(df['total_ventas'], order=(5, 1, 0))
        self.model = self.model.fit()
        
    def predecir_productos_mas_vendidos(self, n=5):
        # Predecir las ventas de los próximos n productos más vendidos
        predicciones = self.model.forecast(steps=n)
        return predicciones
    