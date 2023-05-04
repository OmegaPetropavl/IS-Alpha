from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
import MySQLdb as mdb
import images

class Ui_oplatastat(object):
    def setupUi(self, oplatastat):
        oplatastat.setObjectName("oplatastat")
        oplatastat.setFixedSize(854, 468)
        icon = QIcon((":/logocompany.png"))
        oplatastat.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(oplatastat.sizePolicy().hasHeightForWidth())
        oplatastat.setSizePolicy(sizePolicy)
        self.background = QtWidgets.QFrame(oplatastat)
        self.background.setEnabled(True)
        self.background.setGeometry(QtCore.QRect(-1, -1, 921, 611))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("#background {\n"
"background-color: rgb(124, 170, 200)\n"
"}")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.tableoplata = QtWidgets.QTableWidget(self.background)
        self.tableoplata.setGeometry(QtCore.QRect(30, 150, 791, 131))
        self.tableoplata.setRowCount(0)
        self.tableoplata.setObjectName("tableoplata")
        self.tableoplata.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableoplata.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableoplata.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableoplata.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableoplata.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableoplata.setHorizontalHeaderItem(4, item)
        
        self.tableoplata.horizontalHeader().setDefaultSectionSize(157)
        self.tableoplata.horizontalHeader().setMinimumSectionSize(40)
        self.label = QtWidgets.QLabel(self.background)
        self.label.setGeometry(QtCore.QRect(220, 60, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.updatebutton = QtWidgets.QPushButton(self.background)
        self.updatebutton.setGeometry(QtCore.QRect(390, 360, 101, 41))
        self.updatebutton.setObjectName("updatebutton")
        self.updatebutton.clicked.connect(lambda: self.updateoplata())
        self.retranslateUi(oplatastat)
        QtCore.QMetaObject.connectSlotsByName(oplatastat)

    def updateoplata(self): #Добавление в таблицу значений из БД, построчно и по колонкам
        try:
            db = mdb.connect('localhost', 'root', 'root', 'arenda')
            mycursor = db.cursor()
            query = "SELECT f.FIO,f.IIN,f.Phone, d.Month_price, d.Dataezhemes_oplaty FROM fizlitca f INNER JOIN dogovory d ON f.IIN = d.IIN_Arendatora WHERE d.Dataezhemes_oplaty < CURDATE()"
            mycursor.execute(query)
            result = mycursor.fetchall()
            result = list(result)
            self.tableoplata.setRowCount(len(result))
        
        # Заполнение таблицы данными из списка result
            for i, row in enumerate(result):
                for j, value in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tableoplata.setItem(i, j, item)
    
        
        except mdb.Error as e:
                error = QMessageBox()
                error.setText('Подключение невозможно!')
                error.exec_()







    def retranslateUi(self, oplatastat):
        _translate = QtCore.QCoreApplication.translate
        oplatastat.setWindowTitle(_translate("oplatastat", "Отчет об оплате"))
        item = self.tableoplata.horizontalHeaderItem(0)
        item.setText(_translate("oplatastat", "ФИО"))
        item = self.tableoplata.horizontalHeaderItem(1)
        item.setText(_translate("oplatastat", "ИИН"))
        item = self.tableoplata.horizontalHeaderItem(2)
        item.setText(_translate("oplatastat", "Телефон"))
        item = self.tableoplata.horizontalHeaderItem(3)
        item.setText(_translate("oplatastat", "Оплата в месяц"))
        item = self.tableoplata.horizontalHeaderItem(4)
        item.setText(_translate("oplatastat", "Дата ежемесячной оплаты"))
        
        self.label.setText(_translate("oplatastat", "Отчет о задолженностях арендаторов"))
        self.updatebutton.setText(_translate("oplatastat", "Сформировать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    oplatastat = QtWidgets.QDialog()
    ui = Ui_oplatastat()
    ui.setupUi(oplatastat)
    oplatastat.show()
    sys.exit(app.exec_())
