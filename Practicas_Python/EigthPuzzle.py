import copy
import sys

import numpy

sys.setrecursionlimit(10000)

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

visitados = []
franja = []

class Nodo(object):
    def __init__(self, estado, padre=None):
        super(Nodo, self).__init__()
        self.estado = estado
        self.heur = 0
        self.hijos = []
        self.padre = padre

    def expande_hijos(self, ficha, meta): #expande y ordena con el metodo sort del objeto lista
        ren, col = self.busca_ficha(ficha)
        if (not ren or not col):
            return None

        movimiento = None
        # movimiento arriba
        if (ren > 0):
            arriba = copy.deepcopy(self.estado)  # para copy valores y no la direccion de memoria
            arriba[ren - 1][col] = self.estado[ren][col]
            arriba[ren][col] = self.estado[ren - 1][col]
            movimiento = Nodo(arriba, self)
            movimiento.heuristica(meta)
            self.hijos.append(movimiento)
        # movimiento derecha
        if (col < 2):
            derecha = copy.deepcopy(self.estado)
            derecha[ren][col + 1] = self.estado[ren][col]
            derecha[ren][col] = self.estado[ren][col + 1]
            movimiento = Nodo(derecha, self)
            movimiento.heuristica(meta)
            self.hijos.append(movimiento)
        # movimiento abajo
        if (ren < 2):
            abajo = copy.deepcopy(self.estado)
            abajo[ren + 1][col] = self.estado[ren][col]
            abajo[ren][col] = self.estado[ren + 1][col]
            movimiento = Nodo(abajo, self)
            movimiento.heuristica(meta)
            self.hijos.append(movimiento)
        # movimiento izquierda
        if (col > 0):
            izquierda = copy.deepcopy(self.estado)
            izquierda[ren][col - 1] = self.estado[ren][col]
            izquierda[ren][col] = self.estado[ren][col - 1]
            movimiento = Nodo(izquierda, self)
            movimiento.heuristica(meta)
            self.hijos.append(movimiento)

        #self.camino_mas_corto(meta, visitados)
    
    def expande_greedy(self, meta): #expande y ordena al insertar
        if self.estado == meta.estado:
            return self
        for visitado in visitados:
            if self.estado == visitado.estado:
                return None
        visitados.append(self)
        self.expande_hijos("_", meta)#si da error, ordenar a patin
        for hijo in self.hijos:
            franja.append(hijo)
        franja.sort(key=lambda x: x.heur)
        return None
    
    def busqueda_greedy(self, meta, visitados, franja, camino):
        #if eres tu
        # if es visitado
        #else
        #expande a tus hijos
        #atender a todos los de la franja mientras se va expandiendo
        franja.append(self)

        while not franja == []:
            frente = franja.pop(0)
            print("Se atiende a:")
            frente.imprime_estado()

            if frente.estado == meta.estado:
                print("¡¡¡SOLUCION ENCONTRADA!!!")
                frente.imprime_estado()
                camino.append(frente)
                padre = frente.padre
                while padre:
                    camino.append(padre)
                    padre = padre.padre
                return

            es_visitado = False
            for visitado in visitados:
                if numpy.array_equal(frente.estado, visitado.estado):
                    es_visitado = True
                    break
            if not es_visitado:
                visitados.append(frente)
                frente.expande_hijos("_", meta, franja)
        
        return None

    def greedy_recursivo(self, meta, visitados, franja, camino):
        print("Se antiende")
        self.imprime_estado()
        if numpy.array_equal(self.estado, meta.estado):
            print("¡¡¡SOLUCION ENCONTRADA!!!")
            self.imprime_estado()
            camino.append(self)
            padre = self.padre
            while padre:
                camino.append(padre)
                padre = padre.padre
            return

        es_visitado = False
        if not visitados == []:
            for visitado in visitados:
                if numpy.array_equal(self.estado, visitado.estado):
                    es_visitado = True

        if not es_visitado:
            visitados.append(self)
            self.expande_hijos("_", meta, franja)

        if not franja == []:
            return franja.pop(0).greedy_recursivo(meta, visitados, franja, camino)

        #return

    def greedy_marin(self, meta):
        camino = []
        franja.append(self)
        while not franja == []:
            frente = franja.pop(0)
            print("Se atiende a:---------")
            frente.imprime_estado()
            solucion = frente.expande_greedy(meta)
            if solucion:
                camino.append(solucion)
                padre = solucion.padre
                while padre:
                    camino.append(padre)
                    padre = padre.padre
                return camino
        return None

    def heuristica(self, meta):
        sum = 0
        re = ce = rm = cm = 0
        for i in range(1, 8):
            rm, cm = meta.busca_ficha(i)
            re, ce = self.busca_ficha(i)
            sum += abs(rm - re) + abs(cm - ce)
        rm, cm = meta.busca_ficha("_")
        re, ce = self.busca_ficha("_")
        sum += abs(rm - re) + abs(cm - ce)
        self.heur = sum
        return sum
    
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
        print("Heuristica:", self.heur)
        print("=======================")

    def camino_mas_corto(self, meta, visitados):
        heur_actual = 0
        heur_menor = 0
        mas_corto = None
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
        
        visitados.append(Nodo(copy.deepcopy(mas_corto.estado)))
        mas_corto.expande("_", meta, visitados)

# ******* main *********
raiz = Nodo(estado_inicial)
nodo_meta = Nodo(meta)
raiz.heuristica(nodo_meta)

print("Estado inicial")
raiz.imprime_estado()

camino = raiz.greedy_marin(nodo_meta)
print("El camino a la solucion es: ")
for i in camino:
    i.imprime_estado()