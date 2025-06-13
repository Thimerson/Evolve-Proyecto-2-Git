# Convertidor de Metros Cúbicos a TEUs/LCL

Una herramienta simple para convertir metros cúbicos de carga a TEUs (Twenty-foot Equivalent Unit) o determinar si la carga es más adecuada para envío LCL.

## Instalación

```bash
pip install teu-converter
```

## Uso

```python
from teu_converter import TeuCalculator

calculator = TeuCalculator()

# Calcular TEUs para una carga
volume = 25.5  # metros cúbicos
result = calculator.calculate_teus(volume)
print(f"Para {volume} m³ se necesitan {result['teus']} TEUs")

# Calcular recomendación de envío
recommendation = calculator.recommend_shipment(volume)
print(f"Recomendación: {recommendation}")
```

## Características

- Conversión automática de metros cúbicos a TEUs
- Recomendación de tipo de envío (TEU o LCL)
- Cálculo optimizado de TEUs necesarios
- Documentación completa

## Requisitos

- Python 3.8+

## Estructura del proyecto

```
Proyecto 2 Git/
├── teu_converter/          # Paquete principal
│   ├── __init__.py
│   └── calculator.py
├── tests/                  # Pruebas
│   ├── __init__.py
│   └── test_calculator.py
├── setup.py               # Configuración del paquete
└── README.md             # Documentación
```
