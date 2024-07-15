# verificar_as.py

def verificar_as(numero_as):
    as_publicos = [64512, 65000]  # Ejemplo de AS públicos

    if numero_as in as_publicos:
        print(f"El AS {numero_as} es público.")
    else:
        print(f"El AS {numero_as} es privado.")

def main():
    numero_as = input("Ingrese el número de AS de BGP: ")
    verificar_as(int(numero_as))

if __name__ == "__main__":
    main()
