# toolbar/app.py
import sys
import os
import webbrowser
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QAction, QDesktopWidget
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class ToolbarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuração da Janela
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(0, 0, QDesktopWidget().availableGeometry().width(), 50)
        self.setWindowOpacity(0.8)

        # Toolbar principal
        toolbar = QToolBar("Toolbar Principal", self)
        toolbar.setMovable(True)
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        # Botões da Toolbar
        # Botão Menu (Esquerda)
        menu_button = QAction(QIcon(None), "Menu 3", self)
        menu_button.triggered.connect(self.dummy_action)
        menu_button.setIconText("M3")
        toolbar.addAction(menu_button)

        # Botões Centrais
        toolbar.addSeparator()
        for i in range(1, 6):
            button = QAction(QIcon(None), f"Botão {i}", self)
            button.triggered.connect(getattr(self, f"action_button{i}"))
            toolbar.addAction(button)

        toolbar.addSeparator()

        # Botão Lateral Direita
        right_button = QAction(QIcon(None), "Direita 6", self)
        right_button.triggered.connect(self.dummy_action)
        right_button.setIconText("D6")
        toolbar.addAction(right_button)

        # Botão Exit
        exit_button = QAction(QIcon(None), "Exit", self)
        exit_button.triggered.connect(self.close)
        toolbar.addAction(exit_button)

    # Ações dos Botões
    def action_button1(self):
        os.system("notepad.exe")

    def action_button2(self):
        webbrowser.open("https://calendar.google.com/calendar/u/0/r")

    def action_button3(self):
        webbrowser.open("https://chat.openai.com/")

    def action_button4(self):
        os.startfile(r"C:\Users\Merlin\Documents")

    def action_button5(self):
        os.system("runas /user:Administrator cmd")

    def dummy_action(self):
        print("Botão não configurado ainda!")


def main():
    app = QApplication(sys.argv)
    toolbar_app = ToolbarApp()
    toolbar_app.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
