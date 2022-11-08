import copy
import string
class Nodo(object):
    def __init__(self, estado):
        super(Nodo, self).__init__()
        self.estado = estado
        self.heur = 0
        self.hijos = []
    
    def expande_peon(self, color, visitados):
        reg = col = 0
        if (color == 'b'):
            try:
                reg = col = self.busca_peon_del_rey(color)
                #primer posible movimiento
                movimiento = copy.deepcopy(self.estado)
                movimiento[reg + 1][col] = self.estado[reg][col]
                movimiento[reg][col] = self.estado[reg + 1][col]
                self.hijos.append(Nodo(movimiento))
                #segundo psible movimiento
                movimiento = copy.deepcopy(self.estado)
                movimiento[reg + 2][col] = self.estado[reg][col]
                movimiento[reg][col] = self.estado[reg + 2][col]
                self.hijos.append(Nodo(movimiento))
            except:
                print("No se encontro la ficha")
        else:
            try:
                reg = col = self.busca_peon_del_rey(color)
                # primer posible movimiento
                movimiento = copy.deepcopy(self.estado)
                movimiento[reg - 1][col] = self.estado[reg][col]
                movimiento[reg][col] = self.estado[reg - 1][col]
                self.hijos.append(Nodo(movimiento))
                # segundo psible movimiento
                movimiento = copy.deepcopy(self.estado)
                movimiento[reg - 2][col] = self.estado[reg][col]
                movimiento[reg][col] = self.estado[reg - 2][col]
                self.hijos.append(Nodo(movimiento))
            except:
                print("No se encontro la ficha")

    def expande_alfil(self, meta, visitados):
        pass

    def expande_caballo(self):
        pass

    def expande_reina(self):
        pass

    def busca_peon_del_rey(self, color):
        col = reg = 0
        for r in self.estado:
            for c in r:
                if color == 'n':
                    if c == "nP" and self.estado[reg - 1, col] == "nK":
                        return (reg, col)
                else:
                    if c == "bP" and self.estado[reg + 1, col] == "bK":
                        return (reg, col)
                col += 1
            reg += 1
            col = 0
        return None, None

    def busca_alfil(self):
        col = reg = 0
        for r in self.estado:
            for c in r:
                if c == "bA":
                    if self.estado[reg][col - 1] == "bK" and self.estado[reg][col + 1] == "bC":
                        return (reg, col)
                col += 1
            reg += 1
            col = 0
        return (None, None)

    def busca_caballo(self):
        reg = col = 0
        for r in self.estado:
            for c in r:
                if r == 0:
                    if c == "nC":
                        return (reg, col)
                col += 1
            reg += 1
            col = 0
        return (None, None)

    def busca_reina(self):
        reg = col = 0
        for r in self.estado:
            for c in r:
                if c == "bQ":
                    return (reg, col)
                col += 1
            reg += 1
            col = 0
        return (None, None)

    def imprime_estado(self):
        for ren in self.estado:
            for col in ren:
                print(col, end=" ")
            print(" ")
        print(" ")





##  De aca para abajo los cambios
##  Descomenta con Ctrl + k + u

#     def busca_peon_del_rey(self, color, matriz):
#         # col = reg = 0
#         for r in range(len(matriz)):
#             for c in range(len(matriz[0])):
#                 if color == 'n':
#                     if matriz[r][c] == "nP" and matriz[r - 1][c] == "nK":
#                         return (r, c)
#                 else:
#                     if matriz[r][c] == "bP" and matriz[r + 1][c] == "bK":
#                         return (r, c)
#             #     col += 1
#             # reg += 1
#         return (None, None)

#     def busca_alfil(self, matriz):
#         # col = reg = 0
#         for r in range(len(matriz)):
#             for c in range(len(matriz[0])):
#                 if matriz[r][c] == "bA":
#                     if matriz[r][c - 1] == "bK" and matriz[r][c + 1] == "bC":
#                         return (r, c)
#             #     col += 1
#             # reg += 1
#         return (None, None)

#     def busca_caballo(self, matriz):
#         # reg = col = 0
#         for r in range(len(matriz)):
#             for c in range(len(matriz[0])):
#                 if r == 0:
#                     if matriz[r][c] == "nC":
#                         return (r, c)
#             #     col += 1
#             # reg += 1
#         return (None, None)

# ## La c la usas como iterador, por lo tanto va recorriendo cada casilla y no solo las columnas, por eso nunca cumple las otras condiciones
# ## Le agrego como parametro una matri, ese seria el estado inicial y de esa manera para que sea mas entendible el recorrido  
#     def busca_reina(self, matriz):
#         # reg = col = 0
#         for r in range(len(matriz)):
#             for c in range(len(matriz[0])):
#                 if matriz[r][c] == "bQ":
#                     return (r, c)
#             #     col += 1
#             # reg += 1
#         return (None, None)