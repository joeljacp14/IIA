import math

mapa = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

franja = []
visitados = []

class Nodo():
    def __init__(self, posx, posy, padre=None):
        self.posx = posx
        self.posy = posy
        self.hijos = []
        self.padre = padre

    def expande(self):
        if self.posy > 0:
            if mapa[self.posx][self.posy - 1] == 0:
                self.hijos.append(Nodo(self.posx, self.posy - 1, self))
        if self.posx < 5:
            if mapa[self.posx + 1][self.posy] == 0:
                self.hijos.append(Nodo(self.posx + 1, self.posy, self))
        if self.posy < 9:
            if mapa[self.posx][self.posy + 1] == 0:
                self.hijos.append(Nodo(self.posx, self.posy + 1, self))
        if self.posx > 0:
            if mapa[self.posx - 1][self.posy] == 0:
                self.hijos.append(Nodo(self.posx - 1, self.posy, self))

    def heuristica(self, metax, metay):
        return math.sqrt((metax - self.posx) ** 2 + (metay - self.posy) ** 2)


## soy la meta, soy visitado, si ninguno cumple, agrego visitados, expando, agrego visitados en la franja
    def greedy(self, metax, metay):
        camino = []
        franja.append(self)
        #soy la meta?
        # if (self.posx == metax) and (self.posy == metay):
        #     return self
        # # ya los visitamos 
        # for x, y in visitados:
        #     if (self.posx == x) and (self.posy == y):
        #         return None

        # visitados.append([self.posx, self.posy])
        # #mapa[self.posx][self.posy] = 2
        # self.expande()
        # for hijo in self.hijos:
        #     for pos, n in enumerate(franja):
        #         if n.heuristica(metax, metay) > hijo.heuristica(metax, metay):
        #             franja.insert(pos, hijo)
        #             break
        # print(franja[0].posx, franja[0].posy)
        while not franja == []:
            primero = franja.pop(0)
            # print(primero.posx, primero.posy)
            if (primero.posx == metax) and (primero.posy == metay):
                camino.append(primero)
                papa = primero.padre
                while papa:
                    camino.append(papa)
                    papa = papa.padre
                print("Te encontre!!!")
                return camino

            es_visitado = False
            for x, y in visitados:
                if (primero.posx == x) and (primero.posy == y):
                    es_visitado = True
                    break
            if not es_visitado:
                visitados.append([primero.posx, primero.posy])

                primero.expande()
                
                for hijo in primero.hijos:
                    # print(hijo.posx, hijo.posy)
                    if franja == []:
                        franja.append(hijo)
                    else:    
                        for pos, n in enumerate(franja):
                            # print("=====")
                            # print(pos, n.posx, n.posy)
                            if n.heuristica(metax, metay) > hijo.heuristica(metax, metay):
                                # print("=====")
                                # print(pos, n.posx, n.posy)
                                franja.insert(pos, hijo)
                                break
        return None    


##  MAIN    ##

raiz = Nodo(2, 1)
camino = raiz.greedy(2, 8)
camino.reverse()

print("Camino:")
for i in camino:
    mapa[i.posx][i.posy] = '*'
    # print(i.posx, i.posy)

for i in range(len(mapa)):
    for j in range(len(mapa[0])):
        print(mapa[i][j], end="   ")
    print("   ")   


