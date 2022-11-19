from ast import If
from mimetypes import init
import this
from tkinter import SEL_FIRST

from symbol import factor


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
            print("Dato", dato, "encontrado")
            return True
        if dato < self.dato:
            if self.izq:
                return self.izq.buscar(dato)
        if dato > self.dato:
            if self.der:
                return self.der.buscar(dato)
        print("No se encontro", dato)
        return False
    
    def mas_izquierda(self):
        if not self.izq:
            return self.dato
        return self.izq.mas_izquierda()
    
    def mas_derecha(self):
        if not self.der:
            return self.dato
        return self.der.mas_derecha()
    
    def eliminar(self, dato):
        if not self:
            return -1
        #si el nodo a eliminar es raiz
        if self.dato == dato:
            if not self.izq and not self.der:
                return 1
            if self.izq and not self.der:
                return 2
            if not self.izq and self.der:
                return 3
            if self.izq and self.izq:
                return 4
        
        if self.izq and self.der:
            #si el nodo a eliminar es el izquierdo
            if self.izq.dato == dato:
                #caso 1: el nodo a eliminar es hoja
                if not self.izq.izq and not self.izq.der:
                    self.izq = None
                    return 0
                #caso 2: el nodo a eliminar tiene UN hijo
                if self.izq.izq and not self.izq.der:
                    self.izq = self.izq.izq
                    return 0
                if not self.izq.izq and self.izq.der:
                    self.izq = self.izq.der
                    return 0
                #caso 3: el nodo tiene DOS hijossss
                if self.izq.izq and self.izq.der:
                    flag = 0
                    #caso A: con mas izquierda
    
    def altura(self):
        if not self:
            return 0
        if self.izq.altura() > self.der.altura():
            return 1 + self.izq.altura()
        else:
            return 1 + self.der.altura()
    
    def factor_equilibrio(self):
        if not self:
            return 0
        return self.izq.altura() - self.der.altura()
    
    def balancear(self):
        if not self:
            return
        if self.factor_equilibrio() == -2 and self.izq.factor_equilibrio() == -1:#rot izq->izq
            self.rot_izq_izq(self.izq)
        if self.factor_equilibrio() == 2 and self.der.factor_equilibrio() == 1:#rot der->
            self.rot_der_der(self.der)
        if self.factor_equilibrio() == 2 and self.der.factor_equilibrio() == -1:#rot der->izq
            self.rot_der_izq(self.der, self.der.izq)
        if self.factor_equilibrio() == -2 and self.der.factor_equilibrio() == 1:#rot izq->der
            self.rot_izq_der(self.izq, self.izq.der)
        self.izq.balancear()
        self.der.balancear()
    
    def rot_izq_izq(self, nodo):
        self.izq = nodo.izq
        nodo.der = self
        self = nodo

    def rot_der_der(self, nodo):
        self.der = nodo.izq
        nodo.izq = self
        self = nodo

    def rot_der_izq(self, nodo1, nodo2):
        nodo1.izq = nodo2.der
        nodo2.der = nodo1
        self.der = nodo2.izq
        nodo2.izq = self
        self = nodo2

    def rot_izq_der(self, nodo1, nodo2):
        nodo1.der = nodo2.izq
        nodo2.izq = nodo1
        self.izq = nodo2.der
        nodo2.der = self
        self = nodo2

raiz = Nodo(55)
raiz.insertar(27)
raiz.insertar(64)
raiz.insertar(100)
raiz.insertar(20)
raiz.insertar(67)
raiz.insertar(60)
raiz.insertar(99)
raiz.insertar(1)
raiz.insertar(53)

print("Impresion preOrden")
raiz.preOrden()
print("Impresion inOrden")
raiz.inOrden()
print("Impresion posOrden")
raiz.posOrden()

print("Busqueda", raiz.buscar(20))
print("Busqueda", raiz.buscar(500))

print("Nodo mas a la derecha del subarbol izquierdo es:", raiz.izq.mas_derecha())
print("Nodo mas a la izquierda del subarbol derecho es:", raiz.der.mas_izquierda())