# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arendatorspravochnik.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem
import images
import MySQLdb as mdb
from fizcreate import *
from EditArendatel import *

class Ui_arendators(object):
    def setupUi(self, arendators):
        arendators.setObjectName("arendators")
        arendators.setFixedSize(901, 609)
        icon = QIcon((":/logocompany.png"))
        arendators.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(arendators.sizePolicy().hasHeightForWidth())
        arendators.setSizePolicy(sizePolicy)
        self.background = QtWidgets.QFrame(arendators)
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
        self.tablearendators.setGeometry(QtCore.QRect(60, 110, 791, 321))
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
        self.label.setGeometry(QtCore.QRect(350, 40, 281, 51))
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
        self.addbutton.clicked.connect(lambda: self.openAddArendator())
        self.updatebutton = QtWidgets.QPushButton(self.background)
        self.updatebutton.setGeometry(QtCore.QRect(120, 490, 101, 41))
        self.updatebutton.setObjectName("updatebutton")
        self.updatebutton.clicked.connect(lambda: self.updatearendatorrows())
        self.editbutton = QtWidgets.QPushButton(self.background)
        self.editbutton.setGeometry(QtCore.QRect(510, 490, 91, 41))
        self.editbutton.setObjectName("editbutton")
        self.editbutton.clicked.connect(lambda: self.openEditArendator())
        self.retranslateUi(arendators)
        QtCore.QMetaObject.connectSlotsByName(arendators)


    def updatearendatorrows(self): #Добавление в таблицу значений из БД, построчно и по колонкам
        try:
            db = mdb.connect('localhost', 'root', 'root', 'arenda')
            mycursor = db.cursor()
            query = "SELECT * from fizlitca"
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



    def delete_row(self): #Удаление выделенной строчки из таблицы и БД
        selected_row = self.tablearendators.currentRow()
        if selected_row >= 0:
            iin = self.tablearendators.item(selected_row, 2).text()  # Получение значения "названия помещения"
            reply = QMessageBox.question(self.background, 'Подтверждение удаления', 'Вы действительно хотите удалить арендатора?',
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.tablearendators.removeRow(selected_row)
                try:
                    db = mdb.connect('localhost', 'root', 'root', 'arenda')
                    mycursor = db.cursor()
                    query = "DELETE FROM  `fizlitca` WHERE IIN = '"+ iin + "'"
                    mycursor.execute(query)
                    db.commit()
                    error = QMessageBox()
                    error.setWindowTitle('Успех')
                    error.setText('Арендатор успешно удален!')
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


    def openAddArendator(self):
        self.AddArendator_window = QtWidgets.QMainWindow()
        self.AddArendator_ui = Ui_fizcreate()
        self.AddArendator_ui.setupUi(self.AddArendator_window)
        self.AddArendator_window.show()


    def openEditArendator(self):
        selected_row = self.tablearendators.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.background, "Ошибка", "Выберите арендатора для редактирования")
        else:
            
            edit_arendator = QtWidgets.QDialog()
            ui = Ui_fizedit()
            ui.setupUi(edit_arendator,selected_row)
        
        # Установка значений полей в окне редактирования
         
            ui.fio.setText(self.tablearendators.item(selected_row, 0).text())
            ui.passport.setText(self.tablearendators.item(selected_row, 1).text())
            ui.iin.setText(self.tablearendators.item(selected_row, 2).text())
            ui.adress.setText(self.tablearendators.item(selected_row, 3).text())
            ui.phone.setText(self.tablearendators.item(selected_row, 4).text())
        
        # Установите значения для других полей в соответствии с их индексами столбцов

            edit_arendator.exec_()











    def retranslateUi(self, arendators):
        _translate = QtCore.QCoreApplication.translate
        arendators.setWindowTitle(_translate("arendators", "Арендаторы"))
        item = self.tablearendators.horizontalHeaderItem(0)
        item.setText(_translate("arendators", "ФИО"))
        item = self.tablearendators.horizontalHeaderItem(1)
        item.setText(_translate("arendators", "Паспорт,№"))
        item = self.tablearendators.horizontalHeaderItem(2)
        item.setText(_translate("arendators", "ИИН"))
        item = self.tablearendators.horizontalHeaderItem(3)
        item.setText(_translate("arendators", "Адрес"))
        item = self.tablearendators.horizontalHeaderItem(4)
        item.setText(_translate("arendators", "Телефон"))
        self.label.setText(_translate("arendators", "Список арендаторов"))
        self.deletebutton.setText(_translate("arendators", "Удалить"))
        self.addbutton.setText(_translate("arendators", "Добавить"))
        self.updatebutton.setText(_translate("arendators", "Обновить"))
        self.editbutton.setText(_translate("arendators", "Редактировать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    arendators = QtWidgets.QDialog()
    ui = Ui_arendators()
    ui.setupUi(arendators)
    arendators.show()
    sys.exit(app.exec_())