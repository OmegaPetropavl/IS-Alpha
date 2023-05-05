# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 471)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_7 = QAction(MainWindow)
        self.action_7.setObjectName(u"action_7")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName(u"action_8")
        self.action_9 = QAction(MainWindow)
        self.action_9.setObjectName(u"action_9")
        self.action_10 = QAction(MainWindow)
        self.action_10.setObjectName(u"action_10")
        self.action_11 = QAction(MainWindow)
        self.action_11.setObjectName(u"action_11")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_12 = QAction(MainWindow)
        self.action_12.setObjectName(u"action_12")
        self.action_13 = QAction(MainWindow)
        self.action_13.setObjectName(u"action_13")
        self.action_14 = QAction(MainWindow)
        self.action_14.setObjectName(u"action_14")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 641, 571))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 511, 451))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 22))
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_2 = QMenu(self.menu_3)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_6 = QMenu(self.menu_3)
        self.menu_6.setObjectName(u"menu_6")
        self.menu_7 = QMenu(self.menu_3)
        self.menu_7.setObjectName(u"menu_7")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu = QMenu(self.menu_4)
        self.menu.setObjectName(u"menu")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menu_3.addAction(self.menu_7.menuAction())
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.menu_2.menuAction())
        self.menu_3.addAction(self.menu_6.menuAction())
        self.menu_2.addAction(self.action_9)
        self.menu_6.addAction(self.action_10)
        self.menu_7.addAction(self.action_11)
        self.menu_7.addAction(self.action_14)
        self.menu_7.addAction(self.action_4)
        self.menu_4.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_5)
        self.menu.addAction(self.action_12)
        self.menu.addAction(self.action_13)
        self.menu_5.addAction(self.action_7)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0418\u0421 \"\u0410\u0440\u0435\u043d\u0434\u0430 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u0439\"", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0434\u043e\u0433\u043e\u0432\u043e\u0440...", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0434\u043e\u0433\u043e\u0432\u043e\u0440...", None))
        self.action_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u0445...", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u043e\u0433\u043e\u0432\u043e\u0440...", None))
        self.action_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c...", None))
        self.action_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c...", None))
        self.action_11.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c...", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c...", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c...", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e\u0432\u0430\u044f \u0441\u0443\u043c\u043c\u0430 \u043e\u043f\u043b\u0430\u0442", None))
        self.action_12.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430 \u0430\u0440\u0435\u043d\u0434\u0430\u0442\u043e\u0440\u043e\u0432", None))
        self.action_13.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u0439", None))
        self.action_14.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c...", None))
        self.label.setText("")
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0438", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0435\u043d\u0434\u0430\u0442\u043e\u0440\u044b", None))
        self.menu_6.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044a\u0435\u043a\u0442\u044b", None))
        self.menu_7.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u044b", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442...", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
    # retranslateUi

