"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letter de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    results = {}

    with open("files/input/data.csv", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")

        for row in reader:
            letter = row[0]
            numero = int(row[1])

            if letter not in results:
                results[letter] = [numero, numero]  # [max, min]
            else:
                if numero > results[letter][0]:
                    results[letter][0] = numero
                if numero < results[letter][1]:
                    results[letter][1] = numero

    
    resultado_final = [
        (letter, results[letter][0], results[letter][1])
        for letter in sorted(results.keys())
    ]

    return resultado_final



if __name__ == "__main__":
    pregunta_05()