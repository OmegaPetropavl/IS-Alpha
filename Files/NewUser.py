from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton
import MySQLdb as mdb
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import images

class Ui_usercreate(object):
    def setupUi(self, usercreate):
        usercreate.setObjectName("usercreate")
        usercreate.setFixedSize(465, 493)
        icon = QIcon((":/logocompany.png"))
        usercreate.setWindowIcon(icon)
        self.background = QtWidgets.QFrame(usercreate)
        self.background.setGeometry(QtCore.QRect(-30, -10, 531, 601))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("#background {\n"
"background-color: rgb(200, 170, 127)\n"
"}")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.namelabel = QtWidgets.QLabel(self.background)
        self.namelabel.setGeometry(QtCore.QRect(120, 150, 61, 41))
        self.namelabel.setObjectName("namelabel")
        self.lastnamelabel = QtWidgets.QLabel(self.background)
        self.lastnamelabel.setGeometry(QtCore.QRect(120, 190, 121, 41))
        self.lastnamelabel.setObjectName("lastnamelabel")
        self.passwordlabel = QtWidgets.QLabel(self.background)
        self.passwordlabel.setGeometry(QtCore.QRect(120, 270, 141, 41))
        self.passwordlabel.setObjectName("passwordlabel")
        self.postlabel = QtWidgets.QLabel(self.background)
        self.postlabel.setGeometry(QtCore.QRect(120, 310, 141, 41))
        self.postlabel.setObjectName("postlabel")
        self.name = QtWidgets.QLineEdit(self.background)
        self.name.setGeometry(QtCore.QRect(260, 160, 161, 20))
        self.name.setObjectName("name")
        self.lastname = QtWidgets.QLineEdit(self.background)
        self.lastname.setGeometry(QtCore.QRect(260, 200, 161, 20))
        self.lastname.setObjectName("lastname")
        self.password = QtWidgets.QLineEdit(self.background)
        self.password.setGeometry(QtCore.QRect(260, 280, 161, 20))
        self.password.setText("")
        self.password.setObjectName("password")
        self.post = QtWidgets.QLineEdit(self.background)
        self.post.setGeometry(QtCore.QRect(260, 320, 161, 20))
        self.post.setObjectName("post")
        self.loginlabel = QtWidgets.QLabel(self.background)
        self.loginlabel.setGeometry(QtCore.QRect(120, 230, 61, 41))
        self.loginlabel.setObjectName("loginlabel")
        self.login = QtWidgets.QLineEdit(self.background)
        self.login.setGeometry(QtCore.QRect(262, 240, 161, 20))
        self.login.setObjectName("login")
        self.nazavanie = QtWidgets.QLabel(self.background)
        self.nazavanie.setGeometry(QtCore.QRect(60, 60, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.nazavanie.setFont(font)
        self.nazavanie.setObjectName("nazavanie")
        self.okey = QtWidgets.QPushButton(self.background)
        self.okey.setGeometry(QtCore.QRect(154, 420, 91, 31))
        self.okey.setObjectName("okey")
        self.okey.clicked.connect(lambda: self.adduser())
        self.cancel = QtWidgets.QPushButton(self.background)
        self.cancel.setGeometry(QtCore.QRect(300, 420, 91, 31))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(usercreate)
        QtCore.QMetaObject.connectSlotsByName(usercreate)

    def adduser(self):
        try:
            db = mdb.connect('localhost', 'root', 'root', 'arenda')
            mycursor = db.cursor()
            name2 = self.name.text()
            lastname2 = self.lastname.text()
            login2 = self.login.text()
            password2 = self.password.text()
            post2 = self.post.text()
            query = "INSERT INTO `login` (`Name`, `LastName`, `Login`, `Password`, `Post`) VALUES ('" +name2 + "', '" +lastname2 + "', '" +login2 + "', '" +password2 + "', '" +post2 + "')"
            mycursor.execute(query)
            db.commit()
            error = QMessageBox()
            error.setWindowTitle('Успех')
            error.setText('Пользователь успешно внесен!')
            error.buttons = QtWidgets.QMessageBox.Ok
            error.exec_()
        
        except mdb.Error as e:
                print (e)
                error = QMessageBox()
                error.setText('Переделывай, данные не внесены!')
                error.exec_()



    def retranslateUi(self, usercreate):
        _translate = QtCore.QCoreApplication.translate
        usercreate.setWindowTitle(_translate("usercreate", "Новый пользователь"))
        self.namelabel.setText(_translate("usercreate", "Имя:"))
        self.lastnamelabel.setText(_translate("usercreate", "Фамилия:"))
        self.passwordlabel.setText(_translate("usercreate", "Пароль:"))
        self.postlabel.setText(_translate("usercreate", "Должность"))
        self.loginlabel.setText(_translate("usercreate", "Логин:"))
        self.nazavanie.setText(_translate("usercreate", "Добавление нового пользователя"))
        self.okey.setText(_translate("usercreate", "ОК"))
        self.cancel.setText(_translate("usercreate", "Отменить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    usercreate = QtWidgets.QDialog()
    ui = Ui_usercreate()
    ui.setupUi(usercreate)
    usercreate.show()
    sys.exit(app.exec_())
