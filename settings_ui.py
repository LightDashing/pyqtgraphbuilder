# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.ApplicationModal)
        Form.resize(245, 250)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.xmax = QLineEdit(Form)
        self.xmax.setObjectName(u"xmax")
        self.xmax.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.xmax, 2, 3, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.xmin = QLineEdit(Form)
        self.xmin.setObjectName(u"xmin")
        self.xmin.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.xmin, 1, 3, 1, 1)

        self.ymin = QLineEdit(Form)
        self.ymin.setObjectName(u"ymin")
        self.ymin.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.ymin, 3, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 6, 4, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.ymax = QLineEdit(Form)
        self.ymax.setObjectName(u"ymax")
        self.ymax.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.ymax, 4, 3, 1, 1)

        self.step = QLineEdit(Form)
        self.step.setObjectName(u"step")
        self.step.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.step, 0, 3, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.auto_ch = QCheckBox(Form)
        self.auto_ch.setObjectName(u"auto_ch")

        self.gridLayout.addWidget(self.auto_ch, 4, 4, 1, 1)

        self.save_b = QPushButton(Form)
        self.save_b.setObjectName(u"save_b")

        self.gridLayout.addWidget(self.save_b, 8, 3, 1, 1)

        self.reset = QPushButton(Form)
        self.reset.setObjectName(u"reset")

        self.gridLayout.addWidget(self.reset, 6, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Settings", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Y_min", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"X_max", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0428\u0430\u0433", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"X_min", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Y_max", None))
        self.auto_ch.setText(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e", None))
        self.save_b.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.reset.setText(QCoreApplication.translate("Form", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
    # retranslateUi

