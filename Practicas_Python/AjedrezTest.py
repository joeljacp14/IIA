import Ajedrez as ajedrez

estado_inicial = [
                    ["nT", "nC", "nA", "nQ", "nR", "nA", "nC", "nT"],
                    ["nP", "nP", "nP", "nP", "nP", "nP", "nP", "nP"],
                    ["__", "__", "__", "__", "__", "__", "__", "__"],
                    ["__", "__", "__", "__", "__", "__", "__", "__"],
                    ["__", "__", "__", "__", "__", "__", "__", "__"],
                    ["__", "__", "__", "__", "__", "__", "__", "__"],
                    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                    ["bT", "bC", "bA", "bQ", "bR", "bA", "bC", "bT"]
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