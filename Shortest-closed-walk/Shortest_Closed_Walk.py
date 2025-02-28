#!git clone https://github.com/pdlmachado/gtufcg.git
#from gtufcg.util.networkx_util import draw_graph

import networkx as nx

#@title  { run: "auto", vertical-output: true }
layout1 = "spring_layout" #@param ["circular_layout", "kamada_kawai_layout", "random_layout", "shell_layout", "spring_layout", "spectral_layout", "spiral_layout"]
filename1 = "s-u-w-cy-sc-p-05.graphml" #@param ["p-u-w-cy-sc-p-01.graphml", "s-u-w-cy-sc-01.graphml", "s-u-w-cy-sc-p-01.graphml", "s-u-w-cy-sc-p-02.graphml", "s-u-w-cy-sc-p-03.graphml", "s-u-w-cy-sc-p-04.graphml", "s-u-w-cy-sc-p-05.graphml"]

def shortest_closed_walk(g, init):
    M = nx.MultiGraph(g)
    odd_nodes = [node for node in M.nodes() if M.degree(node) % 2 == 1]

    while odd_nodes:
      distancia_minima = float("inf")
      x,y = None, None

      for u in odd_nodes:
        for v in odd_nodes:
          if u != v:
            distancia = nx.shortest_path_length(M, u, v, weight= "weight")
            if distancia < distancia_minima:
              distancia_minima = distancia
              x, y = u, v

      key = 1
      caminho = nx.shortest_path(M, x, y, weight= "weight")

      for i in range(len(caminho) -1):
        u, v = caminho[i], caminho[i+1]
        M.add_edge(u, v, key=key)
        M[u][v][key]['weight'] = g[u][v]['weight']
        key += 1

      odd_nodes.remove(x)
      odd_nodes.remove(y)

    circuito = list(nx.eulerian_circuit(M, source= init))
    resultado = [(u, v) for u,v in circuito]

    return resultado


# Exemplo de uso da função
G1 = nx.read_graphml("gtufcg/graphs/"+filename1)
for u,v in G1.edges:
    G1[u][v]['weight']=float(G1[u][v]['label'])

draw_graph(G1,layoutid=layout1,
           edge_labels=nx.get_edge_attributes(G1,'weight'))
print(shortest_closed_walk(G1,'n0'))