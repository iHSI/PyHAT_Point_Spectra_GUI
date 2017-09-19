# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\ui\CrossValidation.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupLayout = QtWidgets.QGroupBox(Form)
        self.groupLayout.setObjectName("groupLayout")
        self.gridLayout = QtWidgets.QGridLayout(self.groupLayout)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.chooseDataLabel = QtWidgets.QLabel(self.groupLayout)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.horizontalLayout_3.addWidget(self.chooseDataLabel)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupLayout)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.horizontalLayout_3.addWidget(self.chooseDataComboBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.xVariableLabel = QtWidgets.QLabel(self.groupLayout)
        self.xVariableLabel.setObjectName("xVariableLabel")
        self.gridLayout.addWidget(self.xVariableLabel, 1, 0, 1, 1)
        self.yVariableLabel = QtWidgets.QLabel(self.groupLayout)
        self.yVariableLabel.setObjectName("yVariableLabel")
        self.gridLayout.addWidget(self.yVariableLabel, 1, 1, 1, 1)
        self.xVariableList = QtWidgets.QListWidget(self.groupLayout)
        self.xVariableList.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xVariableList.sizePolicy().hasHeightForWidth())
        self.xVariableList.setSizePolicy(sizePolicy)
        self.xVariableList.setMinimumSize(QtCore.QSize(0, 0))
        self.xVariableList.setMaximumSize(QtCore.QSize(900, 16777215))
        self.xVariableList.setObjectName("xVariableList")
        item = QtWidgets.QListWidgetItem()
        self.xVariableList.addItem(item)
        self.gridLayout.addWidget(self.xVariableList, 2, 0, 1, 1)
        self.yVariableList = QtWidgets.QListWidget(self.groupLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yVariableList.sizePolicy().hasHeightForWidth())
        self.yVariableList.setSizePolicy(sizePolicy)
        self.yVariableList.setMinimumSize(QtCore.QSize(0, 0))
        self.yVariableList.setMaximumSize(QtCore.QSize(900, 16777215))
        self.yVariableList.setObjectName("yVariableList")
        item = QtWidgets.QListWidgetItem()
        self.yVariableList.addItem(item)
        self.gridLayout.addWidget(self.yVariableList, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chooseAlgorithmLabel = QtWidgets.QLabel(self.groupLayout)
        self.chooseAlgorithmLabel.setObjectName("chooseAlgorithmLabel")
        self.horizontalLayout_2.addWidget(self.chooseAlgorithmLabel)
        self.chooseAlgorithmComboBox = QtWidgets.QComboBox(self.groupLayout)
        self.chooseAlgorithmComboBox.setObjectName("chooseAlgorithmComboBox")
        self.horizontalLayout_2.addWidget(self.chooseAlgorithmComboBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yMinLabel = QtWidgets.QLabel(self.groupLayout)
        self.yMinLabel.setObjectName("yMinLabel")
        self.horizontalLayout.addWidget(self.yMinLabel)
        self.yMinDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupLayout)
        self.yMinDoubleSpinBox.setObjectName("yMinDoubleSpinBox")
        self.horizontalLayout.addWidget(self.yMinDoubleSpinBox)
        self.yMaxLabel = QtWidgets.QLabel(self.groupLayout)
        self.yMaxLabel.setObjectName("yMaxLabel")
        self.horizontalLayout.addWidget(self.yMaxLabel)
        self.yMaxDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupLayout)
        self.yMaxDoubleSpinBox.setObjectName("yMaxDoubleSpinBox")
        self.horizontalLayout.addWidget(self.yMaxDoubleSpinBox)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.algorithmLayout = QtWidgets.QVBoxLayout()
        self.algorithmLayout.setObjectName("algorithmLayout")
        self.gridLayout.addLayout(self.algorithmLayout, 4, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.groupLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupLayout.setTitle(_translate("Form", "Cross Validation / Training"))
        self.chooseDataLabel.setText(_translate("Form", "Choose Data"))
        self.xVariableLabel.setText(_translate("Form", "X Variable"))
        self.yVariableLabel.setText(_translate("Form", "Y Variable"))
        __sortingEnabled = self.xVariableList.isSortingEnabled()
        self.xVariableList.setSortingEnabled(False)
        item = self.xVariableList.item(0)
        item.setText(_translate("Form", "Choose X"))
        self.xVariableList.setSortingEnabled(__sortingEnabled)
        self.yVariableList.setSortingEnabled(True)
        __sortingEnabled = self.yVariableList.isSortingEnabled()
        self.yVariableList.setSortingEnabled(False)
        item = self.yVariableList.item(0)
        item.setText(_translate("Form", "Choose Y"))
        self.yVariableList.setSortingEnabled(__sortingEnabled)
        self.chooseAlgorithmLabel.setText(_translate("Form", "Choose Algorithm"))
        self.yMinLabel.setText(_translate("Form", "Y Min"))
        self.yMaxLabel.setText(_translate("Form", "Y Max"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

