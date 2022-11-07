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

raiz = EigthPuzzle.Nodo(estado_inicial)
nodoMeta = EigthPuzzle.Nodo(meta)
visitados = []

print("Heuristica", raiz.heuristica(nodoMeta))
print("Estado inicial")
raiz.imprime_estado()
visitados.append(EigthPuzzle.Nodo(copy.deepcopy(raiz.estado)))

raiz.expande("_", nodoMeta, visitados)