from eigth_puzzle import Puzzle
from eigth_puzzle import get_num

## MAIN ##
estado1 = [
                [3,   1,   6],
                [4,  '_',  8],
                [7,   5,   2]
]

estado2 = [
                [7,   1,   6],  
                [4,  '_',  8],
                [3,   5,   2]
] 

meta = [
                [1,   2,   3],
                [4,   5,   6],
                [7,   8, '_']
]

meta2 = [
                [1,   2,   3],
                [8,  '_',  4],
                [7,   6,   5]
]

raiz1 = Puzzle(estado1)
raiz2 = Puzzle(estado2)

# raiz2.expand()
# for lista in raiz2.branches:
#     lista.state_print()


# print(f"Suma recorrido: {raiz2.heuristic(meta)}")
# numero = 8
# print(f"Posicion del {numero}: {get_num(raiz2.state, numero)}")
# print("Estado inicial")
# raiz2.state_print()
# raiz2.expand()

# for hijo in raiz2.branches:
#     print(f"Heuristica: {hijo.heuristic(meta)}")
#     hijo.state_print()
    

print("Busqueda Greedy")
camino = raiz2.greedy_search(meta)
for i in camino:
    print(i.state)

# print("Busqueda A *")
# camino = raiz2.astar_search(meta)
# for i in camino:
#     print(i.state)

# print("Busqueda por Anchura")
# camino = raiz2.BFS(meta)
# for i in camino:
#     print(i.state)
