from PyQt5 import QtCore, QtGui, QtWidgets
import pickle
from PyQt5.QtWidgets import QMessageBox, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem
import images
import MySQLdb as mdb
from objectspravochnik import *
class Ui_EditObject():
    def setupUi(self, EditObject, selected_row):
        self.selected_row = selected_row
        EditObject.setObjectName("EditObject")
        EditObject.setFixedSize(470, 555)
        icon = QIcon((":/logocompany.png"))
        EditObject.setWindowIcon(icon)
        self.background = QtWidgets.QFrame(EditObject)
        self.background.setGeometry(QtCore.QRect(-30, -10, 531, 601))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("#background {\n"
"background-color: rgb(170, 170, 150)\n"
"}")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.namelabel = QtWidgets.QLabel(self.background)
        self.namelabel.setGeometry(QtCore.QRect(120, 150, 61, 41))
        self.namelabel.setObjectName("namelabel")
        self.adresslabel = QtWidgets.QLabel(self.background)
        self.adresslabel.setGeometry(QtCore.QRect(120, 190, 121, 41))
        self.adresslabel.setObjectName("adresslabel")
        self.square_podval_label = QtWidgets.QLabel(self.background)
        self.square_podval_label.setGeometry(QtCore.QRect(120, 270, 141, 41))
        self.square_podval_label.setObjectName("square_podval_label")
        self.koefpodvallabel = QtWidgets.QLabel(self.background)
        self.koefpodvallabel.setGeometry(QtCore.QRect(120, 310, 141, 41))
        self.koefpodvallabel.setObjectName("koefpodvallabel")
        self.name = QtWidgets.QLineEdit(self.background)
        self.name.setGeometry(QtCore.QRect(260, 160, 161, 20))
        self.name.setObjectName("name")
        self.adress = QtWidgets.QLineEdit(self.background)
        self.adress.setGeometry(QtCore.QRect(260, 200, 161, 20))
        self.adress.setObjectName("adress")
        self.adress.setReadOnly(True)
        self.podva_square = QtWidgets.QLineEdit(self.background)
        self.podva_square.setGeometry(QtCore.QRect(260, 280, 161, 20))
        self.podva_square.setText("")
        self.podva_square.setObjectName("podva_square")
        self.koef_podvl = QtWidgets.QLineEdit(self.background)
        self.koef_podvl.setGeometry(QtCore.QRect(260, 320, 161, 20))
        self.koef_podvl.setObjectName("koef_podvl")
        self.squarelabel = QtWidgets.QLabel(self.background)
        self.squarelabel.setGeometry(QtCore.QRect(120, 230, 81, 41))
        self.squarelabel.setObjectName("squarelabel")
        self.square = QtWidgets.QLineEdit(self.background)
        self.square.setGeometry(QtCore.QRect(262, 240, 161, 20))
        self.square.setObjectName("square")
        self.nazavanie = QtWidgets.QLabel(self.background)
        self.nazavanie.setGeometry(QtCore.QRect(120, 60, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.nazavanie.setFont(font)
        self.nazavanie.setObjectName("nazavanie")
        self.okey = QtWidgets.QPushButton(self.background)
        self.okey.setGeometry(QtCore.QRect(144, 500, 91, 31))
        self.okey.setObjectName("okey")
        self.okey.clicked.connect(lambda: self.editobjecttodatabase())
        self.cancel = QtWidgets.QPushButton(self.background)
        self.cancel.setGeometry(QtCore.QRect(290, 500, 91, 31))
        self.cancel.setObjectName("cancel")
        self.podvalradio = QtWidgets.QRadioButton(self.background)
        self.podvalradio.setGeometry(QtCore.QRect(340, 410, 80, 18))
        self.podvalradio.setObjectName("podvalradio")
        self.podvalradio.setChecked(True)
        self.koef_tech = QtWidgets.QLineEdit(self.background)
        self.koef_tech.setGeometry(QtCore.QRect(260, 360, 161, 20))
        self.koef_tech.setText("")
        self.koef_tech.setObjectName("koef_tech")
        self.koeftechlabel = QtWidgets.QLabel(self.background)
        self.koeftechlabel.setGeometry(QtCore.QRect(120, 350, 141, 101))
        self.koeftechlabel.setTextFormat(QtCore.Qt.PlainText)
        self.koeftechlabel.setScaledContents(False)
        self.koeftechlabel.setWordWrap(True)
        self.koeftechlabel.setObjectName("koeftechlabel")
        
        self.retranslateUi(EditObject)
        QtCore.QMetaObject.connectSlotsByName(EditObject)

    def editobjecttodatabase(self):
        try:
            db = mdb.connect('localhost', 'root', 'root', 'arenda')
            mycursor = db.cursor()
            VAR1111 = self.name.text()
            VAR2222 = self.adress.text()
            VAR3333 = self.square.text()
            VAR4444 = ('1') #Подвал1
            VAR5555 = self.podva_square.text()
            VAR6666 = self.koef_podvl.text()
            VAR7777 = self.koef_tech.text()
            with open('adres1.pkl', 'rb') as file:
                Adres1 = pickle.load(file)
            query = f"UPDATE objecty SET Name='{VAR1111}', Adress='{VAR2222}', Object_Square='{VAR3333}', Podval='{VAR4444}', Podval_Square='{VAR5555}', Koef_Podval='{VAR6666}', Koef_techobustr='{VAR7777}' WHERE Adress = '{Adres1}'"
            mycursor.execute(query)
            db.commit()
            error = QMessageBox()
            error.setWindowTitle('Успех')
            error.setText('Объект успешно внесен!')
            error.buttons = QtWidgets.QMessageBox.Ok
            error.exec_()
            
        

        except mdb.Error as e:
                print (e)
                error = QMessageBox()
                error.setText('Переделывай, данные не внесены!')
                error.exec_()





    def retranslateUi(self, EditObject):
        _translate = QtCore.QCoreApplication.translate
        EditObject.setWindowTitle(_translate("EditObject", "Редактирование объекта"))
        self.namelabel.setText(_translate("EditObject", "Название:"))
        self.adresslabel.setText(_translate("EditObject", "Адрес:"))
        self.square_podval_label.setText(_translate("EditObject", "Площадь подвала, м2:"))
        self.koefpodvallabel.setText(_translate("EditObject", "Коэффициент подвала:"))
        self.squarelabel.setText(_translate("EditObject", "Площадь, м2:"))
        self.nazavanie.setText(_translate("EditObject", "Редактирование Объекта"))
        self.okey.setText(_translate("EditObject", "ОК"))
        self.cancel.setText(_translate("EditObject", "Отменить"))
        self.podvalradio.setText(_translate("EditObject", "Подвал"))
        self.koeftechlabel.setText(_translate("EditObject", "Коэффициент технического обустройства помещения:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditObject = QtWidgets.QDialog()
    ui = Ui_EditObject()
    ui.setupUi(EditObject)
    EditObject.show()
    sys.exit(app.exec_())
