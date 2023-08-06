


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_df_select_multiple_col:
    def setupUi(self, df_select_cols):
        df_select_cols.setObjectName("df_operations_window")
        df_select_cols.resize(421, 293)
        self.label = QtWidgets.QLabel(df_select_cols)
        self.label.setGeometry(QtCore.QRect(120, 30, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ui_first_col_name = QtWidgets.QLineEdit(df_select_cols)
        self.ui_first_col_name.setGeometry(QtCore.QRect(160, 70, 113, 22))
        self.ui_first_col_name.setObjectName("ui_column_name")
        self.select_columns_btn = QtWidgets.QPushButton(df_select_cols)
        self.select_columns_btn.setGeometry(QtCore.QRect(160, 210, 111, 28))
        self.select_columns_btn.setObjectName("show_results_btn")
        self.label_2 = QtWidgets.QLabel(df_select_cols)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ui_last_col_name = QtWidgets.QLineEdit(df_select_cols)
        self.ui_last_col_name.setGeometry(QtCore.QRect(160, 160, 113, 22))
        self.ui_last_col_name.setObjectName("ui_column_name_2")

        self.retranslateUi(df_select_cols)
        QtCore.QMetaObject.connectSlotsByName(df_select_cols)

    def retranslateUi(self, df_operations_row_window):
        _translate = QtCore.QCoreApplication.translate
        df_operations_row_window.setWindowTitle(_translate("df_operations_window", "Select multiple columns"))
        self.label.setText(_translate("df_operations_window", "Enter first column name"))
        self.select_columns_btn.setText(_translate("df_operations_window", "Apply "))
        self.label_2.setText(_translate("df_operations_window", "Enter last column name?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    df_sel_columns = QtWidgets.QDialog()
    ui = Ui_df_select_multiple_col()
    ui.setupUi(df_sel_columns)
    df_sel_columns.show()
    sys.exit(app.exec_())
