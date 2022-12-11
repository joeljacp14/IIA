import copy
import random


class Juego(object):

    def __init__(self):
        self.tablero = Tablero()

    def proceso(self, turno):

        empate = False
        while not empate and not self.tablero.victoria(turno):  # Mientras no empate, y mientras no gane
            if turno == 1:  # si juega el usuario
                self.tablero.print_estado()
                self.tablero.usuario()  # aquí juega el usuario
                # cambio de turno
                if self.tablero.victoria(turno):
                    continue
                turno = -1
            else:
                self.tablero.computadora()  # juega la computadora
                # cambio de turno
                if self.tablero.victoria(turno):
                    continue
                turno = 1

            # verifica si hay o no empate
            if self.tablero.casillas_libre():
                empate = False
            else:
                empate = True

        # Se sale del While, ya hay un ganador o un empate.
        self.tablero.print_estado()

        if self.tablero.victoria(turno):
            ganador = 0
            if turno == 1:
                ganador = "El usuario"
            if turno == -1:
                ganador = "La computadora"
            print("\nGanador:", ganador)

        else:
            print("\nEmpate")


class Tablero(object):

    def __init__(self):

        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def casillas_libre(self):
        # recorre las casillas buscando todas las libres, y las regresa como una lista
        lista = []
        for j in range(0, 3):
            for i in range(0, 3):
                if self.tablero[i][j] == 0:
                    lista.append((i, j))  # agrega las casillas libres a la lista
        return lista

    def victoria(self, jugador):
        # Descifra si un jugador ganó (el caso en el que una columna/fila/diagonal esté llena)

        # 1.Busca ganador en la fila
        for x in self.tablero:
            if abs(sum(x)) == 3 and jugador in x:
                return True  # Jugador ganó

        # 2.Busca un ganador en la columna, rotando el tablero
        for y in zip(*self.tablero):
            if abs(sum(y)) == 3 and jugador in y:
                return True

        # 3.Busca en la primera diagonal
        d1 = [self.tablero[i][i] for i in range(3)]
        if abs(sum(d1)) == 3 and jugador in d1:
            return True

        # 4.Busca en la diagonal invertida
        d2 = [self.tablero[2 - i][i] for i in range(3)]
        if abs(sum(d2)) == 3 and jugador in d2:
            return True

        # Si no encontró ningún ganador, regresa un False
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
                    linea += '. '
                if j == 1:
                    linea += 'x '
                if j == -1:
                    linea += 'o '
            print(" ", linea)
        print("__________")

    def usuario(self):
        # Entra cuando es turno del usuario de jugar
        print("\nEs tu turno!")
        tirada = False  # Todavía no ha tirado
        while not tirada:
            resp = input("Elije una casilla (fila,columna): ")  # guarda coordenada como string
            p = [int(resp[0]), int(resp[2])]  # guarda la coordenada con enteros
            if self.tablero[p[0]][p[1]] == 0:  # pregunta si la coordenada está vacía
                self.tablero[p[0]][p[1]] = 1  # agrega un 1 a la posición que se tiró
                tirada = True
            else:
                print("Inténtalo de nuevo, inténtalo de nuevo:")
                print()

    def computadora(self):
        # Entra cuando es el turno de la computadora de jugar
        print("\nTurno de la computadora!")
        casillas = self.casillas_libre()

        # Busca si puede ganar en la siguiente jugada, si es así,hace el movimieno
        # gano.yo + gana.usuario+esquinas+centro+lados

        for p in casillas:
            tablero2 = copy.deepcopy(self)
            tablero2.tablero[p[0]][p[1]] = -1
            if tablero2.victoria(-1):
                self.tablero[p[0]][p[1]] = -1
                return

        # Busca si el usuario puede ganar en la siguiente jugada, si es así, lo bloquea
        # poniendose en donde ganaría el usuario
        for p in casillas:
            tablero2 = copy.deepcopy(self)
            tablero2.tablero[p[0]][p[1]] = 1
            # tablero2.haz_tirada(c, 1)
            if tablero2.victoria(1):
                self.tablero[p[0]][p[1]] = -1  # lo tapa
                # self.haz_tirada(c, -1)
                return

        # Ahora podrá prioridad a tiros en las esquinas
        esquinas = []
        for p in casillas:
            if self.esquina(p):
                esquinas.append(p)
        if esquinas:
            y = esquinas[0]
            self.tablero[y[0]][y[1]] = -1
            return

        # Pondrá prioridad a tiros en el centro, por último en los lados
        c = []  # centro y lados
        for p in casillas:
            if p not in esquinas:
                c.append(p)
        if (1, 1) in c:
            y = (1, 1)
            self.tablero[y[0]][y[1]] = -1
            return


# Inicia Proceso
jugada1 = Juego()  # Declaro jugada1 classe Juego

print("Instruciones de llenado:\nAgrega la coordenada de la cansilla que quieres, separada por una coma\nEjemplo: 0,0")
print("\nEmpecemos! Computadora será 'o', usuario será 'x'")
print("Nota:El primer jugador se eligirá aleatoriamente.\n")

turno = random.choice([-1, 1])  # Elije quien será el jugador: -1 Máquina, 1 Usuario
jugada1.proceso(turno)

