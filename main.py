# -------------------------------------------------------------------------- #
# ------- PLANTILLA DE CÓDIGO - -------------------------------------------- #
# ------- Coceptos básicos de PDI------------------------------------------- #
# ------- Por: Camilo Hernández Ruiz    camilo.hernandez1@udea.edu.co ------ #
# -------      Yeison Monsalve Sánchez  yeison.monsalves@udea.edu.co ------- #
# ------- Estudiantes Facultad de Ingenieria - Universidad de Antioquia ---- #
# ------- Programa: Ingeniería de Telecomunicaciones ----------------------- #
# ------- Curso Básico de Procesamiento de Imágenes y Visión Artificial----- #
# -------------------------------------------------------------------------- #
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
