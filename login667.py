from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import MySQLdb as mdb
import mysql.connector as mc

class LoginBeg(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(359, 373)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-10, -20, 371, 371))
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(60, 80, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setTabletTracking(False)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEditLogin = QtWidgets.QLineEdit(self.widget)
        self.lineEditLogin.setGeometry(QtCore.QRect(130, 150, 113, 20))
        self.lineEditLogin.setAutoFillBackground(False)
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.lineEditPassword = QtWidgets.QLineEdit(self.widget)
        self.lineEditPassword.setGeometry(QtCore.QRect(130, 200, 113, 20))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(150, 300, 71, 23))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(lambda: self.loginka())
        
        self.labelResult = QtWidgets.QLabel(self.widget)
        self.labelResult.setObjectName("labelResult")
        self.labelResult.setGeometry(QtCore.QRect(50, 320, 271, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 359, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "АИС \"Аренда помещений\""))
        self.label.setText(_translate("MainWindow", " Добро пожаловать!"))
        self.lineEditLogin.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.lineEditPassword.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.pushButton.setText(_translate("MainWindow", "Войти"))

    
 
    def loginka(self):
        try:
            login = self.lineEditLogin.text()
            password = self.lineEditPassword.text()
            db = mdb.connect('localhost', 'root', 'root', 'arenda')
            mycursor1 = db.cursor()
            mycursor2 = db.cursor()
            query1 = "SELECT Login,Password, Post from login where Login like '" +login + "'AND Password LIKE '" + password + "'AND Post like 'Менеджер'"
            query2 = "SELECT Login,Password, Post from login where Login like '" +login + "'AND Password LIKE '" + password + "'AND Post like 'Администратор'"
            mycursor1.execute(query1)
            mycursor2.execute(query2)
            result1 = mycursor1.fetchone()
            result2 = mycursor2.fetchone()

            if result1 == None and result2 == None:
                self.labelResult.setText("Неправильный логин или пароль!")
                

            else:
                self.labelResult.setText("Вход проведен успешно!")
                self.main_menu = Ui_MainWindow()
                
        except mdb.Error as e:
            error = QMessageBox()
            error.setText('Подключение невозможно!')
            error.exec_()
            

class Ui_MainWindow():
    def __init__(self):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.menu_2.addAction(self.action)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_8)
        self.menu_3.addAction(self.action_3)
        self.menu_3.addAction(self.action_4)
        self.menu_3.addAction(self.action_5)
        self.menu_4.addAction(self.action_6)
        self.menu_5.addAction(self.action_7)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "АИС \"Аренда помещений\""))
        self.menu.setTitle(_translate("MainWindow", "Статистика"))
        self.menu_2.setTitle(_translate("MainWindow", "Файл"))
        self.menu_3.setTitle(_translate("MainWindow", "Справочники"))
        self.menu_4.setTitle(_translate("MainWindow", "Отчеты"))
        self.menu_5.setTitle(_translate("MainWindow", "Параметры"))
        self.action.setText(_translate("MainWindow", "Создать договор..."))
        self.action_2.setText(_translate("MainWindow", "Просмотреть договор..."))
        self.action_3.setText(_translate("MainWindow", "Арендаторы"))
        self.action_4.setText(_translate("MainWindow", "Объекты"))
        self.action_5.setText(_translate("MainWindow", "Договоры"))
        self.action_6.setText(_translate("MainWindow", "Сформировать отчет..."))
        self.action_7.setText(_translate("MainWindow", "Сведения о разработчиках..."))
        self.action_8.setText(_translate("MainWindow", "Редактировать договор..."))
   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginBeg()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
