import NReinas

estado_inicial = [
    ["_", "_", "X", "_"],
    ["X", "_", "_", "_"],
    ["_", "_", "_", "X"],
    ["_", "X", "_", "_"]
]

estado_meta = [
    ["_", "_", "X", "_"],
    ["X", "_", "_", "_"],
    ["_", "_", "_", "X"],
    ["_", "X", "_", "_"]
]

raiz = NReinas.Nodo(estado_inicial)