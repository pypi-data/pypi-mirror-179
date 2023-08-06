


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_split_col_data:
    def setupUi(self, df_split_column_data):
        df_split_column_data.setObjectName("df_operations_window")
        df_split_column_data.resize(421, 293)
        self.label = QtWidgets.QLabel(df_split_column_data)
        self.label.setGeometry(QtCore.QRect(120, 30, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ui_column_name = QtWidgets.QLineEdit(df_split_column_data)
        self.ui_column_name.setGeometry(QtCore.QRect(160, 70, 113, 22))
        self.ui_column_name.setObjectName("ui_column_name")
        self.split_btn = QtWidgets.QPushButton(df_split_column_data)
        self.split_btn.setGeometry(QtCore.QRect(160, 210, 111, 28))
        self.split_btn.setObjectName("show_results_btn")
        self.label_2 = QtWidgets.QLabel(df_split_column_data)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ui_separator = QtWidgets.QLineEdit(df_split_column_data)
        self.ui_separator.setGeometry(QtCore.QRect(160, 160, 113, 22))
        self.ui_separator.setObjectName("ui_column_name_2")

        self.retranslateUi(df_split_column_data)
        QtCore.QMetaObject.connectSlotsByName(df_split_column_data)

    def retranslateUi(self, df_operations_row_window):
        _translate = QtCore.QCoreApplication.translate
        df_operations_row_window.setWindowTitle(_translate("df_operations_window", "Split column data"))
        self.label.setText(_translate("df_operations_window", "Enter the column name"))
        self.split_btn.setText(_translate("df_operations_window", "Apply"))
        self.label_2.setText(_translate("df_operations_window", "Which is the separator?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    df_split = QtWidgets.QDialog()
    ui = Ui_split_col_data()
    ui.setupUi(df_split)
    df_split.show()
    sys.exit(app.exec_())
