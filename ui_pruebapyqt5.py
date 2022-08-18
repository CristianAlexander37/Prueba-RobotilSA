# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pruebapyqt5mCdJfZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icono_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(838, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblHora = QLabel(self.centralwidget)
        self.lblHora.setObjectName(u"lblHora")
        self.lblHora.setGeometry(QRect(210, 60, 151, 41))
        font = QFont()
        font.setPointSize(16)
        self.lblHora.setFont(font)
        self.lblFecha = QLabel(self.centralwidget)
        self.lblFecha.setObjectName(u"lblFecha")
        self.lblFecha.setGeometry(QRect(470, 60, 201, 41))
        self.lblFecha.setFont(font)
        self.lbl1 = QLabel(self.centralwidget)
        self.lbl1.setObjectName(u"lbl1")
        self.lbl1.setGeometry(QRect(140, 60, 61, 41))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.lbl1.setFont(font1)
        self.lbl2 = QLabel(self.centralwidget)
        self.lbl2.setObjectName(u"lbl2")
        self.lbl2.setGeometry(QRect(390, 60, 61, 41))
        self.lbl2.setFont(font)
        self.btnConsultar = QPushButton(self.centralwidget)
        self.btnConsultar.setObjectName(u"btnConsultar")
        self.btnConsultar.setGeometry(QRect(530, 260, 181, 71))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.btnConsultar.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icon/consultar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnConsultar.setIcon(icon)
        self.btnConsultar.setIconSize(QSize(30, 30))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(130, 170, 321, 321))
        font3 = QFont()
        font3.setPointSize(13)
        self.listWidget.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 838, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PostulanteparaROBOTILSA S.A", None))
        self.lblHora.setText(QCoreApplication.translate("MainWindow", u"hh:mm:ss", None))
        self.lblFecha.setText(QCoreApplication.translate("MainWindow", u"dd/mm/yy", None))
        self.lbl1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#550000;\">Hora:</span></p></body></html>", None))
        self.lbl2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#550000;\">Fecha:</span></p></body></html>", None))
        self.btnConsultar.setText(QCoreApplication.translate("MainWindow", u"  REQUEST", None))
    # retranslateUi

