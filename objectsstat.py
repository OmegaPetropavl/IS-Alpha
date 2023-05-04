from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
import MySQLdb as mdb
import images

class Ui_objectsstat(object):
    def setupUi(self, objectsstat):
        objectsstat.setObjectName("objectsstat")
        objectsstat.setFixedSize(901, 609)
        icon = QIcon((":/logocompany.png"))
        objectsstat.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(objectsstat.sizePolicy().hasHeightForWidth())
        objectsstat.setSizePolicy(sizePolicy)
        self.background = QtWidgets.QFrame(objectsstat)
        self.background.setEnabled(True)
        self.background.setGeometry(QtCore.QRect(-1, -1, 921, 611))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("#background {\n"
"background-color: rgb(170, 170, 200)\n"
"}")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.tableobjects = QtWidgets.QTableWidget(self.background)
        self.tableobjects.setGeometry(QtCore.QRect(60, 110, 791, 131))
        self.tableobjects.setRowCount(0)
        self.tableobjects.setObjectName("tableobjects")
        self.tableobjects.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableobjects.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableobjects.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableobjects.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableobjects.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableobjects.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableobjects.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableobjects.setHorizontalHeaderItem(6, item)
        self.tableobjects.horizontalHeader().setDefaultSectionSize(157)
        self.tableobjects.horizontalHeader().setMinimumSectionSize(40)
        self.label = QtWidgets.QLabel(self.background)
        self.label.setGeometry(QtCore.QRect(280, 50, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.updatebutton = QtWidgets.QPushButton(self.background)
        self.updatebutton.setGeometry(QtCore.QRect(400, 530, 101, 41))
        self.updatebutton.setObjectName("updatebutton")
        self.updatebutton.clicked.connect(lambda: self.updateobjectstat_1())
        self.updatebutton.clicked.connect(lambda: self.updateobjectstat_2())
        self.label_2 = QtWidgets.QLabel(self.background)
        self.label_2.setGeometry(QtCore.QRect(260, 290, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableobjects_2 = QtWidgets.QTableWidget(self.background)
        self.tableobjects_2.setGeometry(QtCore.QRect(60, 360, 791, 131))
        self.tableobjects_2.setRowCount(0)
        self.tableobjects_2.setObjectName("tableobjects_2")
        self.tableobjects_2.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableobjects_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableobjects_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableobjects_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableobjects_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableobjects_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableobjects_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableobjects_2.setHorizontalHeaderItem(6, item)
        self.tableobjects_2.horizontalHeader().setDefaultSectionSize(157)
        self.tableobjects_2.horizontalHeader().setMinimumSectionSize(40)

        self.retranslateUi(objectsstat)
        QtCore.QMetaObject.connectSlotsByName(objectsstat)

    def updateobjectstat_1(self): #Добавление в таблицу значений из БД, построчно и по колонкам
        try:
            db = mdb.connect('localhost', 'root', 'root', 'arenda')
            mycursor = db.cursor()
            query = "SELECT o.Name, o.Adress, o.Object_Square, o.Podval_Square,o.Koef_Podval,o.Koef_techobustr,o.Plata FROM objecty o WHERE o.Adress IN (SELECT ID_Objecta FROM dogovory)"
            mycursor.execute(query)
            result = mycursor.fetchall()
            result = list(result)
            self.tableobjects.setRowCount(len(result))
        
        # Заполнение таблицы данными из списка result
            for i, row in enumerate(result):
                for j, value in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tableobjects.setItem(i, j, item)
    
        
        except mdb.Error as e:
                error = QMessageBox()
                error.setText('Подключение невозможно!')
                error.exec_()
    
    def updateobjectstat_2(self): #Добавление в таблицу значений из БД, построчно и по колонкам
        try:
            db = mdb.connect('localhost', 'root', 'root', 'arenda')
            mycursor = db.cursor()
            query = "SELECT o.Name, o.Adress, o.Object_Square, o.Podval_Square,o.Koef_Podval,o.Koef_techobustr,o.Plata FROM objecty o WHERE o.Adress NOT IN (SELECT ID_Objecta FROM dogovory)"
            mycursor.execute(query)
            result = mycursor.fetchall()
            result = list(result)
            self.tableobjects_2.setRowCount(len(result))
        
        # Заполнение таблицы данными из списка result
            for i, row in enumerate(result):
                for j, value in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tableobjects_2.setItem(i, j, item)
    
        
        except mdb.Error as e:
                error = QMessageBox()
                error.setText('Подключение невозможно!')
                error.exec_()



    def retranslateUi(self, objectsstat):
        _translate = QtCore.QCoreApplication.translate
        objectsstat.setWindowTitle(_translate("objectsstat", "Отчет об объектах"))
        item = self.tableobjects.horizontalHeaderItem(0)
        item.setText(_translate("objectsstat", "Название"))
        item = self.tableobjects.horizontalHeaderItem(1)
        item.setText(_translate("objectsstat", "Адрес"))
        item = self.tableobjects.horizontalHeaderItem(2)
        item.setText(_translate("objectsstat", "Площадь помещения"))
        item = self.tableobjects.horizontalHeaderItem(3)
        item.setText(_translate("objectsstat", "Площадь подвала"))
        item = self.tableobjects.horizontalHeaderItem(4)
        item.setText(_translate("objectsstat", "Коэф. подвала"))
        item = self.tableobjects.horizontalHeaderItem(5)
        item.setText(_translate("objectsstat", "Коэф. тех. обустройства"))
        item = self.tableobjects.horizontalHeaderItem(6)
        item.setText(_translate("objectsstat", "Арендная плата"))
        self.label.setText(_translate("objectsstat", "Cданные в аренду помещения"))
        self.updatebutton.setText(_translate("objectsstat", "Сформировать"))
        self.label_2.setText(_translate("objectsstat", "Не сданные в аренду помещения"))
        item = self.tableobjects_2.horizontalHeaderItem(0)
        item.setText(_translate("objectsstat", "Название"))
        item = self.tableobjects_2.horizontalHeaderItem(1)
        item.setText(_translate("objectsstat", "Адрес"))
        item = self.tableobjects_2.horizontalHeaderItem(2)
        item.setText(_translate("objectsstat", "Площадь помещения"))
        item = self.tableobjects_2.horizontalHeaderItem(3)
        item.setText(_translate("objectsstat", "Площадь подвала"))
        item = self.tableobjects_2.horizontalHeaderItem(4)
        item.setText(_translate("objectsstat", "Коэф. подвала"))
        item = self.tableobjects_2.horizontalHeaderItem(5)
        item.setText(_translate("objectsstat", "Коэф. тех. обустройства"))
        item = self.tableobjects_2.horizontalHeaderItem(6)
        item.setText(_translate("objectsstat", "Арендная плата"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    objectsstat = QtWidgets.QDialog()
    ui = Ui_objectsstat()
    ui.setupUi(objectsstat)
    objectsstat.show()
    sys.exit(app.exec_())
