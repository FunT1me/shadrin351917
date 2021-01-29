from PyQt5 import QtCore, QtGui, QtWidgets
from teh_show import Showteh
import MySQLdb   as mysql


class Technic(object):
    def show_teh(self):
        self.window = QtWidgets.QMainWindow()
        self.ui =  Showteh()
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
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 50, 121, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 50, 111, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 50, 131, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(500, 50, 31, 20))
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
        self.label_3.setGeometry(QtCore.QRect(200, 30, 111, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 30, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 30, 151, 20))
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 140, 161, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.show_teh)
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
        self.label.setText(_translate("MainWindow", "Inv_num"))
        self.label_2.setText(_translate("MainWindow", "technics_name"))
        self.label_3.setText(_translate("MainWindow", "technics_model"))
        self.label_4.setText(_translate("MainWindow", "Div_Num"))
        self.label_5.setText(_translate("MainWindow", "technics_year_of_release"))
        self.pushButton_4.setText(_translate("MainWindow", "Show_Tehnics"))
        self.pushButton.setText(_translate("MainWindow", "Change_Tehnics"))
        self.pushButton_2.setText(_translate("MainWindow", "Add_Tehnics"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete_Tehnics"))



    def change(self):

        try:
            technics_inventory_num = int(self.lineEdit.text())
            technics_name = self.lineEdit_2.text()
            technics_model = self.lineEdit_3.text()
            technics_year_of_release = self.lineEdit_4.text()
            Division_Division_num = int(self.lineEdit_5.text())
        except:
            return

        try:
            db = mysql.connect(host="localhost", user="root", passwd="1234", db="lab4")
            cur = db.cursor()
            ch1="""UPDATE technics SET technics_name = %s, technics_model = %s, technics_year_of_release = %s,Division_Division_num = %s WHERE technics_inventory_num = %s"""
            ch2=( technics_name, technics_model, technics_year_of_release,Division_Division_num, technics_inventory_num)
            cur.execute(ch1, ch2)
            db.commit()
            cur.close()
        finally:
            db.close()

    def add(self):

        try:
            technics_inventory_num = int(self.lineEdit.text())
            technics_name = self.lineEdit_2.text()
            technics_model = self.lineEdit_3.text()
            technics_year_of_release = self.lineEdit_4.text()
            Division_Division_num = int(self.lineEdit_5.text())
        except:
            return
        db = mysql.connect(host="localhost", user="root", passwd="1234", db="lab4")
        cur = db.cursor()
        cur.execute('insert into technics values(%s, %s, %s, %s, %s)', \
            (int(technics_inventory_num), technics_name, technics_model, technics_year_of_release, int(Division_Division_num),))
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
        cur.execute("DELETE FROM technics WHERE technics_inventory_num= %s",(int(ids),))
        db.commit()
        cur.close()
        db.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Technic()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
