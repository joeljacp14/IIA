from mimetypes import init
import copy as copiar
import math as mate

class Nodo(object):
    def __init__(self, estado):
        super(Nodo, self).__init__()
        self.estado = estado
        self.hijos = []
    
    def expande(self, ficha):
        ren, col = self.busca_ficha(ficha)
        if (not ren or not col):
            return None
        
        #generar arriba
        if (ren > 0):
            arriba = copiar.deepcopy(self.estado) #para copiar valores y no la direccion de memoria
            arriba[ren - 1][col] = self.estado[ren][col]
            arriba[ren][col] = self.estado[ren - 1][col]
            self.hijos.append(Nodo(arriba))
        #generar derecha
        if (col < 2):
            derecha = copiar.deepcopy(self.estado)
            derecha[ren][col + 1] = self.estado[ren][col]
            derecha[ren][col] = self.estado[ren][col + 1]
            self.hijos.append(Nodo(derecha))
        #generar abajo
        if (ren < 2):
            abajo = copiar.deepcopy(self.estado)
            abajo[ren + 1][col] = self.estado[ren][col]
            abajo[ren][col] = self.estado[ren + 1][col]
            self.hijos.append(Nodo(abajo))
        #generar izquierda
        if (col > 0):
            izquierda = copiar.deepcopy(self.estado)
            izquierda[ren][col - 1] = self.estado[ren][col]
            izquierda[ren][col] = self.estado[ren][col - 1]
            self.hijos.append(Nodo(izquierda))
    
    def busca_ficha(self, ficha):
        col = 0
        reg = 0
        for renglon in self.estado:
            for columna in renglon:
                if columna == ficha:
                    return(reg, col)
                col = col + 1
            reg = reg + 1
            col = 0
        return (None, None)

    def imprime_estado(self):
        for renglon in self.estado:
            for columna in renglon:
                print(columna, end = " ")
            print(" ")
        print(" ")
    
    def heuristica(self, meta):
        sum = 0
        re = ce = rm = cm = 0
        for i in range(8):
            rm, cm = meta.busca_ficha(i + 1)
            re, ce = self.busca_ficha(i + 1)
            sum += mate.sqrt(mate.pow((rm - re), 2)) + mate.sqrt(mate.pow((cm - ce), 2))
        rm, cm = meta.busca_ficha("_")
        re, ce = self.busca_ficha("_")
        sum += mate.sqrt(mate.pow((rm - re), 2)) + mate.sqrt(mate.pow((cm - ce), 2))
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
print("Heuristica", raiz.heuristica(nodoMeta))
print("Estado inicial")
raiz.imprime_estado()
raiz.expande()
# print("Espacio arriba")
# raiz.hijos[0].imprime_estado()
# print("Espacio derecha")
# raiz.hijos[1].imprime_estado()
# print("Espacio abajo")
# raiz.hijos[2].imprime_estado()
# print("Espacio izquierda")
# raiz.hijos[3].imprime_estado()
for i in raiz.hijos:
    i.imprime_estado()