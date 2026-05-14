"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    result = {}
    with open("files/input/data.csv", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for fila in reader:
            letter = fila[0]
            valores = fila[4].split(",")

            suma = 0
            for item in valores:
                clave, valor = item.split(":")
                suma += int(valor)

            if letter not in result:
                result[letter] = 0

            result[letter] += suma

    return result

if __name__ == "__main__":
    pregunta_12()