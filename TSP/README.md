# Problema do Caixeiro Viajante (TSP) - Solução em Python

Este projeto implementa uma solução para o **Problema do Caixeiro Viajante (TSP)** utilizando o método de **força bruta**. O objetivo é encontrar a rota mais curta que visita todas as cidades exatamente uma vez e retorna à cidade inicial.

## Índice

1. [Descrição do Problema](#descrição-do-problema)
2. [Requisitos](#requisitos)
3. [Como Executar](#como-executar)
4. [Exemplo de Saída](#exemplo-de-saída)
5. [Explicação do Código](#explicação-do-código)
6. [Limitações](#limitações)

---

## Descrição do Problema

O **Problema do Caixeiro Viajante (TSP)** é um problema clássico de otimização combinatória. Dado um conjunto de cidades e as distâncias entre elas, o objetivo é encontrar a rota mais curta que:

- Visite cada cidade exatamente uma vez.
- Retorne à cidade inicial.

Este programa usa o método de **força bruta**, que gera todas as permutações possíveis das cidades e calcula o custo total de cada rota para encontrar a melhor solução.

---

## Requisitos

Para executar este programa, você precisará de:

- **Python 3.x**: Certifique-se de ter o Python instalado. Você pode verificar sua versão executando:

    ```bash
    python --version
    ```

- **Bibliotecas Padrão**: Este programa usa apenas bibliotecas padrão do Python (`math` e `itertools`), portanto, não há necessidade de instalar dependências adicionais.

---

## Como Executar

1. **Clone ou Baixe o Código**:
   - Clone este repositório ou baixe o arquivo `tsp.py`.

2. **Execute o Programa**:
   - Abra um terminal ou prompt de comando.
   - Navegue até o diretório onde o arquivo `tsp.py` está localizado.
   - Execute o programa com o seguinte comando:

     ```bash
     python tsp.py
     ```

3. **Resultado**:
   - O programa imprimirá as cidades fornecidas, a melhor rota encontrada e o custo mínimo da rota.

---

## Exemplo de Saída

Ao executar o programa com o conjunto de cidades `[(0, 0), (3, 4), (7, 3), (6, 0), (2, 2)]`, a saída será:

```
Cidades: [(0, 0), (3, 4), (7, 3), (6, 0), (2, 2)]
Melhor rota: ((0, 0), (2, 2), (3, 4), (7, 3), (6, 0))
Custo mínimo: 16.48
```

---

## Explicação do Código

O código é dividido nas seguintes partes principais:

1. **Função `distancia`**:
   - Calcula a distância euclidiana entre duas cidades usando a fórmula:
   
     $$
     \text{distância}(A, B) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
     $$

2. **Função `custoRota`**:
   - Calcula o custo total de uma rota somando as distâncias entre cidades consecutivas e conectando a última cidade à primeira.

3. **Função `forcaBrutaTsp`**:
   - Gera todas as permutações possíveis das cidades usando `itertools.permutations`.
   - Calcula o custo de cada rota e retorna a rota com o menor custo.

4. **Função Principal (`if __name__ == "__main__":`)**:
   - Define um conjunto de cidades de exemplo.
   - Chama a função `forcaBrutaTsp` para encontrar a melhor rota e o custo mínimo.
   - Imprime os resultados no terminal.

---