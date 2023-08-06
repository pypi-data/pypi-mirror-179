


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_df_add_new_rows:
    def setupUi(self, df_operations_replace_val_row):
        df_operations_replace_val_row.setObjectName("df_operations_window")
        df_operations_replace_val_row.resize(421, 293)
        self.label = QtWidgets.QLabel(df_operations_replace_val_row)
        self.label.setGeometry(QtCore.QRect(120, 30, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ui_row_name = QtWidgets.QLineEdit(df_operations_replace_val_row)
        self.ui_row_name.setGeometry(QtCore.QRect(160, 70, 113, 22))
        self.ui_row_name.setObjectName("ui_column_name")
        self.replace_btn = QtWidgets.QPushButton(df_operations_replace_val_row)
        self.replace_btn.setGeometry(QtCore.QRect(160, 210, 111, 28))
        self.replace_btn.setObjectName("show_results_btn")
        self.label_2 = QtWidgets.QLabel(df_operations_replace_val_row)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ui_fill_row_value = QtWidgets.QLineEdit(df_operations_replace_val_row)
        self.ui_fill_row_value.setGeometry(QtCore.QRect(160, 160, 113, 22))
        self.ui_fill_row_value.setObjectName("ui_column_name_2")

        self.retranslateUi(df_operations_replace_val_row)
        QtCore.QMetaObject.connectSlotsByName(df_operations_replace_val_row)

    def retranslateUi(self, df_operations_replace_values_in_row):
        _translate = QtCore.QCoreApplication.translate
        df_operations_replace_values_in_row.setWindowTitle(_translate("df_operations_window", "Add new rows"))
        self.label.setText(_translate("df_operations_window", "Enter the row name"))
        self.replace_btn.setText(_translate("df_operations_window", "Add row"))
        self.label_2.setText(_translate("df_operations_window", "Fill row with  "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    df_replace_values = QtWidgets.QDialog()
    ui = Ui_df_add_new_rows()
    ui.setupUi(df_replace_values)
    df_replace_values.show()
    sys.exit(app.exec_())
