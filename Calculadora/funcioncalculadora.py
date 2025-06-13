def menu():
    print("¡Bienvenido a nuestra calculadora!")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def calculos(num1, num2, opcion):
    if opcion == 1:
        return num1 + num2
    if opcion == 2:
        return num1 - num2
    if opcion == 3:
        return num1 * num2
    if opcion == 4:
        while num2 == 0:
            print("¡No se puede dividir por cero!")
            num2 = int(input("Ingrese el segundo número otra vez: "))
        else:
            return num1 / num2