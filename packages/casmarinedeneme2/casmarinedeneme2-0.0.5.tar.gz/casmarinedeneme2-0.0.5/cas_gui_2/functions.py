from PyQt5.QtWidgets import *
from cas_gui_2.interface import Ui_MainWindow
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal, pyqtSlot
import time
import datetime
import cv2 as cv
import numpy as np
from PyQt5.QtGui import QPixmap
import cas_gui_2.qfi_ADI as qfi_ADI
import cas_gui_2.qfi_ADI_dark as qfi_ADI_dark
import cas_gui_2.database as db
from cas_gui_2.missions_enum import Missions
from cas_gui_2.style import Style


CAMERA_LABEL_RATIO = 1.3333

class Interface(QMainWindow):

        def __init__(self):
                super().__init__()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)

                #First Design Arrangements
                self.DesignArrangements()

                #Resize Event
                self.ui.centralwidget.resizeEvent = self.ResizeAllWidget
                
                #Menu
                self.ui.pushButton_menu_home.clicked.connect(self.clickedHomeButton)
                self.ui.pushButton_menu_pid.clicked.connect(self.clickedPidButton)
                self.ui.pushButton_menu_code.clicked.connect(self.clickedCodeButton)

                #Timer
                self.QTtimer = QTimer()
                self.QTtimer.setInterval(100)
                self.QTtimer.timeout.connect(self.Timer)
                self.QTsetTimer = QTimer()
                self.QTsetTimer.setInterval(100)
                self.QTsetTimer.timeout.connect(self.SetTimer)
                self.timer = 0
                self.timerIsActive = False
                self.ui.pushButton_timer_start.clicked.connect(self.StartTimer)
                self.ui.pushButton_timer_stop.clicked.connect(self.StopTimer)
                self.ui.pushButton_timer_end.clicked.connect(self.EndTimer)

                #Cyro
                self.adi = qfi_ADI.qfi_ADI(self)
                self.ui.horizontalLayout.addWidget(self.adi)

                #Set Info Timer
                self.infos = QTimer()
                self.infos.setInterval(100)
                self.infos.timeout.connect(self.SetInfos)
                self.infos.start()

                #Open Camera Timer
                self.capture = cv.VideoCapture(0)
                self.openCameraTimer = QTimer()
                self.openCameraTimer.setInterval(int(1000/30))
                self.openCameraTimer.timeout.connect(self.openCamera)
                self.openCameraTimer.start()

                #Open Camera Timer
                self.capture2 = cv.VideoCapture(2)
                self.openCameraTimer2 = QTimer()
                self.openCameraTimer2.setInterval(int(1000/30))
                self.openCameraTimer2.timeout.connect(self.openUSB)
                self.openCameraTimer2.start()

                #Set Front Camera Timer
                self.setFrontCameraTimer = QTimer()
                self.setFrontCameraTimer.setInterval(int(1000/30))
                self.setFrontCameraTimer.timeout.connect(self.SetFrontCamera)
                self.setFrontCameraTimer.start()

                #Set Bottom Camera Timer
                self.setBottomCameraTimer = QTimer()
                self.setBottomCameraTimer.setInterval(int(1000/30))
                self.setBottomCameraTimer.timeout.connect(self.SetBottomCamera)
                self.setBottomCameraTimer.start()

                #Missions
                self.mission = None
                self.startMission = False
                self.ui.pushButton_mission_change.clicked.connect(self.clickedMissionChangeButton)
                self.ui.pushButton_mission_select_1.clicked.connect(self.missionSelect1)
                self.ui.pushButton_mission_select_2.clicked.connect(self.missionSelect2)
                self.ui.pushButton_mission_drop.clicked.connect(self.MissionDrop)
                self.ui.pushButton_mission_start.clicked.connect(self.MissionStart)
                self.ui.pushButton_mission_end.clicked.connect(self.MissionEnd)

                #Theme Mode
                self.lightMode = True
                self.ui.pushButton_theme_mode.clicked.connect(self.ThemeMode)
                self.activeMenu = 0
                self.ThemeMode()
                
        def ThemeMode(self):
            if self.lightMode == False:
                self.lightMode = True
                self.infos.stop()

                self.ui.horizontalLayout.itemAt(0).widget().deleteLater()
                self.adi = qfi_ADI.qfi_ADI(self)
                self.ui.horizontalLayout.addWidget(self.adi)

                self.ui.pushButton_theme_mode.setIcon(Style.LightMoonIcon())
                self.ui.pushButton_menu_home.setIcon(Style.LightHomeIcon())
                self.ui.pushButton_menu_pid.setIcon(Style.LightPIDIcon())
                self.ui.pushButton_menu_code.setIcon(Style.LightCodeIcon())
                self.ui.label_main_mission_image.setPixmap(Style.LightMissionsIcon())
                self.ui.pushButton_theme_mode.setIconSize(QtCore.QSize(35, 35))
                self.ui.widget_menu.setStyleSheet(Style.LightMenuWidget())
                if self.activeMenu == 0:
                    self.ui.pushButton_menu_home.setStyleSheet(Style.LightMenuButtonClicked())
                    self.ui.pushButton_menu_pid.setStyleSheet(Style.LightMenuButton())
                    self.ui.pushButton_menu_code.setStyleSheet(Style.LightMenuButton())
                elif self.activeMenu == 2:
                    self.ui.pushButton_menu_home.setStyleSheet(Style.LightMenuButton())
                    self.ui.pushButton_menu_pid.setStyleSheet(Style.LightMenuButtonClicked())
                    self.ui.pushButton_menu_code.setStyleSheet(Style.LightMenuButton())
                elif self.activeMenu == 3:
                    self.ui.pushButton_menu_home.setStyleSheet(Style.LightMenuButton())
                    self.ui.pushButton_menu_pid.setStyleSheet(Style.LightMenuButton())
                    self.ui.pushButton_menu_code.setStyleSheet(Style.LightMenuButtonClicked())

                self.ui.pushButton_theme_mode.setStyleSheet(Style.LightThemeButton())
                self.ui.stackedWidget.setStyleSheet(Style.LightStackWidget())
                self.ui.label_camera_front.setStyleSheet(Style.LightCamera())
                self.ui.label_camera_bottom.setStyleSheet(Style.LightCamera())
                self.ui.pushButton_mission_start.setStyleSheet(Style.LightMissionSEButton())
                self.ui.pushButton_mission_end.setStyleSheet(Style.LightMissionSEButton())
                self.ui.widget_main_mission.setStyleSheet(Style.LightGeneralWidget())
                self.ui.label_main_mission_name.setStyleSheet(Style.LightModeDarkFont())
                self.ui.pushButton_mission_drop.setStyleSheet(Style.LightGeneralButton())
                self.ui.pushButton_mission_change.setStyleSheet(Style.LightGeneralButton())
                self.ui.widget_timer.setStyleSheet(Style.LightGeneralWidget())
                self.ui.label_timer.setStyleSheet(Style.LightModeDarkFont())
                self.ui.pushButton_timer_start.setStyleSheet(Style.LightGeneralButton())
                self.ui.pushButton_timer_stop.setStyleSheet(Style.LightGeneralButton())
                self.ui.pushButton_timer_end.setStyleSheet(Style.LightGeneralButton())
                self.ui.widget_values.setStyleSheet(Style.LightGeneralWidget())
                self.ui.label_infos.setStyleSheet(Style.LightModeDarkFont())
                self.ui.label_value_1.setStyleSheet(Style.LightInfoValue())
                self.ui.label_value_2.setStyleSheet(Style.LightInfoValue())
                self.ui.widget_cyro.setStyleSheet(Style.LightGeneralWidget())
                if self.mission == Missions.YOSUN:
                    self.ui.widget_mission_1.setStyleSheet(Style.LightSelectedMissionWidget())
                    self.ui.widget_mission_2.setStyleSheet(Style.LightGeneralWidget())
                else:
                    self.ui.widget_mission_1.setStyleSheet(Style.LightGeneralWidget())
                    self.ui.widget_mission_2.setStyleSheet(Style.LightGeneralWidget())

                self.ui.label_mission_name_1.setStyleSheet(Style.LightModeDarkFont())
                self.ui.pushButton_mission_select_1.setStyleSheet(Style.LightMissionSelectButton())
                self.ui.label_mission_name_2.setStyleSheet(Style.LightModeDarkFont())
                self.ui.pushButton_mission_select_2.setStyleSheet(Style.LightMissionSelectButton())
                self.ui.widget_mission_3.setStyleSheet(Style.LightDisabeleMissionWidget())
                self.ui.widget_mission_4.setStyleSheet(Style.LightDisabeleMissionWidget())
                self.ui.widget_mission_5.setStyleSheet(Style.LightDisabeleMissionWidget())
                self.ui.widget_mission_6.setStyleSheet(Style.LightDisabeleMissionWidget())
                self.ui.widget_mission_7.setStyleSheet(Style.LightDisabeleMissionWidget())
                self.ui.widget_mission_8.setStyleSheet(Style.LightDisabeleMissionWidget())
                self.ui.widget_mission_9.setStyleSheet(Style.LightDisabeleMissionWidget())
                self.ui.widget_mission_10.setStyleSheet(Style.LightDisabeleMissionWidget())
                self.ui.pushButton_pid_update.setStyleSheet(Style.LightPidButton())
                self.ui.pushButton_pid_upload.setStyleSheet(Style.LightPidButton())
                self.ui.lineEdit_pid_title_p.setStyleSheet(Style.LightModeDarkFont())
                self.ui.lineEdit_pid_title_i.setStyleSheet(Style.LightModeDarkFont())
                self.ui.lineEdit_pid_title_d.setStyleSheet(Style.LightModeDarkFont())
                self.ui.lineEdit_pid_roll_p.setStyleSheet(Style.LightPidValue())
                self.ui.lineEdit_pid_roll_i.setStyleSheet(Style.LightPidValue())
                self.ui.lineEdit_pid_roll_d.setStyleSheet(Style.LightPidValue())
                self.ui.lineEdit_pid_depth_p.setStyleSheet(Style.LightPidValue())
                self.ui.lineEdit_pid_depth_i.setStyleSheet(Style.LightPidValue())
                self.ui.lineEdit_pid_depth_d.setStyleSheet(Style.LightPidValue())
                self.ui.lineEdit_pid_pitch_p.setStyleSheet(Style.LightPidValue())
                self.ui.lineEdit_pid_pitch_i.setStyleSheet(Style.LightPidValue())
                self.ui.lineEdit_pid_pitch_d.setStyleSheet(Style.LightPidValue())
                self.ui.lineEdit_pid_title_i.setStyleSheet(Style.LightPidTitle())
                self.ui.lineEdit_pid_title_d.setStyleSheet(Style.LightPidTitle())
                self.ui.lineEdit_pid_title_p.setStyleSheet(Style.LightPidTitle())

                self.infos.start()

            else:
                self.lightMode = False
                self.infos.stop()

                self.ui.horizontalLayout.itemAt(0).widget().deleteLater()
                self.adi = qfi_ADI_dark.qfi_ADI(self)
                self.ui.horizontalLayout.addWidget(self.adi)

                self.ui.pushButton_theme_mode.setIcon(Style.DarkSunIcon())
                self.ui.pushButton_menu_home.setIcon(Style.DarkHomeIcon())
                self.ui.pushButton_menu_pid.setIcon(Style.DarkPIDIcon())
                self.ui.pushButton_menu_code.setIcon(Style.DarkCodeIcon())
                self.ui.label_main_mission_image.setPixmap(Style.DarkMissionsIcon())
                self.ui.pushButton_theme_mode.setIconSize(QtCore.QSize(35, 35))
                self.ui.widget_menu.setStyleSheet(Style.DarkMenuWidget())
                if self.activeMenu == 0:
                    self.ui.pushButton_menu_home.setStyleSheet(Style.DarkMenuButtonClicked())
                    self.ui.pushButton_menu_pid.setStyleSheet(Style.DarkMenuButton())
                    self.ui.pushButton_menu_code.setStyleSheet(Style.DarkMenuButton())
                elif self.activeMenu == 2:
                    self.ui.pushButton_menu_home.setStyleSheet(Style.DarkMenuButton())
                    self.ui.pushButton_menu_pid.setStyleSheet(Style.DarkMenuButtonClicked())
                    self.ui.pushButton_menu_code.setStyleSheet(Style.DarkMenuButton())
                elif self.activeMenu == 3:
                    self.ui.pushButton_menu_home.setStyleSheet(Style.DarkMenuButton())
                    self.ui.pushButton_menu_pid.setStyleSheet(Style.DarkMenuButton())
                    self.ui.pushButton_menu_code.setStyleSheet(Style.DarkMenuButtonClicked())

                self.ui.pushButton_theme_mode.setStyleSheet(Style.DarkThemeButton())
                self.ui.stackedWidget.setStyleSheet(Style.DarkStackWidget())
                self.ui.label_camera_front.setStyleSheet(Style.DarkCamera())
                self.ui.label_camera_bottom.setStyleSheet(Style.DarkCamera())
                self.ui.pushButton_mission_start.setStyleSheet(Style.DarkMissionSEButton())
                self.ui.pushButton_mission_end.setStyleSheet(Style.DarkMissionSEButton())
                self.ui.widget_main_mission.setStyleSheet(Style.DarkGeneralWidget())
                self.ui.label_main_mission_name.setStyleSheet(Style.DarkModeDarkFont())
                self.ui.pushButton_mission_drop.setStyleSheet(Style.DarkGeneralButton())
                self.ui.pushButton_mission_change.setStyleSheet(Style.DarkGeneralButton())
                self.ui.widget_timer.setStyleSheet(Style.DarkGeneralWidget())
                self.ui.label_timer.setStyleSheet(Style.DarkModeDarkFont())
                self.ui.pushButton_timer_start.setStyleSheet(Style.DarkGeneralButton())
                self.ui.pushButton_timer_stop.setStyleSheet(Style.DarkGeneralButton())
                self.ui.pushButton_timer_end.setStyleSheet(Style.DarkGeneralButton())
                self.ui.widget_values.setStyleSheet(Style.DarkGeneralWidget())
                self.ui.label_infos.setStyleSheet(Style.DarkModeDarkFont())
                self.ui.label_value_1.setStyleSheet(Style.DarkInfoValue())
                self.ui.label_value_2.setStyleSheet(Style.DarkInfoValue())
                self.ui.widget_cyro.setStyleSheet(Style.DarkGeneralWidget())
                if self.mission == Missions.YOSUN:
                    self.ui.widget_mission_1.setStyleSheet(Style.DarkSelectedMissionWidget())
                    self.ui.widget_mission_2.setStyleSheet(Style.DarkGeneralWidget())
                else:
                    self.ui.widget_mission_1.setStyleSheet(Style.DarkGeneralWidget())
                    self.ui.widget_mission_2.setStyleSheet(Style.DarkGeneralWidget())

                self.ui.label_mission_name_1.setStyleSheet(Style.DarkModeDarkFont())
                self.ui.pushButton_mission_select_1.setStyleSheet(Style.DarkMissionSelectButton())
                self.ui.label_mission_name_2.setStyleSheet(Style.DarkModeDarkFont())
                self.ui.pushButton_mission_select_2.setStyleSheet(Style.DarkMissionSelectButton())
                self.ui.widget_mission_3.setStyleSheet(Style.DarkDisabeleMissionWidget())
                self.ui.widget_mission_4.setStyleSheet(Style.DarkDisabeleMissionWidget())
                self.ui.widget_mission_5.setStyleSheet(Style.DarkDisabeleMissionWidget())
                self.ui.widget_mission_6.setStyleSheet(Style.DarkDisabeleMissionWidget())
                self.ui.widget_mission_7.setStyleSheet(Style.DarkDisabeleMissionWidget())
                self.ui.widget_mission_8.setStyleSheet(Style.DarkDisabeleMissionWidget())
                self.ui.widget_mission_9.setStyleSheet(Style.DarkDisabeleMissionWidget())
                self.ui.widget_mission_10.setStyleSheet(Style.DarkDisabeleMissionWidget())
                self.ui.pushButton_pid_update.setStyleSheet(Style.DarkPidButton())
                self.ui.pushButton_pid_upload.setStyleSheet(Style.DarkPidButton())
                self.ui.lineEdit_pid_title_p.setStyleSheet(Style.DarkModeDarkFont())
                self.ui.lineEdit_pid_title_i.setStyleSheet(Style.DarkModeDarkFont())
                self.ui.lineEdit_pid_title_d.setStyleSheet(Style.DarkModeDarkFont())
                self.ui.lineEdit_pid_roll_p.setStyleSheet(Style.DarkPidValue())
                self.ui.lineEdit_pid_title_i.setStyleSheet(Style.DarkModeDarkFont())
                self.ui.lineEdit_pid_title_d.setStyleSheet(Style.DarkModeDarkFont())
                self.ui.lineEdit_pid_roll_p.setStyleSheet(Style.DarkPidValue())
                self.ui.lineEdit_pid_roll_i.setStyleSheet(Style.DarkPidValue())
                self.ui.lineEdit_pid_roll_d.setStyleSheet(Style.DarkPidValue())
                self.ui.lineEdit_pid_depth_p.setStyleSheet(Style.DarkPidValue())
                self.ui.lineEdit_pid_depth_i.setStyleSheet(Style.DarkPidValue())
                self.ui.lineEdit_pid_depth_d.setStyleSheet(Style.DarkPidValue())
                self.ui.lineEdit_pid_pitch_p.setStyleSheet(Style.DarkPidValue())
                self.ui.lineEdit_pid_pitch_i.setStyleSheet(Style.DarkPidValue())
                self.ui.lineEdit_pid_pitch_d.setStyleSheet(Style.DarkPidValue())
                self.ui.lineEdit_pid_title_p.setStyleSheet(Style.DarkPidTitle())
                self.ui.lineEdit_pid_title_i.setStyleSheet(Style.DarkPidTitle())
                self.ui.lineEdit_pid_title_d.setStyleSheet(Style.DarkPidTitle())

                self.infos.start()

        def MissionStart(self):
            if self.mission is not None:
                self.startMission = True


        def MissionEnd(self):
            self.startMission = False


        def Yosun(self,frame):
            hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

            lower_color=np.array([40,40,40])
            upper_color=np.array([70,255,255])

            mask=cv.inRange(hsv,lower_color,upper_color)
            filtering_img=cv.bitwise_and(frame,frame,mask=mask)
            return filtering_img
            

        def ConvertCvToQt(self, cv_img):
            # rounded_img = self.rect_with_rounded_corners(cv_img, 10,1,(245,245,220))
            rgb_image = cv.cvtColor(cv_img, cv.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
            p = convert_to_Qt_format.scaled(self.ui.label_camera_front.width(), self.ui.label_camera_front.height(), Qt.KeepAspectRatio)
            return QPixmap.fromImage(convert_to_Qt_format)


        def openCamera(self):
            ret, frame = self.capture.read()
            if ret:
                db.frontFrame = frame
                # db.bottomFrame = frame
        
        def openUSB(self):
            ret, frame = self.capture2.read()
            if ret:
                db.bottomFrame = frame


        def SetFrontCamera(self):
            if self.mission == Missions.YOSUN and self.startMission == True:
                self.ui.label_camera_front.setPixmap(self.ConvertCvToQt(self.Yosun(db.frontFrame)))
            elif db.frontFrame is not None:
                self.ui.label_camera_front.setPixmap(self.ConvertCvToQt(db.frontFrame))
            else:
                self.ui.label_camera_front.clear()


        def SetBottomCamera(self):
            # if self.mission == Missions.YOSUN and self.startMission == True:
            #     self.ui.label_camera_bottom.setPixmap(self.ConvertCvToQt(self.Yosun(db.bottomFrame)))
            if db.bottomFrame is not None:
                self.ui.label_camera_bottom.setPixmap(self.ConvertCvToQt(db.bottomFrame))
            else:
                self.ui.label_camera_bottom.clear()


        def MissionDrop(self):
            self.startMission = False
            self.mission = None
            self.ui.label_main_mission_name.setText("Aktif Görev Yok")
            self.ui.label_main_mission_image.setPixmap(QtGui.QPixmap(":/logo/missions_blue.png"))
            self.ui.widget_mission_1.setStyleSheet("background-color: rgb(226, 226, 226);\n"
            "border-radius: 10px;")
            self.ui.widget_mission_2.setStyleSheet("background-color: rgb(226, 226, 226);\n"
            "border-radius: 10px;")
            self.ui.pushButton_mission_change.setText("Görev Seç")


        def missionSelect1(self):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.label_main_mission_name.setText("Yosun Üzerinde Çizgi Bulma Görevi")
            self.ui.label_main_mission_image.setPixmap(QtGui.QPixmap(":/logo/alg_yosun_1.jpg"))
            if self.lightMode == True:
                self.ui.widget_mission_1.setStyleSheet(Style.LightSelectedMissionWidget())
                self.ui.widget_mission_2.setStyleSheet(Style.LightGeneralWidget())
            else:
                self.ui.widget_mission_1.setStyleSheet(Style.DarkSelectedMissionWidget())
                self.ui.widget_mission_2.setStyleSheet(Style.DarkGeneralWidget())
            self.ui.pushButton_mission_change.setText("Görevi Değiştir")
            self.mission = Missions.YOSUN


        def missionSelect2(self):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.label_main_mission_name.setText("Yosun Üzerinde Çizgi Bulma Görevi")
            self.ui.label_main_mission_image.setPixmap(QtGui.QPixmap(":/logo/alg_yosun_1.jpg"))
            if self.lightMode == True:
                self.ui.widget_mission_2.setStyleSheet(Style.LightSelectedMissionWidget())
                self.ui.widget_mission_1.setStyleSheet(Style.LightGeneralWidget())
            else:
                self.ui.widget_mission_2.setStyleSheet(Style.DarkSelectedMissionWidget())
                self.ui.widget_mission_1.setStyleSheet(Style.DarkGeneralWidget())
            self.ui.pushButton_mission_change.setText("Görevi Değiştir")
            self.mission = Missions.CEMBER


        def clickedMissionChangeButton(self):
            self.ui.stackedWidget.setCurrentIndex(1)


        def clickedHomeButton(self):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.activeMenu = 0
            if self.lightMode == True:
                self.ui.pushButton_menu_home.setStyleSheet(Style.LightMenuButtonClicked())
                self.ui.pushButton_menu_pid.setStyleSheet(Style.LightMenuButton())
                self.ui.pushButton_menu_code.setStyleSheet(Style.LightMenuButton())
            else:
                self.ui.pushButton_menu_home.setStyleSheet(Style.DarkMenuButtonClicked())
                self.ui.pushButton_menu_pid.setStyleSheet(Style.DarkMenuButton())
                self.ui.pushButton_menu_code.setStyleSheet(Style.DarkMenuButton())


        def clickedPidButton(self):
            self.ui.stackedWidget.setCurrentIndex(2)
            self.activeMenu = 2
            if self.lightMode == True:
                self.ui.pushButton_menu_pid.setStyleSheet(Style.LightMenuButtonClicked())
                self.ui.pushButton_menu_home.setStyleSheet(Style.LightMenuButton())
                self.ui.pushButton_menu_code.setStyleSheet(Style.LightMenuButton())
            else:
                self.ui.pushButton_menu_pid.setStyleSheet(Style.DarkMenuButtonClicked())
                self.ui.pushButton_menu_home.setStyleSheet(Style.DarkMenuButton())
                self.ui.pushButton_menu_code.setStyleSheet(Style.DarkMenuButton())


        def clickedCodeButton(self):
            self.ui.stackedWidget.setCurrentIndex(3)
            self.activeMenu = 3
            if self.lightMode == True:
                self.ui.pushButton_menu_code.setStyleSheet(Style.LightMenuButtonClicked())
                self.ui.pushButton_menu_home.setStyleSheet(Style.LightMenuButton())
                self.ui.pushButton_menu_pid.setStyleSheet(Style.LightMenuButton())
            else:
                self.ui.pushButton_menu_code.setStyleSheet(Style.DarkMenuButtonClicked())
                self.ui.pushButton_menu_home.setStyleSheet(Style.DarkMenuButton())
                self.ui.pushButton_menu_pid.setStyleSheet(Style.DarkMenuButton())


        def SetInfos(self):
            if db.depth != None:
                self.ui.label_value_2.setText(f"Derinlik: {db.depth}")
            if db.temp != None:
                self.ui.label_value_1.setText(f"Sıcaklık: {db.temp}")
            if db.pitch != None:
                self.adi.setPitch(db.pitch)
                self.adi.update()
            if db.roll != None:
                self.adi.setRoll(db.roll)
                self.adi.update()
            if db.yaw != None:
                self.adi.setYaw(db.yaw)
                self.adi.update()


        def ResizeAllWidget(self, event):
            width = (self.ui.widget_camera.width()-9)/2
            if width<378:
                width = 378
            self.ui.label_camera_front.setMinimumHeight(width/CAMERA_LABEL_RATIO)
            self.ui.label_camera_front.setMaximumWidth(width)
            self.ui.label_camera_front.setMaximumHeight(width/CAMERA_LABEL_RATIO)
            self.ui.label_camera_bottom.setMinimumHeight(width/CAMERA_LABEL_RATIO)
            self.ui.label_camera_bottom.setMaximumWidth(width)
            self.ui.label_camera_bottom.setMaximumHeight(width/CAMERA_LABEL_RATIO)


        def StartTimer(self):
            if self.timerIsActive == False:
                self.ui.label_timer.setText("00:00:00")
                self.QTsetTimer.start()
                self.QTtimer.start()
                
                self.timerIsActive = True


        def StopTimer(self):
            if self.timerIsActive == True:
                if self.ui.pushButton_timer_stop.text() == "Durdur":
                    self.QTsetTimer.stop()
                    self.QTtimer.stop()
                    self.ui.pushButton_timer_stop.setText("Devam Et")
                else:
                    self.ui.pushButton_timer_stop.setText("Durdur")
                    self.QTsetTimer.start()
                    self.QTtimer.start()


        def EndTimer(self):
            self.QTsetTimer.stop()
            self.QTtimer.stop()
            self.ui.label_timer.setText("00:00:00")
            self.timer = 0
            self.timerIsActive = False
            self.ui.pushButton_timer_stop.setText("Durdur")


        def Timer(self):
            self.timer = self.timer + 100


        def SetTimer(self):
            allSecond = int(self.timer/1000)
            hour = int(allSecond/3600)
            minute = int((allSecond-hour*3600)/60)
            second = int(allSecond-hour*3600-minute*60)
            self.ui.label_timer.setText("{}:{}:{}".format(str(hour).zfill(2),str(minute).zfill(2),str(second).zfill(2)))
            if self.ui.label_timer.text() == "99:59:59":
                self.QTsetTimer.stop()
                self.QTtimer.stop()
                self.timer = 0
                self.timerIsActive == False


        def DesignArrangements(self):
            self.ui.pushButton_mission_change.setText("Görev Seç")
            self.ui.widget_mission_1.setStyleSheet("background-color: rgb(226, 226, 226);\n"
            "border-radius: 10px;")
            self.ui.label_main_mission_image.setPixmap(QtGui.QPixmap(":/logo/missions_blue.png"))
            self.ui.label_main_mission_name.setText("Aktif Görev Yok")
            self.ui.label_camera_front.setScaledContents(True)
            self.ui.label_camera_bottom.setScaledContents(True)
            font = QtGui.QFont()
            font.setPointSize(40)
            font.setBold(True)
            font.setWeight(75)
            self.ui.label_timer.setFont(font)
            self.ui.pushButton_timer_end.setMinimumWidth(100)
            self.ui.pushButton_timer_stop.setMinimumWidth(100)
            self.ui.pushButton_timer_start.setMinimumWidth(100)
            self.ui.widget_main_right.setMinimumWidth(349)
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.label_value_1.setText("Sıcaklık:")
            self.ui.label_value_2.setText("Derinlik:")
            self.ui.lineEdit_pid_title_p.setEnabled(False)
            self.ui.lineEdit_pid_title_i.setEnabled(False)
            self.ui.lineEdit_pid_title_d.setEnabled(False)


        def rect_with_rounded_corners(self, image, r, t, c):
            """
            :param image: image as NumPy array
            :param r: radius of rounded corners
            :param t: thickness of border
            :param c: color of border
            :return: new image as NumPy array with rounded corners
            """

            c += (255, )

            h, w = image.shape[:2]

            # Create new image (three-channel hardcoded here...)
            new_image = np.ones((h+2*t, w+2*t, 4), np.uint8) * 255
            new_image[:, :, 3] = 0

            # Draw four rounded corners
            new_image = cv.ellipse(new_image, (int(r+t/2), int(r+t/2)), (r, r), 180, 0, 90, c, t)
            new_image = cv.ellipse(new_image, (int(w-r+3*t/2-1), int(r+t/2)), (r, r), 270, 0, 90, c, t)
            new_image = cv.ellipse(new_image, (int(r+t/2), int(h-r+3*t/2-1)), (r, r), 90, 0, 90, c, t)
            new_image = cv.ellipse(new_image, (int(w-r+3*t/2-1), int(h-r+3*t/2-1)), (r, r), 0, 0, 90, c, t)

            # Draw four edges
            new_image = cv.line(new_image, (int(r+t/2), int(t/2)), (int(w-r+3*t/2-1), int(t/2)), c, t)
            new_image = cv.line(new_image, (int(t/2), int(r+t/2)), (int(t/2), int(h-r+3*t/2)), c, t)
            new_image = cv.line(new_image, (int(r+t/2), int(h+3*t/2)), (int(w-r+3*t/2-1), int(h+3*t/2)), c, t)
            new_image = cv.line(new_image, (int(w+3*t/2), int(r+t/2)), (int(w+3*t/2), int(h-r+3*t/2)), c, t)

            # Generate masks for proper blending
            mask = new_image[:, :, 3].copy()
            mask = cv.floodFill(mask, None, (int(w/2+t), int(h/2+t)), 128)[1]
            mask[mask != 128] = 0
            mask[mask == 128] = 1
            mask = np.stack((mask, mask, mask), axis=2)

            # Blend images
            temp = np.zeros_like(new_image[:, :, :3])
            temp[(t-1):(h+t-1), (t-1):(w+t-1)] = image.copy()
            new_image[:, :, :3] = new_image[:, :, :3] * (1 - mask) + temp * mask

            # Set proper alpha channel in new image
            temp = new_image[:, :, 3].copy()
            new_image[:, :, 3] = cv.floodFill(temp, None, (int(w/2+t), int(h/2+t)), 255)[1]

            return new_image

