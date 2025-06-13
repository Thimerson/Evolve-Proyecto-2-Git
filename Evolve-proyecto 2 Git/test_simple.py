from teu_converter.calculator import TeuCalculator

def test_calculator():
    calculator = TeuCalculator()
    
    # Test con volumen que requiere 1 TEU
    result = calculator.calculate_teus(30.0)
    print(f"\nPara 30 m³:")
    print(f"TEUs necesarios: {result['teus']}")
    print(f"Capacidad utilizada: {result['capacity_used']} m³")
    
    # Test con volumen que requiere 2 TEUs
    result = calculator.calculate_teus(60.0)
    print(f"\nPara 60 m³:")
    print(f"TEUs necesarios: {result['teus']}")
    print(f"Capacidad utilizada: {result['capacity_used']} m³")
    
    # Test con volumen límite
    result = calculator.calculate_teus(33.2)
    print(f"\nPara 33.2 m³:")
    print(f"TEUs necesarios: {result['teus']}")
    print(f"Capacidad utilizada: {result['capacity_used']} m³")
    
    # Test con volumen que requiere redondeo
    result = calculator.calculate_teus(40.0)
    print(f"\nPara 40 m³:")
    print(f"TEUs necesarios: {result['teus']}")
    print(f"Capacidad utilizada: {result['capacity_used']} m³")
    
    # Test con volumen para LCL
    recommendation = calculator.recommend_shipment(15.0)
    print(f"\nPara 15 m³:")
    print(f"Recomendación: {recommendation}")
    
    # Test con volumen para TEU
    recommendation = calculator.recommend_shipment(25.0)
    print(f"\nPara 25 m³:")
    print(f"Recomendación: {recommendation}")

if __name__ == "__main__":
    test_calculator()
