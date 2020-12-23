# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'questions_test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(521, 420)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 40, 112, 23))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 80, 112, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 120, 112, 23))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 160, 112, 23))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(240, 40, 112, 23))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_6.setGeometry(QtCore.QRect(240, 80, 112, 23))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_7.setGeometry(QtCore.QRect(240, 120, 112, 23))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_8.setGeometry(QtCore.QRect(240, 160, 112, 23))
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Вопрос: ... ?"))
        self.radioButton.setText(_translate("Form", "Ответ"))
        self.radioButton_2.setText(_translate("Form", "Ответ"))
        self.radioButton_3.setText(_translate("Form", "Ответ"))
        self.radioButton_4.setText(_translate("Form", "Ответ"))
        self.radioButton_5.setText(_translate("Form", "Ответ"))
        self.radioButton_6.setText(_translate("Form", "Ответ"))
        self.radioButton_7.setText(_translate("Form", "Ответ"))
        self.radioButton_8.setText(_translate("Form", "Ответ"))
        self.pushButton.setText(_translate("Form", "Предыдущий вопрос"))
        self.pushButton_2.setText(_translate("Form", "Следующий вопрос"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
