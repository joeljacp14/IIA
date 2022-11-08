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
        reg = col = 0
        try:
            reg = col = self.busca_alfil()
            izq = col - 1
            der = col + 1
            regtmp = reg - 1
            #movimientos en diagonales a la izquierda
            while izq >= 0 and regtmp >= 0:
                movimiento = copy.deepcopy(self.estado)
                movimiento[regtmp][izq] = self.estado[reg][col]
                movimiento[reg][col] = self.estado[regtmp][izq]
                self.hijos.append(Nodo(movimiento))
                regtmp -= 1
                izq -= 1
            #movimientos en diagonal a la derecha
            regtmp = reg - 1
            while der <= 7 and regtmp >= 0:
                movimiento = copy.deepcopy(self.estado)
                movimiento[regtmp][der] = self.estado[reg][col]
                movimiento[reg][col] = self.estado[regtmp][der]
                self.hijos.append(Nodo(movimiento))
                regtmp -= 1
                der += 1
        except:
            print("No se pudieron crear los movimientos")


    def expande_caballo(self):
        try:
            reg = col = self.busca_caballo()
            #primer movimiento
            movimiento = copy.deepcopy(self.estado)
            movimiento[reg + 2][col - 1] = self.estado[reg][col]
            movimiento[reg][col] = self.estado[reg + 2][col - 1]
            self.hijos.append(Nodo(movimiento))
            #segundo movimiento
            movimiento = copy.deepcopy(self.estado)
            movimiento[reg + 2][col + 1] = self.estado[reg][col]
            movimiento[reg][col] = self.estado[reg + 2][col + 1]
            self.hijos.append(Nodo(movimiento))
        except:
            print("no se pudieron crear los movimientos")

    def expande_reina(self):
        try:
            reg = col = self.busca_reina()
            # movimientos en diagonal arriba - izquierda
            izq = col - 1
            arr = reg - 1
            while izq >= 0 and arr >= 0:
                movimiento = copy.deepcopy(self.estado)
                movimiento[arr][izq] = self.estado[reg][col]
                movimiento[reg][col] = self.estado[arr][izq]
                self.hijos.append(Nodo(movimiento))
                arr -= 1
                izq -= 1
            # movimiento arriba
            arr = reg - 1
            while arr >= 0:
                movimiento = copy.deepcopy(self.estado)
                movimiento[arr][col] = self.estado[reg][col]
                movimiento[reg][col] = self.estado[arr][col]
                self.hijos.append(Nodo(movimiento))
                arr -= 1
            # movimientos en diagonal arriba - derecha
            arr = reg - 1
            der = col + 1
            while der <= 7 and arr >= 0:
                movimiento = copy.deepcopy(self.estado)
                movimiento[arr][der] = self.estado[reg][col]
                movimiento[reg][col] = self.estado[arr][der]
                self.hijos.append(Nodo(movimiento))
                arr -= 1
                der += 1
            #movimiento derecha
            der = col + 1
            while der <= 7:
                movimiento = copy.deepcopy(self.estado)
                movimiento[reg][der] = self.estado[reg][col]
                movimiento[reg][col] = self.estado[reg][der]
                self.hijos.append(Nodo(movimiento))
                der += 1
            #movimiento abajo - derecha
            aba = reg + 1
            der = col + 1
            while aba <= 7 and der <= 7:
                movimiento = copy.deepcopy(self.estado)
                movimiento[aba][der] = self.estado[reg][col]
                movimiento[reg][col] = self.estado[aba][der]
                self.hijos.append(Nodo(movimiento))
                aba += 1
                der += 1
            #movimiento abajo
            aba = reg + 1
            while aba <= 7:
                movimiento = copy.deepcopy(self.estado)
                movimiento[aba][col] = self.estado[reg][col]
                movimiento[reg][col] = self.estado[aba][col]
                self.hijos.append(Nodo(movimiento))
                aba += 1
            #movimiento abajo - izquierda
            aba = reg + 1
            izq = col - 1
            while izq >= 0 and aba <= 7:
                movimiento = copy.deepcopy(self.estado)
                movimiento[aba][izq] = self.estado[reg][col]
                movimiento[reg][col] = self.estado[aba][izq]
                self.hijos.append(Nodo(movimiento))
                aba += 1
                izq -= 1
            #movimiento izquierda
            izq = col - 1
            while izq >= 0:
                movimiento = copy.deepcopy(self.estado)
                movimiento[reg][izq] = self.estado[reg][col]
                movimiento[reg][col] = self.estado[reg][izq]
                self.hijos.append(Nodo(movimiento))
                izq -= 1
        except:
            print("no se pud crear los movimientos")

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