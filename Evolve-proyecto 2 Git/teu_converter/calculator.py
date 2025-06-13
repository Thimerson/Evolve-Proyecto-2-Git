"""
Calculador de TEUs y recomendador de envío
"""

class TeuCalculator:
    """
    Clase para calcular TEUs y recomendar tipo de envío
    """
    def __init__(self):
        # Un TEU tiene aproximadamente 33.2 m³ de capacidad
        self.teu_capacity = 33.2
        # Umbral para recomendar TEU en lugar de LCL
        self.teu_threshold = 20.0

    def calculate_teus(self, volume: float) -> dict:
        """
        Calcula el número de TEUs necesarios para una carga
        
        Args:
            volume: Volumen en metros cúbicos
            
        Returns:
            Diccionario con el número de TEUs necesarios
        """
        if volume <= 0:
            raise ValueError("El volumen debe ser mayor que 0")
            
        # Un TEU tiene aproximadamente 33.2 m³
        teus_needed = volume / self.teu_capacity
        
        # Redondear hacia arriba ya que no podemos tener fracciones de TEU
        teus_needed = int(teus_needed) + (1 if teus_needed % 1 != 0 else 0)
        
        return {
            'volume': volume,
            'teus': teus_needed,
            'capacity_used': teus_needed * self.teu_capacity
        }

    def recommend_shipment(self, volume: float) -> str:
        """
        Recomienda el tipo de envío (TEU o LCL)
        
        Args:
            volume: Volumen en metros cúbicos
            
        Returns:
            Recomendación de envío
        """
        if volume <= 0:
            raise ValueError("El volumen debe ser mayor que 0")
            
        if volume < self.teu_threshold:
            return "Recomendación: Envío LCL"
        else:
            result = self.calculate_teus(volume)
            return f"Recomendación: Envío en {result['teus']} TEUs"

    def __str__(self):
        return f"TEU Calculator (TEU capacity: {self.teu_capacity} m³)"
