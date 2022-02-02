from platform import release
import cv2
import numpy as np
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (60, 255, 255), 'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (
    255, 255, 255), 'black': (0, 0, 0), 'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(), 'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Rango de color azul para detectarlo
celesteBajo = np.array([75, 185, 88], np.uint8)
celesteAlto = np.array([112, 255, 255], np.uint8)

# Coordenadas del punto
x1 = None
y1 = None

# Ciclo de video-streaming
while True:
    ret, frame = cap.read()
    if ret == False: break
    frame = cv2.flip(frame, 1) # Efecto espejo
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Pasarlo de BGR a HSV
    
    # ------------- Botones UP LEFT RIGHT DOWN ------------- #
    # -- Cuadrados dibujados en la parte inferior derecha que representan el movimiento del tablero -- #
    
    # ------- Dibujar los rectángulos -------- #
    ANCHO = 92

    # Rectángulo arriba
    UP_Px = 424
    UP_Py = 216
    UP_P = (UP_Px, UP_Py)
    UP_LONG = (UP_Px+ANCHO, UP_Py+ANCHO)
    cv2.rectangle(frame, UP_P, UP_LONG, colors['yellow'], 2)

    # Rectángulo abajo
    DOWN_Px = UP_Px
    DOWN_Py = UP_Py + 168
    DOWN_P = (DOWN_Px, DOWN_Py)
    DOWN_LONG = (DOWN_Px+ANCHO, DOWN_Py+ANCHO)
    cv2.rectangle(frame, DOWN_P, DOWN_LONG, colors['yellow'], 2)

    # Rectángulo izquierda
    LEFT_Px = UP_Px - 113
    LEFT_Py = UP_Py + 86
    LEFT_P = (LEFT_Px, LEFT_Py)
    LEFT_LONG = (LEFT_Px+ANCHO, LEFT_Py+ANCHO)
    cv2.rectangle(frame, LEFT_P, LEFT_LONG, colors['yellow'], 2)

    # Rectángulo derecha
    RIGHT_Px = LEFT_Px + 2*ANCHO + 2*(UP_Px-LEFT_Px-ANCHO)
    RIGHT_Py = LEFT_Py
    RIGHT_P = (RIGHT_Px, RIGHT_Py)
    RIGHT_LONG = (RIGHT_Px+ANCHO, RIGHT_Py+ANCHO)
    cv2.rectangle(frame, RIGHT_P, RIGHT_LONG, colors['yellow'], 2)


    # ---- Dibujar flechas ---- #
    # Flecha arriba
    UP_ARROW_X = (UP_P[0] + UP_LONG[0])//2
    UP_ARROW_Pt1y = UP_LONG[1] - 20
    UP_ARROW_Pt1 = (UP_ARROW_X, UP_ARROW_Pt1y)
    UP_ARROW_Pt2y = UP_P[1] + 20
    UP_ARROW_Pt2 = (UP_ARROW_X, UP_ARROW_Pt2y)
    cv2.arrowedLine(frame, UP_ARROW_Pt1,
                    UP_ARROW_Pt2, colors['red'], 4)

    # Flecha abajo
    DOWN_ARROW_X = (DOWN_P[0] + DOWN_LONG[0])//2
    DOWN_ARROW_Pt2y = DOWN_LONG[1] - 20
    DOWN_ARROW_Pt2 = (DOWN_ARROW_X, DOWN_ARROW_Pt2y)
    DOWN_ARROW_Pt1y = DOWN_P[1] + 20
    DOWN_ARROW_Pt1 = (DOWN_ARROW_X, DOWN_ARROW_Pt1y)
    cv2.arrowedLine(frame, DOWN_ARROW_Pt1,
                    DOWN_ARROW_Pt2, colors['red'], 4)

    # Flecha izquierda
    LEFT_ARROW_Y = (LEFT_P[1] + LEFT_LONG[1])//2
    LEFT_ARROW_Pt2x = LEFT_P[0] + 20
    LEFT_ARROW_Pt2 = (LEFT_ARROW_Pt2x, LEFT_ARROW_Y)
    LEFT_ARROW_Pt1x = LEFT_LONG[0] - 20
    LEFT_ARROW_Pt1 = (LEFT_ARROW_Pt1x, LEFT_ARROW_Y)
    cv2.arrowedLine(frame, LEFT_ARROW_Pt1,
                    LEFT_ARROW_Pt2, colors['red'], 4)

    # Flecha derecha
    RIGHT_ARROW_Pt1x = RIGHT_P[0] + 20
    RIGHT_ARROW_Y = (RIGHT_P[1] + RIGHT_LONG[1])//2
    RIGHT_ARROW_Pt1 = (RIGHT_ARROW_Pt1x, RIGHT_ARROW_Y)
    RIGHT_ARROW_Pt2x = RIGHT_LONG[0] - 20
    RIGHT_ARROW_Pt2 = (RIGHT_ARROW_Pt2x, RIGHT_ARROW_Y)
    cv2.arrowedLine(frame, RIGHT_ARROW_Pt1,
                    RIGHT_ARROW_Pt2, colors['red'], 4)

    # ------------- Detección del color celeste y obtención de la imagen binaria ------------- #
    # Detección del color celeste y limpiar el ruido del objeto con transformaciones marfológicas
    maskCeleste = cv2.inRange(frameHSV, celesteBajo, celesteAlto)
    maskCeleste = cv2.erode(maskCeleste, None, iterations=1) 
    maskCeleste = cv2.dilate(maskCeleste, None, iterations=2)
    maskCeleste = cv2.medianBlur(maskCeleste, 13)
    # Obtener el contorno de los objetos para reconocer el más grande (la tapa o lapicero azul)
    cnts, _ = cv2.findContours(
        maskCeleste, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Tomar el de más grande contorno para ignorar los objetos siguientes más pequeños
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]
    # Aplicar un for para ignorar el lapicero azul si se aleja mucho de la pantalla
    for c in cnts:
        area = cv2.contourArea(c)
        if area < 1000:
            x1 = None
            y1 = None
        else:
            # Dibujar un rectángulo alrededor del lapicero (area blanca de la imagen binaria)
            x, y2, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y2),(x+w,y2+h),colors['green'],2)
            x2 = x + w//2

            if x1 is not None:
                # Si detecta la punta del lapicero en UP
                if x2 > UP_P[0] and y2 > UP_P[1] and x2 < UP_LONG[0] and y2 < UP_LONG[1]:
                    print('está en UP')
                # # Si detecta la punta del lapicero en DOWN
                if x2 > DOWN_P[0] and y2 > DOWN_P[1] and x2 < DOWN_LONG[0] and y2 < DOWN_LONG[1]:
                    print('está en DOWN')
                # # Si detecta la punta del lapicero en LEFT
                if x2 > LEFT_P[0] and y2 > LEFT_P[1] and x2 < LEFT_LONG[0] and y2 < LEFT_LONG[1]:
                    print('está en LEFT')
                # # Si detecta la punta del lapicero en RIGHT
                if x2 > RIGHT_P[0] and y2 > RIGHT_P[1] and x2 < RIGHT_LONG[0] and y2 < RIGHT_LONG[1]:
                    print('está en RIGHT')
            cv2.circle(frame, (x2, y2), 2, colors['cyan'], 3)
            x1 = x2
            y1 = y2

                




    cv2.imshow('maskCeleste', maskCeleste)
    cv2.imshow('Frame', frame)
    k = cv2.waitKey(1)
    if k == 27: break # abortar con ESC

cap.release()
cv2.destroyAllWindows
