from platform import release
import cv2
from funcion_deteccion_aux import *

cap = cv2.VideoCapture(0)
# Ciclo de video-streaming
while True:
    ret, frame = cap.read()
    if ret == False:
        break
    frame = cv2.flip(frame, 1)  # Efecto espejo
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Pasarlo de BGR a HSV
    
    UP_P, UP_LONG, DOWN_P, DOWN_LONG, LEFT_P, LEFT_LONG, RIGHT_P, RIGHT_LONG = dibujar_botones(frame)
    
    cnts = detectar_objeto(frameHSV)

    detectar_objeto_dentro(
        cnts, frame, UP_P, UP_LONG, DOWN_P, DOWN_LONG, LEFT_P, LEFT_LONG, RIGHT_P, RIGHT_LONG)
    
    # Mostrar en la pantalla
    # cv2.imshow('maskCeleste', maskCeleste) # Imagen binaria del objeto
    cv2.imshow('Frame', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break  # abortar con ESC
    
cap.release()
cv2.destroyAllWindows

