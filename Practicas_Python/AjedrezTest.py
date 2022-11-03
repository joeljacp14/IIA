import Ajedrez as ajedrez

estado_inicial = [
                    ["T", "C", "A", "K", "Q", "A", "C", "T"],
                    ["P", "nP", "P", "P", "P", "P", "P", "P"],
                    ["_", "_", "_", "_", "_", "_", "_", "_"],
                    ["_", "_", "_", "_", "_", "_", "_", "_"],
                    ["_", "_", "_", "_", "_", "_", "_", "_"],
                    ["_", "_", "_", "_", "_", "_", "_", "_"],
                    ["P", "bP", "P", "P", "P", "P", "P", "P"],
                    ["T", "C", "A", "K", "Q", "A", "C", "T"]
                ]

meta = [
    [],
    [],
    [],
    [],
    [],
    []
]

raiz = ajedrez.Nodo(estado_inicial)
raiz.imprime_estado()