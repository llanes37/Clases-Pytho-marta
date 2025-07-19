# -------------------------------------------------------------------------------------------
# PROYECTO: Crear un restaurante Burger King con clases en Python
# Nivel: Fácil | Objetivo: Practicar clases, atributos, métodos y herencia
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * CLASE PRINCIPAL: Restaurante
# TODO: Crea una clase llamada Restaurante que tenga:
#   - Atributos: nombre, ciudad, tipo_comida
#   - Método: mostrar_informacion (muestra los datos del restaurante)
#   - Método: abrir (imprime un mensaje que diga que el restaurante está abierto)
# -------------------------------------------------------------------------------------------

# class Restaurante:
#     def __init__(...):
#         # Guardar los valores en atributos

#     def mostrar_informacion(self):
#         # Imprimir el nombre, ciudad y tipo de comida del restaurante

#     def abrir(self):
#         # Mostrar mensaje como "¡El restaurante está abierto!"


# -------------------------------------------------------------------------------------------
# * CLASE HEREDADA: BurgerKing
# TODO: Crea una clase llamada BurgerKing que herede de Restaurante
#   - Atributo adicional: tiene_autopedido (True o False)
#   - Método especial: promocion (imprime "Hoy: menú Whopper por solo 4,99 €")
#   - Sobrescribe el método mostrar_informacion para mostrar también si tiene autopedido
# -------------------------------------------------------------------------------------------

# class BurgerKing(Restaurante):
#     def __init__(...):
#         # Llamar al constructor de la clase madre y añadir el atributo tiene_autopedido

#     def mostrar_informacion(self):
#         # Mostrar la información normal + si tiene autopedido

#     def promocion(self):
#         # Mostrar mensaje especial de promoción


# -------------------------------------------------------------------------------------------
# * PRUEBA DEL CÓDIGO (Cuando todo esté hecho)
# TODO: Crea un objeto de tipo BurgerKing y llama a los métodos para ver si funciona
# -------------------------------------------------------------------------------------------

# restaurante1 = BurgerKing("Burger King Plaza", "Madrid", "hamburguesas", True)
# restaurante1.mostrar_informacion()
# restaurante1.abrir()
# restaurante1.promocion()
