while True:
    num = int(input("Ingrese un valor: "))
    if num % 2 == 0: # "num" es par si su residuo al dividirlo entre 2 es 0; si no, es impar.
        print(f"El número {num} es par")
    else:
        print(f"El número {num} es impar")