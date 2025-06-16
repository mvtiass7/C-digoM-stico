import random

print ("¡Juego de busqueda de tesoro!")

tesoro = random.randint(1, 10)

print ("La carta del tesoro está oculta, debes adivinarla...")
print ("Elige un número entre el 1 y el 10")

while True:
    adivinanza = int(input("Selecciona tu opción: "))
    
    if adivinanza == tesoro:
        print ("¡Adivinaste el número secreto!")
        print ("¡Felicitaciones!")
        break
    elif abs (adivinanza - tesoro) <= 2:
        print ("¡Estás cerca!")
    else:
        print ("¡Estás lejos!")