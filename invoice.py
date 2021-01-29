from PyQt5 import QtCore, QtGui, QtWidgets
from inv_show import Showinvs
import MySQLdb   as mysql

class Invoices(object):
    def show_invs(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  Showinvs()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 31, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 50, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 50, 181, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(430, 50, 31, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(510, 50, 31, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 30, 181, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 30, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 30, 111, 20))
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 140, 161, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.show_invs)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 80, 541, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.change)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.add)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.dels)
        self.horizontalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "inv_num"))
        self.label_2.setText(_translate("MainWindow", "invoice_price_componentParrt"))
        self.label_3.setText(_translate("MainWindow", "invoice_list_of_required_spare_parts"))
        self.label_4.setText(_translate("MainWindow", "Teh_Dev_Num"))
        self.label_5.setText(_translate("MainWindow", "Teh_Inv_Num"))
        self.pushButton_4.setText(_translate("MainWindow", "Show_Invoice"))
        self.pushButton.setText(_translate("MainWindow", "Change_Invoice"))
        self.pushButton_2.setText(_translate("MainWindow", "Add_Invoice"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete_Invoice"))



    def change(self):

        try:
            invoice_num = int(self.lineEdit.text())
            invoice_price_componentParrt = int(self.lineEdit_2.text())
            invoice_list_of_required_spare_parts = self.lineEdit_3.text()
            technics_technics_inventory_num = int(self.lineEdit_4.text())
            technics_Division_Division_num = self.lineEdit_5.text()
        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="1234", db="lab4")
            cur = db.cursor()
            ch1="""UPDATE invoice SET invoice_price_componentParrt = %s, invoice_list_of_required_spare_parts = %s, technics_technics_inventory_num = %s,technics_Division_Division_num = %s WHERE invoice_num = %s"""
            ch2=(invoice_price_componentParrt, invoice_list_of_required_spare_parts, technics_technics_inventory_num,technics_Division_Division_num, invoice_num)
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            invoice_num = int(self.lineEdit.text())
            invoice_price_componentParrt = int(self.lineEdit_2.text())
            invoice_list_of_required_spare_parts = self.lineEdit_3.text()
            technics_technics_inventory_num = int(self.lineEdit_4.text())
            technics_Division_Division_num = self.lineEdit_5.text()
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="1234", db="lab4")
        cur = db.cursor()
        cur.execute('insert into invoice values(%s, %s, %s, %s, %s)', \
            (invoice_num,invoice_price_componentParrt, invoice_list_of_required_spare_parts, technics_technics_inventory_num,technics_Division_Division_num,))
        db.commit()

        cur.close()
        db.close()

    def dels(self):

        db = mysql.connect(host="localhost", user="root", passwd="1234", db="lab4")
        cur = db.cursor()
        try:
            ids = int(self.lineEdit.text())
        except:
            return
        cur.execute("DELETE FROM invoice WHERE invoice_num= %s",(int(ids),))
        db.commit()
        cur.close()
        db.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Invoices()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
