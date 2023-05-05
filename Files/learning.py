import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Окно регистрации')

        self.label_username = QLabel('Имя пользователя')
        self.label_password = QLabel('Пароль')

        self.textbox_username = QLineEdit()
        self.textbox_password = QLineEdit()
        self.textbox_password.setEchoMode(QLineEdit.Password)

        self.button_login = QPushButton('Войти')
        self.button_login.clicked.connect(self.check_login)

        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.textbox_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.textbox_password)
        layout.addWidget(self.button_login)

        self.setLayout(layout)

    def check_login(self):
        # здесь можно проверить правильность введенного логина и пароля
        # если логин и пароль правильные, можно создать главное меню и открыть его
        self.main_menu = MainMenuWindow()
        self.main_menu.show()
        login_window.close()

class MainMenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Главное меню')

        self.label_main_menu = QLabel('Это главное меню')
        self.button_exit = QPushButton('Выход')
        self.button_exit.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.label_main_menu)
        layout.addWidget(self.button_exit)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())