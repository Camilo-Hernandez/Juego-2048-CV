from functools import partial
from threading import Thread
import os


def f():
    os.system("python funcion_deteccion.py &")


def g():
    os.system("python game.py &")


#now to run f and g at a time
Thread(target=f).start()
Thread(target=g).start()

print('Mantenga la ventana del Juego 2048 activa para mover el tablero')
