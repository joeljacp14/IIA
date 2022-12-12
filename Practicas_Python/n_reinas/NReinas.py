import copy

class Nodo(object):
    def __int__(self, estado, padre=None):
        super(Nodo, self).__int__()
        self.estado = estado
        self.h = 0
        self.hijos = []
        self.padre = padre

    def imprime_estado(self):
        for renglon in self.estado:
            for columna in renglon:
                print(columna, end=" ")
            print(" ")
        print("Heuristica:", self.heur)
        print("=======================")

    def busca_reinas(self):
        reinas = []
        col = 0
        reg = 0
        for renglon in self.estado:
            for columna in renglon:
                if columna == "X":
                    reinas.append([reg, col])
                col = col + 1
            reg = reg + 1
            col = 0
        return reinas

    def heuristica(self, meta):
        h = 0
        reinas_estado = self.busca_reinas()
        reinas_meta = meta.busca_reinas()

        for re in reinas_estado:
            for ce in re:
                for rm in reinas_meta:
                    if re == rm[0]:
                        h += abs(rm[0] - re)
                    if ce == rm[1]:
                        h += abs(rm[1] - ce)

        self.h = h


    def expande(self, meta, franja):
        reinas = self.busca_reinas()
        lenght = len(reinas)

        if lenght == 1:
            for renglon in self.estado:
                for columna in renglon:
                    if not (renglon == reinas[0][0] or columna == reinas[0][1]):
                        estado = copy.deepcopy(self.estado)
                        estado[renglon][columna] = "X"
                        hijo = Nodo(estado, self)
                        hijo.heuristica(meta)
                        self.hijos.append(hijo)

        if lenght == 2:
            for renglon in self.estado:
                for columna in renglon:
                    if not (renglon == reinas[0][0] or columna == reinas[0][1] or
                            renglon == reinas[1][0] or columna == reinas[1][1]):
                        estado = copy.deepcopy(self.estado)
                        estado[renglon][columna] = "X"
                        hijo = Nodo(estado, self)
                        hijo.heuristica(meta)
                        self.hijos.append(hijo)

        if lenght == 3:
            for renglon in self.estado:
                for columna in renglon:
                    if not (renglon == reinas[0][0] or columna == reinas[0][1] or
                            renglon == reinas[1][0] or columna == reinas[1][1] or
                            renglon == reinas[2][0] or columna == reinas[2][1]):
                        estado = copy.deepcopy(self.estado)
                        estado[renglon][columna] = "X"
                        hijo = Nodo(estado, self)
                        hijo.heuristica(meta)
                        self.hijos.append(hijo)

        for hijo in self.hijos:
            franja.append(hijo)
        franja.sort(key=lambda x: x.h)

    def greedy(self, meta, visitados, franja):
        franja.append(self)

        while not franja == []:
            frente = franja.pop(0)

            if frente.estado == meta.estado:
                print("sol. encontrado!!!")
                frente.imprime_estado()

                camino = []
                camino.append(frente)
                padre = frente.padre
                while padre:
                    camino.append(padre)
                    padre = padre.padre
                return camino

            es_visitado = False
            for visitado in visitados:
                if frente.estado == visitado.estado:
                    es_visitado = True
                    break

            if not es_visitado:
                visitados.append(frente)
                frente.expande(meta, franja)

        return None