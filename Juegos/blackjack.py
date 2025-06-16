from random import randint

print("¡Bienvenido al casino!")
print("1. Blackjack")

opcion = int(input("Ingrese qué desea jugar: "))
carta1 = randint(1, 10)
carta2 = randint(1, 10)
cartac1 = randint(1, 10)
cartac2 = randint(1, 10)

# Función para contar el 1 o el 11 como un AS
def mostrar_carta(carta):
    if carta == 1:
        return "AS"
    else:
        return str(carta) #str es para imprimir la variable como texto, ejemplo con: int(10) y con str("10")

def ajustar_as(valores):
    total = sum(valores) # A esto me refiero con, "Variable" = "Suma"("Todos los valores de la suma, puede ser ejemplo, 11 + 6")
    contador_as = valores.count(11) # .count es el que cuenta cuantas veces aparece un elemento dentro de una lista (EN ESTE CASO 11 YA QUE SERÍA AS)
    while total > 21 and contador_as > 0: 
        total -= 10 # Mientras el total sea mayor que 21 y tenga ASES que pueda bajar de 11 a 1 el bucle va restando de 10 al total.
        contador_as -= 1
    return total

if opcion == 1:
    print("¡Jugarás blackjack!")
    print("Recuerda el número que sea mayor sin pasarse del 21 ganará")
    print("También recuerda que el 1 es un AS")
    print("-------------------")
    print("El crupier comienza a revolver las cartas")
    print("Revolviendo...")
    if carta1 == 1:
        valor1 = 11
    else:
        valor1 = carta1
    print(f"Comienza el juego, tienes un {mostrar_carta(carta1)}")
    if cartac1 == 1:
        valorc1 = 11
    else:
        valorc1 = cartac1
    print(f"El crupier tiene {mostrar_carta(cartac1)}")
    if carta2 == 1:
        if valor1 + 11 > 21:
            valor2 = 1
        else:
            valor2 = 11
    else:
        valor2 = carta2
    print(f"El crupier saca tu segunda carta y es un {mostrar_carta(carta2)}")
    valores_jugador = [valor1, valor2] # Coloco la variable valores_jugadores que tendrá en su interior [valor1, valor2]
    sumacartas = ajustar_as(valores_jugador)  # Usará la función para ver si hay ASES en el interior de valor1 o valor2 y si es que se debe devolver un resultado (AJUSTAR)
    valores_crupier = [valorc1]
    sumacartasc = ajustar_as(valores_crupier)  # El crupier solo muestra su primera carta
    
    print(f"El crupier deja su carta oculta...")
    print(f"Crupier: {sumacartasc} / Tú: {sumacartas}")
    while sumacartas <= 21:
        pregunta = input("¿Pides o te plantas? ").lower().strip() #.lower() es para que la respuesta que mandamos siga siendo leída aunque pongamos MAYUS o MINUSCULA, ejemplo: "PIDO"
        while pregunta not in ["pido", "s", "planto", "p"]:
            pregunta = input("Respuesta inválida. ¿Pides o te plantas? ").lower().strip() #.strip() es para que la respuesta que mandamos siga siendo leído aunque tenga espacios
        if pregunta == "pido" or pregunta == "s":
            carta3 = randint(1, 10)
            print("--------------------")
            if carta3 == 1:
                if sumacartas + 11 <= 21:
                    valor3 = 11
                else:
                    valor3 = 1
            else:
                valor3 = carta3
            print(f"Pediste. El crupier saca una nueva carta y tienes un {mostrar_carta(carta3)}")
            valores_jugador.append(valor3) #.append se utiliza para agregar un elemento al final de una lista, es decir en este caso [valor1, valor2, valor3]
            sumacartas = ajustar_as(valores_jugador)  # Ajustar después de agregar carta (valor3)
            print(f"Crupier: {mostrar_carta(cartac1)} / Tú: {sumacartas}")
            if sumacartas > 21:
                print("¡Te pasaste, perdiste!")
                break
        elif pregunta == "planto" or pregunta == "p":
            print(f"Te plantaste con {sumacartas}")
            if cartac2 == 1:
                if valorc1 + 11 <= 21:
                    valorc2 = 11
                else:
                    valorc2 = 1
            else:
                valorc2 = cartac2
            valores_crupier.append(valorc2) # Estoy agregando valorc2 ya que la carta del crupier número 2 estaba oculta
            print("----------------------")
            print(f"El crupier destapa su carta y es un {mostrar_carta(cartac2)}")
            sumacartasc = ajustar_as(valores_crupier)  # Reviso si es que debe descontar cartas en el caso de pasarse
            print(f"Crupier: {sumacartasc} / Tú: {sumacartas}")
            while sumacartasc < 17:
                cartarandomc = randint(1, 10)
                if cartarandomc == 1:
                    if sumacartasc + 11 <= 21:
                        valorc3 = 11
                    else:
                        valorc3 = 1
                else:
                    valorc3 = cartarandomc
                print(f"El crupier saca su carta y es un {mostrar_carta(cartarandomc)}")
                valores_crupier.append(valorc3) # En el caso de que el crupier tenga menos que 17 debe seguir sacando cartas, es decir seguir agregando elementos a la lista [valorc3]
                sumacartasc = ajustar_as(valores_crupier)  # Ajusto la sumatoria del crupier con nuestro nuevo elemento, "valorc3"
                print(f"Crupier: {sumacartasc} / Tú: {sumacartas}")
            if sumacartasc > 21:
                print("El crupier se pasó, ganaste")
            elif sumacartas > sumacartasc:
                print("¡Ganaste!")
            elif sumacartas < sumacartasc:
                print("¡Perdiste!")
            else:
                print("¡Empate!")
            break