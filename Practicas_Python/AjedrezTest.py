import Ajedrez as ajedrez

estado_inicial = [
                    ["nT", "nC", "nA", "nQ", "nK", "nA", "nC", "nT"],
                    ["nP", "nP", "nP", "nP", "nP", "nP", "nP", "nP"],
                    ["__", "__", "__", "__", "__", "__", "__", "__"],
                    ["__", "__", "__", "__", "__", "__", "__", "__"],
                    ["__", "__", "__", "__", "__", "__", "__", "__"],
                    ["__", "__", "__", "__", "__", "__", "__", "__"],
                    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                    ["bT", "bC", "bA", "bQ", "bK", "bA", "bC", "bT"]
                ]

meta = [# jaque mate del loco (se pierde un peon negro, donde esta la reina blanca) GANAN LAS FICHAS BLANCAS
                    ["nT", "__", "nA", "nQ", "nK", "nA", "__", "nT"],
                    ["nP", "nP", "nP", "nP", "__", "bQ", "nP", "nP"],
                    ["__", "__", "nC", "__", "__", "nC", "__", "__"],
                    ["__", "__", "__", "__", "nP", "__", "__", "__"],
                    ["__", "__", "bA", "__", "bP", "__", "__", "__"],
                    ["__", "__", "__", "__", "__", "__", "__", "__"],
                    ["bP", "bP", "bP", "bP", "__", "bP", "bP", "bP"],
                    ["bT", "bC", "bA", "__", "bK", "__", "bC", "bT"]
]

raiz = ajedrez.Nodo(estado_inicial)
raiz.imprime_estado()