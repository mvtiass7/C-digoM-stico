from funcionescalculadora import menu, calculos

menu()

while True:
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        print("¡Suma!")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = calculos(num1, num2, opcion)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == 2:
        print("¡Resta!")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = calculos(num1, num2, opcion)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == 3:
        print("¡Multiplicación!")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = calculos(num1, num2, opcion)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == 4:
        print("¡División!")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = calculos(num1, num2, opcion)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == 5:
        print("¡Gracias por utilizar la calculadora, hasta luego!")
        break