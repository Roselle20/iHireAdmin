

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 580)
        MainWindow.setMaximumSize(QtCore.QSize(1050, 580))
        MainWindow.setStyleSheet("QMainWindow{\n"
"url(:/icon/images/loginbtn.svg);\n"
"url(:/image/images/logo.svg);\n"
"url(:/image/images/logotext.svg);\n"
"url(:/image/images/username.svg);\n"
"}\n"
"\n"
"*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.logotext = QtWidgets.QLabel(self.body)
        self.logotext.setGeometry(QtCore.QRect(170, 60, 230, 63))
        self.logotext.setText("")
        self.logotext.setPixmap(QtGui.QPixmap(":/image/images/logotext.svg"))
        self.logotext.setObjectName("logotext")
        self.logo = QtWidgets.QLabel(self.body)
        self.logo.setGeometry(QtCore.QRect(590, 80, 391, 421))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/image/images/logo.svg"))
        self.logo.setObjectName("logo")
        self.input = QtWidgets.QLabel(self.body)
        self.input.setGeometry(QtCore.QRect(160, 190, 391, 201))
        self.input.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.input.setText("")
        self.input.setPixmap(QtGui.QPixmap(":/image/images/username.svg"))
        self.input.setObjectName("input")
        self.username = QtWidgets.QLineEdit(self.body)
        self.username.setGeometry(QtCore.QRect(170, 239, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setText("")
        self.username.setFrame(False)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.body)
        self.password.setGeometry(QtCore.QRect(170, 340, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setFrame(False)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.loginbtn = QtWidgets.QPushButton(self.body)
        self.loginbtn.setGeometry(QtCore.QRect(160, 410, 101, 31))
        self.loginbtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/images/loginbtn.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginbtn.setIcon(icon)
        self.loginbtn.setIconSize(QtCore.QSize(100, 50))
        self.loginbtn.setFlat(True)
        self.loginbtn.setObjectName("loginbtn")
        self.welcome = QtWidgets.QLabel(self.body)
        self.welcome.setGeometry(QtCore.QRect(170, 160, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")
        self.gridLayout.addWidget(self.body, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome.setText(_translate("MainWindow", "Welcome Admin!"))
import resource_rc
