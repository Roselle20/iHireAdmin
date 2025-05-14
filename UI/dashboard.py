
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
            "pending": False,
            "interview": False,
            "screening": False,   
        }
        self.last_pressed_button = None


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1203, 541)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255)\n"
"}\n"
"#menu, #logo,#logoo,#logoicon, #menulist, #buttons, #add_job\n"
"\n"
"{\n"
"background-color: rgb(226, 249, 255)\n"
"}\n"
"#dashboard_2{\n"
"background-color: rgb(255, 255, 255)\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_38 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.dashboard_2 = QtWidgets.QWidget()
        self.dashboard_2.setObjectName("dashboard_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dashboard_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dashboard_body = QtWidgets.QFrame(self.dashboard_2)
        self.dashboard_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dashboard_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dashboard_body.setObjectName("dashboard_body")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.dashboard_body)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.dashboard_header = QtWidgets.QFrame(self.dashboard_body)
        self.dashboard_header.setMinimumSize(QtCore.QSize(0, 80))
        self.dashboard_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dashboard_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dashboard_header.setObjectName("dashboard_header")
        self.gridLayout = QtWidgets.QGridLayout(self.dashboard_header)
        self.gridLayout.setContentsMargins(0, 15, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.header_4 = QtWidgets.QFrame(self.dashboard_header)
        self.header_4.setMinimumSize(QtCore.QSize(0, 80))
        self.header_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_4.setObjectName("header_4")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.header_4)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.frame_78 = QtWidgets.QFrame(self.header_4)
        self.frame_78.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_78.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_78.setObjectName("frame_78")
        self.gridLayout_55 = QtWidgets.QGridLayout(self.frame_78)
        self.gridLayout_55.setObjectName("gridLayout_55")
        self.label_14 = QtWidgets.QLabel(self.frame_78)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_55.addWidget(self.label_14, 0, 0, 1, 1)
        self.horizontalLayout_24.addWidget(self.frame_78, 0, QtCore.Qt.AlignLeft)
        self.frame_79 = QtWidgets.QFrame(self.header_4)
        self.frame_79.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_79.setObjectName("frame_79")
        self.gridLayout_56 = QtWidgets.QGridLayout(self.frame_79)
        self.gridLayout_56.setObjectName("gridLayout_56")
        self.home_6 = QtWidgets.QPushButton(self.frame_79)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.home_6.setFont(font)
        self.home_6.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.home_6.setFlat(True)
        self.home_6.setObjectName("home_6")
        self.gridLayout_56.addWidget(self.home_6, 0, 0, 1, 1)
        self.horizontalLayout_24.addWidget(self.frame_79)
        self.frame_80 = QtWidgets.QFrame(self.header_4)
        self.frame_80.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_80.setObjectName("frame_80")
        self.gridLayout_57 = QtWidgets.QGridLayout(self.frame_80)
        self.gridLayout_57.setObjectName("gridLayout_57")
        self.pushButton_30 = QtWidgets.QPushButton(self.frame_80)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_30.setFlat(True)
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_57.addWidget(self.pushButton_30, 0, 0, 1, 1)
        self.horizontalLayout_24.addWidget(self.frame_80)
        self.frame_81 = QtWidgets.QFrame(self.header_4)
        self.frame_81.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_81.setObjectName("frame_81")
        self.gridLayout_58 = QtWidgets.QGridLayout(self.frame_81)
        self.gridLayout_58.setObjectName("gridLayout_58")
        self.add_job_2 = QtWidgets.QPushButton(self.frame_81)
        self.add_job_2.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            padding: 10px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.add_job_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/images/newjobbtn.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_job_2.setIcon(icon)
        self.add_job_2.setIconSize(QtCore.QSize(150, 30))
        self.add_job_2.setFlat(True)
        self.add_job_2.setObjectName("add_job_2")
        self.gridLayout_58.addWidget(self.add_job_2, 0, 0, 1, 1)
        self.horizontalLayout_24.addWidget(self.frame_81)
        self.gridLayout.addWidget(self.header_4, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.dashboard_header)
        self.buttonlist = QtWidgets.QFrame(self.dashboard_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonlist.sizePolicy().hasHeightForWidth())
        self.buttonlist.setSizePolicy(sizePolicy)
        self.buttonlist.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonlist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonlist.setObjectName("buttonlist")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.buttonlist)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lists = QtWidgets.QFrame(self.buttonlist)
        self.lists.setMinimumSize(QtCore.QSize(0, 0))
        self.lists.setMaximumSize(QtCore.QSize(981, 151))
        self.lists.setStyleSheet("#total_applicants, #pending_applicant, #total_job {\n"
"background-color: white;\n"
" border: 3px solid rgb(221, 221, 221);\n"
"border-radius:10px;\n"
"padding: 5px;\n"
"}\n"
"")
        self.lists.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lists.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lists.setObjectName("lists")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.lists)
        self.horizontalLayout_5.setContentsMargins(50, 1, 50, 9)
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_9 = QtWidgets.QFrame(self.lists)
        self.frame_9.setMaximumSize(QtCore.QSize(249, 139))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_4.setContentsMargins(30, 10, 30, 10)
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.total_applicants = QtWidgets.QFrame(self.frame_9)
        self.total_applicants.setMaximumSize(QtCore.QSize(230, 117))
        self.total_applicants.setStyleSheet("")
        self.total_applicants.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.total_applicants.setFrameShadow(QtWidgets.QFrame.Raised)
        self.total_applicants.setObjectName("total_applicants")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.total_applicants)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.total_applicants)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
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
        self.horizontalLayout_5.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.lists)
        self.frame_10.setMaximumSize(QtCore.QSize(248, 139))
        self.frame_10.setStyleSheet("")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_5.setContentsMargins(30, 10, 30, 10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.total_job = QtWidgets.QFrame(self.frame_10)
        self.total_job.setMaximumSize(QtCore.QSize(230, 117))
        self.total_job.setStyleSheet("")
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
        self.number_job.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.number_job.setFont(font)
        self.number_job.setObjectName("number_job")
        self.verticalLayout_11.addWidget(self.number_job, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_5.addWidget(self.total_job, 0, 1, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.lists)
        self.frame_11.setMaximumSize(QtCore.QSize(290, 139))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_6.setContentsMargins(30, 10, 30, 10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pending_applicant = QtWidgets.QFrame(self.frame_11)
        self.pending_applicant.setMaximumSize(QtCore.QSize(230, 117))
        self.pending_applicant.setStyleSheet("")
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
        self.horizontalLayout_5.addWidget(self.frame_11)
        self.verticalLayout_8.addWidget(self.lists)
        self.frame_12 = QtWidgets.QFrame(self.buttonlist)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.frame_12)
        self.scrollArea_5.setStyleSheet("\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: rgb(204, 204, 204);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertica:hoverl{\n"
"    background-color: rgb(5, 74, 91);\n"
"}\n"
"")
        self.scrollArea_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 921, 253))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.widget_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.widget_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.widget_5)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.widget_5)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.gridLayout_12.addWidget(self.widget_5, 0, 0, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_32.addWidget(self.scrollArea_5)
        self.verticalLayout_8.addWidget(self.frame_12)
        self.verticalLayout_7.addWidget(self.buttonlist)
        self.verticalLayout.addWidget(self.dashboard_body)
        self.stackedWidget.addWidget(self.dashboard_2)
        self.applicants_2 = QtWidgets.QWidget()
        self.applicants_2.setObjectName("applicants_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.applicants_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.applicant_header = QtWidgets.QFrame(self.applicants_2)
        self.applicant_header.setMinimumSize(QtCore.QSize(0, 80))
        self.applicant_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.applicant_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.applicant_header.setObjectName("applicant_header")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.applicant_header)
        self.gridLayout_11.setContentsMargins(0, 18, 0, 0)
        self.gridLayout_11.setHorizontalSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.header_3 = QtWidgets.QFrame(self.applicant_header)
        self.header_3.setMinimumSize(QtCore.QSize(0, 80))
        self.header_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_3.setObjectName("header_3")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.header_3)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_74 = QtWidgets.QFrame(self.header_3)
        self.frame_74.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_74.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_74.setObjectName("frame_74")
        self.gridLayout_51 = QtWidgets.QGridLayout(self.frame_74)
        self.gridLayout_51.setObjectName("gridLayout_51")
        self.label_13 = QtWidgets.QLabel(self.frame_74)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_51.addWidget(self.label_13, 0, 0, 1, 1)
        self.horizontalLayout_23.addWidget(self.frame_74, 0, QtCore.Qt.AlignLeft)
        self.frame_75 = QtWidgets.QFrame(self.header_3)
        self.frame_75.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_75.setObjectName("frame_75")
        self.gridLayout_52 = QtWidgets.QGridLayout(self.frame_75)
        self.gridLayout_52.setObjectName("gridLayout_52")
        self.home = QtWidgets.QPushButton(self.frame_75)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.home.setFont(font)
        self.home.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.home.setFlat(True)
        self.home.setObjectName("home")
        self.gridLayout_52.addWidget(self.home, 0, 0, 1, 1)
        self.horizontalLayout_23.addWidget(self.frame_75)
        self.frame_76 = QtWidgets.QFrame(self.header_3)
        self.frame_76.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_76.setObjectName("frame_76")
        self.gridLayout_53 = QtWidgets.QGridLayout(self.frame_76)
        self.gridLayout_53.setObjectName("gridLayout_53")
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_76)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_27.setFlat(True)
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_53.addWidget(self.pushButton_27, 0, 0, 1, 1)
        self.horizontalLayout_23.addWidget(self.frame_76)
        self.frame_77 = QtWidgets.QFrame(self.header_3)
        self.frame_77.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_77.setObjectName("frame_77")
        self.gridLayout_54 = QtWidgets.QGridLayout(self.frame_77)
        self.gridLayout_54.setObjectName("gridLayout_54")
        self.add_job_3 = QtWidgets.QPushButton(self.frame_77)
        self.add_job_3.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.add_job_3.setText("")
        self.add_job_3.setIcon(icon)
        self.add_job_3.setIconSize(QtCore.QSize(150, 30))
        self.add_job_3.setFlat(True)
        self.add_job_3.setObjectName("add_job_3")
        self.gridLayout_54.addWidget(self.add_job_3, 0, 0, 1, 1)
        self.horizontalLayout_23.addWidget(self.frame_77)
        self.gridLayout_11.addWidget(self.header_3, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.applicant_header)
        self.applicant_body = QtWidgets.QFrame(self.applicants_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applicant_body.sizePolicy().hasHeightForWidth())
        self.applicant_body.setSizePolicy(sizePolicy)
        self.applicant_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.applicant_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.applicant_body.setObjectName("applicant_body")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.applicant_body)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.select = QtWidgets.QFrame(self.applicant_body)
        self.select.setMinimumSize(QtCore.QSize(0, 30))
        self.select.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.select.setFrameShadow(QtWidgets.QFrame.Raised)
        self.select.setObjectName("select")
        self.formLayout = QtWidgets.QFormLayout(self.select)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.select)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayout_13.addWidget(self.select, 0, QtCore.Qt.AlignTop)
        self.downbody = QtWidgets.QFrame(self.applicant_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downbody.sizePolicy().hasHeightForWidth())
        self.downbody.setSizePolicy(sizePolicy)
        self.downbody.setMinimumSize(QtCore.QSize(0, 150))
        self.downbody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.downbody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.downbody.setObjectName("downbody")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.downbody)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.status = QtWidgets.QFrame(self.downbody)
        self.status.setMinimumSize(QtCore.QSize(0, 70))
        self.status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.status.setObjectName("status")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.status)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.positiondroplist = QtWidgets.QFrame(self.status)
        self.positiondroplist.setMinimumSize(QtCore.QSize(450, 0))
        self.positiondroplist.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.positiondroplist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.positiondroplist.setObjectName("positiondroplist")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.positiondroplist)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.comboBox = QtWidgets.QComboBox(self.positiondroplist)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("*{\n"
"background-color: white;\n"
" border: 3px solid rgb(221, 221, 221);\n"
"border-radius:5px;\n"
"padding: 5px;\n"
"}")
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_31.addWidget(self.comboBox)
        self.horizontalLayout.addWidget(self.positiondroplist, 0, QtCore.Qt.AlignLeft)
        self.frame_27 = QtWidgets.QFrame(self.status)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_27)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.pending = QtWidgets.QPushButton(self.frame_27)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pending.setFont(font)
        self.pending.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            padding: 10px; \n"
"            background-color: rgb(226, 249, 255);\n"
"            border: 3px solid rgb(220, 221, 221);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pending.setFlat(True)
        self.pending.setObjectName("pending")
        self.gridLayout_14.addWidget(self.pending, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_27)
        self.frame_28 = QtWidgets.QFrame(self.status)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_28)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.screening = QtWidgets.QPushButton(self.frame_28)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.screening.setFont(font)
        self.screening.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            padding: 10px; \n"
"            background-color: rgb(226, 249, 255);\n"
"            border: 3px solid rgb(220, 221, 221);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.screening.setFlat(True)
        self.screening.setObjectName("screening")
        self.gridLayout_15.addWidget(self.screening, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_28)
        self.frame_29 = QtWidgets.QFrame(self.status)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_29)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.interview = QtWidgets.QPushButton(self.frame_29)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.interview.setFont(font)
        self.interview.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            padding: 10px; \n"
"            background-color: rgb(226, 249, 255);\n"
"            border: 3px solid rgb(220, 221, 221);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.interview.setFlat(True)
        self.interview.setObjectName("interview")
        self.gridLayout_16.addWidget(self.interview, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_29)
        self.verticalLayout_14.addWidget(self.status, 0, QtCore.Qt.AlignTop)
        self.name_lists = QtWidgets.QWidget(self.downbody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_lists.sizePolicy().hasHeightForWidth())
        self.name_lists.setSizePolicy(sizePolicy)
        self.name_lists.setObjectName("name_lists")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.name_lists)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.name_lists)
        self.stackedWidget_2.setStyleSheet("\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: rgb(204, 204, 204);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertica:hoverl{\n"
"    background-color: rgb(5, 74, 91);\n"
"}\n"
"")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.pending_page = QtWidgets.QWidget()
        self.pending_page.setObjectName("pending_page")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.pending_page)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.pending_page)
        self.scrollArea_4.setStyleSheet("\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    width: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: rgb(204, 204, 204);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertica:hoverl{\n"
"    background-color: rgb(124, 124, 124);\n"
"}\n"
"")
        self.scrollArea_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 905, 308))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents_5)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_29.setContentsMargins(100, 0, 100, -1)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.frame = QtWidgets.QFrame(self.widget_4)
        self.frame.setStyleSheet("QPushButton{\n"
"background-color: rgb(241, 242, 242);\n"
"border-radius: 10px;\n"
"border: 3px solid  rgb(220, 221, 221);\n"
"min-height: 35px;\n"
"text-align: center;\n"
"text-color: rgb(0, 0, 0);\n"
"font-family: Arial;\n"
"font-size: 16px;\n"
"font-weight: bold; \n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_9.setVerticalSpacing(10)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.roselle = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roselle.sizePolicy().hasHeightForWidth())
        self.roselle.setSizePolicy(sizePolicy)
        self.roselle.setObjectName("roselle")
        self.gridLayout_9.addWidget(self.roselle, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_9.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_9.addWidget(self.pushButton_13, 3, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_9.addWidget(self.pushButton_15, 1, 0, 1, 1)
        self.verticalLayout_29.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_30.addWidget(self.widget_4)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_28.addWidget(self.scrollArea_4)
        self.stackedWidget_2.addWidget(self.pending_page)
        self.screening_page = QtWidgets.QWidget()
        self.screening_page.setObjectName("screening_page")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.screening_page)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.screening_page)
        self.scrollArea_3.setStyleSheet("\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    width: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: rgb(204, 204, 204);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertica:hoverl{\n"
"    background-color: rgb(124, 124, 124);\n"
"}\n"
"")
        self.scrollArea_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 905, 308))
        self.scrollAreaWidgetContents_4.setStyleSheet("")
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents_4)
        self.widget_3.setStyleSheet("\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: rgb(204, 204, 204);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertica:hoverl{\n"
"    background-color: rgb(5, 74, 91);\n"
"}\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_26.setContentsMargins(100, 0, 100, -1)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.namelist_2 = QtWidgets.QFrame(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.namelist_2.sizePolicy().hasHeightForWidth())
        self.namelist_2.setSizePolicy(sizePolicy)
        self.namelist_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(241, 242, 242);\n"
"border-radius: 10px;\n"
"border: 3px solid  rgb(220, 221, 221);\n"
"min-height: 35px;\n"
"text-align: center;\n"
"text-color: rgb(0, 0, 0);\n"
"font-family: Arial;\n"
"font-size: 16px;\n"
"font-weight: bold; \n"
"}\n"
"\n"
"")
        self.namelist_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.namelist_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.namelist_2.setObjectName("namelist_2")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.namelist_2)
        self.verticalLayout_33.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_33.setSpacing(10)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.pushButton_4 = QtWidgets.QPushButton(self.namelist_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_33.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.namelist_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_33.addWidget(self.pushButton_3)
        self.pushButton_9 = QtWidgets.QPushButton(self.namelist_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_33.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.namelist_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_33.addWidget(self.pushButton_10)
        self.verticalLayout_26.addWidget(self.namelist_2, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_27.addWidget(self.widget_3)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_25.addWidget(self.scrollArea_3)
        self.stackedWidget_2.addWidget(self.screening_page)
        self.interview_page = QtWidgets.QWidget()
        self.interview_page.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"")
        self.interview_page.setObjectName("interview_page")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.interview_page)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.interview_page)
        self.scrollArea_2.setStyleSheet("\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    width: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: rgb(204, 204, 204);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertica:hoverl{\n"
"    background-color: rgb(124, 124, 124);\n"
"}\n"
"")
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 898, 343))
        self.scrollAreaWidgetContents_3.setStyleSheet("")
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_24.setContentsMargins(100, 0, 100, -1)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frame_2 = QtWidgets.QFrame(self.widget_2)
        self.frame_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(241, 242, 242);\n"
"border-radius: 10px;\n"
"border: 3px solid  rgb(220, 221, 221);\n"
"min-height: 35px;\n"
"text-align: center;\n"
"text-color: rgb(0, 0, 0);\n"
"font-family: Arial;\n"
"font-size: 16px;\n"
"font-weight: bold; \n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_10.setVerticalSpacing(10)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_10.addWidget(self.pushButton_12, 3, 0, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_10.addWidget(self.pushButton_16, 4, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_10.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_10.addWidget(self.pushButton_11, 5, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_10.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_10.addWidget(self.pushButton_17, 1, 0, 1, 1)
        self.verticalLayout_24.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_19.addWidget(self.widget_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_10.addWidget(self.scrollArea_2)
        self.stackedWidget_2.addWidget(self.interview_page)
        self.gridLayout_8.addWidget(self.stackedWidget_2, 0, 0, 1, 1)
        self.verticalLayout_14.addWidget(self.name_lists)
        self.verticalLayout_13.addWidget(self.downbody)
        self.verticalLayout_6.addWidget(self.applicant_body)
        self.stackedWidget.addWidget(self.applicants_2)
        self.job_management_2 = QtWidgets.QWidget()
        self.job_management_2.setObjectName("job_management_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.job_management_2)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.job_body = QtWidgets.QWidget(self.job_management_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.job_body.sizePolicy().hasHeightForWidth())
        self.job_body.setSizePolicy(sizePolicy)
        self.job_body.setObjectName("job_body")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.job_body)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.job_header = QtWidgets.QFrame(self.job_body)
        self.job_header.setMinimumSize(QtCore.QSize(0, 80))
        self.job_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.job_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.job_header.setObjectName("job_header")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.job_header)
        self.gridLayout_3.setContentsMargins(9, 18, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_42 = QtWidgets.QFrame(self.job_header)
        self.frame_42.setMinimumSize(QtCore.QSize(350, 0))
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.frame_42)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.label_6 = QtWidgets.QLabel(self.frame_42)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_28.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_42, 0, 0, 1, 1)
        self.frame_43 = QtWidgets.QFrame(self.job_header)
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.frame_43)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.home_2 = QtWidgets.QPushButton(self.frame_43)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.home_2.setFont(font)
        self.home_2.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.home_2.setFlat(True)
        self.home_2.setObjectName("home_2")
        self.gridLayout_29.addWidget(self.home_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_43, 0, 1, 1, 1)
        self.frame_44 = QtWidgets.QFrame(self.job_header)
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.frame_44)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_44)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_14.setFlat(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_30.addWidget(self.pushButton_14, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_44, 0, 2, 1, 1)
        self.verticalLayout_18.addWidget(self.job_header)
        self.job_body_2 = QtWidgets.QFrame(self.job_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.job_body_2.sizePolicy().hasHeightForWidth())
        self.job_body_2.setSizePolicy(sizePolicy)
        self.job_body_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.job_body_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.job_body_2.setObjectName("job_body_2")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.job_body_2)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_45 = QtWidgets.QFrame(self.job_body_2)
        self.frame_45.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.frame_45)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.label_8 = QtWidgets.QLabel(self.frame_45)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_31.addWidget(self.label_8, 0, 0, 1, 1)
        self.verticalLayout_20.addWidget(self.frame_45, 0, QtCore.Qt.AlignTop)
        self.frame_46 = QtWidgets.QFrame(self.job_body_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy)
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_46)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.frame_46)
        self.scrollArea_6.setStyleSheet("\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    width: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: rgb(204, 204, 204);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertica:hoverl{\n"
"    background-color: rgb(124, 124, 124);\n"
"}\n"
"")
        self.scrollArea_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 505, 372))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.widget_7 = QtWidgets.QWidget(self.scrollAreaWidgetContents_6)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_35.addWidget(self.widget_7)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.verticalLayout_34.addWidget(self.scrollArea_6)
        self.verticalLayout_20.addWidget(self.frame_46)
        self.verticalLayout_18.addWidget(self.job_body_2)
        self.horizontalLayout_11.addWidget(self.job_body)
        self.add_job = QtWidgets.QFrame(self.job_management_2)
        self.add_job.setMinimumSize(QtCore.QSize(400, 0))
        self.add_job.setStyleSheet("*{\n"
"background-color: rgb(226, 249, 255)\n"
"}")
        self.add_job.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_job.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_job.setObjectName("add_job")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.add_job)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_3 = QtWidgets.QFrame(self.add_job)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_31 = QtWidgets.QFrame(self.frame_3)
        self.frame_31.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.frame_31)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(226, 249, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color:rgb(226, 249, 255);\n"
"        }\n"
"")
        self.pushButton_7.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/images/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(100, 30))
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_20.addWidget(self.pushButton_7, 0, 0, 1, 1)
        self.verticalLayout_16.addWidget(self.frame_31, 0, QtCore.Qt.AlignRight)
        self.frame_30 = QtWidgets.QFrame(self.frame_3)
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.frame_30)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_5 = QtWidgets.QLabel(self.frame_30)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_19.addWidget(self.label_5, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_16.addWidget(self.frame_30)
        self.verticalLayout_15.addWidget(self.frame_3, 0, QtCore.Qt.AlignTop)
        self.frame_23 = QtWidgets.QFrame(self.add_job)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.frame_23)
        self.gridLayout_21.setSpacing(6)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_23)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 250))
        self.scrollArea.setStyleSheet("\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    width: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: rgb(204, 204, 204);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertica:hoverl{\n"
"    background-color: rgb(124, 124, 124);\n"
"}\n"
"")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 353, 878))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.widget_6 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setStyleSheet("QPlainTextEdit{\n"
"border: 3px solid #F1F2F2;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"            border: none; \n"
"            border-radius: 10px; \n"
"            background-color: rgb(5, 74, 91);\n"
"            color: rgb(255, 255, 255);\n"
"            text-align: center;\n"
"            text-color: rgb(0, 0, 0);\n"
"            font-family: Arial;\n"
"            font-size: 12px;\n"
"            font-weight: bold; \n"
"            border: 3px solid rgb(220, 221, 221);\n"
"            padding: 5px;\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_17.setHorizontalSpacing(10)
        self.gridLayout_17.setVerticalSpacing(20)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.frame_121 = QtWidgets.QFrame(self.widget_6)
        self.frame_121.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_121.setObjectName("frame_121")
        self.gridLayout_110 = QtWidgets.QGridLayout(self.frame_121)
        self.gridLayout_110.setObjectName("gridLayout_110")
        self.work_experience = QtWidgets.QPlainTextEdit(self.frame_121)
        self.work_experience.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.work_experience.setFont(font)
        self.work_experience.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.work_experience.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.work_experience.setObjectName("work_experience")
        self.gridLayout_110.addWidget(self.work_experience, 0, 0, 1, 1)
        self.add_work_expe = QtWidgets.QPushButton(self.frame_121)
        self.add_work_expe.setFlat(True)
        self.add_work_expe.setObjectName("add_work_expe")
        self.gridLayout_110.addWidget(self.add_work_expe, 0, 1, 1, 1)
        self.gridLayout_17.addWidget(self.frame_121, 4, 0, 1, 1)
        self.job_position = QtWidgets.QLineEdit(self.widget_6)
        self.job_position.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.job_position.setFont(font)
        self.job_position.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.job_position.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.job_position.setObjectName("job_position")
        self.gridLayout_17.addWidget(self.job_position, 0, 0, 1, 1)
        self.frame_119 = QtWidgets.QFrame(self.widget_6)
        self.frame_119.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_119.setObjectName("frame_119")
        self.gridLayout_108 = QtWidgets.QGridLayout(self.frame_119)
        self.gridLayout_108.setObjectName("gridLayout_108")
        self.roles_2 = QtWidgets.QPlainTextEdit(self.frame_119)
        self.roles_2.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.roles_2.setFont(font)
        self.roles_2.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.roles_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.roles_2.setObjectName("roles_2")
        self.gridLayout_108.addWidget(self.roles_2, 0, 0, 1, 1)
        self.add_roles = QtWidgets.QPushButton(self.frame_119)
        self.add_roles.setFlat(True)
        self.add_roles.setObjectName("add_roles")
        self.gridLayout_108.addWidget(self.add_roles, 0, 1, 1, 1)
        self.gridLayout_17.addWidget(self.frame_119, 2, 0, 1, 1)
        self.frame_120 = QtWidgets.QFrame(self.widget_6)
        self.frame_120.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_120.setObjectName("frame_120")
        self.gridLayout_109 = QtWidgets.QGridLayout(self.frame_120)
        self.gridLayout_109.setObjectName("gridLayout_109")
        self.add_skills = QtWidgets.QPushButton(self.frame_120)
        self.add_skills.setFlat(True)
        self.add_skills.setObjectName("add_skills")
        self.gridLayout_109.addWidget(self.add_skills, 1, 1, 1, 1)
        self.skills_3 = QtWidgets.QPlainTextEdit(self.frame_120)
        self.skills_3.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.skills_3.setFont(font)
        self.skills_3.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.skills_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.skills_3.setObjectName("skills_3")
        self.gridLayout_109.addWidget(self.skills_3, 1, 0, 1, 1)
        self.gridLayout_17.addWidget(self.frame_120, 3, 0, 1, 1)
        self.general_description = QtWidgets.QPlainTextEdit(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_description.sizePolicy().hasHeightForWidth())
        self.general_description.setSizePolicy(sizePolicy)
        self.general_description.setMinimumSize(QtCore.QSize(0, 250))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.general_description.setFont(font)
        self.general_description.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.general_description.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.general_description.setFrameShadow(QtWidgets.QFrame.Plain)
        self.general_description.setObjectName("general_description")
        self.gridLayout_17.addWidget(self.general_description, 1, 0, 1, 1)
        self.frame_122 = QtWidgets.QFrame(self.widget_6)
        self.frame_122.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_122.setObjectName("frame_122")
        self.gridLayout_111 = QtWidgets.QGridLayout(self.frame_122)
        self.gridLayout_111.setObjectName("gridLayout_111")
        self.education_requirements = QtWidgets.QPlainTextEdit(self.frame_122)
        self.education_requirements.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.education_requirements.setFont(font)
        self.education_requirements.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.education_requirements.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.education_requirements.setObjectName("education_requirements")
        self.gridLayout_111.addWidget(self.education_requirements, 0, 0, 1, 1)
        self.add_education = QtWidgets.QPushButton(self.frame_122)
        self.add_education.setFlat(True)
        self.add_education.setObjectName("add_education")
        self.gridLayout_111.addWidget(self.add_education, 0, 1, 1, 1)
        self.gridLayout_17.addWidget(self.frame_122, 5, 0, 1, 1)
        self.gridLayout_13.addWidget(self.widget_6, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_21.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout_15.addWidget(self.frame_23)
        self.frame_26 = QtWidgets.QFrame(self.add_job)
        self.frame_26.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_17.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_34 = QtWidgets.QFrame(self.frame_26)
        self.frame_34.setMinimumSize(QtCore.QSize(100, 30))
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.frame_34)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_22.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.verticalLayout_17.addWidget(self.frame_34)
        self.frame_33 = QtWidgets.QFrame(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy)
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.frame_33)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.textEdit = QtWidgets.QTextEdit(self.frame_33)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_23.addWidget(self.textEdit, 0, 0, 1, 1)
        self.verticalLayout_17.addWidget(self.frame_33)
        self.frame_32 = QtWidgets.QFrame(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy)
        self.frame_32.setMinimumSize(QtCore.QSize(100, 30))
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.frame_32)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_32)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 10px; \n"
"            background-color: rgb(5, 74, 91);\n"
"            color: rgb(255, 255, 255);\n"
"            border: 3px solid rgb(220, 221, 221);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_24.addWidget(self.pushButton_8, 0, 0, 1, 1)
        self.verticalLayout_17.addWidget(self.frame_32, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout_15.addWidget(self.frame_26)
        self.horizontalLayout_11.addWidget(self.add_job)
        self.stackedWidget.addWidget(self.job_management_2)
        self.history_2 = QtWidgets.QWidget()
        self.history_2.setObjectName("history_2")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.history_2)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.history_header = QtWidgets.QFrame(self.history_2)
        self.history_header.setMinimumSize(QtCore.QSize(0, 80))
        self.history_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.history_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.history_header.setObjectName("history_header")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.history_header)
        self.gridLayout_32.setContentsMargins(0, 10, 0, 0)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.header_2 = QtWidgets.QFrame(self.history_header)
        self.header_2.setMinimumSize(QtCore.QSize(0, 80))
        self.header_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_2.setObjectName("header_2")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.header_2)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frame_70 = QtWidgets.QFrame(self.header_2)
        self.frame_70.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_70.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_70.setObjectName("frame_70")
        self.gridLayout_47 = QtWidgets.QGridLayout(self.frame_70)
        self.gridLayout_47.setObjectName("gridLayout_47")
        self.label_12 = QtWidgets.QLabel(self.frame_70)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_47.addWidget(self.label_12, 0, 0, 1, 1)
        self.horizontalLayout_22.addWidget(self.frame_70, 0, QtCore.Qt.AlignLeft)
        self.frame_71 = QtWidgets.QFrame(self.header_2)
        self.frame_71.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_71.setObjectName("frame_71")
        self.gridLayout_48 = QtWidgets.QGridLayout(self.frame_71)
        self.gridLayout_48.setObjectName("gridLayout_48")
        self.home_3 = QtWidgets.QPushButton(self.frame_71)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.home_3.setFont(font)
        self.home_3.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.home_3.setFlat(True)
        self.home_3.setObjectName("home_3")
        self.gridLayout_48.addWidget(self.home_3, 0, 0, 1, 1)
        self.horizontalLayout_22.addWidget(self.frame_71)
        self.frame_72 = QtWidgets.QFrame(self.header_2)
        self.frame_72.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_72.setObjectName("frame_72")
        self.gridLayout_49 = QtWidgets.QGridLayout(self.frame_72)
        self.gridLayout_49.setObjectName("gridLayout_49")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_72)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_24.setFlat(True)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_49.addWidget(self.pushButton_24, 0, 0, 1, 1)
        self.horizontalLayout_22.addWidget(self.frame_72)
        self.frame_73 = QtWidgets.QFrame(self.header_2)
        self.frame_73.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_73.setObjectName("frame_73")
        self.gridLayout_50 = QtWidgets.QGridLayout(self.frame_73)
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.add_job_4 = QtWidgets.QPushButton(self.frame_73)
        self.add_job_4.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.add_job_4.setText("")
        self.add_job_4.setIcon(icon)
        self.add_job_4.setIconSize(QtCore.QSize(150, 30))
        self.add_job_4.setFlat(True)
        self.add_job_4.setObjectName("add_job_4")
        self.gridLayout_50.addWidget(self.add_job_4, 0, 0, 1, 1)
        self.horizontalLayout_22.addWidget(self.frame_73)
        self.gridLayout_32.addWidget(self.header_2, 0, 0, 1, 1)
        self.verticalLayout_21.addWidget(self.history_header)
        self.frame_48 = QtWidgets.QFrame(self.history_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy)
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.frame_48)
        self.verticalLayout_36.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.frame_8 = QtWidgets.QFrame(self.frame_48)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_13 = QtWidgets.QFrame(self.frame_8)
        self.frame_13.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("*{\n"
"background-color: white;\n"
" border: 3px solid rgb(221, 221, 221);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"}")
        self.comboBox_2.setFrame(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_37.addWidget(self.comboBox_2)
        self.horizontalLayout_4.addWidget(self.frame_13, 0, QtCore.Qt.AlignLeft)
        self.frame_14 = QtWidgets.QFrame(self.frame_8)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("*{\n"
"background-color: white;\n"
" border: 3px solid rgb(221, 221, 221);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"}")
        self.comboBox_3.setFrame(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout_38.addWidget(self.comboBox_3)
        self.horizontalLayout_4.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setContentsMargins(10, 9, 10, 9)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.frame_15)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/image/images/search.svg"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("*{\n"
"background-color: white;\n"
" border: 3px solid rgb(221, 221, 221);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        self.horizontalLayout_4.addWidget(self.frame_15, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_36.addWidget(self.frame_8, 0, QtCore.Qt.AlignTop)
        self.frame_7 = QtWidgets.QFrame(self.frame_48)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_16 = QtWidgets.QFrame(self.frame_7)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.frame_18 = QtWidgets.QFrame(self.frame_16)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.label_10 = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("*{\n"
"color: rgb(3, 53, 65);\n"
"}")
        self.label_10.setObjectName("label_10")
        self.gridLayout_33.addWidget(self.label_10, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_39.addWidget(self.frame_18)
        self.widget_8 = QtWidgets.QWidget(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.scrollArea_8 = QtWidgets.QScrollArea(self.widget_8)
        self.scrollArea_8.setStyleSheet("\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    width: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: rgb(204, 204, 204);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertica:hoverl{\n"
"    background-color: rgb(124, 124, 124);\n"
"}\n"
"")
        self.scrollArea_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 435, 322))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.frame_20 = QtWidgets.QFrame(self.scrollAreaWidgetContents_10)
        self.frame_20.setStyleSheet("QPushButton{\n"
"background-color: rgb(5, 74, 91);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(220, 221, 221);\n"
"min-height: 35px;\n"
"text-align: center;\n"
"text-color: rgb(0, 0, 0);\n"
"font-family: Arial;\n"
"font-size: 16px;\n"
"font-weight: bold; \n"
"}")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_27.setSpacing(10)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_27.addWidget(self.pushButton_23, 1, 0, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout_27.addWidget(self.pushButton_32, 4, 0, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_27.addWidget(self.pushButton_20, 0, 0, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_27.addWidget(self.pushButton_29, 3, 0, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_27.addWidget(self.pushButton_26, 2, 0, 1, 1)
        self.pushButton_35 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout_27.addWidget(self.pushButton_35, 5, 0, 1, 1)
        self.verticalLayout_42.addWidget(self.frame_20, 0, QtCore.Qt.AlignTop)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_10)
        self.verticalLayout_41.addWidget(self.scrollArea_8)
        self.verticalLayout_39.addWidget(self.widget_8)
        self.horizontalLayout_8.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_7)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.frame_19 = QtWidgets.QFrame(self.frame_17)
        self.frame_19.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.frame_19)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.label_16 = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("*{\n"
"color: rgb(91, 5, 6);\n"
"}\n"
"")
        self.label_16.setObjectName("label_16")
        self.gridLayout_34.addWidget(self.label_16, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_40.addWidget(self.frame_19, 0, QtCore.Qt.AlignTop)
        self.widget_9 = QtWidgets.QWidget(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.widget_9)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.widget_9)
        self.scrollArea_7.setStyleSheet("\n"
"\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    width: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: rgb(204, 204, 204);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertica:hoverl{\n"
"    background-color: rgb(124, 124, 124);\n"
"}\n"
"")
        self.scrollArea_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 434, 322))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.frame_21 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.frame_21.setStyleSheet("QPushButton{\n"
"background-color: rgb(91, 5, 6);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid  rgb(220, 221, 221);\n"
"min-height: 35px;\n"
"text-align: center;\n"
"text-color: rgb(0, 0, 0);\n"
"font-family: Arial;\n"
"font-size: 16px;\n"
"font-weight: bold; \n"
"}\n"
"\n"
"")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.frame_21)
        self.gridLayout_26.setVerticalSpacing(10)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.pushButton_36 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout_26.addWidget(self.pushButton_36, 4, 0, 1, 1)
        self.pushButton_38 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout_26.addWidget(self.pushButton_38, 2, 0, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_26.addWidget(self.pushButton_19, 5, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_26.addWidget(self.pushButton_18, 0, 0, 1, 1)
        self.pushButton_39 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout_26.addWidget(self.pushButton_39, 1, 0, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout_26.addWidget(self.pushButton_37, 3, 0, 1, 1)
        self.gridLayout_25.addWidget(self.frame_21, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_8)
        self.gridLayout_18.addWidget(self.scrollArea_7, 0, 0, 1, 1)
        self.verticalLayout_40.addWidget(self.widget_9)
        self.horizontalLayout_8.addWidget(self.frame_17)
        self.verticalLayout_36.addWidget(self.frame_7)
        self.verticalLayout_21.addWidget(self.frame_48)
        self.stackedWidget.addWidget(self.history_2)
        self.account_2 = QtWidgets.QWidget()
        self.account_2.setObjectName("account_2")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.account_2)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.account_header = QtWidgets.QFrame(self.account_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_header.sizePolicy().hasHeightForWidth())
        self.account_header.setSizePolicy(sizePolicy)
        self.account_header.setMinimumSize(QtCore.QSize(0, 80))
        self.account_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.account_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.account_header.setObjectName("account_header")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.account_header)
        self.gridLayout_35.setContentsMargins(0, 20, 0, 0)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.header = QtWidgets.QFrame(self.account_header)
        self.header.setMinimumSize(QtCore.QSize(0, 80))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.frame_66 = QtWidgets.QFrame(self.header)
        self.frame_66.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_66.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_66.setObjectName("frame_66")
        self.gridLayout_43 = QtWidgets.QGridLayout(self.frame_66)
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.label_11 = QtWidgets.QLabel(self.frame_66)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_43.addWidget(self.label_11, 0, 0, 1, 1)
        self.horizontalLayout_21.addWidget(self.frame_66, 0, QtCore.Qt.AlignLeft)
        self.frame_67 = QtWidgets.QFrame(self.header)
        self.frame_67.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_67.setObjectName("frame_67")
        self.gridLayout_44 = QtWidgets.QGridLayout(self.frame_67)
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.home_4 = QtWidgets.QPushButton(self.frame_67)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.home_4.setFont(font)
        self.home_4.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.home_4.setFlat(True)
        self.home_4.setObjectName("home_4")
        self.gridLayout_44.addWidget(self.home_4, 0, 0, 1, 1)
        self.horizontalLayout_21.addWidget(self.frame_67)
        self.frame_68 = QtWidgets.QFrame(self.header)
        self.frame_68.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_68.setObjectName("frame_68")
        self.gridLayout_45 = QtWidgets.QGridLayout(self.frame_68)
        self.gridLayout_45.setObjectName("gridLayout_45")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_68)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_21.setFlat(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_45.addWidget(self.pushButton_21, 0, 0, 1, 1)
        self.horizontalLayout_21.addWidget(self.frame_68)
        self.frame_69 = QtWidgets.QFrame(self.header)
        self.frame_69.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_69.setObjectName("frame_69")
        self.gridLayout_46 = QtWidgets.QGridLayout(self.frame_69)
        self.gridLayout_46.setObjectName("gridLayout_46")
        self.add_job_5 = QtWidgets.QPushButton(self.frame_69)
        self.add_job_5.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.add_job_5.setText("")
        self.add_job_5.setIcon(icon)
        self.add_job_5.setIconSize(QtCore.QSize(150, 30))
        self.add_job_5.setFlat(True)
        self.add_job_5.setObjectName("add_job_5")
        self.gridLayout_46.addWidget(self.add_job_5, 0, 0, 1, 1)
        self.horizontalLayout_21.addWidget(self.frame_69)
        self.gridLayout_35.addWidget(self.header, 0, 0, 1, 1)
        self.verticalLayout_22.addWidget(self.account_header, 0, QtCore.Qt.AlignTop)
        self.account_body = QtWidgets.QFrame(self.account_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_body.sizePolicy().hasHeightForWidth())
        self.account_body.setSizePolicy(sizePolicy)
        self.account_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.account_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.account_body.setObjectName("account_body")
        self.gridLayout_36 = QtWidgets.QGridLayout(self.account_body)
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.frame_22 = QtWidgets.QFrame(self.account_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setStyleSheet("#change_pass{\n"
"background-color: rgb(248, 248, 248);\n"
"border-radius: 20px;\n"
"border: 3px solid #F1F2F2;\n"
"\n"
"}")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.change_pass = QtWidgets.QFrame(self.frame_22)
        self.change_pass.setMinimumSize(QtCore.QSize(500, 300))
        self.change_pass.setStyleSheet("")
        self.change_pass.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.change_pass.setFrameShadow(QtWidgets.QFrame.Raised)
        self.change_pass.setObjectName("change_pass")
        self.gridLayout_39 = QtWidgets.QGridLayout(self.change_pass)
        self.gridLayout_39.setContentsMargins(50, -1, 50, -1)
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.label_19 = QtWidgets.QLabel(self.change_pass)
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("*{\n"
"\n"
"background-color: rgb(248, 248, 248);\n"
"}")
        self.label_19.setObjectName("label_19")
        self.gridLayout_39.addWidget(self.label_19, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.change_pass)
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("*{\n"
"\n"
"background-color: rgb(248, 248, 248);\n"
"}")
        self.label_20.setObjectName("label_20")
        self.gridLayout_39.addWidget(self.label_20, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.change_pass)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_39.addWidget(self.lineEdit_5, 5, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.change_pass)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_39.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.change_pass)
        self.label_18.setMinimumSize(QtCore.QSize(0, 0))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("*{\n"
"\n"
"background-color: rgb(248, 248, 248);\n"
"}")
        self.label_18.setObjectName("label_18")
        self.gridLayout_39.addWidget(self.label_18, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.change_pass)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_39.addWidget(self.lineEdit_3, 1, 0, 1, 1)
        self.frame_25 = QtWidgets.QFrame(self.change_pass)
        self.frame_25.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_25.setStyleSheet("*{\n"
"\n"
"background-color: rgb(248, 248, 248);\n"
"}")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_44.setContentsMargins(100, -1, 100, -1)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.frame_35 = QtWidgets.QFrame(self.frame_25)
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.pushButton_40 = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_40.sizePolicy().hasHeightForWidth())
        self.pushButton_40.setSizePolicy(sizePolicy)
        self.pushButton_40.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 10px; \n"
"            background-color: rgb(5, 74, 91);\n"
"            color: rgb(255, 255, 255);\n"
"            border: 3px solid rgb(220, 221, 221);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_40.setObjectName("pushButton_40")
        self.verticalLayout_45.addWidget(self.pushButton_40, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_44.addWidget(self.frame_35, 0, QtCore.Qt.AlignTop)
        self.gridLayout_39.addWidget(self.frame_25, 6, 0, 1, 1)
        self.verticalLayout_43.addWidget(self.change_pass, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_36.addWidget(self.frame_22, 1, 0, 1, 1)
        self.frame_24 = QtWidgets.QFrame(self.account_body)
        self.frame_24.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.gridLayout_37 = QtWidgets.QGridLayout(self.frame_24)
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.label_17 = QtWidgets.QLabel(self.frame_24)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_37.addWidget(self.label_17, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_36.addWidget(self.frame_24, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.verticalLayout_22.addWidget(self.account_body)
        self.stackedWidget.addWidget(self.account_2)
        self.satistics = QtWidgets.QWidget()
        self.satistics.setObjectName("satistics")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.satistics)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.stats_header = QtWidgets.QFrame(self.satistics)
        self.stats_header.setMinimumSize(QtCore.QSize(0, 80))
        self.stats_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stats_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stats_header.setObjectName("stats_header")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.stats_header)
        self.gridLayout_2.setContentsMargins(0, 20, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.header_5 = QtWidgets.QFrame(self.stats_header)
        self.header_5.setMinimumSize(QtCore.QSize(0, 80))
        self.header_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_5.setObjectName("header_5")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.header_5)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.frame_82 = QtWidgets.QFrame(self.header_5)
        self.frame_82.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_82.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_82.setObjectName("frame_82")
        self.gridLayout_59 = QtWidgets.QGridLayout(self.frame_82)
        self.gridLayout_59.setObjectName("gridLayout_59")
        self.label_15 = QtWidgets.QLabel(self.frame_82)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_59.addWidget(self.label_15, 0, 0, 1, 1)
        self.horizontalLayout_25.addWidget(self.frame_82, 0, QtCore.Qt.AlignLeft)
        self.frame_83 = QtWidgets.QFrame(self.header_5)
        self.frame_83.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_83.setObjectName("frame_83")
        self.gridLayout_60 = QtWidgets.QGridLayout(self.frame_83)
        self.gridLayout_60.setObjectName("gridLayout_60")
        self.home_5 = QtWidgets.QPushButton(self.frame_83)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.home_5.setFont(font)
        self.home_5.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.home_5.setFlat(True)
        self.home_5.setObjectName("home_5")
        self.gridLayout_60.addWidget(self.home_5, 0, 0, 1, 1)
        self.horizontalLayout_25.addWidget(self.frame_83)
        self.frame_84 = QtWidgets.QFrame(self.header_5)
        self.frame_84.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_84.setObjectName("frame_84")
        self.gridLayout_61 = QtWidgets.QGridLayout(self.frame_84)
        self.gridLayout_61.setObjectName("gridLayout_61")
        self.pushButton_33 = QtWidgets.QPushButton(self.frame_84)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_33.setFlat(True)
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout_61.addWidget(self.pushButton_33, 0, 0, 1, 1)
        self.horizontalLayout_25.addWidget(self.frame_84)
        self.frame_85 = QtWidgets.QFrame(self.header_5)
        self.frame_85.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_85.setObjectName("frame_85")
        self.gridLayout_62 = QtWidgets.QGridLayout(self.frame_85)
        self.gridLayout_62.setObjectName("gridLayout_62")
        self.pushButton_34 = QtWidgets.QPushButton(self.frame_85)
        self.pushButton_34.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 5px; \n"
"            background-color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_34.setText("")
        self.pushButton_34.setIcon(icon)
        self.pushButton_34.setIconSize(QtCore.QSize(150, 30))
        self.pushButton_34.setFlat(True)
        self.pushButton_34.setObjectName("pushButton_34")
        self.gridLayout_62.addWidget(self.pushButton_34, 0, 0, 1, 1)
        self.horizontalLayout_25.addWidget(self.frame_85)
        self.gridLayout_2.addWidget(self.header_5, 0, 0, 1, 1)
        self.verticalLayout_23.addWidget(self.stats_header)
        self.stats_body = QtWidgets.QFrame(self.satistics)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_body.sizePolicy().hasHeightForWidth())
        self.stats_body.setSizePolicy(sizePolicy)
        self.stats_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stats_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stats_body.setObjectName("stats_body")
        self.verticalLayout_23.addWidget(self.stats_body)
        self.stackedWidget.addWidget(self.satistics)
        self.profile = QtWidgets.QWidget()
        self.profile.setObjectName("profile")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.profile)
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.header_6 = QtWidgets.QWidget(self.profile)
        self.header_6.setMinimumSize(QtCore.QSize(0, 0))
        self.header_6.setStyleSheet("*{\n"
"background-color: rgb(179, 225, 236);\n"
"}")
        self.header_6.setObjectName("header_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_36 = QtWidgets.QFrame(self.header_6)
        self.frame_36.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.frame_36)
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.frame_38 = QtWidgets.QFrame(self.frame_36)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy)
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_38)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_40 = QtWidgets.QFrame(self.frame_38)
        self.frame_40.setMinimumSize(QtCore.QSize(40, 0))
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.horizontalLayout_9.addWidget(self.frame_40, 0, QtCore.Qt.AlignLeft)
        self.frame_41 = QtWidgets.QFrame(self.frame_38)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy)
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.gridLayout_40 = QtWidgets.QGridLayout(self.frame_41)
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.label_21 = QtWidgets.QLabel(self.frame_41)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_40.addWidget(self.label_21, 0, 0, 1, 1)
        self.horizontalLayout_9.addWidget(self.frame_41)
        self.verticalLayout_47.addWidget(self.frame_38)
        self.frame_39 = QtWidgets.QFrame(self.frame_36)
        self.frame_39.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.gridLayout_41 = QtWidgets.QGridLayout(self.frame_39)
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.frame_47 = QtWidgets.QFrame(self.frame_39)
        self.frame_47.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.frame_47.setFont(font)
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.gridLayout_42 = QtWidgets.QGridLayout(self.frame_47)
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.label_22 = QtWidgets.QLabel(self.frame_47)
        self.label_22.setObjectName("label_22")
        self.gridLayout_42.addWidget(self.label_22, 0, 0, 1, 1)
        self.gridLayout_41.addWidget(self.frame_47, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.frame_49 = QtWidgets.QFrame(self.frame_39)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_49.sizePolicy().hasHeightForWidth())
        self.frame_49.setSizePolicy(sizePolicy)
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.gridLayout_63 = QtWidgets.QGridLayout(self.frame_49)
        self.gridLayout_63.setObjectName("gridLayout_63")
        self.label_23 = QtWidgets.QLabel(self.frame_49)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_63.addWidget(self.label_23, 0, 0, 1, 1)
        self.gridLayout_41.addWidget(self.frame_49, 0, 2, 1, 1)
        self.verticalLayout_47.addWidget(self.frame_39, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.frame_36, 0, QtCore.Qt.AlignLeft)
        self.frame_37 = QtWidgets.QFrame(self.header_6)
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.frame_51 = QtWidgets.QFrame(self.frame_37)
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.gridLayout_65 = QtWidgets.QGridLayout(self.frame_51)
        self.gridLayout_65.setObjectName("gridLayout_65")
        self.label_24 = QtWidgets.QLabel(self.frame_51)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_65.addWidget(self.label_24, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_48.addWidget(self.frame_51)
        self.frame_50 = QtWidgets.QFrame(self.frame_37)
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_50)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_52 = QtWidgets.QFrame(self.frame_50)
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.gridLayout_66 = QtWidgets.QGridLayout(self.frame_52)
        self.gridLayout_66.setObjectName("gridLayout_66")
        self.pushButton_41 = QtWidgets.QPushButton(self.frame_52)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 10px; \n"
"            background-color: rgb(91, 5, 6);\n"
"            color: rgb(255, 255, 255);\n"
"            border: 3px solid rgb(220, 221, 221);\n"
"            padding: 10px;\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_41.setFlat(True)
        self.pushButton_41.setObjectName("pushButton_41")
        self.gridLayout_66.addWidget(self.pushButton_41, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_10.addWidget(self.frame_52)
        self.frame_53 = QtWidgets.QFrame(self.frame_50)
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.gridLayout_67 = QtWidgets.QGridLayout(self.frame_53)
        self.gridLayout_67.setObjectName("gridLayout_67")
        self.approve = QtWidgets.QPushButton(self.frame_53)
        self.approve.setMinimumSize(QtCore.QSize(116, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.approve.setFont(font)
        self.approve.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 10px; \n"
"            background-color: rgb(5, 74, 91);\n"
"            color: rgb(255, 255, 255);\n"
"            border: 3px solid rgb(220, 221, 221);\n"
"            padding: 10px;\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }")
        self.approve.setFlat(True)
        self.approve.setObjectName("approve")
        self.gridLayout_67.addWidget(self.approve, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_10.addWidget(self.frame_53)
        self.verticalLayout_48.addWidget(self.frame_50)
        self.horizontalLayout_2.addWidget(self.frame_37, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_46.addWidget(self.header_6, 0, QtCore.Qt.AlignTop)
        self.profile_body = QtWidgets.QWidget(self.profile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_body.sizePolicy().hasHeightForWidth())
        self.profile_body.setSizePolicy(sizePolicy)
        self.profile_body.setStyleSheet("*{\n"
"background-color: rgb(179, 225, 236);\n"
"}")
        self.profile_body.setObjectName("profile_body")
        self.gridLayout_64 = QtWidgets.QGridLayout(self.profile_body)
        self.gridLayout_64.setObjectName("gridLayout_64")
        self.scrollArea_9 = QtWidgets.QScrollArea(self.profile_body)
        self.scrollArea_9.setStyleSheet("QScrollBar:vertical{\n"
"    border: none;\n"
"    width: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: rgb(204, 204, 204);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertica:hoverl{\n"
"    background-color: rgb(124, 124, 124);\n"
"}\n"
"")
        self.scrollArea_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setObjectName("scrollArea_9")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 902, 1108))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.gridLayout_68 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_68.setObjectName("gridLayout_68")
        self.frame_58 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.gridLayout_382 = QtWidgets.QGridLayout(self.frame_58)
        self.gridLayout_382.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_382.setObjectName("gridLayout_382")
        self.personal_info_16 = QtWidgets.QFrame(self.frame_58)
        self.personal_info_16.setMinimumSize(QtCore.QSize(0, 190))
        self.personal_info_16.setStyleSheet("*{\n"
"background-color: rgb(248, 248, 248);\n"
"}\n"
"")
        self.personal_info_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.personal_info_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.personal_info_16.setObjectName("personal_info_16")
        self.verticalLayout_83 = QtWidgets.QVBoxLayout(self.personal_info_16)
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName("verticalLayout_83")
        self.frame_270 = QtWidgets.QFrame(self.personal_info_16)
        self.frame_270.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_270.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_270.setObjectName("frame_270")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.frame_270)
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_51.setSpacing(2)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.frame_271 = QtWidgets.QFrame(self.frame_270)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_271.sizePolicy().hasHeightForWidth())
        self.frame_271.setSizePolicy(sizePolicy)
        self.frame_271.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_271.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_271.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_271.setObjectName("frame_271")
        self.gridLayout_366 = QtWidgets.QGridLayout(self.frame_271)
        self.gridLayout_366.setObjectName("gridLayout_366")
        self.label_168 = QtWidgets.QLabel(self.frame_271)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_168.setFont(font)
        self.label_168.setObjectName("label_168")
        self.gridLayout_366.addWidget(self.label_168, 0, 0, 1, 1)
        self.degreee = QtWidgets.QFrame(self.frame_271)
        self.degreee.setMinimumSize(QtCore.QSize(0, 40))
        self.degreee.setStyleSheet("#degreee{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.degreee.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.degreee.setFrameShadow(QtWidgets.QFrame.Raised)
        self.degreee.setObjectName("degreee")
        self.gridLayout_367 = QtWidgets.QGridLayout(self.degreee)
        self.gridLayout_367.setObjectName("gridLayout_367")
        self.degree = QtWidgets.QLabel(self.degreee)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.degree.setFont(font)
        self.degree.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.degree.setObjectName("degree")
        self.gridLayout_367.addWidget(self.degree, 0, 0, 1, 1)
        self.gridLayout_366.addWidget(self.degreee, 1, 0, 1, 1)
        self.horizontalLayout_51.addWidget(self.frame_271)
        self.frame_272 = QtWidgets.QFrame(self.frame_270)
        self.frame_272.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_272.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_272.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_272.setObjectName("frame_272")
        self.gridLayout_368 = QtWidgets.QGridLayout(self.frame_272)
        self.gridLayout_368.setObjectName("gridLayout_368")
        self.label_169 = QtWidgets.QLabel(self.frame_272)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_169.setFont(font)
        self.label_169.setObjectName("label_169")
        self.gridLayout_368.addWidget(self.label_169, 0, 0, 1, 1)
        self.insti = QtWidgets.QFrame(self.frame_272)
        self.insti.setMinimumSize(QtCore.QSize(0, 40))
        self.insti.setStyleSheet("#insti{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.insti.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.insti.setFrameShadow(QtWidgets.QFrame.Raised)
        self.insti.setObjectName("insti")
        self.gridLayout_369 = QtWidgets.QGridLayout(self.insti)
        self.gridLayout_369.setObjectName("gridLayout_369")
        self.institution = QtWidgets.QLabel(self.insti)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.institution.setFont(font)
        self.institution.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.institution.setObjectName("institution")
        self.gridLayout_369.addWidget(self.institution, 0, 0, 1, 1)
        self.gridLayout_368.addWidget(self.insti, 1, 0, 1, 1)
        self.horizontalLayout_51.addWidget(self.frame_272)
        self.verticalLayout_83.addWidget(self.frame_270)
        self.frame_275 = QtWidgets.QFrame(self.personal_info_16)
        self.frame_275.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_275.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_275.setObjectName("frame_275")
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout(self.frame_275)
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_52.setSpacing(50)
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.frame_276 = QtWidgets.QFrame(self.frame_275)
        self.frame_276.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_276.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_276.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_276.setObjectName("frame_276")
        self.gridLayout_374 = QtWidgets.QGridLayout(self.frame_276)
        self.gridLayout_374.setObjectName("gridLayout_374")
        self.label_172 = QtWidgets.QLabel(self.frame_276)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_172.setFont(font)
        self.label_172.setObjectName("label_172")
        self.gridLayout_374.addWidget(self.label_172, 0, 0, 1, 1)
        self.grad = QtWidgets.QFrame(self.frame_276)
        self.grad.setMinimumSize(QtCore.QSize(0, 40))
        self.grad.setStyleSheet("#grad{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.grad.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.grad.setFrameShadow(QtWidgets.QFrame.Raised)
        self.grad.setObjectName("grad")
        self.gridLayout_375 = QtWidgets.QGridLayout(self.grad)
        self.gridLayout_375.setObjectName("gridLayout_375")
        self.graduation_date = QtWidgets.QLabel(self.grad)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.graduation_date.setFont(font)
        self.graduation_date.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.graduation_date.setObjectName("graduation_date")
        self.gridLayout_375.addWidget(self.graduation_date, 0, 0, 1, 1)
        self.gridLayout_374.addWidget(self.grad, 1, 0, 1, 1)
        self.horizontalLayout_52.addWidget(self.frame_276, 0, QtCore.Qt.AlignLeft)
        self.frame_277 = QtWidgets.QFrame(self.frame_275)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_277.sizePolicy().hasHeightForWidth())
        self.frame_277.setSizePolicy(sizePolicy)
        self.frame_277.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_277.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_277.setObjectName("frame_277")
        self.gridLayout_376 = QtWidgets.QGridLayout(self.frame_277)
        self.gridLayout_376.setObjectName("gridLayout_376")
        self.label_173 = QtWidgets.QLabel(self.frame_277)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_173.setFont(font)
        self.label_173.setObjectName("label_173")
        self.gridLayout_376.addWidget(self.label_173, 0, 0, 1, 1)
        self.award = QtWidgets.QFrame(self.frame_277)
        self.award.setMinimumSize(QtCore.QSize(0, 40))
        self.award.setStyleSheet("#award{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.award.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.award.setFrameShadow(QtWidgets.QFrame.Raised)
        self.award.setObjectName("award")
        self.gridLayout_377 = QtWidgets.QGridLayout(self.award)
        self.gridLayout_377.setObjectName("gridLayout_377")
        self.awards = QtWidgets.QLabel(self.award)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.awards.setFont(font)
        self.awards.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.awards.setObjectName("awards")
        self.gridLayout_377.addWidget(self.awards, 0, 0, 1, 1)
        self.gridLayout_376.addWidget(self.award, 1, 0, 1, 1)
        self.horizontalLayout_52.addWidget(self.frame_277)
        self.frame_55 = QtWidgets.QFrame(self.frame_275)
        self.frame_55.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.frame_55)
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.frame_86 = QtWidgets.QFrame(self.frame_55)
        self.frame_86.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_86.setObjectName("frame_86")
        self.verticalLayout_51.addWidget(self.frame_86)
        self.frame_59 = QtWidgets.QFrame(self.frame_55)
        self.frame_59.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59.setObjectName("frame_59")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_59)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_87 = QtWidgets.QFrame(self.frame_59)
        self.frame_87.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_87.setObjectName("frame_87")
        self.gridLayout_71 = QtWidgets.QGridLayout(self.frame_87)
        self.gridLayout_71.setObjectName("gridLayout_71")
        self.pushButton_43 = QtWidgets.QPushButton(self.frame_87)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 10px; \n"
"            background-color: rgb(91, 5, 6);\n"
"            color: rgb(255, 255, 255);\n"
"            border: 3px solid rgb(220, 221, 221);\n"
"            padding: 5px;\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_43.setFlat(True)
        self.pushButton_43.setObjectName("pushButton_43")
        self.gridLayout_71.addWidget(self.pushButton_43, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_29 = QtWidgets.QLabel(self.frame_87)
        self.label_29.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 10px; \n"
"            background-color: rgb(91, 5, 6);\n"
"            color: rgb(255, 255, 255);\n"
"            border: 3px solid rgb(220, 221, 221);\n"
"            padding: 10px;\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.gridLayout_71.addWidget(self.label_29, 0, 1, 1, 1)
        self.horizontalLayout_14.addWidget(self.frame_87, 0, QtCore.Qt.AlignHCenter)
        self.frame_89 = QtWidgets.QFrame(self.frame_59)
        self.frame_89.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_89.setObjectName("frame_89")
        self.gridLayout_88 = QtWidgets.QGridLayout(self.frame_89)
        self.gridLayout_88.setObjectName("gridLayout_88")
        self.pushButton_44 = QtWidgets.QPushButton(self.frame_89)
        self.pushButton_44.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 10px; \n"
"            background-color: rgb(5, 74, 91);\n"
"            color: rgb(255, 255, 255);\n"
"            border: 3px solid rgb(220, 221, 221);\n"
"            padding: 5px;\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }")
        self.pushButton_44.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_44.setFlat(True)
        self.pushButton_44.setObjectName("pushButton_44")
        self.gridLayout_88.addWidget(self.pushButton_44, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_14.addWidget(self.frame_89)
        self.verticalLayout_51.addWidget(self.frame_59)
        self.horizontalLayout_52.addWidget(self.frame_55)
        self.verticalLayout_83.addWidget(self.frame_275)
        self.gridLayout_382.addWidget(self.personal_info_16, 1, 0, 1, 1)
        self.label_176 = QtWidgets.QLabel(self.frame_58)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_176.setFont(font)
        self.label_176.setObjectName("label_176")
        self.gridLayout_382.addWidget(self.label_176, 0, 0, 1, 1)
        self.gridLayout_68.addWidget(self.frame_58, 1, 0, 1, 1)
        self.widget_10 = QtWidgets.QWidget(self.scrollAreaWidgetContents_7)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.frame_54 = QtWidgets.QFrame(self.widget_10)
        self.frame_54.setStyleSheet("#personal_info{\n"
"background-color: rgb(248, 248, 248);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.gridLayout_70 = QtWidgets.QGridLayout(self.frame_54)
        self.gridLayout_70.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_70.setObjectName("gridLayout_70")
        self.frame_56 = QtWidgets.QFrame(self.frame_54)
        self.frame_56.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_56.setStyleSheet("")
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.gridLayout_69 = QtWidgets.QGridLayout(self.frame_56)
        self.gridLayout_69.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_69.setSpacing(0)
        self.gridLayout_69.setObjectName("gridLayout_69")
        self.personal_info = QtWidgets.QFrame(self.frame_56)
        self.personal_info.setMinimumSize(QtCore.QSize(0, 190))
        self.personal_info.setStyleSheet("*{\n"
"background-color: rgb(248, 248, 248);\n"
"}\n"
"")
        self.personal_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.personal_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.personal_info.setObjectName("personal_info")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.personal_info)
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.frame_57 = QtWidgets.QFrame(self.personal_info)
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_57)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_61 = QtWidgets.QFrame(self.frame_57)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_61.sizePolicy().hasHeightForWidth())
        self.frame_61.setSizePolicy(sizePolicy)
        self.frame_61.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_61.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.gridLayout_76 = QtWidgets.QGridLayout(self.frame_61)
        self.gridLayout_76.setObjectName("gridLayout_76")
        self.label_26 = QtWidgets.QLabel(self.frame_61)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_76.addWidget(self.label_26, 0, 0, 1, 1)
        self.name = QtWidgets.QFrame(self.frame_61)
        self.name.setMinimumSize(QtCore.QSize(0, 40))
        self.name.setStyleSheet("#name{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.name.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name.setObjectName("name")
        self.gridLayout_79 = QtWidgets.QGridLayout(self.name)
        self.gridLayout_79.setObjectName("gridLayout_79")
        self.first_name = QtWidgets.QLabel(self.name)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.first_name.setFont(font)
        self.first_name.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.first_name.setObjectName("first_name")
        self.gridLayout_79.addWidget(self.first_name, 0, 0, 1, 1)
        self.gridLayout_76.addWidget(self.name, 1, 0, 1, 1)
        self.horizontalLayout_12.addWidget(self.frame_61)
        self.frame_62 = QtWidgets.QFrame(self.frame_57)
        self.frame_62.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_62.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_62.setObjectName("frame_62")
        self.gridLayout_72 = QtWidgets.QGridLayout(self.frame_62)
        self.gridLayout_72.setObjectName("gridLayout_72")
        self.label_30 = QtWidgets.QLabel(self.frame_62)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.gridLayout_72.addWidget(self.label_30, 0, 0, 1, 1)
        self.m_name = QtWidgets.QFrame(self.frame_62)
        self.m_name.setMinimumSize(QtCore.QSize(0, 40))
        self.m_name.setStyleSheet("#m_name{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.m_name.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m_name.setObjectName("m_name")
        self.gridLayout_80 = QtWidgets.QGridLayout(self.m_name)
        self.gridLayout_80.setObjectName("gridLayout_80")
        self.middle_name = QtWidgets.QLabel(self.m_name)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.middle_name.setFont(font)
        self.middle_name.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.middle_name.setObjectName("middle_name")
        self.gridLayout_80.addWidget(self.middle_name, 0, 0, 1, 1)
        self.gridLayout_72.addWidget(self.m_name, 1, 0, 1, 1)
        self.horizontalLayout_12.addWidget(self.frame_62)
        self.frame_63 = QtWidgets.QFrame(self.frame_57)
        self.frame_63.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_63.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_63.setObjectName("frame_63")
        self.gridLayout_77 = QtWidgets.QGridLayout(self.frame_63)
        self.gridLayout_77.setObjectName("gridLayout_77")
        self.label_31 = QtWidgets.QLabel(self.frame_63)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_77.addWidget(self.label_31, 0, 0, 1, 1)
        self.l_name = QtWidgets.QFrame(self.frame_63)
        self.l_name.setMinimumSize(QtCore.QSize(0, 40))
        self.l_name.setStyleSheet("#l_name{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.l_name.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.l_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.l_name.setObjectName("l_name")
        self.gridLayout_81 = QtWidgets.QGridLayout(self.l_name)
        self.gridLayout_81.setObjectName("gridLayout_81")
        self.last_name = QtWidgets.QLabel(self.l_name)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.last_name.setFont(font)
        self.last_name.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.last_name.setObjectName("last_name")
        self.gridLayout_81.addWidget(self.last_name, 0, 0, 1, 1)
        self.gridLayout_77.addWidget(self.l_name, 1, 0, 1, 1)
        self.horizontalLayout_12.addWidget(self.frame_63)
        self.frame_64 = QtWidgets.QFrame(self.frame_57)
        self.frame_64.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_64.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_64.setObjectName("frame_64")
        self.gridLayout_78 = QtWidgets.QGridLayout(self.frame_64)
        self.gridLayout_78.setObjectName("gridLayout_78")
        self.label_32 = QtWidgets.QLabel(self.frame_64)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gridLayout_78.addWidget(self.label_32, 0, 0, 1, 1)
        self.agee = QtWidgets.QFrame(self.frame_64)
        self.agee.setMinimumSize(QtCore.QSize(0, 0))
        self.agee.setMaximumSize(QtCore.QSize(50, 16777215))
        self.agee.setStyleSheet("#agee{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.agee.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.agee.setFrameShadow(QtWidgets.QFrame.Raised)
        self.agee.setObjectName("agee")
        self.gridLayout_82 = QtWidgets.QGridLayout(self.agee)
        self.gridLayout_82.setObjectName("gridLayout_82")
        self.age = QtWidgets.QLabel(self.agee)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.age.setFont(font)
        self.age.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.age.setObjectName("age")
        self.gridLayout_82.addWidget(self.age, 0, 0, 1, 1)
        self.gridLayout_78.addWidget(self.agee, 1, 0, 1, 1)
        self.horizontalLayout_12.addWidget(self.frame_64)
        self.verticalLayout_50.addWidget(self.frame_57)
        self.frame_60 = QtWidgets.QFrame(self.personal_info)
        self.frame_60.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_60)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_88 = QtWidgets.QFrame(self.frame_60)
        self.frame_88.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_88.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_88.setObjectName("frame_88")
        self.gridLayout_73 = QtWidgets.QGridLayout(self.frame_88)
        self.gridLayout_73.setObjectName("gridLayout_73")
        self.label_27 = QtWidgets.QLabel(self.frame_88)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_73.addWidget(self.label_27, 0, 0, 1, 1)
        self.email = QtWidgets.QFrame(self.frame_88)
        self.email.setMinimumSize(QtCore.QSize(0, 40))
        self.email.setStyleSheet("#email{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.email.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.email.setFrameShadow(QtWidgets.QFrame.Raised)
        self.email.setObjectName("email")
        self.gridLayout_83 = QtWidgets.QGridLayout(self.email)
        self.gridLayout_83.setObjectName("gridLayout_83")
        self.email_address = QtWidgets.QLabel(self.email)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.email_address.setFont(font)
        self.email_address.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.email_address.setObjectName("email_address")
        self.gridLayout_83.addWidget(self.email_address, 0, 0, 1, 1)
        self.gridLayout_73.addWidget(self.email, 1, 0, 1, 1)
        self.horizontalLayout_13.addWidget(self.frame_88)
        self.frame_91 = QtWidgets.QFrame(self.frame_60)
        self.frame_91.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_91.setObjectName("frame_91")
        self.gridLayout_74 = QtWidgets.QGridLayout(self.frame_91)
        self.gridLayout_74.setObjectName("gridLayout_74")
        self.label_28 = QtWidgets.QLabel(self.frame_91)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_74.addWidget(self.label_28, 0, 0, 1, 1)
        self.primary = QtWidgets.QFrame(self.frame_91)
        self.primary.setMinimumSize(QtCore.QSize(0, 40))
        self.primary.setStyleSheet("#primary{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.primary.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.primary.setFrameShadow(QtWidgets.QFrame.Raised)
        self.primary.setObjectName("primary")
        self.gridLayout_84 = QtWidgets.QGridLayout(self.primary)
        self.gridLayout_84.setObjectName("gridLayout_84")
        self.primary_phone_number = QtWidgets.QLabel(self.primary)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.primary_phone_number.setFont(font)
        self.primary_phone_number.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.primary_phone_number.setObjectName("primary_phone_number")
        self.gridLayout_84.addWidget(self.primary_phone_number, 0, 0, 1, 1)
        self.gridLayout_74.addWidget(self.primary, 1, 0, 1, 1)
        self.horizontalLayout_13.addWidget(self.frame_91)
        self.frame_65 = QtWidgets.QFrame(self.frame_60)
        self.frame_65.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_65.setObjectName("frame_65")
        self.gridLayout_86 = QtWidgets.QGridLayout(self.frame_65)
        self.gridLayout_86.setObjectName("gridLayout_86")
        self.label_33 = QtWidgets.QLabel(self.frame_65)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout_86.addWidget(self.label_33, 0, 0, 1, 1)
        self.secondary = QtWidgets.QFrame(self.frame_65)
        self.secondary.setMinimumSize(QtCore.QSize(0, 40))
        self.secondary.setStyleSheet("#secondary{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.secondary.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.secondary.setFrameShadow(QtWidgets.QFrame.Raised)
        self.secondary.setObjectName("secondary")
        self.gridLayout_85 = QtWidgets.QGridLayout(self.secondary)
        self.gridLayout_85.setObjectName("gridLayout_85")
        self.secondary_phone_number = QtWidgets.QLabel(self.secondary)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.secondary_phone_number.setFont(font)
        self.secondary_phone_number.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.secondary_phone_number.setObjectName("secondary_phone_number")
        self.gridLayout_85.addWidget(self.secondary_phone_number, 0, 0, 1, 1)
        self.gridLayout_86.addWidget(self.secondary, 1, 0, 1, 1)
        self.horizontalLayout_13.addWidget(self.frame_65)
        self.frame_94 = QtWidgets.QFrame(self.frame_60)
        self.frame_94.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_94.setObjectName("frame_94")
        self.verticalLayout_54 = QtWidgets.QVBoxLayout(self.frame_94)
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_54.setSpacing(1)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.frame_95 = QtWidgets.QFrame(self.frame_94)
        self.frame_95.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_95.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_95.setObjectName("frame_95")
        self.gridLayout_75 = QtWidgets.QGridLayout(self.frame_95)
        self.gridLayout_75.setObjectName("gridLayout_75")
        self.label_34 = QtWidgets.QLabel(self.frame_95)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout_75.addWidget(self.label_34, 0, 0, 1, 1)
        self.address = QtWidgets.QFrame(self.frame_95)
        self.address.setMinimumSize(QtCore.QSize(0, 40))
        self.address.setStyleSheet("#address{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.address.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.address.setFrameShadow(QtWidgets.QFrame.Raised)
        self.address.setObjectName("address")
        self.gridLayout_87 = QtWidgets.QGridLayout(self.address)
        self.gridLayout_87.setObjectName("gridLayout_87")
        self.city_address = QtWidgets.QLabel(self.address)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.city_address.setFont(font)
        self.city_address.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.city_address.setObjectName("city_address")
        self.gridLayout_87.addWidget(self.city_address, 0, 0, 1, 1)
        self.gridLayout_75.addWidget(self.address, 1, 0, 1, 1)
        self.verticalLayout_54.addWidget(self.frame_95)
        self.horizontalLayout_13.addWidget(self.frame_94)
        self.verticalLayout_50.addWidget(self.frame_60)
        self.gridLayout_69.addWidget(self.personal_info, 1, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.frame_56)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_69.addWidget(self.label_25, 0, 0, 1, 1)
        self.gridLayout_70.addWidget(self.frame_56, 0, 0, 1, 1)
        self.verticalLayout_49.addWidget(self.frame_54)
        self.gridLayout_68.addWidget(self.widget_10, 0, 0, 1, 1)
        self.frame_98 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
        self.frame_98.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_98.setObjectName("frame_98")
        self.gridLayout_95 = QtWidgets.QGridLayout(self.frame_98)
        self.gridLayout_95.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_95.setObjectName("gridLayout_95")
        self.label_186 = QtWidgets.QLabel(self.frame_98)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_186.setFont(font)
        self.label_186.setObjectName("label_186")
        self.gridLayout_95.addWidget(self.label_186, 0, 0, 1, 1)
        self.personal_info_18 = QtWidgets.QFrame(self.frame_98)
        self.personal_info_18.setMinimumSize(QtCore.QSize(0, 190))
        self.personal_info_18.setStyleSheet("*{\n"
"background-color: rgb(248, 248, 248);\n"
"}\n"
"")
        self.personal_info_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.personal_info_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.personal_info_18.setObjectName("personal_info_18")
        self.verticalLayout_86 = QtWidgets.QVBoxLayout(self.personal_info_18)
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName("verticalLayout_86")
        self.frame_286 = QtWidgets.QFrame(self.personal_info_18)
        self.frame_286.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_286.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_286.setObjectName("frame_286")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout(self.frame_286)
        self.horizontalLayout_55.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_55.setSpacing(2)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.frame_288 = QtWidgets.QFrame(self.frame_286)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_288.sizePolicy().hasHeightForWidth())
        self.frame_288.setSizePolicy(sizePolicy)
        self.frame_288.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_288.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_288.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_288.setObjectName("frame_288")
        self.gridLayout_389 = QtWidgets.QGridLayout(self.frame_288)
        self.gridLayout_389.setObjectName("gridLayout_389")
        self.label_180 = QtWidgets.QLabel(self.frame_288)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_180.setFont(font)
        self.label_180.setObjectName("label_180")
        self.gridLayout_389.addWidget(self.label_180, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.hire = QtWidgets.QFrame(self.frame_288)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hire.sizePolicy().hasHeightForWidth())
        self.hire.setSizePolicy(sizePolicy)
        self.hire.setMinimumSize(QtCore.QSize(0, 0))
        self.hire.setStyleSheet("#hire{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.hire.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hire.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hire.setObjectName("hire")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.hire)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.linked = QtWidgets.QLabel(self.hire)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.linked.setFont(font)
        self.linked.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.linked.setObjectName("linked")
        self.verticalLayout_52.addWidget(self.linked)
        self.indeed = QtWidgets.QLabel(self.hire)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.indeed.setFont(font)
        self.indeed.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.indeed.setObjectName("indeed")
        self.verticalLayout_52.addWidget(self.indeed)
        self.facebook = QtWidgets.QLabel(self.hire)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.facebook.setFont(font)
        self.facebook.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.facebook.setObjectName("facebook")
        self.verticalLayout_52.addWidget(self.facebook)
        self.referral = QtWidgets.QLabel(self.hire)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.referral.setFont(font)
        self.referral.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.referral.setObjectName("referral")
        self.verticalLayout_52.addWidget(self.referral)
        self.others = QtWidgets.QLabel(self.hire)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.others.setFont(font)
        self.others.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.others.setObjectName("others")
        self.verticalLayout_52.addWidget(self.others)
        self.indeed.raise_()
        self.facebook.raise_()
        self.linked.raise_()
        self.referral.raise_()
        self.others.raise_()
        self.gridLayout_389.addWidget(self.hire, 1, 0, 1, 1)
        self.horizontalLayout_55.addWidget(self.frame_288, 0, QtCore.Qt.AlignLeft)
        self.frame_290 = QtWidgets.QFrame(self.frame_286)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_290.sizePolicy().hasHeightForWidth())
        self.frame_290.setSizePolicy(sizePolicy)
        self.frame_290.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_290.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_290.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_290.setObjectName("frame_290")
        self.gridLayout_391 = QtWidgets.QGridLayout(self.frame_290)
        self.gridLayout_391.setObjectName("gridLayout_391")
        self.namee = QtWidgets.QFrame(self.frame_290)
        self.namee.setMinimumSize(QtCore.QSize(0, 40))
        self.namee.setStyleSheet("#namee{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.namee.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.namee.setFrameShadow(QtWidgets.QFrame.Raised)
        self.namee.setObjectName("namee")
        self.gridLayout_392 = QtWidgets.QGridLayout(self.namee)
        self.gridLayout_392.setObjectName("gridLayout_392")
        self.company_name = QtWidgets.QLabel(self.namee)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.company_name.setFont(font)
        self.company_name.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.company_name.setObjectName("company_name")
        self.gridLayout_392.addWidget(self.company_name, 0, 0, 1, 1)
        self.gridLayout_391.addWidget(self.namee, 3, 0, 1, 1)
        self.label_181 = QtWidgets.QLabel(self.frame_290)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_181.setFont(font)
        self.label_181.setObjectName("label_181")
        self.gridLayout_391.addWidget(self.label_181, 0, 0, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.frame_290)
        self.label_41.setObjectName("label_41")
        self.gridLayout_391.addWidget(self.label_41, 2, 0, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.frame_290)
        self.label_42.setObjectName("label_42")
        self.gridLayout_391.addWidget(self.label_42, 1, 0, 1, 1)
        self.frame_99 = QtWidgets.QFrame(self.frame_290)
        self.frame_99.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_99.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_99.setObjectName("frame_99")
        self.gridLayout_391.addWidget(self.frame_99, 4, 0, 1, 1)
        self.horizontalLayout_55.addWidget(self.frame_290)
        self.frame_291 = QtWidgets.QFrame(self.frame_286)
        self.frame_291.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_291.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_291.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_291.setObjectName("frame_291")
        self.gridLayout_395 = QtWidgets.QGridLayout(self.frame_291)
        self.gridLayout_395.setObjectName("gridLayout_395")
        self.numm = QtWidgets.QFrame(self.frame_291)
        self.numm.setMinimumSize(QtCore.QSize(0, 40))
        self.numm.setStyleSheet("#numm{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.numm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.numm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.numm.setObjectName("numm")
        self.gridLayout_396 = QtWidgets.QGridLayout(self.numm)
        self.gridLayout_396.setObjectName("gridLayout_396")
        self.reference_number = QtWidgets.QLabel(self.numm)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.reference_number.setFont(font)
        self.reference_number.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.reference_number.setObjectName("reference_number")
        self.gridLayout_396.addWidget(self.reference_number, 0, 0, 1, 1)
        self.gridLayout_395.addWidget(self.numm, 1, 0, 1, 1)
        self.label_183 = QtWidgets.QLabel(self.frame_291)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_183.setFont(font)
        self.label_183.setObjectName("label_183")
        self.gridLayout_395.addWidget(self.label_183, 0, 0, 1, 1)
        self.frame_100 = QtWidgets.QFrame(self.frame_291)
        self.frame_100.setMinimumSize(QtCore.QSize(0, 55))
        self.frame_100.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_100.setObjectName("frame_100")
        self.gridLayout_395.addWidget(self.frame_100, 2, 0, 1, 1)
        self.horizontalLayout_55.addWidget(self.frame_291, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_86.addWidget(self.frame_286)
        self.gridLayout_95.addWidget(self.personal_info_18, 1, 0, 1, 1)
        self.gridLayout_68.addWidget(self.frame_98, 3, 0, 1, 1)
        self.frame_101 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
        self.frame_101.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_101.setObjectName("frame_101")
        self.gridLayout_96 = QtWidgets.QGridLayout(self.frame_101)
        self.gridLayout_96.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_96.setObjectName("gridLayout_96")
        self.label_187 = QtWidgets.QLabel(self.frame_101)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_187.setFont(font)
        self.label_187.setObjectName("label_187")
        self.gridLayout_96.addWidget(self.label_187, 0, 0, 1, 1)
        self.personal_info_19 = QtWidgets.QFrame(self.frame_101)
        self.personal_info_19.setMinimumSize(QtCore.QSize(0, 190))
        self.personal_info_19.setStyleSheet("*{\n"
"background-color: rgb(248, 248, 248);\n"
"}\n"
"")
        self.personal_info_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.personal_info_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.personal_info_19.setObjectName("personal_info_19")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.personal_info_19)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.frame_102 = QtWidgets.QFrame(self.personal_info_19)
        self.frame_102.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_102.setObjectName("frame_102")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.frame_102)
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.frame_105 = QtWidgets.QFrame(self.frame_102)
        self.frame_105.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_105.setObjectName("frame_105")
        self.gridLayout_92 = QtWidgets.QGridLayout(self.frame_105)
        self.gridLayout_92.setObjectName("gridLayout_92")
        self.label_184 = QtWidgets.QLabel(self.frame_105)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_184.setFont(font)
        self.label_184.setObjectName("label_184")
        self.gridLayout_92.addWidget(self.label_184, 0, 0, 1, 1)
        self.years = QtWidgets.QFrame(self.frame_105)
        self.years.setMinimumSize(QtCore.QSize(0, 40))
        self.years.setStyleSheet("#years{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.years.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.years.setFrameShadow(QtWidgets.QFrame.Raised)
        self.years.setObjectName("years")
        self.gridLayout_390 = QtWidgets.QGridLayout(self.years)
        self.gridLayout_390.setObjectName("gridLayout_390")
        self.years_role_applied = QtWidgets.QLabel(self.years)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.years_role_applied.setFont(font)
        self.years_role_applied.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.years_role_applied.setObjectName("years_role_applied")
        self.gridLayout_390.addWidget(self.years_role_applied, 0, 0, 1, 1)
        self.gridLayout_92.addWidget(self.years, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout_53.addWidget(self.frame_105)
        self.frame_104 = QtWidgets.QFrame(self.frame_102)
        self.frame_104.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_104.setObjectName("frame_104")
        self.gridLayout_93 = QtWidgets.QGridLayout(self.frame_104)
        self.gridLayout_93.setObjectName("gridLayout_93")
        self.label_188 = QtWidgets.QLabel(self.frame_104)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_188.setFont(font)
        self.label_188.setObjectName("label_188")
        self.gridLayout_93.addWidget(self.label_188, 0, 0, 1, 1)
        self.employ = QtWidgets.QFrame(self.frame_104)
        self.employ.setMinimumSize(QtCore.QSize(0, 40))
        self.employ.setStyleSheet("#employ{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.employ.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.employ.setFrameShadow(QtWidgets.QFrame.Raised)
        self.employ.setObjectName("employ")
        self.gridLayout_94 = QtWidgets.QGridLayout(self.employ)
        self.gridLayout_94.setObjectName("gridLayout_94")
        self.yes = QtWidgets.QLabel(self.employ)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.yes.setFont(font)
        self.yes.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.yes.setObjectName("yes")
        self.gridLayout_94.addWidget(self.yes, 0, 0, 1, 1)
        self.no = QtWidgets.QLabel(self.employ)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.no.setFont(font)
        self.no.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.no.setObjectName("no")
        self.gridLayout_94.addWidget(self.no, 1, 0, 1, 1)
        self.gridLayout_93.addWidget(self.employ, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout_53.addWidget(self.frame_104)
        self.horizontalLayout_16.addWidget(self.frame_102)
        self.frame_106 = QtWidgets.QFrame(self.personal_info_19)
        self.frame_106.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_106.setObjectName("frame_106")
        self.gridLayout_97 = QtWidgets.QGridLayout(self.frame_106)
        self.gridLayout_97.setObjectName("gridLayout_97")
        self.hiring = QtWidgets.QFrame(self.frame_106)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hiring.sizePolicy().hasHeightForWidth())
        self.hiring.setSizePolicy(sizePolicy)
        self.hiring.setMinimumSize(QtCore.QSize(0, 0))
        self.hiring.setStyleSheet("#hiring{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.hiring.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hiring.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hiring.setObjectName("hiring")
        self.gridLayout_98 = QtWidgets.QGridLayout(self.hiring)
        self.gridLayout_98.setObjectName("gridLayout_98")
        self.about_hiring = QtWidgets.QLabel(self.hiring)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.about_hiring.setFont(font)
        self.about_hiring.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.about_hiring.setObjectName("about_hiring")
        self.gridLayout_98.addWidget(self.about_hiring, 0, 0, 1, 1)
        self.gridLayout_97.addWidget(self.hiring, 1, 0, 1, 1)
        self.label_189 = QtWidgets.QLabel(self.frame_106)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_189.setFont(font)
        self.label_189.setObjectName("label_189")
        self.gridLayout_97.addWidget(self.label_189, 0, 0, 1, 1)
        self.frame_107 = QtWidgets.QFrame(self.frame_106)
        self.frame_107.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_107.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_107.setObjectName("frame_107")
        self.gridLayout_97.addWidget(self.frame_107, 2, 0, 1, 1)
        self.horizontalLayout_16.addWidget(self.frame_106)
        self.frame_103 = QtWidgets.QFrame(self.personal_info_19)
        self.frame_103.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_103.setObjectName("frame_103")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout(self.frame_103)
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.frame_108 = QtWidgets.QFrame(self.frame_103)
        self.frame_108.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_108.setObjectName("frame_108")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout(self.frame_108)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.label_36 = QtWidgets.QLabel(self.frame_108)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_56.addWidget(self.label_36)
        self.label_190 = QtWidgets.QLabel(self.frame_108)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_190.setFont(font)
        self.label_190.setObjectName("label_190")
        self.verticalLayout_56.addWidget(self.label_190)
        self.cover = QtWidgets.QFrame(self.frame_108)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cover.sizePolicy().hasHeightForWidth())
        self.cover.setSizePolicy(sizePolicy)
        self.cover.setMinimumSize(QtCore.QSize(0, 0))
        self.cover.setStyleSheet("#cover{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.cover.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cover.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cover.setObjectName("cover")
        self.gridLayout_99 = QtWidgets.QGridLayout(self.cover)
        self.gridLayout_99.setObjectName("gridLayout_99")
        self.verticalLayout_56.addWidget(self.cover)
        self.verticalLayout_55.addWidget(self.frame_108)
        self.frame_109 = QtWidgets.QFrame(self.frame_103)
        self.frame_109.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_109.setObjectName("frame_109")
        self.gridLayout_101 = QtWidgets.QGridLayout(self.frame_109)
        self.gridLayout_101.setObjectName("gridLayout_101")
        self.label_191 = QtWidgets.QLabel(self.frame_109)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_191.setFont(font)
        self.label_191.setObjectName("label_191")
        self.gridLayout_101.addWidget(self.label_191, 0, 0, 1, 1)
        self.resumee = QtWidgets.QFrame(self.frame_109)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resumee.sizePolicy().hasHeightForWidth())
        self.resumee.setSizePolicy(sizePolicy)
        self.resumee.setMinimumSize(QtCore.QSize(0, 0))
        self.resumee.setStyleSheet("#resumee{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.resumee.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resumee.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resumee.setObjectName("resumee")
        self.gridLayout_100 = QtWidgets.QGridLayout(self.resumee)
        self.gridLayout_100.setObjectName("gridLayout_100")
        self.gridLayout_101.addWidget(self.resumee, 1, 0, 1, 1)
        self.verticalLayout_55.addWidget(self.frame_109)
        self.horizontalLayout_16.addWidget(self.frame_103)
        self.gridLayout_96.addWidget(self.personal_info_19, 1, 0, 1, 1)
        self.gridLayout_68.addWidget(self.frame_101, 4, 0, 1, 1)
        self.frame_281 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
        self.frame_281.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_281.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_281.setObjectName("frame_281")
        self.gridLayout_399 = QtWidgets.QGridLayout(self.frame_281)
        self.gridLayout_399.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_399.setObjectName("gridLayout_399")
        self.personal_info_17 = QtWidgets.QFrame(self.frame_281)
        self.personal_info_17.setMinimumSize(QtCore.QSize(0, 190))
        self.personal_info_17.setStyleSheet("*{\n"
"background-color: rgb(248, 248, 248);\n"
"}\n"
"")
        self.personal_info_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.personal_info_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.personal_info_17.setObjectName("personal_info_17")
        self.verticalLayout_85 = QtWidgets.QVBoxLayout(self.personal_info_17)
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName("verticalLayout_85")
        self.frame_282 = QtWidgets.QFrame(self.personal_info_17)
        self.frame_282.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_282.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_282.setObjectName("frame_282")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout(self.frame_282)
        self.horizontalLayout_53.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_53.setSpacing(2)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.frame_283 = QtWidgets.QFrame(self.frame_282)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_283.sizePolicy().hasHeightForWidth())
        self.frame_283.setSizePolicy(sizePolicy)
        self.frame_283.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_283.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_283.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_283.setObjectName("frame_283")
        self.gridLayout_383 = QtWidgets.QGridLayout(self.frame_283)
        self.gridLayout_383.setObjectName("gridLayout_383")
        self.label_177 = QtWidgets.QLabel(self.frame_283)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_177.setFont(font)
        self.label_177.setObjectName("label_177")
        self.gridLayout_383.addWidget(self.label_177, 0, 0, 1, 1)
        self.job = QtWidgets.QFrame(self.frame_283)
        self.job.setMinimumSize(QtCore.QSize(0, 40))
        self.job.setStyleSheet("#job{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.job.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.job.setFrameShadow(QtWidgets.QFrame.Raised)
        self.job.setObjectName("job")
        self.gridLayout_384 = QtWidgets.QGridLayout(self.job)
        self.gridLayout_384.setObjectName("gridLayout_384")
        self.first_name_19 = QtWidgets.QLabel(self.job)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.first_name_19.setFont(font)
        self.first_name_19.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.first_name_19.setObjectName("first_name_19")
        self.gridLayout_384.addWidget(self.first_name_19, 0, 0, 1, 1)
        self.gridLayout_383.addWidget(self.job, 1, 0, 1, 1)
        self.horizontalLayout_53.addWidget(self.frame_283, 0, QtCore.Qt.AlignLeft)
        self.frame_284 = QtWidgets.QFrame(self.frame_282)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_284.sizePolicy().hasHeightForWidth())
        self.frame_284.setSizePolicy(sizePolicy)
        self.frame_284.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_284.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_284.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_284.setObjectName("frame_284")
        self.gridLayout_385 = QtWidgets.QGridLayout(self.frame_284)
        self.gridLayout_385.setObjectName("gridLayout_385")
        self.label_178 = QtWidgets.QLabel(self.frame_284)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_178.setFont(font)
        self.label_178.setObjectName("label_178")
        self.gridLayout_385.addWidget(self.label_178, 0, 0, 1, 1)
        self.com = QtWidgets.QFrame(self.frame_284)
        self.com.setMinimumSize(QtCore.QSize(0, 40))
        self.com.setStyleSheet("#com{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.com.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.com.setFrameShadow(QtWidgets.QFrame.Raised)
        self.com.setObjectName("com")
        self.gridLayout_386 = QtWidgets.QGridLayout(self.com)
        self.gridLayout_386.setObjectName("gridLayout_386")
        self.middle_name_19 = QtWidgets.QLabel(self.com)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.middle_name_19.setFont(font)
        self.middle_name_19.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.middle_name_19.setObjectName("middle_name_19")
        self.gridLayout_386.addWidget(self.middle_name_19, 0, 0, 1, 1)
        self.gridLayout_385.addWidget(self.com, 1, 0, 1, 1)
        self.horizontalLayout_53.addWidget(self.frame_284)
        self.frame_285 = QtWidgets.QFrame(self.frame_282)
        self.frame_285.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_285.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_285.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_285.setObjectName("frame_285")
        self.gridLayout_387 = QtWidgets.QGridLayout(self.frame_285)
        self.gridLayout_387.setObjectName("gridLayout_387")
        self.datee = QtWidgets.QFrame(self.frame_285)
        self.datee.setMinimumSize(QtCore.QSize(0, 40))
        self.datee.setStyleSheet("#datee{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.datee.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.datee.setFrameShadow(QtWidgets.QFrame.Raised)
        self.datee.setObjectName("datee")
        self.gridLayout_388 = QtWidgets.QGridLayout(self.datee)
        self.gridLayout_388.setObjectName("gridLayout_388")
        self.last_name_19 = QtWidgets.QLabel(self.datee)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.last_name_19.setFont(font)
        self.last_name_19.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.last_name_19.setObjectName("last_name_19")
        self.gridLayout_388.addWidget(self.last_name_19, 0, 0, 1, 1)
        self.gridLayout_387.addWidget(self.datee, 1, 0, 1, 1)
        self.label_179 = QtWidgets.QLabel(self.frame_285)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_179.setFont(font)
        self.label_179.setObjectName("label_179")
        self.gridLayout_387.addWidget(self.label_179, 0, 0, 1, 1)
        self.horizontalLayout_53.addWidget(self.frame_285, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_85.addWidget(self.frame_282)
        self.frame_287 = QtWidgets.QFrame(self.personal_info_17)
        self.frame_287.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_287.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_287.setObjectName("frame_287")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout(self.frame_287)
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.frame_289 = QtWidgets.QFrame(self.frame_287)
        self.frame_289.setMinimumSize(QtCore.QSize(600, 0))
        self.frame_289.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_289.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_289.setObjectName("frame_289")
        self.gridLayout_393 = QtWidgets.QGridLayout(self.frame_289)
        self.gridLayout_393.setObjectName("gridLayout_393")
        self.label_182 = QtWidgets.QLabel(self.frame_289)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_182.setFont(font)
        self.label_182.setObjectName("label_182")
        self.gridLayout_393.addWidget(self.label_182, 0, 0, 1, 1)
        self.res = QtWidgets.QFrame(self.frame_289)
        self.res.setMinimumSize(QtCore.QSize(0, 40))
        self.res.setStyleSheet("#res{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 3px solid rgb(229, 230, 230);\n"
"}\n"
"")
        self.res.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.res.setFrameShadow(QtWidgets.QFrame.Raised)
        self.res.setObjectName("res")
        self.gridLayout_394 = QtWidgets.QGridLayout(self.res)
        self.gridLayout_394.setObjectName("gridLayout_394")
        self.primary_phone_number_19 = QtWidgets.QLabel(self.res)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.primary_phone_number_19.setFont(font)
        self.primary_phone_number_19.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.primary_phone_number_19.setObjectName("primary_phone_number_19")
        self.gridLayout_394.addWidget(self.primary_phone_number_19, 0, 0, 1, 1)
        self.gridLayout_393.addWidget(self.res, 1, 0, 1, 1)
        self.horizontalLayout_54.addWidget(self.frame_289, 0, QtCore.Qt.AlignLeft)
        self.frame_90 = QtWidgets.QFrame(self.frame_287)
        self.frame_90.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_90.setObjectName("frame_90")
        self.gridLayout_91 = QtWidgets.QGridLayout(self.frame_90)
        self.gridLayout_91.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_91.setObjectName("gridLayout_91")
        self.frame_92 = QtWidgets.QFrame(self.frame_90)
        self.frame_92.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_92.setObjectName("frame_92")
        self.gridLayout_91.addWidget(self.frame_92, 0, 0, 1, 1)
        self.frame_93 = QtWidgets.QFrame(self.frame_90)
        self.frame_93.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_93.setObjectName("frame_93")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_93)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_96 = QtWidgets.QFrame(self.frame_93)
        self.frame_96.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_96.setObjectName("frame_96")
        self.gridLayout_89 = QtWidgets.QGridLayout(self.frame_96)
        self.gridLayout_89.setObjectName("gridLayout_89")
        self.pushButton_45 = QtWidgets.QPushButton(self.frame_96)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 10px; \n"
"            background-color: rgb(91, 5, 6);\n"
"            color: rgb(255, 255, 255);\n"
"            border: 3px solid rgb(220, 221, 221);\n"
"            padding: 5px;\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_45.setFlat(True)
        self.pushButton_45.setObjectName("pushButton_45")
        self.gridLayout_89.addWidget(self.pushButton_45, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_35 = QtWidgets.QLabel(self.frame_96)
        self.label_35.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 10px; \n"
"            background-color: rgb(91, 5, 6);\n"
"            color: rgb(255, 255, 255);\n"
"            border: 3px solid rgb(220, 221, 221);\n"
"            padding: 10px;\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.gridLayout_89.addWidget(self.label_35, 0, 1, 1, 1)
        self.horizontalLayout_15.addWidget(self.frame_96, 0, QtCore.Qt.AlignHCenter)
        self.frame_97 = QtWidgets.QFrame(self.frame_93)
        self.frame_97.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_97.setObjectName("frame_97")
        self.gridLayout_90 = QtWidgets.QGridLayout(self.frame_97)
        self.gridLayout_90.setObjectName("gridLayout_90")
        self.pushButton_46 = QtWidgets.QPushButton(self.frame_97)
        self.pushButton_46.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 10px; \n"
"            background-color: rgb(5, 74, 91);\n"
"            color: rgb(255, 255, 255);\n"
"            border: 3px solid rgb(220, 221, 221);\n"
"            padding: 5px;\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }")
        self.pushButton_46.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_46.setFlat(True)
        self.pushButton_46.setObjectName("pushButton_46")
        self.gridLayout_90.addWidget(self.pushButton_46, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_15.addWidget(self.frame_97)
        self.gridLayout_91.addWidget(self.frame_93, 1, 0, 1, 1)
        self.horizontalLayout_54.addWidget(self.frame_90, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_85.addWidget(self.frame_287)
        self.gridLayout_399.addWidget(self.personal_info_17, 1, 0, 1, 1)
        self.label_185 = QtWidgets.QLabel(self.frame_281)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_185.setFont(font)
        self.label_185.setObjectName("label_185")
        self.gridLayout_399.addWidget(self.label_185, 0, 0, 1, 1)
        self.gridLayout_68.addWidget(self.frame_281, 2, 0, 1, 1)
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_7)
        self.gridLayout_64.addWidget(self.scrollArea_9, 0, 0, 1, 1)
        self.verticalLayout_46.addWidget(self.profile_body)
        self.stackedWidget.addWidget(self.profile)
        self.interviewer = QtWidgets.QWidget()
        self.interviewer.setObjectName("interviewer")
        self.verticalLayout_57 = QtWidgets.QVBoxLayout(self.interviewer)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.widget_11 = QtWidgets.QWidget(self.interviewer)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_58 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.frame_110 = QtWidgets.QFrame(self.widget_11)
        self.frame_110.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_110.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_110.setObjectName("frame_110")
        self.gridLayout_102 = QtWidgets.QGridLayout(self.frame_110)
        self.gridLayout_102.setObjectName("gridLayout_102")
        self.label_37 = QtWidgets.QLabel(self.frame_110)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.gridLayout_102.addWidget(self.label_37, 0, 0, 1, 1)
        self.verticalLayout_58.addWidget(self.frame_110, 0, QtCore.Qt.AlignTop)
        self.frame_111 = QtWidgets.QFrame(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_111.sizePolicy().hasHeightForWidth())
        self.frame_111.setSizePolicy(sizePolicy)
        self.frame_111.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_111.setObjectName("frame_111")
        self.gridLayout_105 = QtWidgets.QGridLayout(self.frame_111)
        self.gridLayout_105.setObjectName("gridLayout_105")
        self.frame_115 = QtWidgets.QFrame(self.frame_111)
        self.frame_115.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_115.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_115.setObjectName("frame_115")
        self.gridLayout_104 = QtWidgets.QGridLayout(self.frame_115)
        self.gridLayout_104.setObjectName("gridLayout_104")
        self.label_43 = QtWidgets.QLabel(self.frame_115)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.gridLayout_104.addWidget(self.label_43, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_105.addWidget(self.frame_115, 0, 0, 1, 1)
        self.frame_112 = QtWidgets.QFrame(self.frame_111)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_112.sizePolicy().hasHeightForWidth())
        self.frame_112.setSizePolicy(sizePolicy)
        self.frame_112.setStyleSheet("#interviewerr{\n"
"background-color: rgb(248, 248, 248);\n"
"border-radius: 20px;\n"
"border: 3px solid #F1F2F2;\n"
"\n"
"}")
        self.frame_112.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_112.setObjectName("frame_112")
        self.verticalLayout_59 = QtWidgets.QVBoxLayout(self.frame_112)
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.interviewerr = QtWidgets.QFrame(self.frame_112)
        self.interviewerr.setMinimumSize(QtCore.QSize(500, 300))
        self.interviewerr.setStyleSheet("")
        self.interviewerr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.interviewerr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.interviewerr.setObjectName("interviewerr")
        self.gridLayout_103 = QtWidgets.QGridLayout(self.interviewerr)
        self.gridLayout_103.setContentsMargins(50, -1, 50, -1)
        self.gridLayout_103.setObjectName("gridLayout_103")
        self.label_40 = QtWidgets.QLabel(self.interviewerr)
        self.label_40.setMinimumSize(QtCore.QSize(0, 0))
        self.label_40.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("*{\n"
"\n"
"background-color: rgb(248, 248, 248);\n"
"}")
        self.label_40.setObjectName("label_40")
        self.gridLayout_103.addWidget(self.label_40, 0, 0, 1, 1)
        self.interviewer_name = QtWidgets.QLineEdit(self.interviewerr)
        self.interviewer_name.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.interviewer_name.setFont(font)
        self.interviewer_name.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"}")
        self.interviewer_name.setText("")
        self.interviewer_name.setObjectName("interviewer_name")
        self.gridLayout_103.addWidget(self.interviewer_name, 1, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.interviewerr)
        self.label_38.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("*{\n"
"\n"
"background-color: rgb(248, 248, 248);\n"
"}")
        self.label_38.setObjectName("label_38")
        self.gridLayout_103.addWidget(self.label_38, 2, 0, 1, 1)
        self.location = QtWidgets.QLineEdit(self.interviewerr)
        self.location.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.location.setFont(font)
        self.location.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"}")
        self.location.setObjectName("location")
        self.gridLayout_103.addWidget(self.location, 3, 0, 1, 1)
        self.frame_116 = QtWidgets.QFrame(self.interviewerr)
        self.frame_116.setStyleSheet("*{\n"
"\n"
"background-color: rgb(248, 248, 248);\n"
"}")
        self.frame_116.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_116.setObjectName("frame_116")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_116)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_117 = QtWidgets.QFrame(self.frame_116)
        self.frame_117.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_117.setObjectName("frame_117")
        self.gridLayout_106 = QtWidgets.QGridLayout(self.frame_117)
        self.gridLayout_106.setObjectName("gridLayout_106")
        self.label_39 = QtWidgets.QLabel(self.frame_117)
        self.label_39.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("*{\n"
"\n"
"background-color: rgb(248, 248, 248);\n"
"}")
        self.label_39.setObjectName("label_39")
        self.gridLayout_106.addWidget(self.label_39, 0, 0, 1, 1)
        self.date = QtWidgets.QLineEdit(self.frame_117)
        self.date.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.date.setFont(font)
        self.date.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"}")
        self.date.setObjectName("date")
        self.gridLayout_106.addWidget(self.date, 1, 0, 1, 1)
        self.horizontalLayout_17.addWidget(self.frame_117)
        self.frame_118 = QtWidgets.QFrame(self.frame_116)
        self.frame_118.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_118.setObjectName("frame_118")
        self.gridLayout_107 = QtWidgets.QGridLayout(self.frame_118)
        self.gridLayout_107.setObjectName("gridLayout_107")
        self.label_44 = QtWidgets.QLabel(self.frame_118)
        self.label_44.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("*{\n"
"\n"
"background-color: rgb(248, 248, 248);\n"
"}")
        self.label_44.setObjectName("label_44")
        self.gridLayout_107.addWidget(self.label_44, 0, 0, 1, 1)
        self.time = QtWidgets.QLineEdit(self.frame_118)
        self.time.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.time.setFont(font)
        self.time.setStyleSheet("*{\n"
"border: 3px solid #F1F2F2;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"}")
        self.time.setObjectName("time")
        self.gridLayout_107.addWidget(self.time, 1, 0, 1, 1)
        self.horizontalLayout_17.addWidget(self.frame_118)
        self.gridLayout_103.addWidget(self.frame_116, 4, 0, 1, 1)
        self.frame_113 = QtWidgets.QFrame(self.interviewerr)
        self.frame_113.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_113.setStyleSheet("*{\n"
"\n"
"background-color: rgb(248, 248, 248);\n"
"}")
        self.frame_113.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_113.setObjectName("frame_113")
        self.verticalLayout_60 = QtWidgets.QVBoxLayout(self.frame_113)
        self.verticalLayout_60.setContentsMargins(100, -1, 100, -1)
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.frame_114 = QtWidgets.QFrame(self.frame_113)
        self.frame_114.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_114.setObjectName("frame_114")
        self.verticalLayout_61 = QtWidgets.QVBoxLayout(self.frame_114)
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.pushButton_47 = QtWidgets.QPushButton(self.frame_114)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy)
        self.pushButton_47.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setStyleSheet("QPushButton {\n"
"            border: none; \n"
"            border-radius: 10px; \n"
"            background-color: rgb(5, 74, 91);\n"
"            color: rgb(255, 255, 255);\n"
"            border: 3px solid rgb(220, 221, 221);\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.pushButton_47.setObjectName("pushButton_47")
        self.verticalLayout_61.addWidget(self.pushButton_47, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_60.addWidget(self.frame_114, 0, QtCore.Qt.AlignTop)
        self.gridLayout_103.addWidget(self.frame_113, 5, 0, 1, 1)
        self.verticalLayout_59.addWidget(self.interviewerr, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_105.addWidget(self.frame_112, 1, 0, 1, 1)
        self.verticalLayout_58.addWidget(self.frame_111)
        self.verticalLayout_57.addWidget(self.widget_11)
        self.stackedWidget.addWidget(self.interviewer)
        self.horizontalLayout_6.addWidget(self.stackedWidget)
        self.gridLayout_38.addWidget(self.widget, 0, 1, 1, 1)
        self.menu = QtWidgets.QWidget(self.centralwidget)
        self.menu.setObjectName("menu")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.menu)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.logo = QtWidgets.QFrame(self.menu)
        self.logo.setMinimumSize(QtCore.QSize(0, 0))
        self.logo.setMaximumSize(QtCore.QSize(16777215, 100))
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.logo)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.logoo = QtWidgets.QFrame(self.logo)
        self.logoo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logoo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logoo.setObjectName("logoo")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.logoo)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.logoicon = QtWidgets.QLabel(self.logoo)
        self.logoicon.setText("")
        self.logoicon.setPixmap(QtGui.QPixmap(":/image/images/logotext.svg"))
        self.logoicon.setObjectName("logoicon")
        self.verticalLayout_5.addWidget(self.logoicon)
        self.verticalLayout_4.addWidget(self.logoo)
        self.gridLayout_7.addWidget(self.logo, 0, 0, 1, 1)
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
        self.dashboard.setMinimumSize(QtCore.QSize(0, 0))
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
"            background-color: rgb(226, 249, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.dashboard.setFlat(True)
        self.dashboard.setObjectName("dashboard")
        self.verticalLayout_3.addWidget(self.dashboard)
        self.applicants = QtWidgets.QPushButton(self.buttons)
        self.applicants.setMinimumSize(QtCore.QSize(0, 0))
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
"            background-color: rgb(226, 249, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.applicants.setFlat(True)
        self.applicants.setObjectName("applicants")
        self.verticalLayout_3.addWidget(self.applicants)
        self.jobmanagent = QtWidgets.QPushButton(self.buttons)
        self.jobmanagent.setMinimumSize(QtCore.QSize(0, 0))
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
"            background-color: rgb(226, 249, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.jobmanagent.setFlat(True)
        self.jobmanagent.setObjectName("jobmanagent")
        self.verticalLayout_3.addWidget(self.jobmanagent)
        self.history = QtWidgets.QPushButton(self.buttons)
        self.history.setMinimumSize(QtCore.QSize(0, 0))
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
"            background-color: rgb(226, 249, 255)\n"
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
"            background-color: rgb(226, 249, 255)\n"
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
"            background-color: rgb(226, 249, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: white;\n"
"        }\n"
"")
        self.account.setFlat(True)
        self.account.setObjectName("account")
        self.verticalLayout_3.addWidget(self.account)
        self.verticalLayout_2.addWidget(self.buttons)
        self.gridLayout_7.addWidget(self.menulist, 1, 0, 1, 1)
        self.gridLayout_38.addWidget(self.menu, 0, 0, 1, 1)
        self.dashboard.clicked.connect(lambda: self.toggleButtonStyle(self.dashboard, "dashboard"))
        self.applicants.clicked.connect(lambda: self.toggleButtonStyle(self.applicants, "applicants"))
        self.jobmanagent.clicked.connect(lambda: self.toggleButtonStyle(self.jobmanagent, "jobmanagent"))
        self.history.clicked.connect(lambda: self.toggleButtonStyle(self.history, "history"))
        self.satsana.clicked.connect(lambda: self.toggleButtonStyle(self.satsana, "satsana"))
        self.account.clicked.connect(lambda: self.toggleButtonStyle(self.account, "account"))
        self.pending.clicked.connect(lambda: self.toggleButtonStyle(self.pending, "pending"))
        self.interview.clicked.connect(lambda: self.toggleButtonStyle(self.interview, "interview"))
        self.screening.clicked.connect(lambda: self.toggleButtonStyle(self.screening, "screening"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def toggleButtonStyle(self, button, button_name):
        
        for key in self.button_states:
            if key != button_name and self.button_states[key]:
                getattr(self, key).setStyleSheet("border: none; border-radius: 5px; padding: 10px; background-color: rgb(226, 249, 255);")
                self.button_states[key] = False

        if self.button_states[button_name]: 
            button.setStyleSheet("border: none; border-radius: 5px; padding: 10px; background-color: rgb(226, 249, 255);")
            self.button_states[button_name] = False
        else:
            button.setStyleSheet("background-color: white; border: 3px solid #F1F2F2; border-radius: 5px; padding: 10px;")
            self.button_states[button_name] = True

        
                
    def connect_buttons(self, MainWindow):
        try:
            self.dashboard.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.dashboard_2))
            self.applicants.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.applicants_2))
            self.jobmanagent.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.job_management_2))
            self.history.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.history_2))
            self.satsana.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.satistics))
            self.account.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.account_2))
            self.pending.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.pending_page))
            self.screening.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.screening_page))
            self.interview.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.interview_page))
            self.home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.dashboard_2))
            self.home_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.dashboard_2))
            self.home_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.dashboard_2))
            self.home_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.dashboard_2))
            self.home_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.dashboard_2))
            self.home_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.dashboard_2))
            self.add_job_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.job_management_2))
            self.add_job_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.job_management_2))
            self.add_job_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.job_management_2))
            self.add_job_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.job_management_2))
            self.roselle.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.profile))
            self.approve.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.interviewer))
        except AttributeError as e:
            print(f"Error connecting buttons: {e}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_14.setText(_translate("MainWindow", "DASHBOARD"))
        self.home_6.setText(_translate("MainWindow", "Home"))
        self.pushButton_30.setText(_translate("MainWindow", "Interview"))
        self.label_3.setText(_translate("MainWindow", "Total Applicant"))
        self.label_4.setText(_translate("MainWindow", "14"))
        self.label_9.setText(_translate("MainWindow", "Total Job"))
        self.number_job.setText(_translate("MainWindow", "5"))
        self.label_7.setText(_translate("MainWindow", "Pending Applicants"))
        self.number_pending.setText(_translate("MainWindow", "45"))
        self.label_13.setText(_translate("MainWindow", "APPLICANTS"))
        self.home.setText(_translate("MainWindow", "Home"))
        self.pushButton_27.setText(_translate("MainWindow", "Interview"))
        self.label.setText(_translate("MainWindow", "Select applicant to view."))
        self.comboBox.setItemText(0, _translate("MainWindow", "WEB DESIGNER"))
        self.comboBox.setItemText(1, _translate("MainWindow", "DOCUMENT AND DATA SPECIALIST I "))
        self.comboBox.setItemText(2, _translate("MainWindow", "IT TECHNICIAN"))
        self.pending.setText(_translate("MainWindow", "Pending"))
        self.screening.setText(_translate("MainWindow", "Screening"))
        self.interview.setText(_translate("MainWindow", "Interview"))
        self.roselle.setText(_translate("MainWindow", "Roselle Durano"))
        self.pushButton_2.setText(_translate("MainWindow", "Gab grabe kabayot"))
        self.pushButton_13.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_15.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "Kent Buno"))
        self.pushButton_3.setText(_translate("MainWindow", "Gab BAyot"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_16.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "Gab Bayot"))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "Gab Bayot Keyo"))
        self.pushButton_17.setText(_translate("MainWindow", "PushButton"))
        self.label_6.setText(_translate("MainWindow", "JOB MANAGEMENT"))
        self.home_2.setText(_translate("MainWindow", "Home"))
        self.pushButton_14.setText(_translate("MainWindow", "Interview"))
        self.label_8.setText(_translate("MainWindow", "Edit the job application."))
        self.label_5.setText(_translate("MainWindow", "Add Job Application"))
        self.work_experience.setPlainText(_translate("MainWindow", "Work Experiences Requirements"))
        self.add_work_expe.setText(_translate("MainWindow", "Add"))
        self.job_position.setText(_translate("MainWindow", "Job Position"))
        self.roles_2.setPlainText(_translate("MainWindow", "Roles and Responsibilities"))
        self.add_roles.setText(_translate("MainWindow", "Add"))
        self.add_skills.setText(_translate("MainWindow", "Add"))
        self.skills_3.setPlainText(_translate("MainWindow", "Key Skills and Competence"))
        self.general_description.setPlainText(_translate("MainWindow", "General Description\n"
""))
        self.education_requirements.setPlainText(_translate("MainWindow", "Education Requirements"))
        self.add_education.setText(_translate("MainWindow", "Add"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_8.setText(_translate("MainWindow", "ADD"))
        self.label_12.setText(_translate("MainWindow", "HISTORY"))
        self.home_3.setText(_translate("MainWindow", "Home"))
        self.pushButton_24.setText(_translate("MainWindow", "Interview"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "DOCUMENT AND DATA TECHNICIAN"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "DOCUMENT AND DATA SPECIALIST I "))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "WEB DESIGNER"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "WEB DEVELOPER"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "IT TECHNICIAN"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "2024"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2023"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "2022"))
        self.lineEdit_2.setText(_translate("MainWindow", "Search"))
        self.label_10.setText(_translate("MainWindow", "HIRED"))
        self.pushButton_23.setText(_translate("MainWindow", "Jess Abapo"))
        self.pushButton_32.setText(_translate("MainWindow", "Lemuel Augusto"))
        self.pushButton_20.setText(_translate("MainWindow", "Roselle Durano"))
        self.pushButton_29.setText(_translate("MainWindow", "Jerry Daan"))
        self.pushButton_26.setText(_translate("MainWindow", "Kent Buno"))
        self.pushButton_35.setText(_translate("MainWindow", "PushButton"))
        self.label_16.setText(_translate("MainWindow", "REJECTED"))
        self.pushButton_36.setText(_translate("MainWindow", "Jonel Jumawan"))
        self.pushButton_38.setText(_translate("MainWindow", "Rolly Casayas"))
        self.pushButton_19.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_18.setText(_translate("MainWindow", "Gab Cabije"))
        self.pushButton_39.setText(_translate("MainWindow", "Ryle Melecio"))
        self.pushButton_37.setText(_translate("MainWindow", "Artzel Diaz"))
        self.label_11.setText(_translate("MainWindow", "ACCOUNT"))
        self.home_4.setText(_translate("MainWindow", "Home"))
        self.pushButton_21.setText(_translate("MainWindow", "Interview"))
        self.label_19.setText(_translate("MainWindow", "New Password"))
        self.label_20.setText(_translate("MainWindow", "Confirm New Password"))
        self.label_18.setText(_translate("MainWindow", "Old Password"))
        self.pushButton_40.setText(_translate("MainWindow", "CHANGE"))
        self.label_17.setText(_translate("MainWindow", "Change Password"))
        self.label_15.setText(_translate("MainWindow", "STATISTICS AND ANALYTICS"))
        self.home_5.setText(_translate("MainWindow", "Home"))
        self.pushButton_33.setText(_translate("MainWindow", "Interview"))
        self.label_21.setText(_translate("MainWindow", "Roselle F. Durano"))
        self.label_22.setText(_translate("MainWindow", "Applicant:"))
        self.label_23.setText(_translate("MainWindow", "Document and Data Specialist I"))
        self.label_24.setText(_translate("MainWindow", "Proceed for interview?"))
        self.pushButton_41.setText(_translate("MainWindow", "Dissapprove"))
        self.approve.setText(_translate("MainWindow", "Approve"))
        self.label_168.setText(_translate("MainWindow", "Degree/Certification"))
        self.degree.setText(_translate("MainWindow", "Bachelor of Science in Information Technology"))
        self.label_169.setText(_translate("MainWindow", "Institution"))
        self.institution.setText(_translate("MainWindow", "Cebu Technological University"))
        self.label_172.setText(_translate("MainWindow", "Graduation Date"))
        self.graduation_date.setText(_translate("MainWindow", "05 / 24 / 2022"))
        self.label_173.setText(_translate("MainWindow", "Awards"))
        self.awards.setText(_translate("MainWindow", "Best in Gown"))
        self.pushButton_43.setText(_translate("MainWindow", "Remove"))
        self.pushButton_44.setText(_translate("MainWindow", "    Add    "))
        self.label_176.setText(_translate("MainWindow", "Education"))
        self.label_26.setText(_translate("MainWindow", "First Name"))
        self.first_name.setText(_translate("MainWindow", "Roselle"))
        self.label_30.setText(_translate("MainWindow", "Middle Name"))
        self.middle_name.setText(_translate("MainWindow", "Federe"))
        self.label_31.setText(_translate("MainWindow", "Last Name"))
        self.last_name.setText(_translate("MainWindow", "Durano"))
        self.label_32.setText(_translate("MainWindow", "Age"))
        self.age.setText(_translate("MainWindow", "20"))
        self.label_27.setText(_translate("MainWindow", "Email Address"))
        self.email_address.setText(_translate("MainWindow", "roselledurano14@gmail.com"))
        self.label_28.setText(_translate("MainWindow", "Primary Phone Number"))
        self.primary_phone_number.setText(_translate("MainWindow", "09915706585"))
        self.label_33.setText(_translate("MainWindow", "Secondary Phone Number"))
        self.secondary_phone_number.setText(_translate("MainWindow", "0923173586"))
        self.label_34.setText(_translate("MainWindow", "City Address"))
        self.city_address.setText(_translate("MainWindow", "Ibo, Lapu-lapu City, Cebu"))
        self.label_25.setText(_translate("MainWindow", "Personal Information"))
        self.label_186.setText(_translate("MainWindow", "References"))
        self.label_180.setText(_translate("MainWindow", "How did you know about the hiring?"))
        self.linked.setText(_translate("MainWindow", "Linkedin"))
        self.indeed.setText(_translate("MainWindow", "Indeed"))
        self.facebook.setText(_translate("MainWindow", "Facebook"))
        self.referral.setText(_translate("MainWindow", "Referral"))
        self.others.setText(_translate("MainWindow", "Others: "))
        self.company_name.setText(_translate("MainWindow", "Del Mundo Company"))
        self.label_181.setText(_translate("MainWindow", "If referral, who referred you and how are you related?"))
        self.label_41.setText(_translate("MainWindow", "Reference Name"))
        self.label_42.setText(_translate("MainWindow", " (write N/A if not referral)"))
        self.reference_number.setText(_translate("MainWindow", "09915706585"))
        self.label_183.setText(_translate("MainWindow", "Reference Phone Number"))
        self.label_187.setText(_translate("MainWindow", "Employment Information"))
        self.label_184.setText(_translate("MainWindow", "Years of Relevant Experience to the Role Applied"))
        self.years_role_applied.setText(_translate("MainWindow", "4 years"))
        self.label_188.setText(_translate("MainWindow", "Are You Currently Employed?"))
        self.yes.setText(_translate("MainWindow", "Yes"))
        self.no.setText(_translate("MainWindow", "No"))
        self.about_hiring.setText(_translate("MainWindow", "ASAP"))
        self.label_189.setText(_translate("MainWindow", "How did you know about the hiring?"))
        self.label_36.setText(_translate("MainWindow", "Upload your original softcopy here:"))
        self.label_190.setText(_translate("MainWindow", "Cover Letter"))
        self.label_191.setText(_translate("MainWindow", "Resume"))
        self.label_177.setText(_translate("MainWindow", "Job Title"))
        self.first_name_19.setText(_translate("MainWindow", "Manager"))
        self.label_178.setText(_translate("MainWindow", "Company "))
        self.middle_name_19.setText(_translate("MainWindow", "Del Mundo Company"))
        self.last_name_19.setText(_translate("MainWindow", "05 / 24 / 2022"))
        self.label_179.setText(_translate("MainWindow", "Date of Employment"))
        self.label_182.setText(_translate("MainWindow", "Responsibilities"))
        self.primary_phone_number_19.setText(_translate("MainWindow", "Tig lung ag"))
        self.pushButton_45.setText(_translate("MainWindow", "Remove"))
        self.pushButton_46.setText(_translate("MainWindow", "    Add    "))
        self.label_185.setText(_translate("MainWindow", "Work Experience"))
        self.label_37.setText(_translate("MainWindow", "Interviewer"))
        self.label_43.setText(_translate("MainWindow", "Assign the interviewer."))
        self.label_40.setText(_translate("MainWindow", "Interviewer"))
        self.label_38.setText(_translate("MainWindow", "Location"))
        self.label_39.setText(_translate("MainWindow", "Date"))
        self.label_44.setText(_translate("MainWindow", "Time"))
        self.pushButton_47.setText(_translate("MainWindow", "DONE"))
        self.dashboard.setText(_translate("MainWindow", "Dashboard"))
        self.applicants.setText(_translate("MainWindow", "Applicants"))
        self.jobmanagent.setText(_translate("MainWindow", "Job Management"))
        self.history.setText(_translate("MainWindow", "History"))
        self.satsana.setText(_translate("MainWindow", "Satistics and Analytics"))
        self.account.setText(_translate("MainWindow", "Account"))
import resource_rc
