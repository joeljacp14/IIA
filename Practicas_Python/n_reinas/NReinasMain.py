from Practicas_Python.n_reinas import NReinas

estado_inicial = [
    ["_", "_", "_", "_"],
    ["X", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"]
]

estado_meta = [
    ["_", "_", "X", "_"],
    ["X", "_", "_", "_"],
    ["_", "_", "_", "X"],
    ["_", "X", "_", "_"]
]

visitados = []
franja = []

raiz = NReinas.Nodo(estado_inicial)
nodo_meta = NReinas.Nodo(estado_meta)
raiz.heuristica(nodo_meta)

camino = raiz.greedy(nodo_meta, visitados, franja)

if not camino == []:
    print("La solucion es: ")
    for i in camino:
        i.imprime_estado()
else:
    print("No hay solucion al problema :(((")