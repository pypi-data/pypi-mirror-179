

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_new_column(object):
    def setupUi(self, add_new_column):
        add_new_column.setObjectName("add_new_column")
        add_new_column.resize(780, 438)
        self.label = QtWidgets.QLabel(add_new_column)
        self.label.setGeometry(QtCore.QRect(180, 50, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ui_col_position = QtWidgets.QLineEdit(add_new_column)
        self.ui_col_position.setGeometry(QtCore.QRect(420, 100, 201, 31))
        self.ui_col_position.setObjectName("ui_col_position")
        self.label_2 = QtWidgets.QLabel(add_new_column)
        self.label_2.setGeometry(QtCore.QRect(180, 100, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(add_new_column)
        self.label_4.setGeometry(QtCore.QRect(180, 160, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ui_new_col_name = QtWidgets.QLineEdit(add_new_column)
        self.ui_new_col_name.setGeometry(QtCore.QRect(420, 160, 201, 31))
        self.ui_new_col_name.setObjectName("ui_new_col_name")
        self.label_5 = QtWidgets.QLabel(add_new_column)
        self.label_5.setGeometry(QtCore.QRect(180, 220, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.ui_data_fill = QtWidgets.QLineEdit(add_new_column)
        self.ui_data_fill.setGeometry(QtCore.QRect(420, 210, 201, 31))
        self.ui_data_fill.setObjectName("ui_data_fill")
        self.label_3 = QtWidgets.QLabel(add_new_column)
        self.label_3.setGeometry(QtCore.QRect(220, 120, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.add_col_btn = QtWidgets.QPushButton(add_new_column)
        self.add_col_btn.setGeometry(QtCore.QRect(420, 270, 201, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_col_btn.setFont(font)
        self.add_col_btn.setObjectName("add_col_btn")

        self.retranslateUi(add_new_column)
        QtCore.QMetaObject.connectSlotsByName(add_new_column)

    def retranslateUi(self, add_new_column):
        _translate = QtCore.QCoreApplication.translate
        add_new_column.setWindowTitle(_translate("add_new_column", "Add new column"))
        self.label.setText(
            _translate("add_new_column", "Create new column on a specific location and fill it with data "))
        self.label_2.setText(_translate("add_new_column", "Enter position of new column"))
        self.label_4.setText(_translate("add_new_column", "Enter the name of new column"))
        self.label_5.setText(_translate("add_new_column", "Enter the data to fill the column"))
        self.label_3.setText(_translate("add_new_column", "(must be a number)"))
        self.add_col_btn.setText(_translate("add_new_column", "Create column"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    add_new_column = QtWidgets.QDialog()
    ui = Ui_add_new_column()
    ui.setupUi(add_new_column)
    add_new_column.show()
    sys.exit(app.exec_())
