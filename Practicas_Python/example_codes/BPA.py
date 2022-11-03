import copy
import sys

visitados = []
visitar = []
queue = []

class Arbol(object):
	def __init__(self, dato, padre):
		self.dato = dato
		self.padre = padre
		self.hijos = []

	def test_objetivo(self, meta):
		return self.dato == meta

	def posicion_espacio(self):
		count = 0
		pos_x = -1
		pos_y = -1
		for lista in self.dato:
			try:
				pos_y = lista.index('_')
				pos_x = count
			except Exception as e:
				pass
			count += 1	
		return pos_x, pos_y

	def mueve_arriba(self, pos_x, pos_y):
		if pos_x <= 0:
			return None
		hijo = copy.deepcopy(self.dato)
		temp = hijo[pos_x-1][pos_y]
		hijo[pos_x-1][pos_y] = "_"
		hijo[pos_x][pos_y] = temp
		self.hijos.append(Arbol(hijo, self))

	def mueve_abajo(self, pos_x, pos_y):
		if pos_x >= 2:
			return None
		hijo = copy.deepcopy(self.dato)
		temp = hijo[pos_x+1][pos_y]
		hijo[pos_x+1][pos_y] = "_"
		hijo[pos_x][pos_y] = temp
		self.hijos.append(Arbol(hijo, self))	

	def mueve_derecha(self, pos_x, pos_y):
		if pos_y >= 2:
			return None
		hijo = copy.deepcopy(self.dato)
		temp = hijo[pos_x][pos_y+1]
		hijo[pos_x][pos_y+1] = "_"
		hijo[pos_x][pos_y] = temp
		self.hijos.append(Arbol(hijo, self))	

	def mueve_izquierda(self, pos_x, pos_y):
		if pos_y <= 0:
			return None
		hijo = copy.deepcopy(self.dato)
		temp = hijo[pos_x][pos_y-1]
		hijo[pos_x][pos_y-1] = "_"
		hijo[pos_x][pos_y] = temp
		self.hijos.append(Arbol(hijo, self))		

	def genera_hijos(self):
		posx, posy = self.posicion_espacio()
		if posx == -1 or posy == -1:
			return None
		self.mueve_arriba(posx, posy)
		self.mueve_derecha(posx, posy)
		self.mueve_abajo(posx, posy)
		self.mueve_izquierda(posx, posy)

	def expandir(self):
		if self.es_visitado():##si ya visitamos este arbol
			return
		visitados.append(self)
		self.genera_hijos()

	def es_visitado(self):
		for estado in visitados:
			if estado == self.dato:
				return True
		return False

	def get_way(self):
		if not self.padre:
			return [self.dato]
		way = [self.dato]
		way.extend(self.padre.get_way())
		return way

	def BPA(self, meta):
		# queue.append(self)
		# for item in queue:
		# 	if item.test_objetivo(meta):
		# 		return item.get_way()
		# 	visitados.append(item.dato)
		# 	item.expandir()
		# 	for hijo in item.hijos:
		# 		if not hijo.dato in visitados:
		# 			queue.append(hijo)

		if not self:
			return None
		# if (self.test_objetivo(meta)):
		# 		return self.dato
		if self.test_objetivo(meta):
			queue.append(self.dato)
			return True
		self.expandir()
		for hijo in self.hijos:
			lista = hijo.BPA(meta)
			if lista:
				lista.append(hijo)
				return lista
		return None	

##	Implementacion propia del deepcopy
def deepcopy(mat):
    aux = []
    aux2 = None
    for i in range(len(mat)):
        aux2 = []
        for j in range(len(mat[0])):
            aux2.append(mat[i][j])
        aux.append(aux2)
    return aux

## MAIN ##
meta = [
				[1,   2,   3],
				[8,  '_',  4],
				[7,   6,   5]
]

meta2 = [
				[1,   2,   3],
				[4,   5,   6],
				[7,   8, '_']
]

estado1  = [
				[5,   4,    1],
				[6,  '_',   8],
				[7,   3 ,   2]
]

estado2  = [
				[1,   2, '_'],
				[8,   3,   4],
				[7,   6,   5]
]
raiz = Arbol(estado1, None)
# raiz = Arbol(estado2, None)

raiz.genera_hijos()
print(raiz.dato)
for l in raiz.hijos:
	print(l.dato)


##	Busqueda Primero en Profundidad (DFS)
recorrido = raiz.BPA(meta)
print(recorrido)
# for solucion in recorrido:
#     print(solucion)

	