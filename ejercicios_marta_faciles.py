# -------------------------------------------------------------------------------------------
# * EJERCICIO 1: ¿Quién trae dulces?
# -------------------------------------------------------------------------------------------

def merienda_dulces():
    # Lista de nombres de amigas que traen dulces
    amigas_con_dulces = []

    # Preguntamos a 3 amigas qué traen
    for i in range(3):
        nombre = input(f"Nombre de la amiga {i + 1}: ")
        comida = input(f"¿Qué ha traído {nombre}? ")

        # Comprobamos si lo que trae es un dulce
        if comida.lower() in ["caramelos", "pastel", "chocolate"]:
            amigas_con_dulces.append(nombre)

    # Mostramos el resultado
    if len(amigas_con_dulces) > 0:
        print("Estas amigas han traído dulces:")
        for amiga in amigas_con_dulces:
            print(f"- {amiga}")
        print("¡Habrá dulces en la merienda! 🎉")
    else:
        print("No hay dulces... 😢")

# Llamamos a la función para probarla
# merienda_dulces()


# -------------------------------------------------------------------------------------------
# * EJERCICIO 2: Lista de pelis favoritas
# -------------------------------------------------------------------------------------------

def pelis_favoritas():
    # Lista vacía para las películas que cumplen la condición
    lista_final = []

    # Pedimos 4 películas
    for i in range(4):
        peli = input(f"Nombre de la película {i + 1}: ")

        # Solo añadimos si tiene más de 5 letras
        if len(peli) > 5:
            lista_final.append(peli)

    # Mostramos la lista final
    print("Películas favoritas (con más de 5 letras):")
    for peli in lista_final:
        print(f"- {peli}")

# Llamamos a la función para probarla
# pelis_favoritas()
