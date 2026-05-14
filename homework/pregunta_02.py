"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    with open("files/input/data.csv", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        data = list(reader)
        columns = list(zip(*data))

    results = [(x, columns[0].count(x)) for x in set(columns[0])]

    return sorted(results)

if __name__ == "__main__":
    pregunta_02()