import numpy as np


def calc_delta(a, b, c):
    return b*b - 4 * a * c


def calc_square_root(a, b, c, delta):
    if (delta < 0):
        resultado = "Não existem raízes reais"
    elif (delta == 0):
        x = b/(2*a)
        resultado = f"A equação possui apenas a raiz: {x}"
    else:
        x1 = (-b - np.sqrt(delta))/(2*a)
        x2 = (-b + np.sqrt(delta))/(2*a)
        resultado = f"A equação possui duas raízes: {x1} e {x2}"
    return resultado


print(calc_square_root(1, 5, 6, calc_delta(1, 5, 6)))
