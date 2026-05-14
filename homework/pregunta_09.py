"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    dict = {}
    with open("files/input/data.csv", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            dict_2 = row[4]

            pares = dict_2.split(",")

            claves_en_fila = set()

            for par in pares:
                clave = par.split(":")[0]
                claves_en_fila.add(clave)

            for clave in claves_en_fila:
                if clave not in dict:
                    dict[clave] = 0
                dict[clave] += 1

    return dict


if __name__ == "__main__":
    pregunta_09()