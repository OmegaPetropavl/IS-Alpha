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
            

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(700, 700)
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
        self.label = QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.label.setPixmap(QtGui.QPixmap("logocompany.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("sozddogovor")
        self.action.triggered.connect(self.fizlitch_select)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("redakdogovor")
        
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("arendatory")
        self.action_3.triggered.connect(self.fizlitch_select)
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
        
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def fizlitch_select(self):
        try:
            
            db = mdb.connect('localhost', 'root', 'root', 'arenda')
            mycursor = db.cursor()
            
            query = "SELECT * from login"
            mycursor.execute(query)
            result = mycursor.fetchone()

            if result == None:
                print("Неправильный логин или пароль!")
                

            else:
                print(result)
                
        except mdb.Error as e:
            error = QMessageBox()
            error.setText('Подключение невозможно!')
            error.exec_()




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
   
class Ui_fizcreate(object):
    def setupUi(self, fizcreate):
        fizcreate.setObjectName("fizcreate")
        fizcreate.resize(465, 493)
        self.background = QtWidgets.QFrame(fizcreate)
        self.background.setGeometry(QtCore.QRect(-30, -10, 531, 601))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("#background {\n"
"background-color: rgb(170, 170, 127)\n"
"}")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.fiolabel = QtWidgets.QLabel(self.background)
        self.fiolabel.setGeometry(QtCore.QRect(120, 150, 61, 41))
        self.fiolabel.setObjectName("fiolabel")
        self.passlabel = QtWidgets.QLabel(self.background)
        self.passlabel.setGeometry(QtCore.QRect(120, 190, 121, 41))
        self.passlabel.setObjectName("passlabel")
        self.adresslabel = QtWidgets.QLabel(self.background)
        self.adresslabel.setGeometry(QtCore.QRect(120, 270, 141, 41))
        self.adresslabel.setObjectName("adresslabel")
        self.numlabel = QtWidgets.QLabel(self.background)
        self.numlabel.setGeometry(QtCore.QRect(120, 310, 141, 41))
        self.numlabel.setObjectName("numlabel")
        self.fio = QtWidgets.QLineEdit(self.background)
        self.fio.setGeometry(QtCore.QRect(260, 160, 161, 20))
        self.fio.setObjectName("fio")
        self.passport = QtWidgets.QLineEdit(self.background)
        self.passport.setGeometry(QtCore.QRect(260, 200, 161, 20))
        self.passport.setObjectName("passport")
        self.adress = QtWidgets.QLineEdit(self.background)
        self.adress.setGeometry(QtCore.QRect(260, 280, 161, 20))
        self.adress.setText("")
        self.adress.setObjectName("adress")
        self.phone = QtWidgets.QLineEdit(self.background)
        self.phone.setGeometry(QtCore.QRect(260, 320, 161, 20))
        self.phone.setObjectName("phone")
        self.iinlabel = QtWidgets.QLabel(self.background)
        self.iinlabel.setGeometry(QtCore.QRect(120, 230, 61, 41))
        self.iinlabel.setObjectName("iinlabel")
        self.iin = QtWidgets.QLineEdit(self.background)
        self.iin.setGeometry(QtCore.QRect(262, 240, 161, 20))
        self.iin.setObjectName("iin")
        self.nazavanie = QtWidgets.QLabel(self.background)
        self.nazavanie.setGeometry(QtCore.QRect(70, 60, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.nazavanie.setFont(font)
        self.nazavanie.setObjectName("nazavanie")
        self.okey = QtWidgets.QPushButton(self.background)
        self.okey.setGeometry(QtCore.QRect(154, 420, 91, 31))
        self.okey.setObjectName("okey")
        self.cancel = QtWidgets.QPushButton(self.background)
        self.cancel.setGeometry(QtCore.QRect(300, 420, 91, 31))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(fizcreate)
        QtCore.QMetaObject.connectSlotsByName(fizcreate)

    def retranslateUi(self, fizcreate):
        _translate = QtCore.QCoreApplication.translate
        fizcreate.setWindowTitle(_translate("fizcreate", "Новый объект"))
        self.fiolabel.setText(_translate("fizcreate", "ФИО:"))
        self.passlabel.setText(_translate("fizcreate", "Паспортные данные:"))
        self.adresslabel.setText(_translate("fizcreate", "Адрес:"))
        self.numlabel.setText(_translate("fizcreate", "Контактный телефон:"))
        self.iinlabel.setText(_translate("fizcreate", "ИИН:"))
        self.nazavanie.setText(_translate("fizcreate", "Добавление Физического лица"))
        self.okey.setText(_translate("fizcreate", "ОК"))
        self.cancel.setText(_translate("fizcreate", "Отменить"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginBeg()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

