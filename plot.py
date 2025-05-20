import heapq
import matplotlib.pyplot as plt
import networkx as nx  # Biblioteca para trabalhar com grafos

def dijkstra(grafo, inicio):
    """
    Função que implementa o algoritmo de Dijkstra para encontrar o menor caminho
    em um grafo com pesos não negativos, com visualização gráfica.
    
    Args:
        grafo (dict): Dicionário que representa o grafo (vértice: {vizinho: peso})
        inicio (str): Vértice de partida para o cálculo dos caminhos
    
    Returns:
        dict: Dicionário com as distâncias mínimas do vértice inicial para todos os outros
    """
    
    # Inicializa as distâncias: infinito para todos, exceto o início (0)
    distancias = {vertice: float('infinity') for vertice in grafo}
    distancias[inicio] = 0
    caminhos = {vertice: [] for vertice in grafo}  # Para armazenar os caminhos
    caminhos[inicio] = [inicio]
    
    # Fila de prioridade (heap) para processar os vértices
    fila_prioridade = [(0, inicio)]
    
    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)
        
        if distancia_atual > distancias[vertice_atual]:
            continue
        
        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso
            
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminhos[vizinho] = caminhos[vertice_atual] + [vizinho]
                heapq.heappush(fila_prioridade, (distancia, vizinho))
    
    return distancias, caminhos

def visualizar_grafo(grafo, caminhos=None, inicio=None):
    """
    Função para visualizar o grafo usando matplotlib e networkx
    
    Args:
        grafo (dict): O grafo a ser visualizado
        caminhos (dict): Caminhos mínimos encontrados (opcional)
        inicio (str): Vértice de início (para destacar)
    """
    G = nx.DiGraph()  # Cria um grafo direcionado
    
    # Adiciona arestas e pesos ao grafo
    for no, vizinhos in grafo.items():
        for vizinho, peso in vizinhos.items():
            G.add_edge(no, vizinho, weight=peso)
    
    # Posicionamento dos nós
    pos = nx.spring_layout(G)
    
    # Desenha o grafo base
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    
    # Adiciona labels com os pesos das arestas
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Destaca o caminho mínimo se fornecido
    if caminhos and inicio:
        for destino, caminho in caminhos.items():
            if destino != inicio and caminho:
                # Desenha as arestas do caminho mínimo em vermelho
                arestas_caminho = list(zip(caminho[:-1], caminho[1:]))
                nx.draw_networkx_edges(G, pos, edgelist=arestas_caminho,
                                     edge_color='r', width=2, arrowstyle='->', arrowsize=25)
    
    # Configurações do gráfico
    plt.title("Visualização do Grafo com Dijkstra")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Grafo de exemplo (mais complexo para melhor visualização)
grafo_exemplo = {
    'A': {'B': 6, 'D': 1, 'H': 2},
    'B': {'A': 6, 'C': 5, 'D': 2, 'G': 3},
    'C': {'B': 5, 'D': 1, 'E': 3, 'I': 1},
    'D': {'A': 1, 'B': 2, 'C': 1, 'E': 4, 'F': 2},
    'E': {'C': 3, 'D': 4, 'F': 1},
    'F': {'D': 2, 'E': 1, 'G': 4},
    'G': {'B': 3, 'F': 4, 'H': 3},
    'H': {'A': 2, 'G': 3, 'I': 2},
    'I': {'C': 1, 'H': 2}
}

# Calcula os caminhos mínimos
inicio = 'A'
distancias, caminhos = dijkstra(grafo_exemplo, inicio)

# Mostra os resultados
print(f"Distâncias mínimas a partir de {inicio}:")
for vertice, distancia in distancias.items():
    print(f"Até {vertice}: {distancia} (Caminho: {' → '.join(caminhos[vertice])})")

# Visualiza o grafo com os caminhos mínimos
visualizar_grafo(grafo_exemplo, caminhos, inicio)