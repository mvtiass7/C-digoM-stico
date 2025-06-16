print ("¡Calculadora!")
print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicación")
print ("4. División")
print ("5. Salir")

opcion = 0
num1 = 0
num2 = 0
resultado = 0

opcion = int(input("Ingrese una opción: "))

while opcion < 5:
    if opcion == 1:
        print ("¡Suma!")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: ")) 
        resultado = num1 + num2
        print (f"El resultado de la suma es: {resultado}")
        opcion = int(input("Ingrese una opción: "))
    elif opcion == 2:
        print ("¡Resta!")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        print (f"El resultado de la resta es: {resultado}")
        opcion = int(input("Ingrese una opción: "))
    elif opcion == 3:
        print ("¡Multiplicación!")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        print (f"El resultado de la multiplicación es: {resultado}")
        opcion = int(input("Ingrese una opción: "))
    elif opcion == 4:
        print ("¡División!")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        while num2 == 0:
            print ("¡No se puede dividir por cero!")
            num2 = int(input("Ingrese el divisor otra vez: "))
        resultado = num1 / num2
        print (f"El resultado de la división es: {resultado}")
        opcion = int(input("Ingrese una opción: "))