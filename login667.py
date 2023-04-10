from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import MySQLdb as mdb
import mysql.connector as mc

class Ui_MainWindow(object):
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
                self.close()
            else:
                self.labelResult.setText("Вход проведен успешно!")
        except mdb.Error as e:
            error = QMessageBox()
            error.setText('Подключение невозможно!')
            error.exec_()
            


   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
