import string
class Nodo(object):
    def __init__(self, estado):
        super(Nodo, self).__init__()
        self.estado = estado
        self.heur = 0
        self.hijos = []
    
    def expande_peon(self, color):
        if (color == 'b'):
            pass
        else:
            pass

    def expande_alfil(self):
        pass

    def expande_caballo(self):
        pass

    def expande_reina(self):
        pass

    def busca_peon_del_rey(self, color):
        col = reg = 0
        for r in self.estado:
            for c in r:
                if color == 'n':
                    if c == "nP" and self.estado[reg - 1, col] == "nK":
                        return (reg, col)
                else:
                    if c == "bP" and self.estado[reg + 1, col] == "bK":
                        return (reg, col)
                col += 1
            reg += 1
        return None, None

    def busca_alfil(self):
        col = reg = 0
        for r in self.estado:
            for c in r:
                if c == "bA":
                    if self.estado[reg][col - 1] == "bK" and self.estado[reg][col + 1] == "bC":
                        return (reg, col)
                col += 1
            reg += 1
        return (None, None)

    def busca_caballo(self):
        reg = col = 0
        for r in self.estado:
            for c in r:
                if r == 0:
                    if c == "nC":
                        return (reg, col)
                col += 1
            reg += 1
        return (None, None)

    def busca_reina(self):
        reg = col = 0
        for r in self.estado:
            for c in r:
                if c == "bQ":
                    return (reg, col)
                col += 1
            reg += 1
        return (None, None)

    def imprime_estado(self):
        for ren in self.estado:
            for col in ren:
                print(col, end=" ")
            print(" ")
        print(" ")