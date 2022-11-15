from mimetypes import init
import copy
import math
import sys
import numpy

sys.setrecursionlimit(1000000)


class Nodo(object):
    def __init__(self, estado):
        super(Nodo, self).__init__()
        self.estado = estado
        self.heur = 0
        self.hijos = []

    def expande(self, ficha, meta, visitados):
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

        self.camino_mas_corto(meta, visitados)

    def camino_mas_corto(self, meta, visitados):
        heur_actual = 0
        heur_menor = 0
        mas_corto = None
        cont = 0
        es_visitado = False

        for hijo in self.hijos:
            #recorrer los visitados, si ese nodo (hijo) ya lo visite. lo ignoro
            for visitado in visitados:
                if (numpy.array_equal(visitado.estado, hijo.estado)):
                    es_visitado = True

            if not es_visitado:
                heur_actual = hijo.heuristica(meta)

                if (heur_actual == 0):
                    print("Solucion encontrada")
                    hijo.imprime_estado()
                    return
                if (heur_menor == 0):
                    heur_menor = hijo.heuristica(meta)
                    mas_corto = hijo
                else:
                    if (heur_actual < heur_menor):
                        heur_menor = heur_actual
                        mas_corto = hijo
            
            es_visitado = False
            #cont += 1

        #agregar este nodo a la lista de visitados
        visitados.append(Nodo(copy.deepcopy(mas_corto.estado)))
        mas_corto.expande("_", meta, visitados)
    
    def greedy_busqueda(self):
        pass

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
            sum += abs(rm - re) + abs(cm - ce)
        rm, cm = meta.busca_ficha("_")
        re, ce = self.busca_ficha("_")
        sum += abs(rm - re) + abs(cm - ce)
        # print("Heuristica: ", sum)
        # self.imprime_estado()
        # print("=====================")
        self.heur = sum
        return sum

