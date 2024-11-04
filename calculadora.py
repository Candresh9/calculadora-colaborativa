def sumar(a, b):
    return a + b

if __name__ == "__main__":
    print("Calculadora de Suma")

    while True:
        print("\nSeleccione una opción:")
        print("1. Sumar")
        print("2. Salir")
        
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "2":
            print("Saliendo de la calculadora...")
            break

        if opcion == "1":
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                
                print("Resultado:", sumar(num1, num2))
            except ValueError:
                print("Error: Por favor ingrese un número válido.")
        else:
            print("Opción no válida. Intente de nuevo.")