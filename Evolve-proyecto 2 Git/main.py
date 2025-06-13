from teu_converter import TeuCalculator

def main():
    calculator = TeuCalculator()
    
    try:
        # Solicitar volumen al usuario
        volume = float(input("Ingrese el volumen en metros cúbicos: "))
        
        # Calcular TEUs
        teu_result = calculator.calculate_teus(volume)
        print(f"\nPara {volume} m³ se necesitan {teu_result['teus']} TEUs")
        print(f"Capacidad total utilizada: {teu_result['capacity_used']} m³")
        
        # Recomendar tipo de envío
        recommendation = calculator.recommend_shipment(volume)
        print(f"\n{recommendation}")
        
    except ValueError as e:
        print(f"Error: {str(e)}")

from teu_converter.calculator import TeuCalculator

def main():
    # Crear una instancia del calculador
    calculator = TeuCalculator()
    
    print("\nBienvenido al Convertidor de Metros Cúbicos a TEUs")
    print("-" * 50)
    
    while True:
        try:
            # Solicitar volumen al usuario
            volume = float(input("\nIngrese el volumen en metros cúbicos (o '0' para salir): "))
            
            if volume == 0:
                print("\n¡Gracias por usar el convertidor!")
                break
                
            # Calcular TEUs
            teu_result = calculator.calculate_teus(volume)
            print(f"\nPara {volume} m³ se necesitan {teu_result['teus']} TEUs")
            print(f"Capacidad total utilizada: {teu_result['capacity_used']} m³")
            
            # Recomendar tipo de envío
            recommendation = calculator.recommend_shipment(volume)
            print(f"\n{recommendation}")
            
        except ValueError as e:
            print(f"Error: {str(e)}")
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
    