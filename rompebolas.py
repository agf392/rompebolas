#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import os.path


class Tablero:
    def __init__(self):
        self.filas = 9
        self.columnas = 9
        self.tablero = [[None] * self.filas for i in range(self.columnas)]

    def crear_tablero(self, tipo):  # crea tablero (tipo: facil 3 medio 4 dificil 5)
        for i in range(self.columnas):
            for j in range(self.filas):
                self.tablero[i][j] = random.randint(1, tipo)

    def tablero_fijo1(self):
        self.tablero = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 3, 3, 3, 3, 3, 2, 1],
                        [1, 2, 3, 1, 1, 1, 3, 2, 1], [1, 2, 3, 1, 2, 1, 3, 2, 1], [1, 2, 3, 1, 1, 1, 3, 2, 1],
                        [1, 2, 3, 3, 3, 3, 3, 2, 1], [1, 2, 2, 2, 2, 2, 2, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def tablero_fijo2(self):
        self.tablero = [[4, 4, 4, 4, 1, 4, 4, 4, 4], [4, 4, 4, 1, 2, 1, 4, 4, 4], [4, 4, 1, 2, 3, 2, 1, 4, 4],
                        [4, 1, 2, 3, 1, 3, 2, 1, 4], [1, 2, 3, 1, 2, 1, 3, 2, 1], [4, 1, 2, 3, 1, 3, 2, 1, 4],
                        [4, 4, 1, 2, 3, 2, 1, 4, 4], [4, 4, 4, 1, 2, 1, 4, 4, 4], [4, 4, 4, 4, 1, 4, 4, 4, 4]]

    def tablero_fijo3(self):
        FilaRandom = random.randint(0, 8)
        ColumnaRandom = random.randint(0, 8)
        self.tablero = [[1, 2, 1, 2, 1, 2, 1, 2, 1], [2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2, 1],
                        [2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2, 1], [2, 1, 2, 1, 2, 1, 2, 1, 2],
                        [1, 2, 1, 2, 1, 2, 1, 2, 1], [2, 1, 2, 1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2, 1]]
        NumActual = self.tablero[FilaRandom][ColumnaRandom]
        if NumActual == 1:
            self.tablero[FilaRandom][ColumnaRandom] = 2
        else:
            self.tablero[FilaRandom][ColumnaRandom] = 1

    def imprimir_tablero(self, puntuacion):
        print "Mejor puntuación: " + str(puntuacion)
        print"  ",
        for i in range(self.columnas):
            print(str("") + str(i + 1)),
        print ""
        for i in range(self.columnas + 2):
            print(str("-")),
        for i in range(self.columnas):
            print(str("\n") + str(self.filas - i) + str("|")),
            for j in range(self.filas):
                print self.tablero[i][j],

    def jugar(self,puntuacion):
        num = -1
        self.movcolumna = -1
        self.movfila = -1
        movcolumna = self.movcolumna
        movfila = self.movfila
        while True:
            try:
                movcolumna = (raw_input("\nIntroduce el número de columna:\n"))
                while int(movcolumna) < 0 or int(movcolumna) > 9:
                    print "Has introducido un valor no válido\n"
                    movcolumna = raw_input("Introduce un número entre 0 y 9 para la columna:\n")
                num = int(movcolumna)
                movfila = (raw_input("Introduce el número de fila:\n"))
                while int(movfila) < 0 or int(movfila) > 9:
                    print "Has introducido un valor no válido\n"
                    movfila = raw_input("Introduce un número entre 0 y 9 para la fila:\n")
                num = int(movfila)
                break
            except ValueError:
                print "Has introducido un valor no válido"
        self.comprobar_posicion(movfila,movcolumna)

    def adyacentes(self, fil, col, num):
        if fil - 1 >= 0 and self.tablero[fil - 1][col] == num:
            return True
        if fil + 1 < len(self.tablero) and self.tablero[fil + 1][col] == num:
            return True
        if col - 1 >= 0 and self.tablero[fil][col - 1] == num:
            return True
        if col + 1 < len(self.tablero) and self.tablero[fil][col + 1] == num:
            return True
        return False

    def comprobar_posicion(self, movfil, movcol):
        tieneady = False
        filaelegida = len(self.tablero) - int(movfil)
        colelegida = int(movcol) - 1
        numelegido = self.tablero[filaelegida][colelegida]
        if numelegido == 0:
            print "No puedes seleccionar esa casilla"
        else:
            tieneady = self.adyacentes(filaelegida, colelegida, numelegido)
            print tieneady


class Puntuaciones:
    def __init__(self):
        archivo = "puntuaciones.txt"
        if os.path.isfile(archivo):
            pass
        else:
            lista = ["0", "0", "0", "0", "0", "0"]
            txt = '\n'.join(lista)
            f = open("puntuaciones.txt", "w")
            f.write(txt)
        self.leer = open("puntuaciones.txt", "r")
        self.escribir = open("puntuaciones.txt", "a")
        self.tabla_puntuaciones = []

    def set_puntuaciones(self):  # Para poner a 0
        lista = ["0", "0", "0", "0", "0", "0"]
        txt = '\n'.join(lista)
        f = open("puntuaciones.txt", "w")
        f.write(txt)
        print "Puntuaciones borradas\n\n"

    def get_puntuaciones(self):  # Para guardar las puntuaciones en una lista  (tabla_puntuaciones)
        while True:
            linea = self.leer.readline()
            if not linea:
                break
            self.tabla_puntuaciones.append(linea)

    def guardar_puntuaciones(self, dificultad, puntuacion):
        while True:
            linea = self.leer.readline()
            if not linea:
                break
        if puntuacion > int(self.tabla_puntuaciones[dificultad]):
            self.tabla_puntuaciones[dificultad] = str(puntuacion) + str("\n")
        else:
            pass
        txt = ''.join(self.tabla_puntuaciones)
        f = open("puntuaciones.txt", "w")
        f.write(txt)

    def imprimir_puntuaciones(self, dificultad):  # 0 facil, 1 medio ... 6 todas
        if dificultad != 6:
            return self.tabla_puntuaciones[dificultad]
        else:
            print "MEJORES PUNTUACIONES\n"
            print "Facil: " + str(self.tabla_puntuaciones[0])
            print "Intermedio: " + str(self.tabla_puntuaciones[1])
            print "Difícil: " + str(self.tabla_puntuaciones[2])
            print "Cuadrado con 3 colores: " + str(self.tabla_puntuaciones[3])
            print "Rombo con 4 colores: : " + str(self.tabla_puntuaciones[4])
            print "Casi-damero: " + str(self.tabla_puntuaciones[5] + str("\n\n"))


def tablero_facil():
    tablero = Tablero()
    puntuaciones = Puntuaciones()
    tablero.crear_tablero(3)
    puntuaciones.get_puntuaciones()
    puntuacion = puntuaciones.imprimir_puntuaciones(0)
    tablero.imprimir_tablero(puntuacion)
    tablero.jugar(puntuacion)


def tablero_intermedio():
    tablero = Tablero()
    puntuaciones = Puntuaciones()
    tablero.crear_tablero(4)
    puntuaciones.get_puntuaciones()
    puntuacion = puntuaciones.imprimir_puntuaciones(1)
    tablero.imprimir_tablero(puntuacion)
    tablero.jugar(puntuacion)


def tablero_dificil():
    tablero = Tablero()
    puntuaciones = Puntuaciones()
    tablero.crear_tablero(5)
    puntuaciones.get_puntuaciones()
    puntuacion = puntuaciones.imprimir_puntuaciones(2)
    tablero.imprimir_tablero(puntuacion)
    tablero.jugar(puntuacion)


def tablero_fijo():
    num = -1
    while True:
        try:
            print "1. Cuadrado con 3 colores" \
                  "\n2. Rombo con 4 colores" \
                  "\n3. Casi-damero, con dos colores" \
                  "\n0. Volver"
            opcion = (raw_input("Introduce una opcion(número entre 0 y 3):\n"))
            while int(opcion) < 0 or int(opcion) > 3:
                print "Has introducido un valor no válido" \
                      "\n1. Cuadrado con 3 colores" \
                      "\n2. Rombo con 4 colores" \
                      "\n3. Casi-damero, con dos colores" \
                      "\n0. Volver"
                opcion = raw_input("Introduce una opción(número entre 0 y 3):\n")
            num = int(opcion)
            break
        except ValueError:
            pass
    menu = {0: menu_principal,
            1: tablero_fijo1,
            2: tablero_fijo2,
            3: tablero_fijo3}
    menu[num]()


def tablero_fijo1():
    tablero = Tablero()
    puntuaciones = Puntuaciones()
    tablero.tablero_fijo1()
    puntuaciones.get_puntuaciones()
    puntuacion = puntuaciones.imprimir_puntuaciones(3)
    tablero.imprimir_tablero(puntuacion)
    tablero.jugar(puntuacion)


def tablero_fijo2():
    tablero = Tablero()
    puntuaciones = Puntuaciones()
    tablero.tablero_fijo2()
    puntuaciones.get_puntuaciones()
    puntuacion = puntuaciones.imprimir_puntuaciones(4)
    tablero.imprimir_tablero(puntuacion)
    tablero.jugar(puntuacion)


def tablero_fijo3():
    tablero = Tablero()
    puntuaciones = Puntuaciones()
    tablero.tablero_fijo3()
    puntuaciones.get_puntuaciones()
    puntuacion = puntuaciones.imprimir_puntuaciones(5)
    tablero.imprimir_tablero(puntuacion)
    tablero.jugar(puntuacion)


def mejores_puntuaciones():
    puntuaciones = Puntuaciones()
    puntuaciones.get_puntuaciones()
    puntuaciones.imprimir_puntuaciones(6)
    raw_input("Pulsa intro para volver al menu")
    menu_principal()


def borrar_puntuaciones():
    puntuaciones = Puntuaciones()
    puntuaciones.set_puntuaciones()
    menu_principal()


def salir():
    print "Hasta la próxima"
    sys.exit()


def menu_principal():
    num = -1
    while True:
        try:
            print "Bienvenido a Rompebolas" \
                  "\nElija tipo de tablero u otras opciones:" \
                  "\n1. Fácil" \
                  "\n2. Intermedio" \
                  "\n3. Difícil" \
                  "\n4. Tablero fijo" \
                  "\n5. Mejores puntuaciones" \
                  "\n6. Borrar mejores puntuaciones" \
                  "\n0. Salir"
            opcion = (raw_input("Introduce una opcion(número entre 0 y 6):\n"))
            while int(opcion) < 0 or int(opcion) > 6:
                print "Has introducido un valor no válido\n" \
                      "Elija tipo de tablero u otras opciones:" \
                      "\n1. Fácil" \
                      "\n2. Intermedio" \
                      "\n3. Difícil" \
                      "\n4. Tablero fijo" \
                      "\n5. Mejores puntuaciones" \
                      "\n6. Borrar mejores puntuaciones" \
                      "\n0. Salir"
                opcion = raw_input("Introduce una opción(número entre 0 y 6):\n")
            num = int(opcion)
            break
        except ValueError:
            pass
    menu = {0: salir,
            1: tablero_facil,
            2: tablero_intermedio,
            3: tablero_dificil,
            4: tablero_fijo,
            5: mejores_puntuaciones,
            6: borrar_puntuaciones}
    menu[num]()


menu_principal()