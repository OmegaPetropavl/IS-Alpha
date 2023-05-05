from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
import MySQLdb as mdb
from fizcreate import *
from dogovor import *
from dogovorspravochnik import *
from objectspravochnik import *
from arendatorspravochnik import *
from userspravochnik import *
from arendatorsstat import *
from oplatasstat import *
from objectsstat import *
import images



class LoginBeg(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(359, 373)
        icon = QIcon((":/logocompany.png"))
        MainWindow.setWindowIcon(icon)
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
        self.lineEditLogin.setText("login")
        self.lineEditPassword = QtWidgets.QLineEdit(self.widget)
        self.lineEditPassword.setGeometry(QtCore.QRect(130, 200, 113, 20))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        self.lineEditPassword.setText("password")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "ИС \"Альфа\""))
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
            global result1
            result1 = mycursor1.fetchone()
            result2 = mycursor2.fetchone()

            if result1 == None and result2 == None:
                self.labelResult.setText("Неправильный логин или пароль!")

              

            else:
                self.labelResult.setText("Вход проведен успешно!")
                self.main_menu = Ui_MainWindow()
                self.main_menu.updateUserAction()
                
        except mdb.Error as e:
            error = QMessageBox()
            error.setText('Подключение невозможно!')
            error.exec_()
            

class Ui_MainWindow(object):
    
    def __init__(self):
        
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(700, 700)
        screen_center = QtWidgets.QApplication.desktop().screen().rect().center()
        window_pos = MainWindow.rect().center() - QtCore.QPoint(0, -20)
        MainWindow.move(screen_center - window_pos)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("file")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("spravochniki")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("otcheti")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("parametry")
        MainWindow.setMenuBar(self.menubar)
        self.label = QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.label.setPixmap(QtGui.QPixmap(":/logocompany.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("sozddogovor")
        self.action.triggered.connect(self.dogovor_create)  
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("arendatory")
        # self.action_3.triggered.connect(self.fizlitch_select)
        self.action_3.triggered.connect(self.openarendatorbook)
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("objecty")
        self.action_4.triggered.connect(self.openobjectbook)
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("dogovory")
        self.action_5.triggered.connect(self.opendogovorbook)
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("users")
        self.action_8.triggered.connect(self.openuserbook)
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("otchet1")
        self.action_6.triggered.connect(self.openarendatorsstat)
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("otchet2")
        self.action_9.triggered.connect(self.openoplatasstat)
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("otchet3")
        self.action_10.triggered.connect(self.openobjectstat)
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("developers")
        self.action_7.triggered.connect(self.viewdevelopers)
        self.menu_2.addAction(self.action)
        self.menu_3.addAction(self.action_3)
        self.menu_3.addAction(self.action_4)
        self.menu_3.addAction(self.action_5)
        self.menu_3.addAction(self.action_8)
        self.menu_4.addAction(self.action_6)
        self.menu_4.addAction(self.action_9)
        self.menu_4.addAction(self.action_10)
        self.menu_5.addAction(self.action_7)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.statusbar = QtWidgets.QStatusBar(MainWindow) #Статусбар для определения пользователя
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def updateUserAction(self):
        if result1 is not None:
            self.action_8.setEnabled(False)
    
    def fizlitch_select(self):
        self.fizcreate_window = QtWidgets.QMainWindow()
        self.fizcreate_ui = Ui_fizcreate()
        self.fizcreate_ui.setupUi(self.fizcreate_window)
        self.fizcreate_window.show()

    def dogovor_create(self):
        self.dogovorcreate_window = QtWidgets.QMainWindow()
        self.dogovorcreate_ui = Ui_Dialog()
        self.dogovorcreate_ui.setupUi(self.dogovorcreate_window)
        self.dogovorcreate_window.show()

    def opendogovorbook(self):
        self.dogovorbook_window = QtWidgets.QMainWindow()
        self.dogovorbook_ui = Ui_dogovors()
        self.dogovorbook_ui.setupUi(self.dogovorbook_window)
        self.dogovorbook_window.show()

    def openobjectbook(self):
        self.objectbook_window = QtWidgets.QMainWindow()
        self.objectbook_ui = Ui_objects()
        self.objectbook_ui.setupUi(self.objectbook_window)
        self.objectbook_window.show()

    def openarendatorbook(self):
        self.arendatorbook_window = QtWidgets.QMainWindow()
        self.arendatorbook_ui = Ui_arendators()
        self.arendatorbook_ui.setupUi(self.arendatorbook_window)
        self.arendatorbook_window.show()

    def openuserbook(self):
        self.userbook_window = QtWidgets.QMainWindow()
        self.userbook_ui = Ui_users()
        self.userbook_ui.setupUi(self.userbook_window)
        self.userbook_window.show()

    def openarendatorsstat(self):
        self.arendatorsstat_window = QtWidgets.QMainWindow()
        self.arendatorsstat_ui = Ui_arendatorsstat()
        self.arendatorsstat_ui.setupUi(self.arendatorsstat_window)
        self.arendatorsstat_window.show()

    def openoplatasstat(self):
        self.oplatasstat_window = QtWidgets.QMainWindow()
        self.oplatasstat_ui = Ui_oplatastat()
        self.oplatasstat_ui.setupUi(self.oplatasstat_window)
        self.oplatasstat_window.show()

    def openobjectstat(self):
        self.objectstat_window = QtWidgets.QMainWindow()
        self.objectstat_ui = Ui_objectsstat()
        self.objectstat_ui.setupUi(self.objectstat_window)
        self.objectstat_window.show()




    def viewdevelopers(self):
        error = QMessageBox()
        error.setWindowTitle('Разработчики')
        error.setText('Приложение разработано студентами группы АПО-20-1 Зайкиной Л.И. и Валиевым Д.Т.')
        error.buttons = QtWidgets.QMessageBox.Ok
        icon = QtGui.QIcon((":/developer.png"))
        error.setWindowIcon(icon)
        error.exec_()

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ИС учета аренды нежилых помещений \"Альфа\""))
        self.menu_2.setTitle(_translate("MainWindow", "Файл"))
        self.menu_3.setTitle(_translate("MainWindow", "Справочники"))
        self.menu_4.setTitle(_translate("MainWindow", "Отчеты"))
        self.menu_5.setTitle(_translate("MainWindow", "Параметры"))
        self.action.setText(_translate("MainWindow", "Создать договор..."))
        self.action_3.setText(_translate("MainWindow", "Арендаторы"))
        self.action_4.setText(_translate("MainWindow", "Объекты"))
        self.action_5.setText(_translate("MainWindow", "Договоры"))
        self.action_8.setText(_translate("MainWindow", "Пользователи"))
        self.action_6.setText(_translate("MainWindow", "Отчет об арендаторах"))
        self.action_9.setText(_translate("MainWindow", "Отчет об оплате"))
        self.action_10.setText(_translate("MainWindow", "Отчет об помещениях"))
        self.action_7.setText(_translate("MainWindow", "Сведения о разработчиках"))
        
   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginBeg()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

