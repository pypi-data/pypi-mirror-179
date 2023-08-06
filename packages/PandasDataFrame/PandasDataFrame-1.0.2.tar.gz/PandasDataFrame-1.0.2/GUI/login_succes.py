

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Log_in_success(object):
    def setupUi(self, Log_in_success):
        Log_in_success.setObjectName("Log_in_success")
        Log_in_success.resize(436, 256)
        self.label_success = QtWidgets.QLabel(Log_in_success)
        self.label_success.setGeometry(QtCore.QRect(70, 110, 296, 45))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_success.setFont(font)
        self.label_success.setStyleSheet("color:rgb(0, 170, 0)")
        self.label_success.setObjectName("label_success")

        self.retranslateUi(Log_in_success)
        QtCore.QMetaObject.connectSlotsByName(Log_in_success)

    def retranslateUi(self, Log_in_success):
        _translate = QtCore.QCoreApplication.translate
        Log_in_success.setWindowTitle(_translate("Log_in_success", "Form"))
        self.label_success.setText(_translate("Log_in_success", "LOG IN SUCCESS!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Log_in_success = QtWidgets.QWidget()
    ui = Ui_Log_in_success()
    ui.setupUi(Log_in_success)
    Log_in_success.show()
    sys.exit(app.exec_())
