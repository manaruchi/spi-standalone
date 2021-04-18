# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spi_utility_point_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SPIUtilityDialogBase(object):
    def setupUi(self, SPIUtilityDialogBase):
        SPIUtilityDialogBase.setObjectName("SPIUtilityDialogBase")
        SPIUtilityDialogBase.resize(899, 489)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SPIUtilityDialogBase.sizePolicy().hasHeightForWidth())
        SPIUtilityDialogBase.setSizePolicy(sizePolicy)
        SPIUtilityDialogBase.setMinimumSize(QtCore.QSize(899, 489))
        SPIUtilityDialogBase.setMaximumSize(QtCore.QSize(899, 489))
        self.label_5 = QtWidgets.QLabel(SPIUtilityDialogBase)
        self.label_5.setGeometry(QtCore.QRect(16, 12, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.progressBar_1 = QtWidgets.QProgressBar(SPIUtilityDialogBase)
        self.progressBar_1.setGeometry(QtCore.QRect(410, 460, 481, 20))
        self.progressBar_1.setAutoFillBackground(False)
        self.progressBar_1.setStyleSheet("QProgressBar{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(0, 255, 127);\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}")
        self.progressBar_1.setProperty("value", 0)
        self.progressBar_1.setTextVisible(True)
        self.progressBar_1.setObjectName("progressBar_1")
        self.tabWidget = QtWidgets.QTabWidget(SPIUtilityDialogBase)
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 391, 421))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(16, 24))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 40, 231, 16))
        self.label.setObjectName("label")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_10.setGeometry(QtCore.QRect(20, 70, 321, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab)
        self.pushButton_11.setGeometry(QtCore.QRect(340, 70, 31, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 231, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_11.setGeometry(QtCore.QRect(20, 150, 321, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab)
        self.pushButton_12.setGeometry(QtCore.QRect(340, 150, 31, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab)
        self.pushButton_13.setGeometry(QtCore.QRect(150, 320, 101, 51))
        self.pushButton_13.setDefault(True)
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(270, 320, 101, 51))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 420, 481, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 410, 471, 16))
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(10, 440, 471, 16))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(30, 450, 481, 16))
        self.label_6.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_6.setObjectName("label_6")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(20, 50, 321, 31))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 49, 31, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(20, 24, 181, 16))
        self.label_22.setObjectName("label_22")
        self.comboBox_10 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_10.setGeometry(QtCore.QRect(112, 164, 221, 31))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(20, 171, 91, 16))
        self.label_7.setObjectName("label_7")
        self.comboBox_11 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_11.setGeometry(QtCore.QRect(112, 220, 121, 31))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_12 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_12.setGeometry(QtCore.QRect(112, 270, 121, 31))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(22, 274, 71, 20))
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(22, 227, 81, 16))
        self.label_11.setObjectName("label_11")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 340, 101, 41))
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_10.setGeometry(QtCore.QRect(340, 116, 31, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_16.setGeometry(QtCore.QRect(20, 116, 321, 31))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(20, 90, 181, 20))
        self.label_23.setObjectName("label_23")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(40, 440, 75, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(20, 440, 46, 13))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(20, 440, 46, 13))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_3, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(SPIUtilityDialogBase)
        self.tabWidget_2.setGeometry(QtCore.QRect(410, 60, 481, 391))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.textEdit_1 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_1.setGeometry(QtCore.QRect(10, 10, 461, 341))
        self.textEdit_1.setTabChangesFocus(True)
        self.textEdit_1.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textEdit_1.setReadOnly(True)
        self.textEdit_1.setObjectName("textEdit_1")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.comboBox = QtWidgets.QComboBox(self.tab_5)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 461, 31))
        self.comboBox.setObjectName("comboBox")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 50, 461, 301))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.label_13 = QtWidgets.QLabel(SPIUtilityDialogBase)
        self.label_13.setGeometry(QtCore.QRect(480, 580, 421, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(SPIUtilityDialogBase)
        self.label_14.setGeometry(QtCore.QRect(480, 600, 421, 16))
        self.label_14.setObjectName("label_14")
        self.tableWidget_2 = QtWidgets.QTableWidget(SPIUtilityDialogBase)
        self.tableWidget_2.setGeometry(QtCore.QRect(410, 550, 451, 341))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.tableWidget = QtWidgets.QTableWidget(SPIUtilityDialogBase)
        self.tableWidget.setGeometry(QtCore.QRect(-40, 600, 451, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)

        self.retranslateUi(SPIUtilityDialogBase)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SPIUtilityDialogBase)

    def retranslateUi(self, SPIUtilityDialogBase):
        _translate = QtCore.QCoreApplication.translate
        SPIUtilityDialogBase.setWindowTitle(_translate("SPIUtilityDialogBase", "SPI Utility for Point Data"))
        self.label_5.setText(_translate("SPIUtilityDialogBase", "Standardized Precipitation Index Utility for Point Data"))
        self.label.setText(_translate("SPIUtilityDialogBase", "Input Precipitation Data :"))
        self.lineEdit_10.setToolTip(_translate("SPIUtilityDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Input Precipitation Data Directory</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the folder where precipitation data is stored. The detailed format for the precipitation data can be found in the documentation.</p></body></html>"))
        self.pushButton_11.setToolTip(_translate("SPIUtilityDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Browse for folder..</p></body></html>"))
        self.pushButton_11.setText(_translate("SPIUtilityDialogBase", "..."))
        self.label_2.setText(_translate("SPIUtilityDialogBase", "Output Data Directory :"))
        self.lineEdit_11.setToolTip(_translate("SPIUtilityDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Output Data Directory</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the folder where all the outputs of all the operatons perfromed via this plugin will be stored. The exact path of each operation output will be displayed in the log.</p></body></html>"))
        self.pushButton_12.setToolTip(_translate("SPIUtilityDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Browse for folder..</p></body></html>"))
        self.pushButton_12.setText(_translate("SPIUtilityDialogBase", "..."))
        self.pushButton_13.setToolTip(_translate("SPIUtilityDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Check Data</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This option checks the presence of data in the user-provided Data Directory.</p></body></html>"))
        self.pushButton_13.setText(_translate("SPIUtilityDialogBase", "Load Data"))
        self.pushButton.setText(_translate("SPIUtilityDialogBase", "Generate\n"
"Composite"))
        self.label_3.setText(_translate("SPIUtilityDialogBase", "TextLabel"))
        self.label_4.setText(_translate("SPIUtilityDialogBase", "TextLabel"))
        self.label_8.setText(_translate("SPIUtilityDialogBase", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SPIUtilityDialogBase", "Data Preparation"))
        self.label_6.setToolTip(_translate("SPIUtilityDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Data Status</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Incomplete :</span> Input parameters are not set. Complete the Data Preparation step.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Complete :</span> Data Preparation is complete. The SPI can be generated now.</p></body></html>"))
        self.label_6.setText(_translate("SPIUtilityDialogBase", "Data Status : Incomplete"))
        self.pushButton_9.setText(_translate("SPIUtilityDialogBase", "..."))
        self.label_22.setText(_translate("SPIUtilityDialogBase", "Monthly composite file :"))
        self.comboBox_10.setItemText(0, _translate("SPIUtilityDialogBase", "1 month"))
        self.comboBox_10.setItemText(1, _translate("SPIUtilityDialogBase", "3 months"))
        self.comboBox_10.setItemText(2, _translate("SPIUtilityDialogBase", "4 months"))
        self.comboBox_10.setItemText(3, _translate("SPIUtilityDialogBase", "6 months"))
        self.comboBox_10.setItemText(4, _translate("SPIUtilityDialogBase", "9 months"))
        self.comboBox_10.setItemText(5, _translate("SPIUtilityDialogBase", "12 months"))
        self.comboBox_10.setItemText(6, _translate("SPIUtilityDialogBase", "24 months"))
        self.comboBox_10.setItemText(7, _translate("SPIUtilityDialogBase", "36 months"))
        self.label_7.setText(_translate("SPIUtilityDialogBase", "Time Scale : "))
        self.comboBox_11.setItemText(0, _translate("SPIUtilityDialogBase", "January"))
        self.comboBox_11.setItemText(1, _translate("SPIUtilityDialogBase", "February"))
        self.comboBox_11.setItemText(2, _translate("SPIUtilityDialogBase", "March"))
        self.comboBox_11.setItemText(3, _translate("SPIUtilityDialogBase", "April"))
        self.comboBox_11.setItemText(4, _translate("SPIUtilityDialogBase", "May"))
        self.comboBox_11.setItemText(5, _translate("SPIUtilityDialogBase", "June"))
        self.comboBox_11.setItemText(6, _translate("SPIUtilityDialogBase", "July"))
        self.comboBox_11.setItemText(7, _translate("SPIUtilityDialogBase", "August"))
        self.comboBox_11.setItemText(8, _translate("SPIUtilityDialogBase", "September"))
        self.comboBox_11.setItemText(9, _translate("SPIUtilityDialogBase", "October"))
        self.comboBox_11.setItemText(10, _translate("SPIUtilityDialogBase", "November"))
        self.comboBox_11.setItemText(11, _translate("SPIUtilityDialogBase", "December"))
        self.comboBox_12.setItemText(0, _translate("SPIUtilityDialogBase", "January"))
        self.comboBox_12.setItemText(1, _translate("SPIUtilityDialogBase", "February"))
        self.comboBox_12.setItemText(2, _translate("SPIUtilityDialogBase", "March"))
        self.comboBox_12.setItemText(3, _translate("SPIUtilityDialogBase", "April"))
        self.comboBox_12.setItemText(4, _translate("SPIUtilityDialogBase", "May"))
        self.comboBox_12.setItemText(5, _translate("SPIUtilityDialogBase", "June"))
        self.comboBox_12.setItemText(6, _translate("SPIUtilityDialogBase", "July"))
        self.comboBox_12.setItemText(7, _translate("SPIUtilityDialogBase", "August"))
        self.comboBox_12.setItemText(8, _translate("SPIUtilityDialogBase", "September"))
        self.comboBox_12.setItemText(9, _translate("SPIUtilityDialogBase", "October"))
        self.comboBox_12.setItemText(10, _translate("SPIUtilityDialogBase", "November"))
        self.comboBox_12.setItemText(11, _translate("SPIUtilityDialogBase", "December"))
        self.label_12.setText(_translate("SPIUtilityDialogBase", "End Month : "))
        self.label_11.setText(_translate("SPIUtilityDialogBase", "Start Month : "))
        self.pushButton_3.setText(_translate("SPIUtilityDialogBase", "Generate SPI"))
        self.pushButton_10.setText(_translate("SPIUtilityDialogBase", "..."))
        self.label_23.setText(_translate("SPIUtilityDialogBase", "Output folder :"))
        self.pushButton_8.setText(_translate("SPIUtilityDialogBase", "PushButton"))
        self.label_9.setText(_translate("SPIUtilityDialogBase", "TextLabel"))
        self.label_10.setText(_translate("SPIUtilityDialogBase", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SPIUtilityDialogBase", "SPI Calculation"))
        self.textEdit_1.setToolTip(_translate("SPIUtilityDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Log</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Log displays the current activities and notes which will be useful while usng this plugin.</p></body></html>"))
        self.textEdit_1.setHtml(_translate("SPIUtilityDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tahoma\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Start with setting Input Precipitation Data Folder (Folder containing precipitation data in *.csv format)  and Output Folder. Then click on </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:600;\">Check Data</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:600;\">Note </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">: The format of data in the CSV file should be like the following:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" align=\"center\" cellspacing=\"2\" cellpadding=\"5\">\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:600;\">Date</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:600;\">Point_1</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:600;\">Point_2</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:600;\">...</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">01-01-1990</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">10</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">18</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">...</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">02-01-1990</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">20</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">52</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">...</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">03-01-1990</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">15</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">22</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">...</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">...</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">...</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">...</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">...</span></p></td></tr></table>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:600;\">Note </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">: It is recommended that the output folder path should not have any subfolders and files.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#5500ff;\">For more information, refer the </span><a href=\"../Documentation.html\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; text-decoration: underline; color:#5500ff;\">Documentation</span></a><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#5500ff;\">.</span></p>\n"
"<hr /></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("SPIUtilityDialogBase", "Log"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("SPIUtilityDialogBase", "Date"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("SPIUtilityDialogBase", "Values"))
        self.label_13.setText(_translate("SPIUtilityDialogBase", "TextLabel"))
        self.label_14.setText(_translate("SPIUtilityDialogBase", "TextLabel"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("SPIUtilityDialogBase", "Date"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SPIUtilityDialogBase", "Date"))
