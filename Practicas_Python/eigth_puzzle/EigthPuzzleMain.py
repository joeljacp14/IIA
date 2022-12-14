from Practicas_Python.eigth_puzzle import EigthPuzzle

estado_inicial = [
    [7, 1, 6],
    [4, "_", 8],
    [3, 5, 2]
]

estado_meta = [
    [7, 1, 6],
    [4, 8, 2],
    [3, 5, "_"]
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

print(">>>>>> Busqueda Primero por Anchura <<<<<")
camino = raiz.bpa(nodo_meta, visitados, franja)
imprime_camino(camino)

visitados.clear()
franja.clear()
print(">>>>>> Busqueda Primero por Profundidad <<<<<")
camino = raiz.bpp(nodo_meta, visitados, franja)
imprime_camino(camino)

visitados.clear()
franja.clear()
print(">>>>>>>>>>> Busqueda Greedy <<<<<<<<<<<<<")
camino = raiz.busqueda_greedy(nodo_meta, visitados, franja)
imprime_camino(camino)

visitados.clear()
franja.clear()
print(">>>>>>>>>>> Busqueda A Estrella <<<<<<<<<<<<<")
camino = raiz.a_estrella(nodo_meta, visitados, franja)
imprime_camino(camino)