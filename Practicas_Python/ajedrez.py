
class Nodo(object):
    def __init__(self, estado):
        super(Nodo, self).__init__()
        self.estado = estado
        self.hijos = []
    
    def expande(self):
        pass

    def imprime_estado(self):
        for ren in self.estado:
            for col in ren:
                print(col, end=" ")
            print(" ")
        print(" ")