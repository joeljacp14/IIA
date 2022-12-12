import copy


class Nodo(object):

    def __init__(self):
        super(Nodo, self).__init__()
        self.tablero = Tablero()

    def proceso(self, turno):

        empate = False
        while not empate and not self.tablero.victoria(turno):
            # -1 Computadora, 1 Persona
            if turno == 1:
                self.tablero.print_estado()
                self.tablero.usuario()
                if self.tablero.victoria(turno):
                    continue
                turno = -1
            else:
                self.tablero.computadora()
                if self.tablero.victoria(turno):
                    continue
                turno = 1

            if self.tablero.casillas_libre():
                empate = False
            else:
                empate = True

        self.tablero.print_estado()

        if self.tablero.victoria(turno):
            if turno == 1:
                print("GANASTE!!!")
            if turno == -1:
                print("PERDISTE :(")
        else:
            print("\n*** HAY EMPATE ***")


class Tablero(object):

    def __init__(self):

        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

    def casillas_libre(self):
        lista = []
        for j in range(0, 3):
            for i in range(0, 3):
                if self.tablero[i][j] == 0:
                    lista.append((i, j))
        return lista

    def victoria(self, jugador):
        # 3 en fila
        for x in self.tablero:
            if abs(sum(x)) == 3 and jugador in x:
                return True

        # 3 en columna
        for y in zip(*self.tablero):
            if abs(sum(y)) == 3 and jugador in y:
                return True

        # 3 en diagonal
        d1 = [self.tablero[i][i] for i in range(3)]
        if abs(sum(d1)) == 3 and jugador in d1:
            return True

        # 3 en diagonal invertida
        d2 = [self.tablero[2 - i][i] for i in range(3)]
        if abs(sum(d2)) == 3 and jugador in d2:
            return True

        return False

    def esquina(self, p):
        if p[0] in [0, 2] and p[1] in [0, 2]:
            return True
        else:
            return False

    def print_estado(self):
        print("__________\n")
        for i in range(len(self.tablero)):
            linea = ""
            for j in self.tablero[i]:
                if j == 0:
                    linea += '_ '
                if j == 1:
                    linea += 'X '
                if j == -1:
                    linea += 'O '
            print(" ", linea)
        print("__________")

    def usuario(self):
        print("\nTu turno (X)")
        tirada = False
        while not tirada:
            resp = input("Elije una casilla (fila,columna): ")
            p = [int(resp[0]), int(resp[2])]
            if self.tablero[p[0]][p[1]] == 0:
                self.tablero[p[0]][p[1]] = 1
                tirada = True
            else:
                print("Inténtalo de nuevo, inténtalo de nuevo:")
                print()

    def computadora(self):
        casillas = self.casillas_libre()

        # evalua si gana en el sig tiro
        for p in casillas:
            tablero2 = copy.deepcopy(self)
            tablero2.tablero[p[0]][p[1]] = -1
            if tablero2.victoria(-1):
                self.tablero[p[0]][p[1]] = -1
                return

        # evalua si el usuario gana el el sig tiro
        for p in casillas:
            tablero2 = copy.deepcopy(self)
            tablero2.tablero[p[0]][p[1]] = 1
            if tablero2.victoria(1):
                self.tablero[p[0]][p[1]] = -1
                return

        # tiros en esquinas
        esquinas = []
        for p in casillas:
            if self.esquina(p):
                esquinas.append(p)
        if esquinas:
            y = esquinas[0]
            self.tablero[y[0]][y[1]] = -1
            return

        # tiros en centro luego en lados
        c = []
        for p in casillas:
            if p not in esquinas:
                c.append(p)
        if (1, 1) in c:
            y = (1, 1)
            self.tablero[y[0]][y[1]] = -1
            return
