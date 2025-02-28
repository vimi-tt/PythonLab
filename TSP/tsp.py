import math
from itertools import permutations

# Função que calcula a distância euclidiana entre duas cidades.
# A distância é calculada usando a fórmula:
# distância(A, B) = sqrt((x2 - x1)^2 + (y2 - y1)^2)
def distancia(cidade1, cidade2):
    x1, x2 = cidade1  # Desempacota as coordenadas da primeira cidade
    y1, y2 = cidade2  # Desempacota as coordenadas da segunda cidade
    return math.sqrt((x2 - x1)** 2 + (y2 - y1)** 2)  # Calcula e retorna a distância euclidiana

# Função que calcula o custo total de uma rota.
# A rota é uma lista de cidades, e o custo é a soma das distâncias entre cidades consecutivas.
def custoRota(rota):
    custoTotal = 0  # Inicializa o custo total como zero
    n = len(rota)  # Obtém o número de cidades na rota
    for i in range(n):
        # Calcula a distância entre a cidade atual e a próxima cidade (usando a operação % n para voltar à cidade inicial)
        custoTotal += distancia(rota[i], rota[(i + 1) % n])
    return custoTotal  # Retorna o custo total da rota

# Função que implementa a solução de força bruta para o problema do Caixeiro Viajante (TSP).
# Gera todas as permutações possíveis das cidades e calcula o custo de cada uma, 
# retornando a rota com o menor custo.
def forcaBrutaTsp(cidades):
    melhorRota = None  # Inicializa a melhor rota como None
    custoMinimo = float('inf')  # Inicializa o custo mínimo com um valor infinito
    # Gera todas as permutações possíveis das cidades
    for perm in permutations(cidades):
        # Calcula o custo da rota atual
        custo = custoRota(perm)
        # Se o custo da rota for menor que o custo mínimo encontrado até agora, atualiza os valores
        if custo < custoMinimo:
            custoMinimo = custo
            melhorRota = perm  # Atualiza a melhor rota
    return melhorRota, custoMinimo  # Retorna a melhor rota e o custo mínimo encontrado

# Bloco principal do programa
if __name__ == "__main__":
    # Definição de um conjunto de cidades como coordenadas (x, y)
    cidades = [(0, 0), (3, 4), (7, 3), (6, 0), (2, 2)]

    print(f"Cidades: {cidades}")  # Imprime as cidades fornecidas
    # Chama a função de força bruta para encontrar a melhor rota e o custo mínimo
    melhorRota, custoMinimo = forcaBrutaTsp(cidades)
    # Imprime a melhor rota encontrada e o custo mínimo
    print(f"Melhor rota: {melhorRota}")
    print(f"Menor custo: {custoMinimo:.2f}")  # Imprime o custo com 2 casas decimais
