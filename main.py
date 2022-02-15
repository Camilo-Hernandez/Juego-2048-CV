# -------------------------------------------------------------------------- #
# ------- PLANTILLA DE CÓDIGO - -------------------------------------------- #
# ------- Coceptos básicos de PDI------------------------------------------- #
# ------- Por: David Fernández    david.fernandez@udea.edu.co - ------------ #
# ------- Profesor Facultad de Ingenieria BLQ 21-409 - --------------------- #
# ------- CC 71629489, Tel 2198528,  Wpp 3007106588 - ---------------------- #
# ------- Curso Básico de Procesamiento de Imágenes y Visión Artificial----- #
# ------- V2 Abril de 2015-------------------------------------------------- #
# -------------------------------------------------------------------------- #

# ------ 1. Importar las librerías ------- #
from functools import partial
from threading import Thread
import os

# ------ 2. Definir las funciones que lanzan el juego y ------- #
# ------ el programa de detección en hilos de procesamiento paralelos -------- #
# ------ ejecutados con la función Thread ------ #

def f():
    os.system("python deteccion.py &")

def g():
    os.system("python 2048v2/game_display.py &")

Thread(target=f).start()
Thread(target=g).start()

print('Mantenga la ventana del Juego 2048 activa para mover el tablero')
