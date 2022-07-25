# Juego 2048 usando la librería OpenCV

Explicación del código y el funcionamiento del juego en el vídeo [Juego 2048 usando Procesamiento de Imágenes](https://youtu.be/tlGB59VHQpQ)

Juego 2048 utilizando la cámara del computador como capturador de la imagen. Se utiliza un objeto azul, un lapicero por ejemplo, para accionar los botones que aparecen en el frame en pantalla.

En este repositorio se desarrolló un programa con el fin de aplicar los conceptos dados en las clases de Procesamiento Digital de Imágenes de la Universidad de Antioquia. En dicho programa se implementó un juego matemático con el cual se controla mediante la cámara web de la computadora.

Para ejecutar el programa es necesario tener todos los archivos en la misma carpeta y abrir cualquier entorno de trabajo que pueda desarrollar o ejecutar el lenguaje de programación Python, por ejemplo, Visual Studio Code o Spyder Anaconda. Una vez abierto el entorno de programación se ejecuta el archivo llamado _main.py_ el cual corre el juego y activa la cámara para el procesamiento del juego. Es importante que mantenga la ventana del Juego 2048 activa en todo momento para mover el tablero.
Otra forma de ejecutar el programa es utilizando una terminal del sistema, para esto se debe estar ubicado en la carpeta del juego donde están todos los archivos para la ejecución y con el comando _Python .\main.py_ se procede a ejecutar el juego.

### Herramientas y librerías necesarias:
- Entorno de ejecución y desarrollo para Python.
##### Librerías:
- opencv-contrib-python==4.5.5.62.
- keyboard==0.13.5.
- PyQt5==5.15.6.
- matplotlib==3.5.1.
- numpy. 
- math.
- sys.
- random. 
- os.

### Instrucciones para ejecutar el juego:
1. Tener a la mano un objeto azul, por ejemplo un lapicero para poder activar los botones.
2. Ejecutar el archivo _main.py_ que está dentro de la carpeta "juego-2048"
3. Mantener la ventana del tablero 2048 activa y proceder a jugar en la ventana de reconocimiento del objeto.
4. La tecla “Esc” para cerrar la cámara web del juego en cualquier momento, pero se debe cerrar la ventana del tablero manualmente.
Si se desea volver a ingresar al juego, es necesario volver a ejecutar el programa desde la consola de Python o desde la terminal.
