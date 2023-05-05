from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
import MySQLdb as mdb
import images

class Ui_arendatorsstat(object):
    def setupUi(self, arendatorsstat):
        arendatorsstat.setObjectName("arendatorsstat")
        arendatorsstat.setFixedSize(901, 609)
        icon = QIcon((":/logocompany.png"))
        arendatorsstat.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(arendatorsstat.sizePolicy().hasHeightForWidth())
        arendatorsstat.setSizePolicy(sizePolicy)
        self.background = QtWidgets.QFrame(arendatorsstat)
        self.background.setEnabled(True)
        self.background.setGeometry(QtCore.QRect(-1, -1, 921, 611))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("#background {\n"
"background-color: rgb(170, 170, 200)\n"
"}")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.tablearendators = QtWidgets.QTableWidget(self.background)
        self.tablearendators.setGeometry(QtCore.QRect(60, 110, 791, 131))
        self.tablearendators.setRowCount(0)
        self.tablearendators.setObjectName("tablearendators")
        self.tablearendators.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tablearendators.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablearendators.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablearendators.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablearendators.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablearendators.setHorizontalHeaderItem(4, item)
        self.tablearendators.horizontalHeader().setDefaultSectionSize(157)
        self.tablearendators.horizontalHeader().setMinimumSectionSize(40)
        self.label = QtWidgets.QLabel(self.background)
        self.label.setGeometry(QtCore.QRect(260, 50, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.updatebutton = QtWidgets.QPushButton(self.background)
        self.updatebutton.setGeometry(QtCore.QRect(400, 530, 101, 41))
        self.updatebutton.setObjectName("updatebutton")
        self.updatebutton.clicked.connect(lambda: self.updatearendatorstatforfirst())
        self.updatebutton.clicked.connect(lambda: self.updatearendatorstatforsecond())
        self.label_2 = QtWidgets.QLabel(self.background)
        self.label_2.setGeometry(QtCore.QRect(230, 290, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tablearendators_2 = QtWidgets.QTableWidget(self.background)
        self.tablearendators_2.setGeometry(QtCore.QRect(60, 350, 791, 131))
        self.tablearendators_2.setRowCount(0)
        self.tablearendators_2.setObjectName("tablearendators_2")
        self.tablearendators_2.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tablearendators_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablearendators_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablearendators_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablearendators_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablearendators_2.setHorizontalHeaderItem(4, item)
        self.tablearendators_2.horizontalHeader().setDefaultSectionSize(157)
        self.tablearendators_2.horizontalHeader().setMinimumSectionSize(40)

        self.retranslateUi(arendatorsstat)
        QtCore.QMetaObject.connectSlotsByName(arendatorsstat)

    def updatearendatorstatforfirst(self): #Добавление в таблицу значений из БД, построчно и по колонкам
        try:
            db = mdb.connect('localhost', 'root', 'root', 'arenda')
            mycursor = db.cursor()
            query = "SELECT * FROM fizlitca WHERE IIN IN (SELECT IIN_Arendatora FROM dogovory)"
            mycursor.execute(query)
            result = mycursor.fetchall()
            result = list(result)
            self.tablearendators.setRowCount(len(result))
        
        # Заполнение таблицы данными из списка result
            for i, row in enumerate(result):
                for j, value in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tablearendators.setItem(i, j, item)
    
        
        except mdb.Error as e:
                error = QMessageBox()
                error.setText('Подключение невозможно!')
                error.exec_()

    def updatearendatorstatforsecond(self): #Добавление в таблицу значений из БД, построчно и по колонкам
        try:
            db = mdb.connect('localhost', 'root', 'root', 'arenda')
            mycursor = db.cursor()
            query = "SELECT * FROM fizlitca WHERE IIN NOT IN (SELECT IIN_Arendatora FROM dogovory)"
            mycursor.execute(query)
            result = mycursor.fetchall()
            result = list(result)
            self.tablearendators_2.setRowCount(len(result))
        
        # Заполнение таблицы данными из списка result
            for i, row in enumerate(result):
                for j, value in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tablearendators_2.setItem(i, j, item)
    
        
        except mdb.Error as e:
                error = QMessageBox()
                error.setText('Подключение невозможно!')
                error.exec_()





    def retranslateUi(self, arendatorsstat):
        _translate = QtCore.QCoreApplication.translate
        arendatorsstat.setWindowTitle(_translate("arendatorsstat", "Отчет об арендаторах"))
        item = self.tablearendators.horizontalHeaderItem(0)
        item.setText(_translate("arendatorsstat", "ФИО"))
        item = self.tablearendators.horizontalHeaderItem(1)
        item.setText(_translate("arendatorsstat", "Пасспорт,№"))
        item = self.tablearendators.horizontalHeaderItem(2)
        item.setText(_translate("arendatorsstat", "ИИН"))
        item = self.tablearendators.horizontalHeaderItem(3)
        item.setText(_translate("arendatorsstat", "Адрес"))
        item = self.tablearendators.horizontalHeaderItem(4)
        item.setText(_translate("arendatorsstat", "Телефон"))
        self.label.setText(_translate("arendatorsstat", "Физ-лица, заключившие договор"))
        self.updatebutton.setText(_translate("arendatorsstat", "Сформировать"))
        self.label_2.setText(_translate("arendatorsstat", "Физ-лица, не заключившие договор"))
        item = self.tablearendators_2.horizontalHeaderItem(0)
        item.setText(_translate("arendatorsstat", "ФИО"))
        item = self.tablearendators_2.horizontalHeaderItem(1)
        item.setText(_translate("arendatorsstat", "Пасспорт,№"))
        item = self.tablearendators_2.horizontalHeaderItem(2)
        item.setText(_translate("arendatorsstat", "ИИН"))
        item = self.tablearendators_2.horizontalHeaderItem(3)
        item.setText(_translate("arendatorsstat", "Адрес"))
        item = self.tablearendators_2.horizontalHeaderItem(4)
        item.setText(_translate("arendatorsstat", "Телефон"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    arendatorsstat = QtWidgets.QDialog()
    ui = Ui_arendatorsstat()
    ui.setupUi(arendatorsstat)
    arendatorsstat.show()
    sys.exit(app.exec_())
