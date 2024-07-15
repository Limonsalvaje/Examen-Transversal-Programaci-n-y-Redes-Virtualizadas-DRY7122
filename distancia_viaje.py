# distancia_viaje.py

# Función para calcular la distancia entre dos ciudades (simulado)
def calcular_distancia(ciudad_origen, ciudad_destino):
    # Simulación de distancia (en millas y kilómetros)
    distancia_millas = 2500
    distancia_kilometros = distancia_millas * 1.60934  # 1 milla = 1.60934 kilómetros

    # Tiempo de viaje estimado (simulado)
    duracion_horas = 10

    return distancia_millas, distancia_kilometros, duracion_horas

# Función para obtener la narrativa del viaje
def obtener_narrativa(ciudad_origen, ciudad_destino, distancia_millas, duracion_horas):
    narrativa = f"Viajando desde {ciudad_origen} hasta {ciudad_destino}:\n"
    narrativa += f"La distancia es de {distancia_millas:.2f} millas ({distancia_millas * 1.60934:.2f} km).\n"
    narrativa += f"El viaje tomará aproximadamente {duracion_horas} horas."
    return narrativa

# Función principal del script
def main():
    print("Bienvenido al sistema de cálculo de viaje.")

    while True:
        ciudad_origen = input("Ingrese la ciudad de origen (Chile): ")
        ciudad_destino = input("Ingrese la ciudad de destino (Perú): ")

        distancia_millas, distancia_kilometros, duracion_horas = calcular_distancia(ciudad_origen, ciudad_destino)

        print(f"\nDistancia del viaje:")
        print(f"- Millas: {distancia_millas:.2f} mi")
        print(f"- Kilómetros: {distancia_kilometros:.2f} km")

        narrativa = obtener_narrativa(ciudad_origen, ciudad_destino, distancia_millas, duracion_horas)
        print(f"\nNarrativa del viaje:\n{narrativa}")

        while True:
            opcion = input("\n¿Qué tipo de medio de transporte desea utilizar? (Avión, Tren, Auto): ").lower()
            if opcion in ['avion', 'tren', 'auto']:
                print(f"Ha elegido viajar en {opcion}. ¡Buen viaje!")
                break
            elif opcion == 'e':
                print("Saliendo del programa...")
                return
            else:
                print("Opción no válida. Por favor, elija entre Avión, Tren o Auto.")

if __name__ == "__main__":
    main()
