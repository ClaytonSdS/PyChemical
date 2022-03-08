from mendeleev import element
import numpy as np
import re

def chemicalWeight (name):
    """
    Test
    """
    elementos = re.sub(r"([A-Z])", r" \1", name).split()
    fatiamento = []
    convert_Str_Int = []
    soma_parcial = []

    # slicing between letters and numbers
    for i in range(len(elementos)):
        # check if has no number after the element
        if any(map(str.isdigit, elementos[i])) == False:
            elementos[i] = elementos[i] + '1'
            match = re.match(r"([a-z]+)([0-9]+)", elementos[i], re.I)

    # normal slice to element + quantity
    for i in range(len(elementos)):
        match = re.match(r"([a-z]+)([0-9]+)", elementos[i], re.I)
        if match:
            fatiamento.append(list(match.groups()))

    # convert to string and int values
    for j in range(len(fatiamento)):
        convert_Str_Int.append(fatiamento[j][0])
        convert_Str_Int.append(int(fatiamento[j][1]))

    # sum of individuals chemical elements
    for i in np.arange(1, len(convert_Str_Int), 2):
        soma_parcial.append(convert_Str_Int[i] * element(convert_Str_Int[i - 1]).atomic_weight)
        # sum of all individuals chemical elements
        result = sum(soma_parcial)

    return result









