# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress_widget.ui'
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
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)


class Ui_ProgressWidget(object):
    def setupUi(self, ProgressWidget):
        if not ProgressWidget.objectName():
            ProgressWidget.setObjectName("ProgressWidget")
        ProgressWidget.resize(296, 82)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProgressWidget.sizePolicy().hasHeightForWidth())
        ProgressWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(ProgressWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(ProgressWidget)
        self.label.setObjectName("label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_terminate = QPushButton(ProgressWidget)
        self.pb_terminate.setObjectName("pb_terminate")

        self.horizontalLayout.addWidget(self.pb_terminate)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.progress_bar = QProgressBar(ProgressWidget)
        self.progress_bar.setObjectName("progress_bar")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.progress_bar.sizePolicy().hasHeightForWidth()
        )
        self.progress_bar.setSizePolicy(sizePolicy1)
        self.progress_bar.setValue(24)

        self.verticalLayout.addWidget(self.progress_bar)

        self.retranslateUi(ProgressWidget)

        QMetaObject.connectSlotsByName(ProgressWidget)

    # setupUi

    def retranslateUi(self, ProgressWidget):
        ProgressWidget.setWindowTitle(
            QCoreApplication.translate("ProgressWidget", "Form", None)
        )
        self.label.setText(
            QCoreApplication.translate("ProgressWidget", "TextLabel", None)
        )
        self.pb_terminate.setText(
            QCoreApplication.translate("ProgressWidget", "X", None)
        )

    # retranslateUi
