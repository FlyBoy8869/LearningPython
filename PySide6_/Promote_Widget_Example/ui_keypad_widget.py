# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keypad_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_keypad(object):
    def setupUi(self, keypad):
        if not keypad.objectName():
            keypad.setObjectName(u"keypad")
        keypad.resize(200, 200)
        keypad.setMinimumSize(QSize(150, 150))
        keypad.setMaximumSize(QSize(200, 200))
        self.verticalLayout = QVBoxLayout(keypad)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.readout = QLabel(keypad)
        self.readout.setObjectName(u"readout")
        self.readout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.readout)

        self.gridLayout = QGridLayout()
#ifndef Q_OS_MAC
        self.gridLayout.setSpacing(-1)
#endif
        self.gridLayout.setObjectName(u"gridLayout")
        self.tb_seven = QToolButton(keypad)
        self.tb_seven.setObjectName(u"tb_seven")

        self.gridLayout.addWidget(self.tb_seven, 0, 0, 1, 1)

        self.tb_eight = QToolButton(keypad)
        self.tb_eight.setObjectName(u"tb_eight")

        self.gridLayout.addWidget(self.tb_eight, 0, 1, 1, 1)

        self.tb_nine = QToolButton(keypad)
        self.tb_nine.setObjectName(u"tb_nine")

        self.gridLayout.addWidget(self.tb_nine, 0, 2, 1, 1)

        self.tb_four = QToolButton(keypad)
        self.tb_four.setObjectName(u"tb_four")

        self.gridLayout.addWidget(self.tb_four, 1, 0, 1, 1)

        self.tb_five = QToolButton(keypad)
        self.tb_five.setObjectName(u"tb_five")

        self.gridLayout.addWidget(self.tb_five, 1, 1, 1, 1)

        self.tb_six = QToolButton(keypad)
        self.tb_six.setObjectName(u"tb_six")

        self.gridLayout.addWidget(self.tb_six, 1, 2, 1, 1)

        self.tb_one = QToolButton(keypad)
        self.tb_one.setObjectName(u"tb_one")

        self.gridLayout.addWidget(self.tb_one, 2, 0, 1, 1)

        self.tb_two = QToolButton(keypad)
        self.tb_two.setObjectName(u"tb_two")

        self.gridLayout.addWidget(self.tb_two, 2, 1, 1, 1)

        self.tb_three = QToolButton(keypad)
        self.tb_three.setObjectName(u"tb_three")

        self.gridLayout.addWidget(self.tb_three, 2, 2, 1, 1)

        self.tb_zero = QToolButton(keypad)
        self.tb_zero.setObjectName(u"tb_zero")

        self.gridLayout.addWidget(self.tb_zero, 3, 0, 1, 1)

        self.tb_decimal_point = QToolButton(keypad)
        self.tb_decimal_point.setObjectName(u"tb_decimal_point")

        self.gridLayout.addWidget(self.tb_decimal_point, 3, 1, 1, 1)

        self.tb_backspace = QToolButton(keypad)
        self.tb_backspace.setObjectName(u"tb_backspace")

        self.gridLayout.addWidget(self.tb_backspace, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(keypad)

        QMetaObject.connectSlotsByName(keypad)
    # setupUi

    def retranslateUi(self, keypad):
        keypad.setWindowTitle(QCoreApplication.translate("keypad", u"Frame", None))
        self.readout.setText(QCoreApplication.translate("keypad", u"Frequency", None))
        self.tb_seven.setText(QCoreApplication.translate("keypad", u"7", None))
        self.tb_eight.setText(QCoreApplication.translate("keypad", u"8", None))
        self.tb_nine.setText(QCoreApplication.translate("keypad", u"9", None))
        self.tb_four.setText(QCoreApplication.translate("keypad", u"4", None))
        self.tb_five.setText(QCoreApplication.translate("keypad", u"5", None))
        self.tb_six.setText(QCoreApplication.translate("keypad", u"6", None))
        self.tb_one.setText(QCoreApplication.translate("keypad", u"1", None))
        self.tb_two.setText(QCoreApplication.translate("keypad", u"2", None))
        self.tb_three.setText(QCoreApplication.translate("keypad", u"3", None))
        self.tb_zero.setText(QCoreApplication.translate("keypad", u"0", None))
        self.tb_decimal_point.setText(QCoreApplication.translate("keypad", u".", None))
        self.tb_backspace.setText(QCoreApplication.translate("keypad", u"<-", None))
    # retranslateUi

