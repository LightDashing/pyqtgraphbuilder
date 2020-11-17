# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(644, 514)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 4, 1, 1)

        self.settings_b = QPushButton(self.centralwidget)
        self.settings_b.setObjectName(u"settings_b")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.settings_b.sizePolicy().hasHeightForWidth())
        self.settings_b.setSizePolicy(sizePolicy1)
        self.settings_b.setMinimumSize(QSize(20, 15))

        self.gridLayout.addWidget(self.settings_b, 4, 2, 1, 5)

        self.limit1 = QLineEdit(self.centralwidget)
        self.limit1.setObjectName(u"limit1")
        self.limit1.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.limit1, 2, 3, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        self.graph_plot = PlotWidget(self.centralwidget)
        self.graph_plot.setObjectName(u"graph_plot")
        sizePolicy1.setHeightForWidth(self.graph_plot.sizePolicy().hasHeightForWidth())
        self.graph_plot.setSizePolicy(sizePolicy1)
        self.graph_plot.setMinimumSize(QSize(250, 250))

        self.gridLayout.addWidget(self.graph_plot, 0, 0, 1, 7)

        self.limit2 = QLineEdit(self.centralwidget)
        self.limit2.setObjectName(u"limit2")
        self.limit2.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.limit2, 2, 5, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 6, 1, 1)

        self.function_inp = QLineEdit(self.centralwidget)
        self.function_inp.setObjectName(u"function_inp")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.function_inp.sizePolicy().hasHeightForWidth())
        self.function_inp.setSizePolicy(sizePolicy2)
        self.function_inp.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.function_inp, 1, 3, 1, 4)

        self.graph_list = QListWidget(self.centralwidget)
        self.graph_list.setObjectName(u"graph_list")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.graph_list.sizePolicy().hasHeightForWidth())
        self.graph_list.setSizePolicy(sizePolicy3)
        self.graph_list.setMaximumSize(QSize(16777215, 130))

        self.gridLayout.addWidget(self.graph_list, 1, 0, 4, 2)

        self.add_graph_button = QPushButton(self.centralwidget)
        self.add_graph_button.setObjectName(u"add_graph_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.add_graph_button.sizePolicy().hasHeightForWidth())
        self.add_graph_button.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.add_graph_button, 3, 2, 1, 2)

        self.delete_graph_button = QPushButton(self.centralwidget)
        self.delete_graph_button.setObjectName(u"delete_graph_button")

        self.gridLayout.addWidget(self.delete_graph_button, 3, 4, 1, 3)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setColumnStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GraphBuilder", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"] [", None))
        self.settings_b.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"y  =", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"x \u2208 [", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"]", None))
#if QT_CONFIG(tooltip)
        self.function_inp.setToolTip(QCoreApplication.translate("MainWindow", u"\u0432\u0444\u0446\u0432\u0446\u0444", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.function_inp.setStatusTip(QCoreApplication.translate("MainWindow", u"\u0432\u0446\u0444\u0432\u0446\u0444\u0432\u0444\u0446", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.function_inp.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u0432\u0444\u0446\u0432\u0444", None))
#endif // QT_CONFIG(whatsthis)
        self.function_inp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0444\u0443\u043d\u043a\u0446\u0438\u044e", None))
        self.add_graph_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_graph_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

