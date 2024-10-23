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

    def dfs_iterative(self, s, visited=None):
        visited = set()
        stack = deque([s])      
        visited.add(s)   
        path = [s]
        while stack:  
            v = stack.pop()  
            print(f'Visitando: {v}') 
            if v not in path:
                path.append(v)  

            for w in self.grafo[v]:
                if w not in visited:
                    stack.append(w)
                    visited.add(w)

        return visited, path  

    def dfs_recursive(self, s, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(s)
        path.append(s)  
        print(f'Visitando: {s}') 

        for w in self.grafo[s]:
            if w not in visited:
                self.dfs_recursive(w, visited, path)

        return visited, path  

    def plot_graph(self):
        G = nx.Graph(self.grafo)
        
      
        pos = nx.spring_layout(G, seed=42) 
        levels = self.get_tree_levels(G)

    
        for node, level in levels.items():
            pos[node][1] = -level  

        plt.figure(figsize=(12, 8))  
        nx.draw(G, pos, with_labels=True, node_size=700, font_size=15, node_color='lightblue', edge_color='gray')
        
        plt.title("Grafo - DFS (Representação em Árvore)")
        plt.axis('off')
        plt.show()

    def get_tree_levels(self, G):
     
        levels = {}
        for node in G.nodes():

            levels[node] = self.get_node_level(G, node)
        return levels

    def get_node_level(self, G, node, visited=None, level=0):
        if visited is None:
            visited = set()

        visited.add(node)
        max_level = level
        
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                child_level = self.get_node_level(G, neighbor, visited, level + 1)
                max_level = max(max_level, child_level)

        return max_level


caminho_arquivo = 'num.txt'  
grafh = Grafo(caminho_arquivo) 

try:
    vertice_inicial = int(input('Digite o vértice inicial: ')) 

    if vertice_inicial not in grafh.grafo:
        print('Vértice não encontrado')
        exit()

    print("DFS Recursivo:")
    visitados_recursivo, caminho_recursivo = grafh.dfs_recursive(vertice_inicial)
    print("Visitados: ", visitados_recursivo)
    print("Caminho: ", caminho_recursivo)
    print()

    print("DFS Iterativo:")
    visitados_iterativo, caminho_iterativo = grafh.dfs_iterative(vertice_inicial)
    print("Visitados: ", visitados_iterativo)
    print("Caminho: ", caminho_iterativo)

    grafh.plot_graph()

except ValueError:
    print("Por favor, insira um número inteiro.")
