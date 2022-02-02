from platform import release
import cv2
import numpy as np

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
    if ret == False:    break
    cv2.imshow('Frame', frame)
    k = cv2.waitKey(1)
    if k == 27:     break # abortar con ESC
cap.release()
cv2.destroyAllWindows
