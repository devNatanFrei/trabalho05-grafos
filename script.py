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

    def dfs_stack(self, start):
        visited = set()
        stack = [(start, None)]
        path = []
        arvore_dfs = []
    
        while stack:
            vertex, dad = stack.pop()
        
            if vertex not in visited:
                visited.add(vertex)
                path.append(vertex)
                print(f"Visitando: {vertex}")
                
                if dad is not None:
                    arvore_dfs.append((dad, vertex))
        

                for neighbor in sorted(self.grafo.get(vertex, []), reverse=True):
                    if neighbor not in visited:
                        stack.append((neighbor, vertex))
          

        return visited, path, arvore_dfs

    def dfs_recursive(self, s, visited=None, path=None, arvore_dfs=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if arvore_dfs is None:
            arvore_dfs = []
        
        visited.add(s)
        path.append(s)
        print(f"Visitando: {s}")

        for w in sorted(self.grafo[s]):
            if w not in visited:
                arvore_dfs.append((s, w))
                self.dfs_recursive(w, visited, path, arvore_dfs)

        return visited, path, arvore_dfs

    def plot_graph(self, arvore_dfs, nome_arquivo='grafo_dfs.png'):
        G = nx.Graph(self.grafo)
        
        pos = nx.spring_layout(G, seed=42)

        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_size=700, font_size=15, node_color='lightblue', edge_color='lightgray')
        
        dfs_tree = nx.Graph()
        dfs_tree.add_edges_from(arvore_dfs)
        nx.draw_networkx_edges(dfs_tree, pos, edge_color='red', width=2)

        plt.title("Grafo e Árvore DFS")
        plt.savefig(nome_arquivo)
        plt.close()

caminho_arquivo = 'num2.txt'  
grafh = Grafo(caminho_arquivo)

try:
    vertice_inicial = int(input('Digite o vértice inicial: '))

    if vertice_inicial not in grafh.grafo:
        print('Vértice não encontrado')
        exit()

    print("\nDFS Recursivo:")
    visitados_recursivo, caminho_recursivo, arvore_dfs_recursiva = grafh.dfs_recursive(vertice_inicial)
    print("\nVisitados: ", visitados_recursivo)
    print("Caminho: ", caminho_recursivo)

    print("\nDFS Iterativo (usando pilha):")
    visitados_iterativo, caminho_iterativo, arvore_dfs_iterativa = grafh.dfs_stack(vertice_inicial)
    print("\nVisitados: ", visitados_iterativo)
    print("Caminho: ", caminho_iterativo)

    grafh.plot_graph(arvore_dfs_recursiva, nome_arquivo='grafo_dfs_recursivo.png')
    grafh.plot_graph(arvore_dfs_iterativa, nome_arquivo='grafo_dfs_pilha.png')

except ValueError:
    print("Por favor, insira um número inteiro.")
