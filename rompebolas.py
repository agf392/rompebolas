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

    def tablero_facil(self):
        for i in range(self.columnas):
            for j in range(self.filas):
                self.tablero[i][j] = random.randint(1, 3)

    def tablero_intermedio(self):
        for i in range(self.columnas):
            for j in range(self.filas):
                self.tablero[i][j] = random.randint(1, 4)

    def tablero_dificil(self):
        for i in range(self.columnas):
            for j in range(self.filas):
                self.tablero[i][j] = random.randint(1, 5)

    def imprimir_tablero(self, puntuacion):
        print "Mejor puntuación: " + str(puntuacion)
        print"  ",
        for i in range(self.columnas):
            print(str("")+str(i+1)),
        print ""
        for i in range(self.columnas+2):
            print(str("-")),
        for i in range(self.columnas):
            print(str("\n")+str(self.filas-i)+str("|")),
            for j in range(self.filas):
                print self.tablero[i][j],

    def jugar(self, puntuacion):
        while True:
            movimiento = raw_input("\n\nIntroduce tu movimiento:")
            if str(movimiento) != "00":
                self.imprimir_tablero(puntuacion)
            else:
                menu_principal()


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
        print "Puntuaciones borradas\n\n"
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
            self.tabla_puntuaciones[dificultad] = str(puntuacion)+str("\n")
        else:
            pass
        txt = ''.join(self.tabla_puntuaciones)
        f = open("puntuaciones.txt", "w")
        f.write(txt)

    def imprimir_puntuaciones(self, dificultad):  # 0 facil, 1 medio ... 6 todas
        self.leer = open("puntuaciones.txt", "r")
        if dificultad != 6:
            return self.tabla_puntuaciones[dificultad]
        else:
            print "MEJORES PUNTUACIONES"
            print "Facil: " + str(self.tabla_puntuaciones[0])
            print "Intermedio: " + str(self.tabla_puntuaciones[1])
            print "Difícil: " + str(self.tabla_puntuaciones[2])
            print "Cuadrado con 3 colores: " + str(self.tabla_puntuaciones[3])
            print "Rombo con 4 colores: : " + str(self.tabla_puntuaciones[4])
            print "Casi-damero: " + str(self.tabla_puntuaciones[5] + str("\n\n"))


def tablero_facil():
    tablero = Tablero()
    puntuaciones = Puntuaciones()
    tablero.tablero_facil()
    puntuaciones.get_puntuaciones()
    puntuacion = puntuaciones.imprimir_puntuaciones(0)
    tablero.imprimir_tablero(puntuacion)
    tablero.jugar(puntuacion)


def tablero_intermedio():
    tablero = Tablero()
    puntuaciones = Puntuaciones()
    tablero.tablero_intermedio()
    puntuaciones.get_puntuaciones()
    puntuacion = puntuaciones.imprimir_puntuaciones(1)
    tablero.imprimir_tablero(puntuacion)
    tablero.jugar(puntuacion)


def tablero_dificil():
    tablero = Tablero()
    puntuaciones = Puntuaciones()
    tablero.tablero_dificil()
    puntuaciones.get_puntuaciones()
    puntuacion = puntuaciones.imprimir_puntuaciones(2)
    tablero.imprimir_tablero(puntuacion)
    tablero.jugar(puntuacion)


def tablero_fijo():
    while True:
        num = -1
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
    menu = {0: menu_principal}
    '''
        1: tres_colores,
        2: cuatro_colores,
        3: dos_colores}'''
    menu[num]()


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