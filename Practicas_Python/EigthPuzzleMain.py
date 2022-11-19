import copy

import EigthPuzzle

estado_inicial = [
    [7, 1, 6],
    [4, "_", 8],
    [3, 5, 2]
]

meta = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, "_"]
]

visitados = []
franja = []
camino = []

raiz = EigthPuzzle.Nodo(estado_inicial)
nodo_meta = EigthPuzzle.Nodo(meta)

print("Estado inicial")
raiz.imprime_estado()

raiz.busqueda_greedy(nodo_meta, visitados, franja, camino)
for i in camino:
    i.imprime_estado()
