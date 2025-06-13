import pytest
from teu_converter.calculator import TeuCalculator

def test_calculate_teus():
    calculator = TeuCalculator()
    
    # Test con volumen que requiere 1 TEU
    result = calculator.calculate_teus(30.0)
    assert result['teus'] == 1
    assert result['capacity_used'] == 33.2
    
    # Test con volumen que requiere 2 TEUs
    result = calculator.calculate_teus(60.0)
    assert result['teus'] == 2
    assert result['capacity_used'] == 66.4
    
    # Test con volumen límite
    result = calculator.calculate_teus(33.2)
    assert result['teus'] == 1
    assert result['capacity_used'] == 33.2
    
    # Test con volumen que requiere redondeo
    result = calculator.calculate_teus(40.0)
    assert result['teus'] == 2
    assert result['capacity_used'] == 66.4

def test_recommend_shipment():
    calculator = TeuCalculator()
    
    # Test con volumen para LCL
    result = calculator.recommend_shipment(15.0)
    assert result == "Recomendación: Envío LCL"
    
    # Test con volumen para TEU
    result = calculator.recommend_shipment(25.0)
    assert "TEUs" in result
    
    # Test con volumen límite
    result = calculator.recommend_shipment(20.0)
    assert "TEUs" in result
