# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_manage_sources.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(854, 421)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lw_sources = QListWidget(Dialog)
        self.lw_sources.setObjectName(u"lw_sources")
        self.lw_sources.setAlternatingRowColors(True)
        self.lw_sources.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.lw_sources)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_add = QPushButton(self.groupBox)
        self.pb_add.setObjectName(u"pb_add")

        self.horizontalLayout.addWidget(self.pb_add)

        self.pb_delete = QPushButton(self.groupBox)
        self.pb_delete.setObjectName(u"pb_delete")

        self.horizontalLayout.addWidget(self.pb_delete)

        self.horizontalSpacer_3 = QSpacerItem(565, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pb_close = QPushButton(self.groupBox)
        self.pb_close.setObjectName(u"pb_close")

        self.horizontalLayout.addWidget(self.pb_close)


        self.horizontalLayout_2.addWidget(self.groupBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle("")
        self.pb_add.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.pb_delete.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.pb_close.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi

