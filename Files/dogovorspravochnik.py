from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem
import images
import MySQLdb as mdb
from docx import Document
from docx.shared import Inches
from dogovor import *


class Ui_dogovors(object):
    def setupUi(self, dogovors):
        dogovors.setObjectName("dogovors")
        dogovors.setFixedSize(901, 609)
        icon = QIcon((":/logocompany.png"))
        dogovors.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dogovors.sizePolicy().hasHeightForWidth())
        dogovors.setSizePolicy(sizePolicy)
        self.background = QtWidgets.QFrame(dogovors)
        self.background.setEnabled(True)
        self.background.setGeometry(QtCore.QRect(-1, -1, 921, 611))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("#background {\n"
"background-color: rgb(170, 170, 200)\n"
"}")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.tabledogovors = QtWidgets.QTableWidget(self.background)
        self.tabledogovors.setGeometry(QtCore.QRect(60, 110, 791, 321))
        self.tabledogovors.setRowCount(0)
        self.tabledogovors.setObjectName("tabledogovors")
        self.tabledogovors.setColumnCount(8)
        self.tabledogovors.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        item = QtWidgets.QTableWidgetItem()
        self.tabledogovors.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledogovors.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledogovors.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledogovors.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledogovors.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledogovors.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledogovors.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabledogovors.setHorizontalHeaderItem(7, item)
        self.tabledogovors.horizontalHeader().setDefaultSectionSize(151)
        self.label = QtWidgets.QLabel(self.background)
        self.label.setGeometry(QtCore.QRect(390, 40, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.deletebutton = QtWidgets.QPushButton(self.background)
        self.deletebutton.setGeometry(QtCore.QRect(690, 490, 91, 41))
        self.deletebutton.setObjectName("deletebutton")
        self.deletebutton.clicked.connect(lambda: self.delete_row())
        self.addbutton = QtWidgets.QPushButton(self.background)
        self.addbutton.setGeometry(QtCore.QRect(320, 490, 91, 41))
        self.addbutton.setObjectName("addbutton")
        self.addbutton.clicked.connect(lambda: self.dogovor_create())
        self.updatebutton = QtWidgets.QPushButton(self.background)
        self.updatebutton.setGeometry(QtCore.QRect(120, 490, 101, 41))
        self.updatebutton.setObjectName("updatebutton")
        self.updatebutton.clicked.connect(lambda: self.updaterows())
        self.savebutton = QtWidgets.QPushButton(self.background)
        self.savebutton.setGeometry(QtCore.QRect(510, 490, 91, 41))
        self.savebutton.setObjectName("savebutton")
        self.savebutton.clicked.connect(lambda: self.pechat())
        self.tabledogovors.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabledogovors.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        #Блокировка всех ячеек
        for column in range(self.tabledogovors.columnCount()):
            for row in range(self.tabledogovors.rowCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)  # Удаление флага ItemIsEditable
                self.dogovors.setItem(row, column, item)
        header_labels = ["Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6", "Column 7", "Column 8"]
        self.tabledogovors.setHorizontalHeaderLabels(header_labels)
        #Конец блокировки
        self.retranslateUi(dogovors)
        QtCore.QMetaObject.connectSlotsByName(dogovors)

    def updaterows(self): #Добавление в таблицу значений из БД, построчно и по колонкам
        try:
            db = mdb.connect('localhost', 'root', 'root', 'arenda')
            mycursor = db.cursor()
            query = "SELECT * from dogovory"
            mycursor.execute(query)
            result = mycursor.fetchall()
            result = list(result)
            self.tabledogovors.setRowCount(len(result))
        
        # Заполнение таблицы данными из списка result
            for i, row in enumerate(result):
                for j, value in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tabledogovors.setItem(i, j, item)
    
        
        except mdb.Error as e:
                error = QMessageBox()
                error.setText('Подключение невозможно!')
                error.exec_()

    def dogovor_create(self):
        self.dogovorcreate_window = QtWidgets.QMainWindow()
        self.dogovorcreate_ui = Ui_Dialog()
        self.dogovorcreate_ui.setupUi(self.dogovorcreate_window)
        self.dogovorcreate_window.show()


    def delete_row(self):
        selected_row = self.tabledogovors.currentRow()
        if selected_row >= 0:
            id_dogovora = self.tabledogovors.item(selected_row, 0).text()  # Получение значения "ID договора"
            reply = QMessageBox.question(self.background, 'Подтверждение удаления', 'Вы действительно хотите удалить договор?',
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.tabledogovors.removeRow(selected_row)
                try:
                    db = mdb.connect('localhost', 'root', 'root', 'arenda')
                    mycursor = db.cursor()
                    
                    query = "DELETE FROM  `dogovory` WHERE ID_Dogovora = '"+ id_dogovora + "'"
                    mycursor.execute(query)
                    db.commit()
                    error = QMessageBox()
                    error.setWindowTitle('Успех')
                    error.setText('Договор успешно удален!')
                    error.buttons = QMessageBox.Ok
                    error.exec_()
                except mdb.Error as e:
                    print (e)
                    error = QMessageBox()
                    error.setText('Переделывай, данные не внесены!')
                    error.exec_()
            else:
                return
        
        else:
            QMessageBox.warning(self.background, 'Предупреждение', 'Пожалуйста, выберите строку для удаления.')

    def pechat(self):
        selected_row = self.tabledogovors.currentRow()
        if selected_row >= 0:
            IIN11 = self.tabledogovors.item(selected_row, 1).text()
            VAR11 = self.tabledogovors.item(selected_row, 2).text()
            VAR21 = self.tabledogovors.item(selected_row, 3).text()
            VAR31 = self.tabledogovors.item(selected_row, 4).text()
            VAR41 = self.tabledogovors.item(selected_row, 5).text()
            VAR51 = self.tabledogovors.item(selected_row, 6).text()
            VAR61 = self.tabledogovors.item(selected_row, 7).text()
            print (VAR11)
            db = mdb.connect('localhost', 'root', 'root', 'arenda')
            mycursor = db.cursor()
            query1 = "SELECT Name from objecty where Adress = '" +VAR11 + "' "
            query2 = "SELECT Object_Square from objecty where Adress = '" +VAR11 + "' "
            mycursor.execute(query1)
            Object_name1 = mycursor.fetchone()
            Object_name1 = str(Object_name1[0]).replace("(", "").replace(")", "")
            mycursor.execute(query2)
            Object_Square1 = mycursor.fetchone()
            Object_Square1 = str(Object_Square1[0]).replace("(", "").replace(")", "")
            document = Document('DogovorShablonPython.docx')  
            for paragraph in document.paragraphs:
                inline = paragraph.runs
                for i in range(len(inline)):
                    if 'ArendnayaPlata' in inline[i].text:
                        inline[i].text = inline[i].text.replace('ArendnayaPlata', VAR61)
                    if 'ChisloOplaty' in inline[i].text:
                        inline[i].text = inline[i].text.replace('ChisloOplaty', VAR51)
                    if 'DataDogovora' in inline[i].text:
                        inline[i].text = inline[i].text.replace('DataDogovora', VAR41)
                    if 'DataOkonchaniya' in inline[i].text:
                        inline[i].text = inline[i].text.replace('DataOkonchaniya', VAR31)
                    if 'DataNachala' in inline[i].text:
                        inline[i].text = inline[i].text.replace('DataNachala', VAR21)
                    if 'AdressObject' in inline[i].text:
                        inline[i].text = inline[i].text.replace('AdressObject', VAR11)
                    if 'Arendator' in inline[i].text:
                        inline[i].text = inline[i].text.replace('Arendator', IIN11)
                    if 'Square' in inline[i].text:
                        inline[i].text = inline[i].text.replace('Square', Object_Square1)
                    if 'Name' in inline[i].text:
                        inline[i].text = inline[i].text.replace('Name', Object_name1)
            document.save(f'{VAR11}_dogovor.docx')
            success = QMessageBox()
            success.setWindowTitle('Успех')
            success.setText('Договор успешно сохранен в файл!')
            success.buttons = QtWidgets.QMessageBox.Ok
            icon = QtGui.QIcon((":/logocompany.png"))
            success.setWindowIcon(icon)
            success.exec_()








    def retranslateUi(self, dogovors):
        _translate = QtCore.QCoreApplication.translate
        dogovors.setWindowTitle(_translate("dogovors", "Справочник договоров"))
        item = self.tabledogovors.horizontalHeaderItem(0)
        item.setText(_translate("dogovors", "ID договора"))
        item = self.tabledogovors.horizontalHeaderItem(1)
        item.setText(_translate("dogovors", "ИИН арендатора"))
        item = self.tabledogovors.horizontalHeaderItem(2)
        item.setText(_translate("dogovors", "ID объекта"))
        item = self.tabledogovors.horizontalHeaderItem(3)
        item.setText(_translate("dogovors", "Дата начала аренды"))
        item = self.tabledogovors.horizontalHeaderItem(4)
        item.setText(_translate("dogovors", "Дата окончания аренды"))
        item = self.tabledogovors.horizontalHeaderItem(5)
        item.setText(_translate("dogovors", "Дата заключения договора"))
        item = self.tabledogovors.horizontalHeaderItem(6)
        item.setText(_translate("dogovors", "Дата ежемес. оплаты"))
        item = self.tabledogovors.horizontalHeaderItem(7)
        item.setText(_translate("dogovors", "Плата в месяц"))
        self.label.setText(_translate("dogovors", "Договоры"))
        self.deletebutton.setText(_translate("dogovors", "Удалить"))
        self.addbutton.setText(_translate("dogovors", "Добавить"))
        self.updatebutton.setText(_translate("dogovors", "Обновить"))
        self.savebutton.setText(_translate("dogovors", "Сохранить "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dogovors = QtWidgets.QDialog()
    ui = Ui_dogovors()
    ui.setupUi(dogovors)
    dogovors.show()
    sys.exit(app.exec_())
