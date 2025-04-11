def suma(a, b):
    return a + b
def resta(a,b)
    return a-b
def multiplicacion(a, b):
    return a * b
def division (a/b):
    return a/b if b! = 0 else "Error division por cero"

def mostrar_menu():
    print("\nCalculadora Básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def solicitar_numeros():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    return a, b


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion in ["1", "2", "3", "4"]:
            a, b = solicitar_numeros()

            if opcion == "1":
                resultado = suma(a, b)
            elif opcion == "2":
                resultado = resta(a, b)
            elif opcion == "3":
                resultado = multiplicacion(a, b)
            elif opcion == "4":
                resultado = division(a, b)

            print(f"Resultado: {resultado}")
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
