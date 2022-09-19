# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myGui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextBrowser, QToolButton,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setMinimumSize(QSize(800, 600))
        mainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 30))
        self.pushButton_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.pushButton_3, 2, 4, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 8)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(0, 30))
        self.checkBox_2.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)

        self.gridLayout.addWidget(self.checkBox_2, 2, 2, 1, 1)

        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(0, 20))
        self.toolButton.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.toolButton, 0, 7, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.pushButton, 2, 6, 1, 2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(0, 20))
        self.lineEdit.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 6)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 20))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 7)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(0, 30))
        self.checkBox.setMaximumSize(QSize(16777215, 30))
        self.checkBox.setFont(font)

        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(30, 30))
        self.pushButton_2.setMaximumSize(QSize(30, 30))

        self.gridLayout.addWidget(self.pushButton_2, 2, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"ALWS", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.pushButton_3.setText(QCoreApplication.translate("mainWindow", u"\u66f4\u65b0\u94fe\u63a5\u5e93", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"WIKI\u7f51\u5740", None))
        self.checkBox_2.setText(QCoreApplication.translate("mainWindow", u"\u753b\u5e08\u540c\u4eba\u8d3a\u56fe", None))
        self.toolButton.setText(QCoreApplication.translate("mainWindow", u"...", None))
        self.pushButton.setText("")
        self.checkBox.setText(QCoreApplication.translate("mainWindow", u"\u80cc\u666f\u58c1\u7eb8\u63d2\u753b", None))
        self.pushButton_2.setText("")
    # retranslateUi

