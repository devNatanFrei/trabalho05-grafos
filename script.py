from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self, arquivo):
        self.grafo = {}
        self.load_data(arquivo)

    def load_data(self, arquivo):
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            for linha in linhas:  
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

    def dfs_recur(self, initial_vertex, visited=None):
        if visited is None:
            visited = set()

        visited.add(initial_vertex)
        
        for vertex in self.grafo[initial_vertex]:
            if vertex not in visited:
                self.dfs_recur(vertex, visited)
        
        return visited

    def dfs_iterative(self, initial_vertex):
        visited = set()
        stack = deque([initial_vertex])

        while stack:
            v = stack.pop()  
            for neighbor in self.grafo[v]:  
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        
        return visited

    def plot_graph(self):
        G = nx.Graph(self.grafo)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=15)
        plt.title("Grafo")
        plt.show()

caminho_arquivo = 'num.txt'  
grafh = Grafo(caminho_arquivo) 
print(grafh.grafo)

vertice_inicial = int(input('Digite o vértice inicial: ')) 
if vertice_inicial not in grafh.grafo:
    print('Vértice não encontrado')
    exit()
elif vertice_inicial in grafh.grafo:
    print("DFS Recursivo:", grafh.dfs_recur(vertice_inicial))
    print("DFS Iterativo:", grafh.dfs_iterative(vertice_inicial))


grafh.plot_graph()