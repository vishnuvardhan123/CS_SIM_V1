import sqlite3
import sys
import traceback
import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from App import Loginform
from IPSettings import Ui_IPSetting
from MainWindow import Ui_MainWindow
from OPWindow import Ui_OPWindow
from PasswordReset import Ui_Pass_Rst
from UtilityPackage.Reuse_Utilities import errormsgs


class Myclass(Loginform.Ui_Login, Ui_Pass_Rst, Ui_OPWindow, Ui_IPSetting, errormsgs, QtWidgets.QWidget):

    def __init__(self, *args,
                 **kwargs):  # creating function for initiating the program. All actions will be triggered under this program
        super(Myclass, self).__init__(*args, **kwargs)  # Initiating MyQtApp
        self.setupUi(self)
        self.setWindowTitle("Login")  # Setting Title for the Login Window
        self.PASS_LE.setEchoMode(QtWidgets.QLineEdit.Password)  # Setting Ecomode to password field
        self.OK_PB.clicked.connect(self.loginCheck)
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        print('\nwaiting to receive message', file=sys.stderr)
        # self.OK_PB.clicked.connect(self.loginCheck)  # when Login ok button clicked calling of loginCheck Method
        self.CNCL_PB.clicked.connect(self.quit)  # Closing of login window when cancle button clicked

    #################################### LOGIN VERIFICATION WITH DATABASE ##########################################

    def loginCheck(self):  # Creating loginCheck method for login verification
        username = self.USR_LE.text()  # Storing username in a variable
        password = self.PASS_LE.text()  # Storing Password in a variable
        print(password)
        connection = sqlite3.connect("E:\Python\CS_SIM_V1\DatabaseFiles\login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",
                                    (username, password))  # connecting to database

        if len(result.fetchall()) > 0:  # Fetching all the data from database
            print("User Found ! ")  # Printing user found
            self.secondwindowshow()  # Once user found opening the mainwindow
            self.close()  # At the same time closing the login window

        else:
            print("User Not Found !")  # In case user not found printing the statement
            self.showMessageBox('Warning',
                                'Invalid Username and Password')  # showMessageBox method called from Utility Package
        connection.close()  # Closing the database connection

    def quit(self):  # Created a method to close the login window when cancle button clicked
        self.close()

    #################################### CALLING CS SIMULATOR WINDOW (MAINWINDOW) #####################################

    def secondwindowshow(self):  # Initializing Mainwindow
        self.ui = Ui_MainWindow()
        self.secondwindow = QtWidgets.QMainWindow()
        self.ui.setupUi(self.secondwindow)
        self.secondwindow.setWindowTitle("CS Simulator")  # Setting title to the window
        self.secondwindow.showMaximized()  # Maximizing the window
        self.secondwindow.show()  # Displaying the window
        self.ui.LRU_Status.triggered.connect(self.OPerationWindow)
        self.ui.Maint_Files.triggered.connect(lambda: self.readfile(
            'E:\Python\CS_SIM_V1\ProjectFiles\Demopdf.pdf'))  # Calling readpdf method when Videos clicked
        self.ui.Maint_Videos.triggered.connect(lambda: self.readfile(
            'E:\Python\CS_SIM_V1\ProjectFiles\Animated Film.mp4'))  # Calling videofiles from Utility package and passing arguments using lambda keyword.
        self.ui.Pass_Reset.triggered.connect(
            self.Passwordwindow)  # Calling Passwordwindow method when Password_Reset clicked
        # self.label_63.setStyleSheet('background: Green')

    #################################### CALLING PASSWORD WINDOW ################################################

    def Passwordwindow(self):  # Initializing password resetting
        self.uf = Ui_Pass_Rst()
        self.passwindow = QtWidgets.QWidget()
        self.ui.setupUi(self.passwindow)
        self.passwindow.setWindowTitle("Password Reset")  # Setting title to password window
        self.passwindow.show()  # Displaying password window
        self.uf.OK_BTN.clicked.connect(self.Password_Reset)  # Connecting to Password_Reset method when OK_btn clicked
        self.uf.CRNT_PW_LE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uf.NW_PW_LE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uf.CNF_PW_LE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uf.pushButton_2.clicked.connect(
            self.passwindowclose)  # Connecting to passwindowclose method when cancle btn clicked

    def OPerationWindow(self):
        self.ui = Ui_OPWindow()
        self.opwindow = QtWidgets.QMainWindow()
        self.ui.setupUi(self.opwindow)
        self.opwindow.setWindowTitle("CS Simulator")  # Setting title to the window
        self.opwindow.showMaximized()  # Maximizing the window
        # print(self.opwindow.size())
        # self.opwindow.setMaximumSize(1315, 600)
        # print(self.opwindow.size())
        self.opwindow.show()  # Displaying the window

    def passwindowclose(self):
        self.passwindow.close()

    #################################### PASSWORD RESETTING #####################################################

    def Password_Reset(self):
        curnt_pass = self.uf.CRNT_PW_LE.text()  # Storing the current password
        print(curnt_pass)
        new_pass = self.uf.NW_PW_LE.text()  # Storing the new password
        print(new_pass)
        cnf_pass = self.uf.CNF_PW_LE.text()  # Storing the conform password
        print(cnf_pass)
        connection = sqlite3.connect("login.db")  # Connecting to sqlite3 database
        result = connection.execute("SELECT * FROM USERS")  # Storing USERS data from database
        for data in result:
            data = (data[1])  # Storing Password from database
            print(data)
            if curnt_pass == data and new_pass == cnf_pass:  # Condition for reset pwd i.e current pwd matches to database pwd & new pwd should matches to confirm

                pass_update = "Update USERS set PASSWORD = '" + cnf_pass + "' WHERE PASSWORD=PASSWORD"  # updating the database pwd fied with new pwd

                connection.execute(pass_update)  # confirming updation of pwd in database
                connection.commit()  # commiting the change
                print(pass_update)
                print('Password Updated Successfully')
                self.passwindow.close()  # successful completion of pwd reset pwd window closes

            else:
                print('Password Updation Failed')
                self.showMessageBox('Warning',
                                    'Password Mismatched')  # showing the error message incase of login failed

        connection.close()  # closing the database connection



if __name__ == '__main__':  # Required to start QtDesigner app to open up the designed GUI
    app = QtWidgets.QApplication(sys.argv)
    qt_app = Myclass()
    qt_app.show()
    app.exec_()
