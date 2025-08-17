# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
)
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
)


class Ui_MainView(object):
    def setupUi(self, MainView):
        if not MainView.objectName():
            MainView.setObjectName("MainView")
        MainView.resize(897, 508)
        self.verticalLayout = QVBoxLayout(MainView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.canvas = QLabel(MainView)
        self.canvas.setObjectName("canvas")

        self.verticalLayout.addWidget(self.canvas)

        self.retranslateUi(MainView)

        QMetaObject.connectSlotsByName(MainView)

    # setupUi

    def retranslateUi(self, MainView):
        MainView.setWindowTitle(QCoreApplication.translate("MainView", "Dialog", None))
        self.canvas.setText("")

    # retranslateUi
