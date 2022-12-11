class Nodo(object):
    def __int__(self, estado, padre=None):
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

    def heuristica(self, meta):
        pass

    def expande(self, meta, franja):

        for hijo in self.hijos:
            franja.append(hijo)
        franja.sort(key=lambda x: x.fn)

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