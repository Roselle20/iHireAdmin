

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.button_states = {
            "dashboard": False,
            "applicants": False,
            "jobmanagent": False,
            "history": False,
            "satsana": False,
            "account": False,
            "pushButton": False,
            "pushButton_2": False,
            "pushButton_3": False,
        }
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1354, 708)
        MainWindow.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1351, 701))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu = QtWidgets.QFrame(self.layoutWidget)
        self.menu.setMaximumSize(QtCore.QSize(280, 16777215))
        self.menu.setStyleSheet("*{\n"
"background-color: rgb(226, 249, 255)\n"
"}")
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QFrame(self.menu)
        self.logo.setMinimumSize(QtCore.QSize(0, 75))
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.logo)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.logoo = QtWidgets.QFrame(self.logo)
        self.logoo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logoo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logoo.setObjectName("logoo")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.logoo)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.logoo)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/image/images/logotext.svg"))
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.logoo)
        self.verticalLayout.addWidget(self.logo, 0, QtCore.Qt.AlignTop)
        self.menulist = QtWidgets.QFrame(self.menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menulist.sizePolicy().hasHeightForWidth())
        self.menulist.setSizePolicy(sizePolicy)
        self.menulist.setStyleSheet("")
        self.menulist.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menulist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menulist.setObjectName("menulist")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menulist)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttons = QtWidgets.QFrame(self.menulist)
        self.buttons.setStyleSheet("")
        self.buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons.setObjectName("buttons")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.buttons)
        self.verticalLayout_3.setContentsMargins(-1, 1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dashboard = QtWidgets.QPushButton(self.buttons)
        self.dashboard.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dashboard.setFont(font)
        self.dashboard.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            padding: 10px; \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.dashboard.setFlat(True)
        self.dashboard.setObjectName("dashboard")
        self.verticalLayout_3.addWidget(self.dashboard)
        self.applicants = QtWidgets.QPushButton(self.buttons)
        self.applicants.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.applicants.setFont(font)
        self.applicants.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            padding: 10px; \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.applicants.setFlat(True)
        self.applicants.setObjectName("applicants")
        self.verticalLayout_3.addWidget(self.applicants)
        self.jobmanagent = QtWidgets.QPushButton(self.buttons)
        self.jobmanagent.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.jobmanagent.setFont(font)
        self.jobmanagent.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            padding: 10px; \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.jobmanagent.setFlat(True)
        self.jobmanagent.setObjectName("jobmanagent")
        self.verticalLayout_3.addWidget(self.jobmanagent)
        self.history = QtWidgets.QPushButton(self.buttons)
        self.history.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.history.setFont(font)
        self.history.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            padding: 10px; \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.history.setFlat(True)
        self.history.setObjectName("history")
        self.verticalLayout_3.addWidget(self.history)
        self.satsana = QtWidgets.QPushButton(self.buttons)
        self.satsana.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.satsana.setFont(font)
        self.satsana.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            padding: 10px; \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.satsana.setFlat(True)
        self.satsana.setObjectName("satsana")
        self.verticalLayout_3.addWidget(self.satsana)
        self.account = QtWidgets.QPushButton(self.buttons)
        self.account.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.account.setFont(font)
        self.account.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            padding: 10px; \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"\n"
"")
        self.account.setFlat(True)
        self.account.setObjectName("account")
        self.verticalLayout_3.addWidget(self.account)
        self.verticalLayout_2.addWidget(self.buttons)
        self.verticalLayout.addWidget(self.menulist)
        self.horizontalLayout.addWidget(self.menu)
        self.body = QtWidgets.QFrame(self.layoutWidget)
        self.body.setStyleSheet("QMainWindow{\n"
"    image: url(:/icon/images/newjobbtn.svg);\n"
"}\n"
"\n"
"")
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.body)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.wholebody = QtWidgets.QFrame(self.body)
        self.wholebody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wholebody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wholebody.setObjectName("wholebody")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.wholebody)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_2 = QtWidgets.QFrame(self.wholebody)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(-1, 1, -1, 1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dashboard_2 = QtWidgets.QFrame(self.frame_2)
        self.dashboard_2.setMinimumSize(QtCore.QSize(350, 0))
        self.dashboard_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dashboard_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dashboard_2.setObjectName("dashboard_2")
        self.formLayout = QtWidgets.QFormLayout(self.dashboard_2)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.dashboard_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.horizontalLayout_2.addWidget(self.dashboard_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            padding: 10px; \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(1)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            padding: 10px; \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMinimumSize(QtCore.QSize(250, 70))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_7)
        self.formLayout_2.setObjectName("formLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            padding: 10px; \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/images/newjobbtn.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(160, 30))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton_3)
        self.gridLayout_3.addWidget(self.frame_7, 0, 0, 1, 2, QtCore.Qt.AlignLeft)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.verticalLayout_7.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        self.buttonlist = QtWidgets.QFrame(self.wholebody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonlist.sizePolicy().hasHeightForWidth())
        self.buttonlist.setSizePolicy(sizePolicy)
        self.buttonlist.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonlist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonlist.setObjectName("buttonlist")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.buttonlist)
        self.verticalLayout_8.setContentsMargins(-1, 1, -1, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lists = QtWidgets.QFrame(self.buttonlist)
        self.lists.setMinimumSize(QtCore.QSize(0, 150))
        self.lists.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lists.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lists.setObjectName("lists")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.lists)
        self.horizontalLayout_4.setContentsMargins(50, 1, 50, 9)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame = QtWidgets.QFrame(self.lists)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setContentsMargins(30, 10, 30, 10)
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.total_applicants = QtWidgets.QFrame(self.frame)
        self.total_applicants.setStyleSheet("*{\n"
"background-color: #F1F2F2;\n"
" border: 3px; \n"
"border-radius: 10px; \n"
"padding: 5px;\n"
"}")
        self.total_applicants.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.total_applicants.setFrameShadow(QtWidgets.QFrame.Raised)
        self.total_applicants.setObjectName("total_applicants")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.total_applicants)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.total_applicants)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4 = QtWidgets.QLabel(self.total_applicants)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_4.addWidget(self.total_applicants, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame)
        self.frame_8 = QtWidgets.QFrame(self.lists)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_5.setContentsMargins(30, 10, 30, 10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.total_job = QtWidgets.QFrame(self.frame_8)
        self.total_job.setStyleSheet("*{\n"
"background-color: #F1F2F2;\n"
" border: 3px; \n"
"border-radius: 10px; \n"
"padding: 5px;\n"
"}\n"
"")
        self.total_job.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.total_job.setFrameShadow(QtWidgets.QFrame.Raised)
        self.total_job.setObjectName("total_job")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.total_job)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.total_job)
        self.label_9.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_11.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.number_job = QtWidgets.QLabel(self.total_job)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_job.sizePolicy().hasHeightForWidth())
        self.number_job.setSizePolicy(sizePolicy)
        self.number_job.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.number_job.setFont(font)
        self.number_job.setObjectName("number_job")
        self.verticalLayout_11.addWidget(self.number_job, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_5.addWidget(self.total_job, 0, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_8)
        self.frame_10 = QtWidgets.QFrame(self.lists)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_6.setContentsMargins(30, 10, 30, 10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pending_applicant = QtWidgets.QFrame(self.frame_10)
        self.pending_applicant.setStyleSheet("*{\n"
"background-color: #F1F2F2;\n"
" border: 3px; \n"
"border-radius: 10px; \n"
"padding: 5px;\n"
"}\n"
"")
        self.pending_applicant.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pending_applicant.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pending_applicant.setObjectName("pending_applicant")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.pending_applicant)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_7 = QtWidgets.QLabel(self.pending_applicant)
        self.label_7.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dashboard.clicked.connect(lambda: self.toggleButtonStyle(self.dashboard, "dashboard"))
        self.applicants.clicked.connect(lambda: self.toggleButtonStyle(self.applicants, "applicants"))
        self.jobmanagent.clicked.connect(lambda: self.toggleButtonStyle(self.jobmanagent, "jobmanagent"))
        self.history.clicked.connect(lambda: self.toggleButtonStyle(self.history, "history"))
        self.satsana.clicked.connect(lambda: self.toggleButtonStyle(self.satsana, "satsana"))
        self.account.clicked.connect(lambda: self.toggleButtonStyle(self.account, "account"))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_12.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.number_pending = QtWidgets.QLabel(self.pending_applicant)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_pending.sizePolicy().hasHeightForWidth())
        self.number_pending.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.number_pending.setFont(font)
        self.number_pending.setObjectName("number_pending")
        self.verticalLayout_12.addWidget(self.number_pending, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_6.addWidget(self.pending_applicant, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_10)
        self.verticalLayout_8.addWidget(self.lists, 0, QtCore.Qt.AlignTop)
        self.frame_9 = QtWidgets.QFrame(self.buttonlist)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8.addWidget(self.frame_9)
        self.verticalLayout_7.addWidget(self.buttonlist)
        self.verticalLayout_6.addWidget(self.wholebody)
        self.horizontalLayout.addWidget(self.body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def apply_stylesheet(self, stylesheet):
        self.dashboard.setStyleSheet(stylesheet)
        self.applicants.setStyleSheet(stylesheet)
        self.jobmanagent.setStyleSheet(stylesheet)
        self.history.setStyleSheet(stylesheet)
        self.satsana.setStyleSheet(stylesheet)
        self.account.setStyleSheet(stylesheet)
        self.pushButton.setStyleSheet(stylesheet)
        self.pushButton_2.setStyleSheet(stylesheet)
        self.pushButton_3.setStyleSheet(stylesheet)

    def toggleButtonStyle(self, button, button_name):
        if self.button_states[button_name]: 
            button.setStyleSheet("border: none; border-radius: 5px; padding: 10px;")
            self.button_states[button_name] = False
        else:
            for key in self.button_states:
                if key != button_name and self.button_states[key]: 
                    getattr(self, key).setStyleSheet("border: none; border-radius: 5px; padding: 10px;")
                    self.button_states[key] = False

            button.setStyleSheet("background-color: white; border: 3px solid #F1F2F2; border-radius: 5px; padding: 10px;")
            self.button_states[button_name] = True

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dashboard.setText(_translate("MainWindow", "Dashboard"))
        self.applicants.setText(_translate("MainWindow", "Applicants"))
        self.jobmanagent.setText(_translate("MainWindow", "Job Management"))
        self.history.setText(_translate("MainWindow", "History"))
        self.satsana.setText(_translate("MainWindow", "Satistics and Analytics"))
        self.account.setText(_translate("MainWindow", "Account"))
        self.label_2.setText(_translate("MainWindow", "DASHBOARD"))
        self.pushButton.setText(_translate("MainWindow", "Home"))
        self.pushButton_2.setText(_translate("MainWindow", "Interview"))
        self.label_3.setText(_translate("MainWindow", "Total Applicant"))
        self.label_4.setText(_translate("MainWindow", "14"))
        self.label_9.setText(_translate("MainWindow", "Total Job"))
        self.number_job.setText(_translate("MainWindow", "5"))
        self.label_7.setText(_translate("MainWindow", "Pending Applicants"))
        self.number_pending.setText(_translate("MainWindow", "45"))
import resource_rc
