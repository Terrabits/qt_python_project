# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(488, 242)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ipAddressLabel = QLabel(self.widget_2)
        self.ipAddressLabel.setObjectName(u"ipAddressLabel")

        self.gridLayout.addWidget(self.ipAddressLabel, 0, 0, 1, 1)

        self.ipAddress = QLineEdit(self.widget_2)
        self.ipAddress.setObjectName(u"ipAddress")

        self.gridLayout.addWidget(self.ipAddress, 0, 1, 1, 1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.idString = QLineEdit(self.widget_2)
        self.idString.setObjectName(u"idString")
        self.idString.setReadOnly(True)

        self.gridLayout.addWidget(self.idString, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.verticalSpacer = QSpacerItem(20, 23, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(315, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button = QPushButton(self.widget)
        self.button.setObjectName(u"button")

        self.horizontalLayout.addWidget(self.button)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 488, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ipAddressLabel.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID String", None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"Get ID String", None))
    # retranslateUi

