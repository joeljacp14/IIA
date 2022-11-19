import Ajedrez as ajedrez

estado_inicial = [  # A     B     C     D     E     F     G     H
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
nodo_meta = ajedrez.Nodo(meta)

raiz.imprime_estado()
raiz.expande_peon("b")
raiz.heuristica(nodo_meta)

print("POSICIONES DE LAS FICHAS")
# print(f"Peon negro: {raiz.busca_peon_del_rey('n', estado_inicial)}")
# print(f"Peon blanco: {raiz.busca_peon_del_rey('b', estado_inicial)}")
# print(f"Alfil blanco casilla blanca: {raiz.busca_alfil(estado_inicial)}")
# print(f"Caballo negro: {raiz.busca_caballo(estado_inicial)}")
# print(f"Reina blanca: {raiz.busca_reina(estado_inicial)}")   # Aqui si da pero la columna la devuelva como el numero general de la casilla

print(f"Peon negro: {raiz.busca_peon_del_rey('n')}")
print(f"Peon blanco: {raiz.busca_peon_del_rey('b')}")
print(f"Alfil blanco casilla blanca: {raiz.busca_alfil()}")
print(f"Caballo negro: {raiz.busca_caballo()}")
print(f"Reina blanca: {raiz.busca_reina()}")   # Aqui si da pero la columna la devuelva como el numero general de la casilla