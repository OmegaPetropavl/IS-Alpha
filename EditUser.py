from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton
import MySQLdb as mdb
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import images

class Ui_useredit(object):
    def setupUi(self, useredit,selected_row):
        self.selected_row = selected_row
        useredit.setObjectName("useredit")
        useredit.setFixedSize(465, 493)
        icon = QIcon((":/logocompany.png"))
        useredit.setWindowIcon(icon)
        self.background = QtWidgets.QFrame(useredit)
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
        self.id = QtWidgets.QLineEdit(self.background)
        self.id.setGeometry(QtCore.QRect(260, 340, 161, 20))
        self.id.setObjectName("id")
        self.id.setVisible(False)
        self.id.setReadOnly(True)
        self.loginlabel = QtWidgets.QLabel(self.background)
        self.loginlabel.setGeometry(QtCore.QRect(120, 230, 61, 41))
        self.loginlabel.setObjectName("loginlabel")
        self.login = QtWidgets.QLineEdit(self.background)
        self.login.setGeometry(QtCore.QRect(262, 240, 161, 20))
        self.login.setObjectName("login")
        self.nazavanie = QtWidgets.QLabel(self.background)
        self.nazavanie.setGeometry(QtCore.QRect(80, 70, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.nazavanie.setFont(font)
        self.nazavanie.setObjectName("nazavanie")
        self.okey = QtWidgets.QPushButton(self.background)
        self.okey.setGeometry(QtCore.QRect(154, 420, 91, 31))
        self.okey.setObjectName("okey")
        self.okey.clicked.connect(lambda: self.editusertodatabase())
        self.cancel = QtWidgets.QPushButton(self.background)
        self.cancel.setGeometry(QtCore.QRect(300, 420, 91, 31))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(useredit)
        QtCore.QMetaObject.connectSlotsByName(useredit)


    def editusertodatabase(self):
        try:
            db = mdb.connect('localhost', 'root', 'root', 'arenda')
            mycursor = db.cursor()
            name4 = self.name.text()
            lastname4 = self.lastname.text()
            login4 = self.login.text()
            password4 = self.password.text()
            post4 = self.post.text()
            id4 = self.id.text()
            query = f"UPDATE login SET Name='{name4}', LastName='{lastname4}', Login='{login4}', Password='{password4}', Post='{post4}' WHERE ID = '{id4}'"
            mycursor.execute(query)
            db.commit()
            error = QMessageBox()
            error.setWindowTitle('Успех')
            error.setText('Данные отредактированы!')
            error.buttons = QtWidgets.QMessageBox.Ok
            error.exec_()
            
        

        except mdb.Error as e:
                print (e)
                error = QMessageBox()
                error.setText('Переделывай, данные не внесены!')
                error.exec_()


    def retranslateUi(self, useredit):
        _translate = QtCore.QCoreApplication.translate
        useredit.setWindowTitle(_translate("useredit", "Редактирование данных пользователя"))
        self.namelabel.setText(_translate("useredit", "Имя:"))
        self.lastnamelabel.setText(_translate("useredit", "Фамилия:"))
        self.passwordlabel.setText(_translate("useredit", "Пароль:"))
        self.postlabel.setText(_translate("useredit", "Должность"))
        self.loginlabel.setText(_translate("useredit", "Логин:"))
        self.nazavanie.setText(_translate("useredit", "Редактирование пользователя"))
        self.okey.setText(_translate("useredit", "ОК"))
        self.cancel.setText(_translate("useredit", "Отменить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    useredit = QtWidgets.QDialog()
    ui = Ui_useredit()
    ui.setupUi(useredit)
    useredit.show()
    sys.exit(app.exec_())
