# ------------------------------------------------------------------- #
# ------ 3. Se ejecuta el programa de reconocimiento de imagen ------ #
# ------------------------------------------------------------------- #
from platform import release # Para cerrar la ventana
import cv2
from deteccion_aux import * # Donde hemos creado las funciones de reconocimiento de imagen paso a paso

# ------------------------------------------------------------------- #
# ------ 4. Se lanza el capturador de imagen por la webcam ---------- #
# ------ y se prepara para la futura detección ---------------------- #
# ------------------------------------------------------------------- #

cap = cv2.VideoCapture(0)
# Ciclo de video-streaming
while True:
    ret, frame = cap.read() # Se lee cada frame en el ciclo infinito
    if ret == False: 
        break
    frame = cv2.flip(frame, 1)  # Efecto espejo
    # Luego se pasa de BGR a HSV para evaluar si la coordenada V está en el rango especificado
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # ------------------------------------------------------------------- #
    # ------ 5. Se dibujan los cuadros amarillos con flechas rojas ------ #
    # ------ que indican las regiones donde se detecta el color azul celeste #
    # ------------------------------------------------------------------- #
    UP_P, UP_LONG, DOWN_P, DOWN_LONG, LEFT_P, LEFT_LONG, RIGHT_P, RIGHT_LONG = dibujar_botones(frame)
    
    # ------------------------------------------------------------------- #
    # ------ 6. Luego se utilizan transformaciones marfológicas --------- #
    # ------ para filtrar el objeto azul del resto de la imagen --------- #
    # ------------------------------------------------------------------- #
    cnts = detectar_objeto(frameHSV)

    # ------------------------------------------------------------------- #
    # ------ 7. Se utiliza el concepto de detección de cambio ----------- #
    # ------ de flanco para detectar si la punta del lapicero ----------- #
    # ------ ingresa a una de las 4 regiones de detección (botones) ----- #
    # ------------------------------------------------------------------- #
    detectar_objeto_dentro(frame, cnts, UP_P, UP_LONG, DOWN_P,
                           DOWN_LONG, LEFT_P, LEFT_LONG, RIGHT_P, RIGHT_LONG)
    
    # ------------------------------------------------------------------- #
    # ------------------ 8. Mostrar en la pantalla ---------------------- #
    # ------------------------------------------------------------------- #
    # cv2.imshow('maskCeleste', maskCeleste) # Imagen binaria del objeto
    cv2.imshow('Frame', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break  # abortar con ESC, ya que 27 es el ASCII del ESC.
    
cap.release() # detener la captura de la pantalla
cv2.destroyAllWindows # cerrar todas las ventanas

# -------------------------------------------------------------------------- #
# --------------------------- FIN DEL PROGRAMA - --------------------------- #
# -------------------------------------------------------------------------- #