##	Hay algun error con el deepcopy
##	La otra es por la cantidad de veces que se llama asi mismo el metodo
import copy
import sys

visitados = []
visitar = []
queue = []

class Arbol(object):
	def __init__(self, dato):
		self.dato = dato
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
		self.hijos.append(Arbol(hijo))

	def mueve_abajo(self, pos_x, pos_y):
		if pos_x >= 2:
			return None
		hijo = copy.deepcopy(self.dato)
		temp = hijo[pos_x+1][pos_y]
		hijo[pos_x+1][pos_y] = "_"
		hijo[pos_x][pos_y] = temp
		self.hijos.append(Arbol(hijo))	

	def mueve_derecha(self, pos_x, pos_y):
		if pos_y >= 2:
			return None
		hijo = copy.deepcopy(self.dato)
		temp = hijo[pos_x][pos_y+1]
		hijo[pos_x][pos_y+1] = "_"
		hijo[pos_x][pos_y] = temp
		self.hijos.append(Arbol(hijo))	

	def mueve_izquierda(self, pos_x, pos_y):
		if pos_y <= 0:
			return None
		hijo = copy.deepcopy(self.dato)
		temp = hijo[pos_x][pos_y-1]
		hijo[pos_x][pos_y-1] = "_"
		hijo[pos_x][pos_y] = temp
		self.hijos.append(Arbol(hijo))		

	def genera_hijos(self): ##expandir
		##buscar posicion del espacio
		##ver movimientos permitidos
		##guardar los movimientos permitidos en los hijos
		# print(self.posicion_espacio())
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
		# if (self in visitados):
		# 	return True
		for estado in visitados:
			if estado == self.dato:
				return True
		return False

	def BPP(self, meta):
		# if (self.test_objetivo(meta)):
		# 	return [self]
		# self.expandir(meta)
		# for hijo in self.hijos:
		# 	lista = hijo.BPP(meta)
		# 	if (lista):
		# 		lista.append(self)
		# 		return lista
		# return None

		# if not self.dato:
		# 	return False
		# if self.test_objetivo(meta):
		# 	visitar.append(self.dato)
		# 	return True
		# if self.es_visitado():
		# 	return False
		# visitados.append(self.dato)
		# self.expandir()
		# for hijo in self.hijos:
		# 	if hijo.BPP(meta):
		# 		visitar.append(self.data)
		# 		return True
		# return False
		if not self.dato:
			return None
		if self.es_visitado():
			return None
		stack = []
		if self.test_objetivo(meta):
			stack.append(self.dato)
			return stack
		visitados.append(self.dato)
		self.expandir()
		for hijo in self.hijos:
			aux = hijo.BPP(meta)
			if aux:
				stack.append(self.dato)
				stack.extend(aux)
				return stack
		return stack


	# def __eq__(self, other): # ==
	# 	return self.dato == other.dato	


# raiz = Arbol([[5,4,1],[6,"_",8],[7,3,2]])
##[[5,4,8],[6,1,"_"],[7,3,2]]	
##[[5,"_",4],[6,1,8],[7,3,2]]

# lista_de_visitados = [Arbol([[5,4,1],[6,"_",8],[7,3,2]]), 
# 				      Arbol([[5,4,8],[6,1,"_"],[7,3,2]]), 
# 				      Arbol([[5,"_",4],[6,1,8],[7,3,2]])]
# estado = Arbol([[5,"_",4],[6,1,8],[7,3,2]])

# tem = [5, 4, 5, 3, 2]	

# if (estado in lista_de_visitados):
# 	print("Si")
# else:
# 	print("No")


# for elemento in lista_de_visitados:
# 	if elemento.dato == estado.dato:
# 		print("Si esta ", elemento)
# 	else:
# 		print("Este no esta: ", elemento)	

# print(estado)

# raiz.genera_hijos()
# print(raiz.dato)
# for h in raiz.hijos:
# 	print(h.dato)



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
raiz = Arbol(estado1)
# raiz = Arbol(estado2)

raiz.genera_hijos()
print(raiz.dato)
for l in raiz.hijos:
	print(l.dato)


##	Busqueda Primero en Profundidad (DFS)
recorrido = raiz.BPP(meta)
for solucion in recorrido:
    print(solucion)

	