def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b


def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Escribe un número.")


def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "5":
            print("Saliendo de la calculadora...")
            break

        if opcion not in {"1", "2", "3", "4"}:
            print("Opción no válida. Elige entre 1 y 5.")
            continue

        num1 = pedir_numero("Primer número: ")
        num2 = pedir_numero("Segundo número: ")

        try:
            if opcion == "1":
                print("Resultado:", sumar(num1, num2))
            elif opcion == "2":
                print("Resultado:", restar(num1, num2))
            elif opcion == "3":
                print("Resultado:", multiplicar(num1, num2))
            elif opcion == "4":
                print("Resultado:", dividir(num1, num2))
        except ZeroDivisionError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
