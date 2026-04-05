# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pwd.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_InputPwdForm(object):
    def setupUi(self, InputPwdForm):
        if not InputPwdForm.objectName():
            InputPwdForm.setObjectName(u"InputPwdForm")
        InputPwdForm.resize(256, 106)
        self.label = QLabel(InputPwdForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 201, 21))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(InputPwdForm)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 70, 75, 24))
        self.lineEdit = QLineEdit(InputPwdForm)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 40, 221, 21))
        self.pushButton_2 = QPushButton(InputPwdForm)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(40, 70, 75, 24))

        self.retranslateUi(InputPwdForm)

        QMetaObject.connectSlotsByName(InputPwdForm)
    # setupUi

    def retranslateUi(self, InputPwdForm):
        InputPwdForm.setWindowTitle(QCoreApplication.translate("InputPwdForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("InputPwdForm", u"Please Entry Password in lineEdit.", None))
        self.pushButton.setText(QCoreApplication.translate("InputPwdForm", u"Confirm", None))
        self.pushButton_2.setText(QCoreApplication.translate("InputPwdForm", u"Cancel", None))
    # retranslateUi

