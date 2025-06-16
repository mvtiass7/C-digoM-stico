colores = ["rojo", "verde", "azul", "naranjo"]

colores.append("negro") # Para agregar elementos al final de la lista
colores.insert(1, "negro") # Para agregar elementos donde tú lo indiques (recuer                                                                                                                                                                                                                                                                                                                                          da que parte desde el 0)
colores.remove("rojo") # Para remover(eliminar) elementos de la lista
colores.reverse() # Para invertir el orden de los elementos, es decir cuando leamos el código empezará desde el naranjo
colores.sort() # Para ordenar mi lista en orden ABC

for color in colores:
    print(f"El color es: {color}")