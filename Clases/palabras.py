
palabra = input("Ingrese una palabra: ")

vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
consonantes = "bcdfghjklmnpqrstvwyzxBCDFGHJKLMNPQRSTVWYXZ"

vocales_encontradas = []
consonantes_encontradas = []
cantidad_vocales = 0
cantidad_consonantes = 0
cantidad_vacios = 0

#Recorrer cada caracter en el texto
for letra in palabra:
    if letra in vocales:
        vocales_encontradas.append(letra)
        cantidad_vocales = cantidad_vocales + 1
    elif letra in consonantes:
        consonantes_encontradas.append(letra)
        cantidad_consonantes = cantidad_consonantes + 1
    else:
        cantidad_vacios = cantidad_vacios + 1
        
print(f"Vocales encontradas: {vocales_encontradas}")
print(f"Consonantes encontradas: {consonantes_encontradas}")
print(f"Cantidad de vocales: {cantidad_vocales}")
print(f"Cantidad de consonantes: {cantidad_consonantes}")
print(f"Cantidad de espacios vacios: {cantidad_vacios}")

