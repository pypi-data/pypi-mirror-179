

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(878, 516)
        self.loginBtn2 = QtWidgets.QPushButton(Form)
        self.loginBtn2.setGeometry(QtCore.QRect(420, 260, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loginBtn2.setFont(font)
        self.loginBtn2.setObjectName("loginBtn2")
        self.ui_password = QtWidgets.QLineEdit(Form)
        self.ui_password.setGeometry(QtCore.QRect(350, 190, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ui_password.setFont(font)
        self.ui_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui_password.setObjectName("ui_password")
        self.ui_username = QtWidgets.QLineEdit(Form)
        self.ui_username.setGeometry(QtCore.QRect(350, 140, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ui_username.setFont(font)
        self.ui_username.setObjectName("ui_username")
        self.welcome_label = QtWidgets.QLabel(Form)
        self.welcome_label.setGeometry(QtCore.QRect(120, 40, 691, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        self.password = QtWidgets.QLabel(Form)
        self.password.setGeometry(QtCore.QRect(230, 190, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.username = QtWidgets.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(230, 140, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setObjectName("username")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loginBtn2.setText(_translate("Form", "Log In"))
        self.welcome_label.setText(_translate("Form", "Please enter your account username and password"))
        self.password.setText(_translate("Form", "Password"))
        self.username.setText(_translate("Form", "Username"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui2 = Ui_Form()
    ui2.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
