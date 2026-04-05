# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_pwd.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(385, 94)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 61, 16))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 30, 351, 23))
        self.AppendPasswordButton = QPushButton(self.centralwidget)
        self.AppendPasswordButton.setObjectName(u"AppendPasswordButton")
        self.AppendPasswordButton.setGeometry(QRect(260, 60, 111, 24))
        self.SetPasswordButton = QPushButton(self.centralwidget)
        self.SetPasswordButton.setObjectName(u"SetPasswordButton")
        self.SetPasswordButton.setGeometry(QRect(140, 60, 111, 24))
        self.CancelButton = QPushButton(self.centralwidget)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.setGeometry(QRect(20, 60, 111, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Create a Password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.AppendPasswordButton.setText(QCoreApplication.translate("MainWindow", u"Append Password", None))
        self.SetPasswordButton.setText(QCoreApplication.translate("MainWindow", u"Set Password", None))
        self.CancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

