import math
from itertools import permutations

def distancia(cidade1, cidade2):
    x1, x2 = cidade1
    y1, y2 = cidade2
    return math.sqrt((x2 - x1)** 2 + (y2 - y1)** 2)

def custoRota(rota):
    custoTotal = 0
    n = len(rota)
    for i in range(n):
        custoTotal += distancia(rota[i], rota[(i + 1) % n])
    return custoTotal

def forcaBrutaTsp(cidades):
    melhorRota = None
    custoMinimo = float('inf')
    for perm in permutations(cidades):
        custo = custoRota(perm)
        if custo < custoMinimo:
            custoMinimo = custo
            melhorRota = perm
    return melhorRota, custoMinimo

if __name__ == "__main__":
    cidades = [(0, 0), (3, 4), (7, 3), (6, 0), (2, 2)]

    print(f"Cidades: {cidades}")
    melhorRota, custoMinimo = forcaBrutaTsp(cidades)
    print(f"Melhor rota: {melhorRota}")
    print(f"Menor custo: {custoMinimo:.2f}")
