def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


if __name__ == "__main__":
    x = float(input("Primer número: "))
    y = float(input("Segundo número: "))
    print("Suma:", sumar(x, y))
    print("Resta:", restar(x, y))
    print("Multiplicación:", multiplicar(x, y))
