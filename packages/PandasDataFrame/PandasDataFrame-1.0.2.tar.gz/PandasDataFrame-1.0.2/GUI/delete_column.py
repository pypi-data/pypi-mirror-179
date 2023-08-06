


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_df_delete_col:
    def setupUi(self, df_operations_delete_col):
        df_operations_delete_col.setObjectName("df_operations_window")
        df_operations_delete_col.resize(421, 209)
        self.label = QtWidgets.QLabel(df_operations_delete_col)
        self.label.setGeometry(QtCore.QRect(120, 30, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ui_column_name_delete = QtWidgets.QLineEdit(df_operations_delete_col)
        self.ui_column_name_delete.setGeometry(QtCore.QRect(160, 70, 113, 22))
        self.ui_column_name_delete.setObjectName("ui_column_name")
        self.delete_col_btn = QtWidgets.QPushButton(df_operations_delete_col)
        self.delete_col_btn.setGeometry(QtCore.QRect(160, 110, 111, 28))
        self.delete_col_btn.setObjectName("show_results_btn")


        self.retranslateUi(df_operations_delete_col)
        QtCore.QMetaObject.connectSlotsByName(df_operations_delete_col)




    def retranslateUi(self, df_operations_delete_col):
        _translate = QtCore.QCoreApplication.translate
        df_operations_delete_col.setWindowTitle(_translate("df_operations_window", "Delete column"))
        self.label.setText(_translate("df_operations_window", "Enter the column name"))
        self.delete_col_btn.setText(_translate("df_operations_window", "Delete"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    delete_col = QtWidgets.QDialog()
    ui = Ui_df_delete_col()
    ui.setupUi(delete_col)
    delete_col.show()
    sys.exit(app.exec_())
