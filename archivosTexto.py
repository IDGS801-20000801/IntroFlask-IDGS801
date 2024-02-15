from io import open

"""
archivo_1 = open('archivo.txt', 'a')
archivo_1.write('\n Saludo IDGS-801 nuevo')
archivo_1.close()
"""

archivo_1 = open('archivo.txt', 'r')

# print(archivo_1.read())
# archivo_1.seek(28)
# print(archivo_1.read())

""" Print an array of the data contained separated by comas or SPACE or ENTER """
# print(archivo_1.readlines())

archivo_1.close()