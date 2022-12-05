import numpy as np
from fractions import Fraction

def maior_potencia2(matrizes):
    print(min(matrizes))

def multiplica_t_g(matrizes_t, matriz_g):
    matrizes = []
    for x in range(len(matrizes_t)):
        matrizes.append(np.dot(matriz_inversa(matrizes_t[x]), matriz_g))
    return matrizes

def testa_matriz_inteira(matriz):
    if(matriz[0][0].denominator== 1):
        if(matriz[0][1].denominator== 1):
            if(matriz[1][0].denominator== 1):
                if(matriz[1][1].denominator== 1):
                    return True
    return False

def matriz_inversa(matriz):
    matriz_float = np.array(matriz, dtype = float)
    matriz_invertida = np.linalg.inv(matriz_float)
    matriz_fracao = np.array([[Fraction(matriz_invertida[0][0]), Fraction(matriz_invertida[0][1])],[Fraction(matriz_invertida[1][0]), Fraction(matriz_invertida[1][1])]])
    return matriz_fracao


def main():
    t = [np.array([[Fraction(0), Fraction(1/2)],[Fraction(-2),Fraction(0)]]), np.array([[Fraction(0), Fraction(2)],[Fraction(-1/2),Fraction(0)]]), np.array([[Fraction(1/2), Fraction(-5/2)],[Fraction(1/2),Fraction(-1/2)]])]
    g = np.array([[Fraction(0), Fraction(-4)],[Fraction(1/4),Fraction(-1/2)]])
    ts_g = multiplica_t_g(t, g)
    maior_potencia2(ts_g)

main()

