"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False

def sort_list(items, ascending=True):
    """
    Ordena una lista de elementos.

    Parámetros:
    items (list): Lista de elementos a ordenar.
    ascending (bool): Si es True, ordena en orden ascendente; si es False, en orden descendente. El valor por defecto es True.

    Retorno:
    list: Lista ordenada.

    Excepciones:
    RuntimeError: Si el parámetro 'items' no es una lista, se lanza una excepción con un mensaje de error.
    """
    if not isinstance(items, list):
        raise RuntimeError(f"Could not sort: {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    """
    Elimina elementos duplicados de una lista.

    Parámetros:
    items (list): Lista de elementos de la cual se desean eliminar duplicados.

    Retorno:
    list: Lista sin elementos duplicados.
    """
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("File must be provided as the first argument")
        print("The second argument must be 'yes' or 'no'")
        sys.exit(1)

    print(f"'{filename}' will be used as the input file")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"File '{filename}' does not exist")
        word_list = ["ravenclaw", "Slytherin", "Howards", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list))
