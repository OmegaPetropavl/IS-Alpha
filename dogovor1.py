# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dogovor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 606)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(140, 30, 381, 511))
        self.widget.setAutoFillBackground(True)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 90, 151, 20))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 130, 141, 20))
        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(190, 90, 151, 22))
        self.comboBox_2 = QComboBox(self.widget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(190, 130, 151, 22))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 170, 151, 20))
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 210, 151, 20))
        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(190, 210, 151, 22))
        self.dateEdit_2 = QDateEdit(self.widget)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(190, 170, 151, 22))
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 250, 141, 20))
        self.dateEdit_3 = QDateEdit(self.widget)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setGeometry(QRect(190, 250, 151, 22))
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 290, 141, 16))
        self.dateEdit_4 = QDateEdit(self.widget)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setGeometry(QRect(190, 290, 151, 22))
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 330, 141, 20))
        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(-260, 420, 621, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(190, 330, 151, 20))
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 50, 151, 20))
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(190, 50, 151, 20))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u043e\u0440 \u0430\u0440\u0435\u043d\u0434\u0430\u0442\u043e\u0440\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u043e\u0440 \u043e\u0431\u044a\u0435\u043a\u0442\u0430:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u0430\u0440\u0435\u043d\u0434\u044b:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0430\u0440\u0435\u043d\u0434\u044b:", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0435\u0436\u0435\u043c\u0435\u0441\u044f\u0447\u043d\u043e\u0439 \u043e\u043f\u043b\u0430\u0442\u044b:", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u0441\u044f\u0447\u043d\u0430\u044f \u0430\u0440\u0435\u043d\u0434\u043d\u0430\u044f \u043f\u043b\u0430\u0442\u0430:", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440 \u2116:", None))
    # retranslateUi

