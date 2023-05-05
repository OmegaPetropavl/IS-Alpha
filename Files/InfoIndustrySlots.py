from InfoIndustry import Ui_w_InfoIndustry
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QTableWidgetItem, QFileDialog
import mysql.connector
import csv

class InfoIndustry(QtWidgets.QMainWindow, Ui_w_InfoIndustry):
    def __init__(self, DBINSTANCE):
            super().__init__()
            self.setupUi(self)
            self.DBINST = DBINSTANCE
            self.tw_ViewIndustry
            self.btn_GetData.clicked.connect(self.GetEnterpriseInfo)
            self.btn_SaveData.clicked.connect(self.SaveToFile)
            self.tw_ViewIndustry.itemChanged.connect(self.UpdateData)
            self.tw_ViewIndustry.itemSelectionChanged.connect(self.GetPrevuiosValue)
            self.selectedRow = ""

    def GetPrevuiosValue(self):
        print(f"Прежнее значение: {self.tw_ViewIndustry.currentItem().text()}")
        cursor1 = self.DBINST.cursor()
        cursor1.execute( f"SELECT Industry_ID FROM test.industry where Industry_Name = '{self.tw_ViewIndustry.currentItem().text()}'")
        self.selectedRow = cursor1.fetchone()
        print(self.selectedRow)
        print(f"его ID: {self.selectedRow[0]}")
        cursor1.close()

    def UpdateData(self):
        currentRow=self.tw_ViewIndustry.currentRow()
        currentColumn=self.tw_ViewIndustry.currentColumn()

        if currentRow>=0:
            newData = self.tw_ViewIndustry.item(currentRow,currentColumn).text();
            print(f"Выбрана строка {currentRow}: {self.tw_ViewIndustry.item(currentRow,currentColumn).text()}")
            cursor = self.DBINST.cursor()
            cursor.execute(f"UPDATE test.industry SET Industry_Name = '{newData}' WHERE (Industry_ID = '{int(self.selectedRow[0])}');")
            self.DBINST.commit()
            self.statusBar().showMessage(f"Данные успешно обновлены! ID:{self.selectedRow[0]} значение: {newData}",3000)

            cursor.close()


    def GetEnterpriseInfo(self):
        infoFromDB = self.SendQueryAllEnterprises(self.DBINST)
        self.statusBar().showMessage(f"Найдено результатов: {infoFromDB.rowcount}",3000)
    
    
    def SendQueryAllEnterprises(self,dbInstance):
        
        cursor = dbInstance.cursor()
        cursor.execute("SELECT * FROM test.industry;")
        columns = []
        row = cursor.fetchone()
        rowCount = 0
        #вычисление количества строк из запроса и создание массива со значениями для ячеек
        while row is not None:
             columns.append(QTableWidgetItem(str(row[0])).setFlags(QtCore.ItemIsEditable))
             columns.append(QTableWidgetItem(row[1]))
             rowCount+=1
             print(row)
             row=cursor.fetchone()
        cursor.close()
        self.tw_ViewIndustry.setRowCount(rowCount)
        row = 0
        col = 0
        for j in columns:
            if col==2:
                col=0
                row+=1
            self.tw_ViewIndustry.setItem(row,col,j)
            col+=1

        print("Успешно выведено")
        return cursor
    
    def SaveToFile(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "CSV (*.csv)")
        if filename:
            self.CollectFromQTW(filename=filename)
        self.statusBar().showMessage(f"Данные успешно сохранены в файл: {filename}",3000)


    def CollectFromQTW(self,filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in range(self.tw_ViewIndustry.rowCount()):
                row_data = []
                for column in range(self.tw_ViewIndustry.columnCount()):
                    item = self.tw_ViewIndustry.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                writer.writerow(row_data)