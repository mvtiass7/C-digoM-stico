print ("¡Bienvenido al menú interactivo!")
print ("1. Saludar")
print ("2. Decir horario")
print ("3. Salir")

while True:
    try:
        opcion = int(input("Ingrese su opción: "))
    
        if opcion == 1:
            print ("¡Hola!")
        elif opcion == 2:
            print ("Son las 3 p.m")
        elif opcion == 3:
            print ("¡Gracias, hasta pronto!")
            break
        else:
            print ("Opción no válida, ingrese una del 1 - 3")
    except ValueError:
        print ("ERROR. ingrese otra opción.")