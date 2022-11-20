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

def imprime_camino(camino):
    if camino:
        print("El camino a la solucion es:")
        for i in camino:
            i.imprime_estado()
    else:
        print("No hay solucion")


visitados = []
franja = []

raiz = EigthPuzzle.Nodo(estado_inicial)
nodo_meta = EigthPuzzle.Nodo(meta)
raiz.heuristica(nodo_meta)

print("Estado inicial")
raiz.imprime_estado()

print("Busqueda Greedy")
camino = raiz.busqueda_greedy(nodo_meta, visitados, franja)
imprime_camino(camino)

print("Greedy recursivo")
camino = raiz.greedy_recursivo(nodo_meta, visitados, franja)
imprime_camino(camino)

print("Greedy Marin")
camino = raiz.greedy_marin(nodo_meta, visitados, franja)
imprime_camino(camino)

print("Greedy posgrado")
camino = raiz.greedy_posgrado(nodo_meta, visitados, franja)
imprime_camino(camino)