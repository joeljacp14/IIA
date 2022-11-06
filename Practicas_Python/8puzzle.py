from mimetypes import init
import copy
import math
import sys

sys.setrecursionlimit(1000000)


class Nodo(object):
    def __init__(self, estado):
        super(Nodo, self).__init__()
        self.estado = estado
        self.hijos = []

    def expande(self, ficha, meta):
        ren, col = self.busca_ficha(ficha)
        if (not ren or not col):
            return None

        # generar arriba
        if (ren > 0):
            arriba = copy.deepcopy(self.estado)  # para copy valores y no la direccion de memoria
            arriba[ren - 1][col] = self.estado[ren][col]
            arriba[ren][col] = self.estado[ren - 1][col]
            self.hijos.append(Nodo(arriba))
        # generar derecha
        if (col < 2):
            derecha = copy.deepcopy(self.estado)
            derecha[ren][col + 1] = self.estado[ren][col]
            derecha[ren][col] = self.estado[ren][col + 1]
            self.hijos.append(Nodo(derecha))
        # generar abajo
        if (ren < 2):
            abajo = copy.deepcopy(self.estado)
            abajo[ren + 1][col] = self.estado[ren][col]
            abajo[ren][col] = self.estado[ren + 1][col]
            self.hijos.append(Nodo(abajo))
        # generar izquierda
        if (col > 0):
            izquierda = copy.deepcopy(self.estado)
            izquierda[ren][col - 1] = self.estado[ren][col]
            izquierda[ren][col] = self.estado[ren][col - 1]
            self.hijos.append(Nodo(izquierda))

        self.camino_mas_corto(meta)

    def camino_mas_corto(self, meta):
        heur = 0
        lessHeur = 0
        masCorto = None
        cont = 0

        for i in self.hijos:
            heur = i.heuristica(meta)

            if (heur == 0):
                print("Solucion encontrada")
                i.imprime_estado()
                return
            if (cont == 0):
                lessHeur = i.heuristica(meta)
                masCorto = i
            else:
                if (heur < lessHeur):
                    lessHeur = heur
                    masCorto = i

            cont += 1

        masCorto.expande("_", meta)

    def busca_ficha(self, ficha):
        col = 0
        reg = 0
        for renglon in self.estado:
            for columna in renglon:
                if columna == ficha:
                    return (reg, col)
                col = col + 1
            reg = reg + 1
            col = 0
        return (None, None)

    def imprime_estado(self):
        for renglon in self.estado:
            for columna in renglon:
                print(columna, end=" ")
            print(" ")
        print(" ")

    def heuristica(self, meta):
        sum = 0
        re = ce = rm = cm = 0
        for i in range(8):
            rm, cm = meta.busca_ficha(i + 1)
            re, ce = self.busca_ficha(i + 1)
            sum += math.sqrt(math.pow((rm - re), 2)) + math.sqrt(math.pow((cm - ce), 2))
        rm, cm = meta.busca_ficha("_")
        re, ce = self.busca_ficha("_")
        sum += math.sqrt(math.pow((rm - re), 2)) + math.sqrt(math.pow((cm - ce), 2))
        print("Heuristica: ", sum)
        self.imprime_estado()
        print("=====================")
        return sum


estado_inicial = [
    [7, 1, 6],
    [4, "_", 8],
    [3, 5, 2]
]

meta = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, "_"]
]

raiz = Nodo(estado_inicial)
nodoMeta = Nodo(meta)
visitados = []

print("Heuristica", raiz.heuristica(nodoMeta))
print("Estado inicial")
raiz.imprime_estado()
visitados.append(raiz)

raiz.expande("_", nodoMeta)