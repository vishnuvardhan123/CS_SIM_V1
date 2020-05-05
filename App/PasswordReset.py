# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PasswordReset.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pass_Rst(object):
    def setupUi(self, Pass_Rst):
        Pass_Rst.setObjectName("Pass_Rst")
        Pass_Rst.resize(453, 333)
        self.Page_Title = QtWidgets.QLabel(Pass_Rst)
        self.Page_Title.setGeometry(QtCore.QRect(140, 20, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Page_Title.setFont(font)
        self.Page_Title.setObjectName("Page_Title")
        self.groupBox = QtWidgets.QGroupBox(Pass_Rst)
        self.groupBox.setGeometry(QtCore.QRect(50, 50, 351, 241))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(56, 30, 241, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.NW_PW_LE = QtWidgets.QLineEdit(self.layoutWidget)
        self.NW_PW_LE.setObjectName("NW_PW_LE")
        self.gridLayout.addWidget(self.NW_PW_LE, 1, 1, 1, 1)
        self.NW_PW_LB = QtWidgets.QLabel(self.layoutWidget)
        self.NW_PW_LB.setObjectName("NW_PW_LB")
        self.gridLayout.addWidget(self.NW_PW_LB, 1, 0, 1, 1)
        self.CRNT_PW_LB = QtWidgets.QLabel(self.layoutWidget)
        self.CRNT_PW_LB.setObjectName("CRNT_PW_LB")
        self.gridLayout.addWidget(self.CRNT_PW_LB, 0, 0, 1, 1)
        self.CRNT_PW_LE = QtWidgets.QLineEdit(self.layoutWidget)
        self.CRNT_PW_LE.setObjectName("CRNT_PW_LE")
        self.gridLayout.addWidget(self.CRNT_PW_LE, 0, 1, 1, 1)
        self.CNF_PW_LB = QtWidgets.QLabel(self.layoutWidget)
        self.CNF_PW_LB.setObjectName("CNF_PW_LB")
        self.gridLayout.addWidget(self.CNF_PW_LB, 2, 0, 1, 1)
        self.CNF_PW_LE = QtWidgets.QLineEdit(self.layoutWidget)
        self.CNF_PW_LE.setObjectName("CNF_PW_LE")
        self.gridLayout.addWidget(self.CNF_PW_LE, 2, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 170, 158, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OK_BTN = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.OK_BTN.setFont(font)
        self.OK_BTN.setObjectName("OK_BTN")
        self.gridLayout_2.addWidget(self.OK_BTN, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.retranslateUi(Pass_Rst)
        QtCore.QMetaObject.connectSlotsByName(Pass_Rst)

    def retranslateUi(self, Pass_Rst):
        _translate = QtCore.QCoreApplication.translate
        Pass_Rst.setWindowTitle(_translate("Pass_Rst", "Form"))
        self.Page_Title.setText(_translate("Pass_Rst", "Password Reset"))
        self.NW_PW_LE.setToolTip(_translate("Pass_Rst", "Enter New Password"))
        self.NW_PW_LB.setText(_translate("Pass_Rst", "New Password"))
        self.CRNT_PW_LB.setText(_translate("Pass_Rst", "Current Password"))
        self.CRNT_PW_LE.setToolTip(_translate("Pass_Rst", "Enter Current Password"))
        self.CNF_PW_LB.setText(_translate("Pass_Rst", "Confirm Password"))
        self.CNF_PW_LE.setToolTip(_translate("Pass_Rst", "Enter Confirm Password"))
        self.OK_BTN.setText(_translate("Pass_Rst", "OK"))
        self.pushButton_2.setText(_translate("Pass_Rst", "Cancle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pass_Rst = QtWidgets.QWidget()
    ui = Ui_Pass_Rst()
    ui.setupUi(Pass_Rst)
    Pass_Rst.show()
    sys.exit(app.exec_())
