#!/usr/bin/env python3
# vim: set ts=4 sts=0 et sw=4 smarttab :
"""2048 game in Python (cli, PyQt 4 or 5)."""

# from curses import window
import time
import math
import sys
from funciones import *



def main():
    def on_FocusChanged():
        nonlocal window
        window.activateWindow()

    """Play the Qt verson of the game."""
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('Juego 2048')
    window = QtWidgets.QWidget()
    window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    window.showNormal()
    app.focusChanged.connect(on_FocusChanged)

    grid = QtWidgets.QGridLayout()
    labels = []
    for i in range(ROW**2):
        label = QtWidgets.QLabel("0")
        label.setAlignment(QtCore.Qt.AlignCenter)
        labels.append(label)
        grid.addWidget(label, i // ROW, i % ROW)
    window.setLayout(grid)

    board = tuple([0] * ROW**2)
    board = round(round(board))

    keys = {
        QtCore.Qt.Key_Up: "w",
        QtCore.Qt.Key_Left: "a",
        QtCore.Qt.Key_Down: "s",
        QtCore.Qt.Key_Right: "d",
    }
    

    def update():
        """Update the state of the board."""
        for i, v in enumerate(board):
            labels[i].setText(str(v))
            x = math.log(max(1, v) / math.log(2))
            font_size = (1.5)**x + 20
            color = x / 10 * 360
            labels[i].setStyleSheet(
                "font-size : {0:0.0f}px;"
                "background-color : hsl({1:0.0f}, 100%, 50%);"
                "min-width: 120px;"
                "min-height: 120px;"
                .format(font_size, color)
            )
        window.update()

    def key_press(event):
        """React to a pressed key by playing."""
        nonlocal board

        key = event.key()
        try:
            w = keys[key] if key in keys else chr(key).lower()
        except ValueError:
            print("Key unknown {}".format(key), file=sys.stderr)
            return

        try:
            m = 4
            while m < 2048:
                
                new_board = shake(board, w, m)
                if new_board != board:
                    board = new_board
                    time.sleep(.1)
                    update()
                    app.processEvents()
                else:
                    board = new_board
                m *= 2
            update()
            app.processEvents()
            time.sleep(.1)
            try:
                board = round(board)
            except IndexError:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setText("You've lost!")
                msg_box.exec_()
                board = tuple([0] * ROW**2)
                board = round(round(board))

            update()
            app.processEvents()
        except ValueError:
            pass

    update()

    window.keyPressEvent = key_press
    window.show()
    window.setFocus(True)
    app.exec_()


if __name__ == "__main__":
    try:
        from PyQt5 import QtWidgets, QtCore
        main()
    except ImportError:
        try:
            from PyQt4 import QtGui as QtWidgets, QtCore
            main()
        except ImportError:
            print("Install PyQt to play a colorful version of 2048.",
                  "On Anaconda use: `conda install pyqt'\n"
	              "Otherwise: `pip install pyqt5'\n",
                  file=sys.stderr)
            cli()