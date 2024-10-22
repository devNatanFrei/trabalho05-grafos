from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

class Grafo:
    def __init__(self, arquivo):
        self.grafo = {}
        self.values = 0
        self.load_data(arquivo)

    def load_data(self, arquivo):
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            self.values = int(linhas[0].strip())
            for linha in linhas[1:]:  
                linha = linha.strip()
                if linha: 
                    a, b = map(int, linha.split())
                    self.add_edge(a, b)
            
    def add_edge(self, a, b):
        if a not in self.grafo:
            self.grafo[a] = []
        if b not in self.grafo:
            self.grafo[b] = []
        
        if b not in self.grafo[a]:
            self.grafo[a].append(b)
        if a not in self.grafo[b]:
            self.grafo[b].append(a)

    def dfs_recur(self, graph, initial_vertex, visited):
        if visited is None:
            visited = set()

        visited.add(initial_vertex)
        
        for vertex in graph[initial_vertex]:
            if vertex not in visited:
                self.dfs_recur(graph, vertex, visited)
        
        return visited

    def dfs_iterative(self, graph, initial_vertex):
        visited = set()
        stack = deque([initial_vertex])

        while stack:
            v = stack[0]
            stack.pop()
            for neighbor in graph[v]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        
        return visited


caminho_arquivo = 'num.txt'  
grafh = Grafo(caminho_arquivo) 
print(grafh.grafo)

vertice_inicial = grafh.values  
print(grafh.dfs_recur(grafh.grafo, vertice_inicial, None))
print(grafh.dfs_iterative(grafh.grafo, vertice_inicial))