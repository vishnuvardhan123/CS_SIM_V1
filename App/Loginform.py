# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Loginform.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(476, 333)
        Login.setToolTip("")
        self.layoutWidget = QtWidgets.QWidget(Login)
        self.layoutWidget.setGeometry(QtCore.QRect(260, 200, 158, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.OK_PB = QtWidgets.QPushButton(self.layoutWidget)
        self.OK_PB.setObjectName("OK_PB")
        self.gridLayout.addWidget(self.OK_PB, 0, 0, 1, 1)
        self.CNCL_PB = QtWidgets.QPushButton(self.layoutWidget)
        self.CNCL_PB.setObjectName("CNCL_PB")
        self.gridLayout.addWidget(self.CNCL_PB, 0, 1, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(Login)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 87, 231, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PASS_LB = QtWidgets.QLabel(Login)
        self.PASS_LB.setGeometry(QtCore.QRect(226, 140, 57, 16))
        self.PASS_LB.setObjectName("PASS_LB")
        self.USR_LB = QtWidgets.QLabel(Login)
        self.USR_LB.setGeometry(QtCore.QRect(226, 103, 54, 16))
        self.USR_LB.setObjectName("USR_LB")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(30, 64, 161, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Login/Login_Image.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.USR_LE = QtWidgets.QLineEdit(Login)
        self.USR_LE.setGeometry(QtCore.QRect(290, 102, 151, 21))
        self.USR_LE.setObjectName("USR_LE")
        self.PASS_LE = QtWidgets.QLineEdit(Login)
        self.PASS_LE.setGeometry(QtCore.QRect(290, 138, 151, 21))
        self.PASS_LE.setObjectName("PASS_LE")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.OK_PB.setText(_translate("Login", "OK"))
        self.CNCL_PB.setText(_translate("Login", "CANCLE"))
        self.PASS_LB.setText(_translate("Login", "PASSWORD"))
        self.USR_LB.setText(_translate("Login", "USERNAME"))
        self.USR_LE.setToolTip(_translate("Login", "Enter Username"))
        self.PASS_LE.setToolTip(_translate("Login", "Enter Password"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
