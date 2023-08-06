

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_log_in_failed(object):
    def setupUi(self, log_in_failed):
        log_in_failed.setObjectName("log_in_failed")
        log_in_failed.resize(436, 256)
        self.label_failed = QtWidgets.QLabel(log_in_failed)
        self.label_failed.setGeometry(QtCore.QRect(60, 100, 296, 45))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_failed.setFont(font)
        self.label_failed.setStyleSheet("color:rgb(255, 0, 0)")
        self.label_failed.setObjectName("label_failed")

        self.retranslateUi(log_in_failed)
        QtCore.QMetaObject.connectSlotsByName(log_in_failed)

    def retranslateUi(self, log_in_failed):
        _translate = QtCore.QCoreApplication.translate
        log_in_failed.setWindowTitle(_translate("log_in_failed", "Form"))
        self.label_failed.setText(_translate("log_in_failed", "LOG IN FAILED!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    log_in_failed = QtWidgets.QWidget()
    ui = Ui_log_in_failed()
    ui.setupUi(log_in_failed)
    log_in_failed.show()
    sys.exit(app.exec_())
