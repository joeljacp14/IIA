from ast import If
from mimetypes import init


class Nodo(object):
    def __init__(self, arg):
        self.dato = arg
        self.izq = None
        self.der = None
    
    def insertar(self, dato):
        if dato < self.dato:
            if self.izq:
                self.izq.insertar(dato)
            else:
                self.izq = Nodo(dato)
        if dato > self.dato:
            if self.der:
                self.der.insertar(dato)
            else:
                self.der = Nodo(dato)
    
    def preOrden(self):
        print(self.dato)
        if self.izq:
            self.izq.preOrden()
        if self.der:
            self.der.preOrden()

    def inOrden(self):
        if self.izq:
            self.izq.inOrden()
        print(self.dato)
        if self.der:
            self.der.inOrden()

    def posOrden(self):
        if self.izq:
            self.izq.posOrden()
        if self.der:
            self.der.posOrden()
        print(self.dato)

    def buscar(self, dato):
        if dato == self.dato:
            #return self.dato
            print("Dato encontrado")
            return True
        if dato < self.dato:
            if self.izq:
                return self.izq.buscar(dato)
        if dato > self.dato:
            if self.der:
                return self.der.buscar(dato)
        print("No se encontro")
        return False

raiz = Nodo(55)
raiz.insertar(27)
raiz.insertar(64)
raiz.insertar(100)
raiz.insertar(20)
print(raiz.buscar(20))
print(raiz.buscar(500))
# 20, 27, 36, 

print("Impresion preOrden")
raiz.preOrden()
print("Impresion inOrden")
raiz.inOrden()
print("Impresion posOrden")
raiz.posOrden()