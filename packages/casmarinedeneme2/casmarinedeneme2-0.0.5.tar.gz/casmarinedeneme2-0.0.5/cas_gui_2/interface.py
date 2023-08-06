# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1176, 799)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_main = QtWidgets.QHBoxLayout()
        self.horizontalLayout_main.setSpacing(0)
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")
        self.widget_menu = QtWidgets.QWidget(self.centralwidget)
        self.widget_menu.setMinimumSize(QtCore.QSize(46, 0))
        self.widget_menu.setMaximumSize(QtCore.QSize(46, 16777215))
        # self.widget_menu.setStyleSheet("background-color: rgb(36, 123, 160);")
        self.widget_menu.setObjectName("widget_menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_menu)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_menu_home = QtWidgets.QPushButton(self.widget_menu)
        self.pushButton_menu_home.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_menu_home.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_menu_home.setStyleSheet("QPushButton{\n"
"background-color: rgb(10, 36, 99);\n"
"border-radius: 10px;\n"
"border: 2px solid  rgb(10, 36, 99);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(10, 36, 99);\n"
"border-radius: 10px;\n"
"border: 2px solid  rgb(10, 36, 99);\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(10, 36, 99);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(10, 36, 99);\n"
"}")
        self.pushButton_menu_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_menu_home.setIcon(icon)
        self.pushButton_menu_home.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_menu_home.setObjectName("pushButton_menu_home")
        self.verticalLayout.addWidget(self.pushButton_menu_home)
        self.pushButton_menu_pid = QtWidgets.QPushButton(self.widget_menu)
        self.pushButton_menu_pid.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_menu_pid.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_menu_pid.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"border: none;\n"
"border-radius: none;}\n"
"QPushButton:hover{\n"
"background-color: rgb(56, 143, 180);\n"
"border-radius: 10px;\n"
"border: 2px solid  rgb(56, 143, 180);\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(10, 36, 99);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(10, 36, 99);\n"
"}")
        self.pushButton_menu_pid.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo/control.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_menu_pid.setIcon(icon1)
        self.pushButton_menu_pid.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_menu_pid.setObjectName("pushButton_menu_pid")
        self.verticalLayout.addWidget(self.pushButton_menu_pid)
        self.pushButton_menu_code = QtWidgets.QPushButton(self.widget_menu)
        self.pushButton_menu_code.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_menu_code.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_menu_code.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"border: none;\n"
"border-radius: none;}\n"
"QPushButton:hover{\n"
"background-color: rgb(56, 143, 180);\n"
"border-radius: 10px;\n"
"border: 2px solid  rgb(56, 143, 180);\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(10, 36, 99);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(10, 36, 99);\n"
"}")
        self.pushButton_menu_code.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/logo/code.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_menu_code.setIcon(icon2)
        self.pushButton_menu_code.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_menu_code.setObjectName("pushButton_menu_code")
        self.verticalLayout.addWidget(self.pushButton_menu_code)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_theme_mode = QtWidgets.QPushButton(self.widget_menu)
        self.pushButton_theme_mode.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_theme_mode.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_theme_mode.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: none;\n"
"border: none;\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(56, 143, 180);\n"
"border-radius: 10px;\n"
"border: 2px solid  rgb(56, 143, 180);\n"
"}")
        self.pushButton_theme_mode.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/logo/moon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_theme_mode.setIcon(icon3)
        self.pushButton_theme_mode.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_theme_mode.setObjectName("pushButton_theme_mode")
        self.verticalLayout.addWidget(self.pushButton_theme_mode)
        self.horizontalLayout_main.addWidget(self.widget_menu)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        # self.stackedWidget.setStyleSheet("background-color: rgb(245, 245, 220);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_main = QtWidgets.QWidget()
        self.page_main.setObjectName("page_main")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.page_main)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_main_left = QtWidgets.QVBoxLayout()
        self.verticalLayout_main_left.setContentsMargins(-1, -1, 9, -1)
        self.verticalLayout_main_left.setObjectName("verticalLayout_main_left")
        self.widget_camera = QtWidgets.QWidget(self.page_main)
        self.widget_camera.setObjectName("widget_camera")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_camera)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_camera_front = QtWidgets.QLabel(self.widget_camera)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_camera_front.sizePolicy().hasHeightForWidth())
        self.label_camera_front.setSizePolicy(sizePolicy)
        self.label_camera_front.setMinimumSize(QtCore.QSize(350, 262))
        self.label_camera_front.setMaximumSize(QtCore.QSize(737, 16777215))
        self.label_camera_front.setStyleSheet("background-color: rgb(96, 95, 94);\n"
"border-radius: 10px;")
        self.label_camera_front.setText("")
        self.label_camera_front.setObjectName("label_camera_front")
        self.horizontalLayout_6.addWidget(self.label_camera_front)
        self.label_camera_bottom = QtWidgets.QLabel(self.widget_camera)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_camera_bottom.sizePolicy().hasHeightForWidth())
        self.label_camera_bottom.setSizePolicy(sizePolicy)
        self.label_camera_bottom.setMinimumSize(QtCore.QSize(350, 262))
        self.label_camera_bottom.setStyleSheet("background-color: rgb(96, 95, 94);\n"
"border-radius: 10px;")
        self.label_camera_bottom.setText("")
        self.label_camera_bottom.setObjectName("label_camera_bottom")
        self.horizontalLayout_6.addWidget(self.label_camera_bottom)
        self.verticalLayout_main_left.addWidget(self.widget_camera)
        self.widget_mission_buttons = QtWidgets.QWidget(self.page_main)
        self.widget_mission_buttons.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_mission_buttons.setObjectName("widget_mission_buttons")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_mission_buttons)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_mission_start = QtWidgets.QPushButton(self.widget_mission_buttons)
        self.pushButton_mission_start.setMinimumSize(QtCore.QSize(90, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mission_start.setFont(font)
        self.pushButton_mission_start.setStyleSheet("QPushButton{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 30px;\n"
"border-bottom: none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 30px;\n"
"border: 3px solid  rgb(199, 27, 32);\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(199, 27, 32);\n"
"border-radius: 30px;\n"
"border: 3px solid  rgb(199, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_mission_start.setObjectName("pushButton_mission_start")
        self.horizontalLayout_4.addWidget(self.pushButton_mission_start)
        self.pushButton_mission_end = QtWidgets.QPushButton(self.widget_mission_buttons)
        self.pushButton_mission_end.setMinimumSize(QtCore.QSize(90, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mission_end.setFont(font)
        self.pushButton_mission_end.setStyleSheet("QPushButton{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 30px;\n"
"border-bottom: none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 30px;\n"
"border: 3px solid  rgb(199, 27, 32);\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(199, 27, 32);\n"
"border-radius: 30px;\n"
"border: 3px solid  rgb(199, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_mission_end.setObjectName("pushButton_mission_end")
        self.horizontalLayout_4.addWidget(self.pushButton_mission_end)
        self.verticalLayout_main_left.addWidget(self.widget_mission_buttons)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_main_left.addItem(spacerItem1)
        self.widget_main_mission = QtWidgets.QWidget(self.page_main)
        self.widget_main_mission.setMinimumSize(QtCore.QSize(0, 62))
        self.widget_main_mission.setMaximumSize(QtCore.QSize(16777215, 62))
        self.widget_main_mission.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 10px;\n"
"color: rgb(10, 36, 99);")
        self.widget_main_mission.setObjectName("widget_main_mission")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_main_mission)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_main_mission_image = QtWidgets.QLabel(self.widget_main_mission)
        self.label_main_mission_image.setMinimumSize(QtCore.QSize(44, 44))
        self.label_main_mission_image.setMaximumSize(QtCore.QSize(44, 44))
        self.label_main_mission_image.setStyleSheet("")
        self.label_main_mission_image.setText("")
        self.label_main_mission_image.setPixmap(QtGui.QPixmap(":/logo/alg_yosun_1.jpg"))
        self.label_main_mission_image.setScaledContents(True)
        self.label_main_mission_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_main_mission_image.setWordWrap(False)
        self.label_main_mission_image.setObjectName("label_main_mission_image")
        self.horizontalLayout_5.addWidget(self.label_main_mission_image)
        self.label_main_mission_name = QtWidgets.QLabel(self.widget_main_mission)
        self.label_main_mission_name.setMinimumSize(QtCore.QSize(0, 44))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_main_mission_name.setFont(font)
        self.label_main_mission_name.setStyleSheet("color: rgb(10, 36, 99);")
        self.label_main_mission_name.setScaledContents(False)
        self.label_main_mission_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_main_mission_name.setWordWrap(False)
        self.label_main_mission_name.setIndent(-1)
        self.label_main_mission_name.setOpenExternalLinks(False)
        self.label_main_mission_name.setObjectName("label_main_mission_name")
        self.horizontalLayout_5.addWidget(self.label_main_mission_name)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.pushButton_mission_drop = QtWidgets.QPushButton(self.widget_main_mission)
        self.pushButton_mission_drop.setMinimumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_mission_drop.setFont(font)
        self.pushButton_mission_drop.setStyleSheet("QPushButton{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 15px;\n"
"border-bottom: none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 15px;\n"
"border: 2px solid  rgb(199, 27, 32);\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(199, 27, 32);\n"
"border-radius: 15px;\n"
"border: 2px solid  rgb(199, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_mission_drop.setObjectName("pushButton_mission_drop")
        self.horizontalLayout_5.addWidget(self.pushButton_mission_drop)
        self.pushButton_mission_change = QtWidgets.QPushButton(self.widget_main_mission)
        self.pushButton_mission_change.setMinimumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_mission_change.setFont(font)
        self.pushButton_mission_change.setStyleSheet("QPushButton{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 15px;\n"
"border-bottom: none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 15px;\n"
"border: 2px solid  rgb(199, 27, 32);\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(199, 27, 32);\n"
"border-radius: 15px;\n"
"border: 2px solid  rgb(199, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_mission_change.setObjectName("pushButton_mission_change")
        self.horizontalLayout_5.addWidget(self.pushButton_mission_change)
        self.verticalLayout_main_left.addWidget(self.widget_main_mission)
        self.horizontalLayout_8.addLayout(self.verticalLayout_main_left)
        self.line = QtWidgets.QFrame(self.page_main)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_8.addWidget(self.line)
        self.widget_main_right = QtWidgets.QWidget(self.page_main)
        self.widget_main_right.setMaximumSize(QtCore.QSize(349, 16777215))
        self.widget_main_right.setObjectName("widget_main_right")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_main_right)
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_logo = QtWidgets.QHBoxLayout()
        self.horizontalLayout_logo.setObjectName("horizontalLayout_logo")
        self.label_flag = QtWidgets.QLabel(self.widget_main_right)
        self.label_flag.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_flag.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_flag.setText("")
        self.label_flag.setPixmap(QtGui.QPixmap(":/logo/images.png"))
        self.label_flag.setScaledContents(True)
        self.label_flag.setAlignment(QtCore.Qt.AlignCenter)
        self.label_flag.setWordWrap(False)
        self.label_flag.setObjectName("label_flag")
        self.horizontalLayout_logo.addWidget(self.label_flag)
        self.label_casmarine = QtWidgets.QLabel(self.widget_main_right)
        self.label_casmarine.setMaximumSize(QtCore.QSize(16777215, 70))
        self.label_casmarine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_casmarine.setText("")
        self.label_casmarine.setPixmap(QtGui.QPixmap(":/logo/caslogo_black.png"))
        self.label_casmarine.setScaledContents(True)
        self.label_casmarine.setAlignment(QtCore.Qt.AlignCenter)
        self.label_casmarine.setObjectName("label_casmarine")
        self.horizontalLayout_logo.addWidget(self.label_casmarine)
        self.verticalLayout_3.addLayout(self.horizontalLayout_logo)
        self.line_2 = QtWidgets.QFrame(self.widget_main_right)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.widget_timer = QtWidgets.QWidget(self.widget_main_right)
        self.widget_timer.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 10px")
        self.widget_timer.setObjectName("widget_timer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_timer)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_timer = QtWidgets.QLabel(self.widget_timer)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_timer.setFont(font)
        self.label_timer.setStyleSheet("color: rgb(10, 36, 99);")
        self.label_timer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_timer.setObjectName("label_timer")
        self.verticalLayout_2.addWidget(self.label_timer)
        self.horizontalLayout_timer_buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_timer_buttons.setObjectName("horizontalLayout_timer_buttons")
        self.pushButton_timer_start = QtWidgets.QPushButton(self.widget_timer)
        self.pushButton_timer_start.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_timer_start.setFont(font)
        self.pushButton_timer_start.setStyleSheet("QPushButton{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 15px;\n"
"border-bottom: none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 15px;\n"
"border: 2px solid  rgb(199, 27, 32);\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(199, 27, 32);\n"
"border-radius: 15px;\n"
"border: 2px solid  rgb(199, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_timer_start.setObjectName("pushButton_timer_start")
        self.horizontalLayout_timer_buttons.addWidget(self.pushButton_timer_start)
        self.pushButton_timer_stop = QtWidgets.QPushButton(self.widget_timer)
        self.pushButton_timer_stop.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_timer_stop.setFont(font)
        self.pushButton_timer_stop.setStyleSheet("QPushButton{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 15px;\n"
"border-bottom: none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 15px;\n"
"border: 2px solid  rgb(199, 27, 32);\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(199, 27, 32);\n"
"border-radius: 15px;\n"
"border: 2px solid  rgb(199, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_timer_stop.setObjectName("pushButton_timer_stop")
        self.horizontalLayout_timer_buttons.addWidget(self.pushButton_timer_stop)
        self.pushButton_timer_end = QtWidgets.QPushButton(self.widget_timer)
        self.pushButton_timer_end.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_timer_end.setFont(font)
        self.pushButton_timer_end.setStyleSheet("QPushButton{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 15px;\n"
"border-bottom: none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 15px;\n"
"border: 2px solid  rgb(199, 27, 32);\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(199, 27, 32);\n"
"border-radius: 15px;\n"
"border: 2px solid  rgb(199, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_timer_end.setObjectName("pushButton_timer_end")
        self.horizontalLayout_timer_buttons.addWidget(self.pushButton_timer_end)
        self.verticalLayout_2.addLayout(self.horizontalLayout_timer_buttons)
        self.verticalLayout_3.addWidget(self.widget_timer)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.widget_values = QtWidgets.QWidget(self.widget_main_right)
        self.widget_values.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 10px;\n"
"color: rgb(10, 36, 99);")
        self.widget_values.setObjectName("widget_values")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_values)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_infos = QtWidgets.QLabel(self.widget_values)
        self.label_infos.setMinimumSize(QtCore.QSize(0, 44))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_infos.setFont(font)
        self.label_infos.setStyleSheet("color: rgb(10, 36, 99);")
        self.label_infos.setAlignment(QtCore.Qt.AlignCenter)
        self.label_infos.setObjectName("label_infos")
        self.verticalLayout_5.addWidget(self.label_infos)
        self.label_value_1 = QtWidgets.QLabel(self.widget_values)
        self.label_value_1.setMinimumSize(QtCore.QSize(0, 44))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_value_1.setFont(font)
        self.label_value_1.setStyleSheet("QLabel{\n"
"background-color: rgb(36, 123, 160);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-left: 7px}")
        self.label_value_1.setObjectName("label_value_1")
        self.verticalLayout_5.addWidget(self.label_value_1)
        self.label_value_2 = QtWidgets.QLabel(self.widget_values)
        self.label_value_2.setMinimumSize(QtCore.QSize(0, 44))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_value_2.setFont(font)
        self.label_value_2.setStyleSheet("QLabel{\n"
"background-color: rgb(36, 123, 160);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-left: 7px}")
        self.label_value_2.setObjectName("label_value_2")
        self.verticalLayout_5.addWidget(self.label_value_2)
        self.verticalLayout_3.addWidget(self.widget_values)
        self.widget_cyro = QtWidgets.QWidget(self.widget_main_right)
        self.widget_cyro.setMinimumSize(QtCore.QSize(300, 350))
        self.widget_cyro.setMaximumSize(QtCore.QSize(16777215, 350))
        self.widget_cyro.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 10px;")
        self.widget_cyro.setObjectName("widget_cyro")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_cyro)
        self.horizontalLayout.setContentsMargins(6, 4, 6, 4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3.addWidget(self.widget_cyro)
        self.horizontalLayout_8.addWidget(self.widget_main_right)
        self.stackedWidget.addWidget(self.page_main)
        self.page_missions = QtWidgets.QWidget()
        self.page_missions.setObjectName("page_missions")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_missions)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_missions = QtWidgets.QVBoxLayout()
        self.verticalLayout_missions.setObjectName("verticalLayout_missions")
        self.horizontalLayout_missions_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_missions_1.setObjectName("horizontalLayout_missions_1")
        self.widget_mission_1 = QtWidgets.QWidget(self.page_missions)
        self.widget_mission_1.setMinimumSize(QtCore.QSize(197, 240))
        self.widget_mission_1.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"border-radius: 10px;")
        self.widget_mission_1.setObjectName("widget_mission_1")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget_mission_1)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_mission_image = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mission_image.setObjectName("horizontalLayout_mission_image")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_mission_image.addItem(spacerItem4)
        self.label_mission_image_1 = QtWidgets.QLabel(self.widget_mission_1)
        self.label_mission_image_1.setMinimumSize(QtCore.QSize(100, 100))
        self.label_mission_image_1.setMaximumSize(QtCore.QSize(100, 100))
        self.label_mission_image_1.setStyleSheet("")
        self.label_mission_image_1.setText("")
        self.label_mission_image_1.setPixmap(QtGui.QPixmap(":/logo/alg_yosun_1.jpg"))
        self.label_mission_image_1.setScaledContents(True)
        self.label_mission_image_1.setWordWrap(False)
        self.label_mission_image_1.setObjectName("label_mission_image_1")
        self.horizontalLayout_mission_image.addWidget(self.label_mission_image_1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_mission_image.addItem(spacerItem5)
        self.verticalLayout_16.addLayout(self.horizontalLayout_mission_image)
        self.label_mission_name_1 = QtWidgets.QLabel(self.widget_mission_1)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_mission_name_1.setFont(font)
        self.label_mission_name_1.setStyleSheet("color: rgb(10, 36, 99);")
        self.label_mission_name_1.setObjectName("label_mission_name_1")
        self.verticalLayout_16.addWidget(self.label_mission_name_1)
        self.pushButton_mission_select_1 = QtWidgets.QPushButton(self.widget_mission_1)
        self.pushButton_mission_select_1.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_mission_select_1.setFont(font)
        self.pushButton_mission_select_1.setStyleSheet("QPushButton{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 25px;\n"
"border-bottom: none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 25px;\n"
"border: 3px solid  rgb(199, 27, 32);\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(199, 27, 32);\n"
"border-radius: 25px;\n"
"border: 3px solid  rgb(199, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_mission_select_1.setObjectName("pushButton_mission_select_1")
        self.verticalLayout_16.addWidget(self.pushButton_mission_select_1)
        self.horizontalLayout_missions_1.addWidget(self.widget_mission_1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_missions_1.addItem(spacerItem6)
        self.widget_mission_2 = QtWidgets.QWidget(self.page_missions)
        self.widget_mission_2.setMinimumSize(QtCore.QSize(197, 240))
        self.widget_mission_2.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border-radius: 10px;")
        self.widget_mission_2.setObjectName("widget_mission_2")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget_mission_2)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_mission_image_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mission_image_2.setObjectName("horizontalLayout_mission_image_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_mission_image_2.addItem(spacerItem7)
        self.label_mission_image_2 = QtWidgets.QLabel(self.widget_mission_2)
        self.label_mission_image_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_mission_image_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_mission_image_2.setStyleSheet("border-radius: 5px;")
        self.label_mission_image_2.setText("")
        self.label_mission_image_2.setPixmap(QtGui.QPixmap(":/logo/alg_yosun_1.jpg"))
        self.label_mission_image_2.setScaledContents(True)
        self.label_mission_image_2.setObjectName("label_mission_image_2")
        self.horizontalLayout_mission_image_2.addWidget(self.label_mission_image_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_mission_image_2.addItem(spacerItem8)
        self.verticalLayout_17.addLayout(self.horizontalLayout_mission_image_2)
        self.label_mission_name_2 = QtWidgets.QLabel(self.widget_mission_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_mission_name_2.setFont(font)
        self.label_mission_name_2.setStyleSheet("color: rgb(10, 36, 99);")
        self.label_mission_name_2.setObjectName("label_mission_name_2")
        self.verticalLayout_17.addWidget(self.label_mission_name_2)
        self.pushButton_mission_select_2 = QtWidgets.QPushButton(self.widget_mission_2)
        self.pushButton_mission_select_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_mission_select_2.setFont(font)
        self.pushButton_mission_select_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 25px;\n"
"border-bottom: none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 25px;\n"
"border: 3px solid  rgb(199, 27, 32);\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(199, 27, 32);\n"
"border-radius: 25px;\n"
"border: 3px solid  rgb(199, 27, 32);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_mission_select_2.setObjectName("pushButton_mission_select_2")
        self.verticalLayout_17.addWidget(self.pushButton_mission_select_2)
        self.horizontalLayout_missions_1.addWidget(self.widget_mission_2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_missions_1.addItem(spacerItem9)
        self.widget_mission_3 = QtWidgets.QWidget(self.page_missions)
        self.widget_mission_3.setMinimumSize(QtCore.QSize(197, 240))
        self.widget_mission_3.setStyleSheet("background-color: rgb(245, 245, 220);\n"
"border-radius: 10px;")
        self.widget_mission_3.setObjectName("widget_mission_3")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.widget_mission_3)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_missions_1.addWidget(self.widget_mission_3)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_missions_1.addItem(spacerItem10)
        self.widget_mission_4 = QtWidgets.QWidget(self.page_missions)
        self.widget_mission_4.setMinimumSize(QtCore.QSize(197, 240))
        self.widget_mission_4.setStyleSheet("background-color: rgb(245, 245, 220);\n"
"border-radius: 10px;")
        self.widget_mission_4.setObjectName("widget_mission_4")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.widget_mission_4)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_missions_1.addWidget(self.widget_mission_4)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_missions_1.addItem(spacerItem11)
        self.widget_mission_5 = QtWidgets.QWidget(self.page_missions)
        self.widget_mission_5.setMinimumSize(QtCore.QSize(197, 240))
        self.widget_mission_5.setStyleSheet("background-color: rgb(245, 245, 220);\n"
"border-radius: 10px;")
        self.widget_mission_5.setObjectName("widget_mission_5")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.widget_mission_5)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.horizontalLayout_missions_1.addWidget(self.widget_mission_5)
        self.horizontalLayout_missions_1.setStretch(0, 1)
        self.horizontalLayout_missions_1.setStretch(2, 1)
        self.horizontalLayout_missions_1.setStretch(4, 1)
        self.horizontalLayout_missions_1.setStretch(6, 1)
        self.horizontalLayout_missions_1.setStretch(8, 1)
        self.verticalLayout_missions.addLayout(self.horizontalLayout_missions_1)
        self.horizontalLayout_missions_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_missions_2.setObjectName("horizontalLayout_missions_2")
        self.widget_mission_6 = QtWidgets.QWidget(self.page_missions)
        self.widget_mission_6.setMinimumSize(QtCore.QSize(197, 240))
        self.widget_mission_6.setStyleSheet("background-color: rgb(245, 245, 220);\n"
"border-radius: 10px;")
        self.widget_mission_6.setObjectName("widget_mission_6")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.widget_mission_6)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_missions_2.addWidget(self.widget_mission_6)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_missions_2.addItem(spacerItem12)
        self.widget_mission_7 = QtWidgets.QWidget(self.page_missions)
        self.widget_mission_7.setMinimumSize(QtCore.QSize(197, 240))
        self.widget_mission_7.setStyleSheet("background-color: rgb(245, 245, 220);\n"
"border-radius: 10px;")
        self.widget_mission_7.setObjectName("widget_mission_7")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.widget_mission_7)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_missions_2.addWidget(self.widget_mission_7)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_missions_2.addItem(spacerItem13)
        self.widget_mission_8 = QtWidgets.QWidget(self.page_missions)
        self.widget_mission_8.setMinimumSize(QtCore.QSize(197, 240))
        self.widget_mission_8.setStyleSheet("background-color: rgb(245, 245, 220);\n"
"border-radius: 10px;")
        self.widget_mission_8.setObjectName("widget_mission_8")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.widget_mission_8)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_missions_2.addWidget(self.widget_mission_8)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_missions_2.addItem(spacerItem14)
        self.widget_mission_9 = QtWidgets.QWidget(self.page_missions)
        self.widget_mission_9.setMinimumSize(QtCore.QSize(197, 240))
        self.widget_mission_9.setStyleSheet("background-color: rgb(245, 245, 220);\n"
"border-radius: 10px;")
        self.widget_mission_9.setObjectName("widget_mission_9")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.widget_mission_9)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_missions_2.addWidget(self.widget_mission_9)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_missions_2.addItem(spacerItem15)
        self.widget_mission_10 = QtWidgets.QWidget(self.page_missions)
        self.widget_mission_10.setMinimumSize(QtCore.QSize(197, 240))
        self.widget_mission_10.setStyleSheet("background-color: rgb(245, 245, 220);\n"
"border-radius: 10px;")
        self.widget_mission_10.setObjectName("widget_mission_10")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.widget_mission_10)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.horizontalLayout_missions_2.addWidget(self.widget_mission_10)
        self.horizontalLayout_missions_2.setStretch(0, 1)
        self.horizontalLayout_missions_2.setStretch(2, 1)
        self.horizontalLayout_missions_2.setStretch(4, 1)
        self.horizontalLayout_missions_2.setStretch(6, 1)
        self.horizontalLayout_missions_2.setStretch(8, 1)
        self.verticalLayout_missions.addLayout(self.horizontalLayout_missions_2)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_missions.addItem(spacerItem16)
        self.verticalLayout_4.addLayout(self.verticalLayout_missions)
        self.stackedWidget.addWidget(self.page_missions)
        self.page_pid = QtWidgets.QWidget()
        self.page_pid.setObjectName("page_pid")
        self.gridLayout = QtWidgets.QGridLayout(self.page_pid)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_pid = QtWidgets.QGridLayout()
        self.gridLayout_pid.setObjectName("gridLayout_pid")
        self.verticalLayout_pid = QtWidgets.QVBoxLayout()
        self.verticalLayout_pid.setObjectName("verticalLayout_pid")
        self.horizontalLayout_pid_title = QtWidgets.QHBoxLayout()
        self.horizontalLayout_pid_title.setObjectName("horizontalLayout_pid_title")
        self.label_pid_title_empty = QtWidgets.QLabel(self.page_pid)
        self.label_pid_title_empty.setMinimumSize(QtCore.QSize(78, 44))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_pid_title_empty.setFont(font)
        self.label_pid_title_empty.setStyleSheet("QLabel{\n"
"border-radius: 10px;\n"
"padding-left: 7px;\n"
"color: rgb(245, 245, 220);\n"
"}")
        self.label_pid_title_empty.setText("")
        self.label_pid_title_empty.setObjectName("label_pid_title_empty")
        self.horizontalLayout_pid_title.addWidget(self.label_pid_title_empty)
        self.lineEdit_pid_title_p = QtWidgets.QLineEdit(self.page_pid)
        self.lineEdit_pid_title_p.setMinimumSize(QtCore.QSize(0, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_pid_title_p.setFont(font)
        self.lineEdit_pid_title_p.setStyleSheet("")
        self.lineEdit_pid_title_p.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pid_title_p.setObjectName("lineEdit_pid_title_p")
        self.horizontalLayout_pid_title.addWidget(self.lineEdit_pid_title_p)
        self.lineEdit_pid_title_i = QtWidgets.QLineEdit(self.page_pid)
        self.lineEdit_pid_title_i.setMinimumSize(QtCore.QSize(0, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_pid_title_i.setFont(font)
        self.lineEdit_pid_title_i.setStyleSheet("")
        self.lineEdit_pid_title_i.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pid_title_i.setObjectName("lineEdit_pid_title_i")
        self.horizontalLayout_pid_title.addWidget(self.lineEdit_pid_title_i)
        self.lineEdit_pid_title_d = QtWidgets.QLineEdit(self.page_pid)
        self.lineEdit_pid_title_d.setMinimumSize(QtCore.QSize(0, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_pid_title_d.setFont(font)
        self.lineEdit_pid_title_d.setStyleSheet("")
        self.lineEdit_pid_title_d.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pid_title_d.setObjectName("lineEdit_pid_title_d")
        self.horizontalLayout_pid_title.addWidget(self.lineEdit_pid_title_d)
        self.verticalLayout_pid.addLayout(self.horizontalLayout_pid_title)
        self.horizontalLayout_pid_roll = QtWidgets.QHBoxLayout()
        self.horizontalLayout_pid_roll.setObjectName("horizontalLayout_pid_roll")
        self.label_pid_roll_title = QtWidgets.QLabel(self.page_pid)
        self.label_pid_roll_title.setMinimumSize(QtCore.QSize(78, 44))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_pid_roll_title.setFont(font)
        self.label_pid_roll_title.setStyleSheet("QLabel{\n"
"background-color: rgb(36, 123, 160);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px}")
        self.label_pid_roll_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pid_roll_title.setObjectName("label_pid_roll_title")
        self.horizontalLayout_pid_roll.addWidget(self.label_pid_roll_title)
        self.lineEdit_pid_roll_p = QtWidgets.QLineEdit(self.page_pid)
        self.lineEdit_pid_roll_p.setMinimumSize(QtCore.QSize(0, 44))
        self.lineEdit_pid_roll_p.setStyleSheet("border-radius: 10px;\n"
"padding-left: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(226, 226, 226);")
        self.lineEdit_pid_roll_p.setObjectName("lineEdit_pid_roll_p")
        self.horizontalLayout_pid_roll.addWidget(self.lineEdit_pid_roll_p)
        self.lineEdit_pid_roll_i = QtWidgets.QLineEdit(self.page_pid)
        self.lineEdit_pid_roll_i.setMinimumSize(QtCore.QSize(0, 44))
        self.lineEdit_pid_roll_i.setStyleSheet("border-radius: 10px;\n"
"padding-left: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(226, 226, 226);")
        self.lineEdit_pid_roll_i.setObjectName("lineEdit_pid_roll_i")
        self.horizontalLayout_pid_roll.addWidget(self.lineEdit_pid_roll_i)
        self.lineEdit_pid_roll_d = QtWidgets.QLineEdit(self.page_pid)
        self.lineEdit_pid_roll_d.setMinimumSize(QtCore.QSize(0, 44))
        self.lineEdit_pid_roll_d.setStyleSheet("border-radius: 10px;\n"
"padding-left: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(226, 226, 226);")
        self.lineEdit_pid_roll_d.setObjectName("lineEdit_pid_roll_d")
        self.horizontalLayout_pid_roll.addWidget(self.lineEdit_pid_roll_d)
        self.verticalLayout_pid.addLayout(self.horizontalLayout_pid_roll)
        self.horizontalLayout_pid_depth = QtWidgets.QHBoxLayout()
        self.horizontalLayout_pid_depth.setObjectName("horizontalLayout_pid_depth")
        self.label_pid_depth_title = QtWidgets.QLabel(self.page_pid)
        self.label_pid_depth_title.setMinimumSize(QtCore.QSize(78, 44))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_pid_depth_title.setFont(font)
        self.label_pid_depth_title.setStyleSheet("QLabel{\n"
"background-color: rgb(36, 123, 160);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px}")
        self.label_pid_depth_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pid_depth_title.setObjectName("label_pid_depth_title")
        self.horizontalLayout_pid_depth.addWidget(self.label_pid_depth_title)
        self.lineEdit_pid_depth_p = QtWidgets.QLineEdit(self.page_pid)
        self.lineEdit_pid_depth_p.setMinimumSize(QtCore.QSize(0, 44))
        self.lineEdit_pid_depth_p.setStyleSheet("border-radius: 10px;\n"
"padding-left: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(226, 226, 226);")
        self.lineEdit_pid_depth_p.setObjectName("lineEdit_pid_depth_p")
        self.horizontalLayout_pid_depth.addWidget(self.lineEdit_pid_depth_p)
        self.lineEdit_pid_depth_i = QtWidgets.QLineEdit(self.page_pid)
        self.lineEdit_pid_depth_i.setMinimumSize(QtCore.QSize(0, 44))
        self.lineEdit_pid_depth_i.setStyleSheet("border-radius: 10px;\n"
"padding-left: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(226, 226, 226);")
        self.lineEdit_pid_depth_i.setObjectName("lineEdit_pid_depth_i")
        self.horizontalLayout_pid_depth.addWidget(self.lineEdit_pid_depth_i)
        self.lineEdit_pid_depth_d = QtWidgets.QLineEdit(self.page_pid)
        self.lineEdit_pid_depth_d.setMinimumSize(QtCore.QSize(0, 44))
        self.lineEdit_pid_depth_d.setStyleSheet("border-radius: 10px;\n"
"padding-left: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(226, 226, 226);")
        self.lineEdit_pid_depth_d.setObjectName("lineEdit_pid_depth_d")
        self.horizontalLayout_pid_depth.addWidget(self.lineEdit_pid_depth_d)
        self.verticalLayout_pid.addLayout(self.horizontalLayout_pid_depth)
        self.horizontalLayout_pid_pitch = QtWidgets.QHBoxLayout()
        self.horizontalLayout_pid_pitch.setObjectName("horizontalLayout_pid_pitch")
        self.label_pid_pitch_title = QtWidgets.QLabel(self.page_pid)
        self.label_pid_pitch_title.setMinimumSize(QtCore.QSize(78, 44))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_pid_pitch_title.setFont(font)
        self.label_pid_pitch_title.setStyleSheet("QLabel{\n"
"background-color: rgb(36, 123, 160);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px}")
        self.label_pid_pitch_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pid_pitch_title.setObjectName("label_pid_pitch_title")
        self.horizontalLayout_pid_pitch.addWidget(self.label_pid_pitch_title)
        self.lineEdit_pid_pitch_p = QtWidgets.QLineEdit(self.page_pid)
        self.lineEdit_pid_pitch_p.setMinimumSize(QtCore.QSize(0, 44))
        self.lineEdit_pid_pitch_p.setStyleSheet("border-radius: 10px;\n"
"padding-left: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(226, 226, 226);")
        self.lineEdit_pid_pitch_p.setObjectName("lineEdit_pid_pitch_p")
        self.horizontalLayout_pid_pitch.addWidget(self.lineEdit_pid_pitch_p)
        self.lineEdit_pid_pitch_i = QtWidgets.QLineEdit(self.page_pid)
        self.lineEdit_pid_pitch_i.setMinimumSize(QtCore.QSize(0, 44))
        self.lineEdit_pid_pitch_i.setStyleSheet("border-radius: 10px;\n"
"padding-left: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(226, 226, 226);")
        self.lineEdit_pid_pitch_i.setObjectName("lineEdit_pid_pitch_i")
        self.horizontalLayout_pid_pitch.addWidget(self.lineEdit_pid_pitch_i)
        self.lineEdit_pid_pitch_d = QtWidgets.QLineEdit(self.page_pid)
        self.lineEdit_pid_pitch_d.setMinimumSize(QtCore.QSize(0, 44))
        self.lineEdit_pid_pitch_d.setStyleSheet("border-radius: 10px;\n"
"padding-left: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(226, 226, 226);")
        self.lineEdit_pid_pitch_d.setObjectName("lineEdit_pid_pitch_d")
        self.horizontalLayout_pid_pitch.addWidget(self.lineEdit_pid_pitch_d)
        self.verticalLayout_pid.addLayout(self.horizontalLayout_pid_pitch)
        self.horizontalLayout_pid_buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_pid_buttons.setObjectName("horizontalLayout_pid_buttons")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_pid_buttons.addItem(spacerItem17)
        self.pushButton_pid_update = QtWidgets.QPushButton(self.page_pid)
        self.pushButton_pid_update.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_pid_update.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_pid_update.setStyleSheet("QPushButton{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 10px;\n"
"border-bottom: none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 85, 91);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(199, 27, 32);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_pid_update.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/logo/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_pid_update.setIcon(icon4)
        self.pushButton_pid_update.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_pid_update.setObjectName("pushButton_pid_update")
        self.horizontalLayout_pid_buttons.addWidget(self.pushButton_pid_update)
        self.pushButton_pid_upload = QtWidgets.QPushButton(self.page_pid)
        self.pushButton_pid_upload.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_pid_upload.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_pid_upload.setStyleSheet("QPushButton{\n"
"background-color: rgb(251, 54, 64);\n"
"border-radius: 10px;\n"
"border-bottom: none;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 85, 91);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:focus:pressed{\n"
"background-color: rgb(199, 27, 32);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_pid_upload.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/logo/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_pid_upload.setIcon(icon5)
        self.pushButton_pid_upload.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_pid_upload.setObjectName("pushButton_pid_upload")
        self.horizontalLayout_pid_buttons.addWidget(self.pushButton_pid_upload)
        self.verticalLayout_pid.addLayout(self.horizontalLayout_pid_buttons)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_pid.addItem(spacerItem18)
        self.gridLayout_pid.addLayout(self.verticalLayout_pid, 0, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_pid.addItem(spacerItem19, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_pid, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_pid)
        self.page_code = QtWidgets.QWidget()
        self.page_code.setObjectName("page_code")
        self.stackedWidget.addWidget(self.page_code)
        self.horizontalLayout_main.addWidget(self.stackedWidget)
        self.gridLayout_3.addLayout(self.horizontalLayout_main, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_menu_home.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>QPushButton{</p><p>background-color: none;</p><p>border: none;</p><p>}</p><p>QPushButton:hover{</p><p>background-color: none;</p><p>border: none;</p><p>}</p><p>QPushButton:focus:pressed{</p><p>background-color: none;</p><p>border: none;</p><p>}</p></body></html>"))
        self.pushButton_mission_start.setText(_translate("MainWindow", "Görevi Başlat"))
        self.pushButton_mission_end.setText(_translate("MainWindow", "Görevi Durdur"))
        self.label_main_mission_name.setText(_translate("MainWindow", "<html><head/><body><p>Yosun Uzerinde Cizgi Bulma Gorevi</p></body></html>"))
        self.pushButton_mission_drop.setText(_translate("MainWindow", "Görevi Bırak"))
        self.pushButton_mission_change.setText(_translate("MainWindow", "Görevi Değiştir"))
        self.label_timer.setText(_translate("MainWindow", "00:00:00"))
        self.pushButton_timer_start.setText(_translate("MainWindow", "Başlat"))
        self.pushButton_timer_stop.setText(_translate("MainWindow", "Durdur"))
        self.pushButton_timer_end.setText(_translate("MainWindow", "Bitir"))
        self.label_infos.setText(_translate("MainWindow", "Araç Bilgileri"))
        self.label_value_1.setText(_translate("MainWindow", "TextLabel"))
        self.label_value_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_mission_name_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Yosun Uzerınde</p><p align=\"center\">Cızgı Bulma Gorevı</p></body></html>"))
        self.pushButton_mission_select_1.setText(_translate("MainWindow", "Görevi Seç"))
        self.label_mission_name_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Yosun Uzerınde</p><p align=\"center\">Cızgı Bulma Gorevı</p></body></html>"))
        self.pushButton_mission_select_2.setText(_translate("MainWindow", "Görevi Seç"))
        self.lineEdit_pid_title_p.setText(_translate("MainWindow", "P"))
        self.lineEdit_pid_title_i.setText(_translate("MainWindow", "I"))
        self.lineEdit_pid_title_d.setText(_translate("MainWindow", "D"))
        self.label_pid_roll_title.setText(_translate("MainWindow", "Roll"))
        self.label_pid_depth_title.setText(_translate("MainWindow", "Depth"))
        self.label_pid_pitch_title.setText(_translate("MainWindow", "Pitch"))
import cas_gui_2.source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
