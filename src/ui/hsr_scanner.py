# Form implementation generated from reading ui file '.\hsr-scanner.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        MainWindow.setMaximumSize(QtCore.QSize(700, 500))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 681, 481))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(130, 20, 111, 91))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.spinBox = QtWidgets.QSpinBox(parent=self.formLayoutWidget_2)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(5)
        self.spinBox.setProperty("value", 3)
        self.spinBox.setObjectName("spinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinBox)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.formLayoutWidget_2)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(80)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinBox_2)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_2)
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 91, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.checkBoxScanLightCones = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        self.checkBoxScanLightCones.setObjectName("checkBoxScanLightCones")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.checkBoxScanLightCones)
        self.checkBoxScanRelics = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        self.checkBoxScanRelics.setObjectName("checkBoxScanRelics")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.checkBoxScanRelics)
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.checkBoxScanChars = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        self.checkBoxScanChars.setObjectName("checkBoxScanChars")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.checkBoxScanChars)
        self.buttonStartScan = QtWidgets.QPushButton(parent=self.tab)
        self.buttonStartScan.setGeometry(QtCore.QRect(20, 390, 121, 41))
        self.buttonStartScan.setObjectName("buttonStartScan")
        self.formLayoutWidget_3 = QtWidgets.QWidget(parent=self.tab)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(260, 20, 111, 91))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(5)
        self.spinBox_3.setProperty("value", 3)
        self.spinBox_3.setObjectName("spinBox_3")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinBox_3)
        self.label_7 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.spinBox_4 = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(80)
        self.spinBox_4.setObjectName("spinBox_4")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spinBox_4)
        self.label_8 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_8)
        self.log = QtWidgets.QPlainTextEdit(parent=self.tab)
        self.log.setGeometry(QtCore.QRect(20, 140, 351, 231))
        self.log.setReadOnly(True)
        self.log.setObjectName("log")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_4 = QtWidgets.QWidget(parent=self.tab_2)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 160, 80))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_9 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_9.setObjectName("label_9")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget_4)
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.label_10 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.formLayoutWidget_4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HSR Scanner"))
        self.label_3.setText(_translate("MainWindow", "Min Rarity"))
        self.label_4.setText(_translate("MainWindow", "Min Level"))
        self.label_2.setText(_translate("MainWindow", "Light Cone options"))
        self.checkBoxScanLightCones.setText(_translate("MainWindow", "Light Cones"))
        self.checkBoxScanRelics.setText(_translate("MainWindow", "Relics"))
        self.label.setText(_translate("MainWindow", "Items to scan"))
        self.checkBoxScanChars.setText(_translate("MainWindow", "Characters"))
        self.buttonStartScan.setText(_translate("MainWindow", "Start Scan"))
        self.label_6.setText(_translate("MainWindow", "Min Rarity"))
        self.label_7.setText(_translate("MainWindow", "Min Level"))
        self.label_8.setText(_translate("MainWindow", "Relic options"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Scan"))
        self.label_9.setText(_translate("MainWindow", "Inventory Key"))
        self.lineEdit.setText(_translate("MainWindow", "B"))
        self.label_10.setText(_translate("MainWindow", "Characters Key"))
        self.lineEdit_2.setText(_translate("MainWindow", "C"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Configure"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
