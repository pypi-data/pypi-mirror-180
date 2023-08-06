from PyQt5 import QtGui

#l - light
#d - dark
light_l_grey = (226, 226, 226)
light_l_l_grey = (240, 240, 240)
light_d_grey = (96, 95, 94)
light_l_blue = (36, 123, 160)
light_d_blue = (10, 36, 99)
light_l_l_blue = (56, 143, 180)
light_beige = (245, 245, 220)
light_l_pink = (251, 54, 64)
light_pink = (255, 85, 91)
light_d_pink = (199, 27, 32)
light_l_l_l_blue = (60, 147, 185)

dark_l_black = (20,20,20)
dark_d_black = (10,10,10)
dark_l_l_black = (30,30,30)
dark_l_purple = (36,0,70)
dark_d_purple = (16,0,43)
dark_l_l_purple = (90, 24, 154)
dark_l_yellow = (255,174,0)
dark_d_yellow = (255,155,0)
dark_grey = (226,226,226)

light_selected_mission_widget = (186, 189, 182)
light_menu_background = light_l_blue
light_menu_button_background = light_l_blue
light_menu_button_hover_background = light_l_l_blue
light_menu_button_pressed_background = light_d_blue
light_camera_background = light_d_grey
light_general_widget_background = light_l_grey
light_main_background = light_beige
light_dark_font = light_d_blue
light_light_font = light_beige
light_general_button_background = light_l_pink
light_general_button_border = light_d_pink
light_general_button_pressed_background = light_d_pink
light_info_value_background = light_l_blue
light_pid_button_background = light_l_pink
light_pid_button_hover_background = light_pink
light_pid_button_pressed_background = light_d_pink
light_pid_value_border = light_l_grey
light_pid_value_background = light_l_l_grey


dark_selected_mission_widget = dark_l_l_black
dark_menu_background = dark_l_black 
dark_menu_button_background = dark_l_black
dark_menu_button_hover_background = (50,50,50)#dark_l_l_black
dark_menu_button_pressed_background = light_l_blue#(0,0,0)
dark_camera_background = dark_l_l_black
dark_general_widget_background = dark_l_black
dark_main_background = dark_d_black
dark_dark_font = dark_grey
dark_light_font = dark_d_black
dark_general_button_background = light_l_blue
dark_general_button_border = light_l_l_blue
dark_general_button_pressed_background = light_l_l_blue
dark_info_value_background = light_l_blue
dark_pid_button_background = light_l_blue
dark_pid_button_hover_background = light_l_l_l_blue
dark_pid_button_pressed_background = light_l_l_blue
dark_pid_value_border = dark_l_black
dark_pid_value_background = (60, 60, 60)


light_home = ":/logo/home.png"
light_missions = ":/logo/missions_blue.png"
light_pid =":/logo/control.png"
light_code = ":/logo/code.png"
light_theme = ":/logo/moon.png"

dark_home = ":/logo/home.png"
dark_missions = ":/logo/missions_blue.png"
dark_pid =":/logo/control.png"
dark_code = ":/logo/code.png"
dark_theme = ":/logo/sun.png"

class Style():

    #Light Mode
    def LightMenuButton():
        return ("QPushButton{\n"
"background-color: none;\n"
"border: none;\n"
"border-radius: none;}\n"
"QPushButton:hover{\n"
f"background-color: rgb{light_menu_button_hover_background};\n"
"border-radius: 10px;\n"
f"border: 2px solid  rgb{light_menu_button_hover_background};\n"
"}\n"
"QPushButton:focus:pressed{\n"
f"background-color: rgb{light_menu_button_pressed_background};\n"
"border-radius: 10px;\n"
f"border: 2px solid rgb{light_menu_button_pressed_background};\n"
"}")

    def LightMenuButtonClicked():
        return ("QPushButton{\n"
f"background-color: rgb{light_menu_button_pressed_background};\n"
"border-radius: 10px;\n"
f"border: 2px solid  rgb{light_menu_button_pressed_background};\n"
"}\n"
"QPushButton:hover{\n"
f"background-color: rgb{light_menu_button_pressed_background};\n"
"border-radius: 10px;\n"
f"border: 2px solid  rgb{light_menu_button_pressed_background};\n"
"}\n"
"QPushButton:focus:pressed{\n"
f"background-color: rgb{light_menu_button_pressed_background};\n"
"border-radius: 10px;\n"
f"border: 2px solid rgb{light_menu_button_pressed_background};\n"
"}")

    def LightStackWidget():
        return (f"background-color: rgb{light_main_background};")

    def LightCamera():
        return (f"background-color: rgb{light_camera_background};\n"
"border-radius: 10px;")

    def LightMissionSEButton():
        return("QPushButton{\n"
f"background-color: rgb{light_general_button_background};\n"
"border-radius: 30px;\n"
"border-bottom: none;\n"
f"color: rgb{light_light_font};\n" 
"}\n"
"QPushButton:hover{\n"
f"background-color: rgb{light_general_button_background};\n"
"border-radius: 30px;\n"
f"border: 3px solid  rgb{light_general_button_border};\n"
"}\n"
"QPushButton:focus:pressed{\n"
f"background-color: rgb{light_general_button_pressed_background};\n"
"border-radius: 30px;\n"
f"border: 3px solid  rgb{light_general_button_border};\n"
f"color: rgb{light_light_font};\n"  
"}")

    def LightGeneralWidget():
        return (f"background-color: rgb{light_general_widget_background};\n"
"border-radius: 10px;\n")

    def LightModeDarkFont():
        return (f"color: rgb{light_dark_font};")

    def LightGeneralButton():
        return ("QPushButton{\n"
f"background-color: rgb{light_general_button_background};\n"
"border-radius: 15px;\n"
"border-bottom: none;\n"
f"color: rgb{light_light_font};\n"  
"}\n"
"QPushButton:hover{\n"
f"background-color: rgb{light_general_button_background};\n"
"border-radius: 15px;\n"
f"border: 2px solid  rgb{light_general_button_border};\n"
"}\n"
"QPushButton:focus:pressed{\n"
f"background-color: rgb{light_general_button_pressed_background};\n"
"border-radius: 15px;\n"
f"border: 2px solid  rgb{light_general_button_border};\n"
f"color: rgb{light_light_font};\n"  
"}")

    def LightInfoValue():
        return ("QLabel{\n"
f"background-color: rgb{light_info_value_background};\n"
f"color: rgb{light_light_font};\n" 
"border-radius: 10px;\n"
"padding-left: 7px}")

    def LightSelectedMissionWidget():
        return (f"background-color: rgb{light_selected_mission_widget};\n"
"border-radius: 10px;")

    def LightMissionSelectButton():
        return ("QPushButton{\n"
f"background-color: rgb{light_general_button_background};\n"
"border-radius: 25px;\n"
"border-bottom: none;\n"
f"color: rgb{light_light_font};\n"  
"}\n"
"QPushButton:hover{\n"
f"background-color: rgb{light_general_button_background};\n"
"border-radius: 25px;\n"
f"border: 3px solid  rgb{light_general_button_border};\n"
"}\n"
"QPushButton:focus:pressed{\n"
f"background-color: rgb{light_general_button_pressed_background};\n"
"border-radius: 25px;\n"
f"border: 3px solid  rgb{light_general_button_border};\n"
f"color: rgb{light_light_font};\n"  
"}")

    def LightDisabeleMissionWidget():
        return (f"background-color: rgb{light_main_background};\n"
"border-radius: 10px;")

    def LightMenuWidget():
        return(f"background-color: rgb{light_menu_background};")

    def LightThemeButton():
        return("QPushButton{\n"
"background-color: none;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: none;\n"
"border: none;\n"
"}\n"
"QPushButton:focus:pressed{\n"
f"background-color: rgb{light_menu_button_hover_background};\n"
"border-radius: 10px;\n"
f"border: 2px solid  rgb{light_menu_button_hover_background};\n"
"}")

    def LightHomeIcon():
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(light_home), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def LightPIDIcon():
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(light_pid), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def LightCodeIcon():
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(light_code), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def LightMissionsIcon():
        icon = QtGui.QPixmap(light_missions)
        return icon

    def LightMoonIcon():
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(light_theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def LightPidButton():
        return("QPushButton{\n"
        f"background-color: rgb{light_pid_button_background};\n"
        "border-radius: 10px;\n"
        "border-bottom: none;\n"
        f"color: rgb{light_light_font};\n"
        "}\n"
        "QPushButton:hover{\n"
        f"background-color: rgb{light_pid_button_hover_background};\n"
        "border-radius: 10px;\n"
        "}\n"
        "QPushButton:focus:pressed{\n"
        f"background-color: rgb{light_pid_button_pressed_background};\n"
        "border-radius: 10px;\n"
        f"color: rgb{light_light_font};\n"
        "}")

    def LightPidValue():
        return("border-radius: 10px;\n"
        f"background-color: rgb{light_pid_value_background};\n"
        f"border: 2px solid rgb{light_pid_value_border};\n"
        f"color: rgb{light_dark_font}\n")

    def LightPidTitle():
        return(f"color: rgb{light_dark_font};\n"
        "border: none;")

    #Dark Mode
    def DarkMenuButton():
        return ("QPushButton{\n"
"background-color: none;\n"
"border: none;\n"
"border-radius: none;}\n"
"QPushButton:hover{\n"
f"background-color: rgb{dark_menu_button_hover_background};\n"
"border-radius: 10px;\n"
f"border: 2px solid  rgb{dark_menu_button_hover_background};\n"
"}\n"
"QPushButton:focus:pressed{\n"
f"background-color: rgb{dark_menu_button_pressed_background};\n"
"border-radius: 10px;\n"
f"border: 2px solid rgb{dark_menu_button_pressed_background};\n"
"}")

    def DarkMenuButtonClicked():
        return ("QPushButton{\n"
f"background-color: rgb{dark_menu_button_pressed_background};\n"
"border-radius: 10px;\n"
f"border: 2px solid  rgb{dark_menu_button_pressed_background};\n"
"}\n"
"QPushButton:hover{\n"
f"background-color: rgb{dark_menu_button_pressed_background};\n"
"border-radius: 10px;\n"
f"border: 2px solid  rgb{dark_menu_button_pressed_background};\n"
"}\n"
"QPushButton:focus:pressed{\n"
f"background-color: rgb{dark_menu_button_pressed_background};\n"
"border-radius: 10px;\n"
f"border: 2px solid rgb{dark_menu_button_pressed_background};\n"
"}")

    def DarkStackWidget():
        return (f"background-color: rgb{dark_main_background};")

    def DarkCamera():
        return (f"background-color: rgb{dark_camera_background};\n"
"border-radius: 10px;")

    def DarkMissionSEButton():
        return("QPushButton{\n"
f"background-color: rgb{dark_general_button_background};\n"
"border-radius: 30px;\n"
"border-bottom: none;\n"
f"color: rgb{dark_light_font};\n"  #ll
"}\n"
"QPushButton:hover{\n"
f"background-color: rgb{dark_general_button_background};\n"
"border-radius: 30px;\n"
f"border: 3px solid  rgb{dark_general_button_border};\n"
"}\n"
"QPushButton:focus:pressed{\n"
f"background-color: rgb{dark_general_button_pressed_background};\n"
"border-radius: 30px;\n"
f"border: 3px solid  rgb{dark_general_button_border};\n"
f"color: rgb{dark_light_font};\n"   #ll
"}")

    def DarkGeneralWidget():
        return (f"background-color: rgb{dark_general_widget_background};\n"
"border-radius: 10px;\n")

    def DarkModeDarkFont():
        return (f"color: rgb{dark_dark_font};") #ld

    def DarkGeneralButton():
        return ("QPushButton{\n"
f"background-color: rgb{dark_general_button_background};\n"
"border-radius: 15px;\n"
"border-bottom: none;\n"
f"color: rgb{dark_light_font};\n"  #ll
"}\n"
"QPushButton:hover{\n"
f"background-color: rgb{dark_general_button_background};\n"
"border-radius: 15px;\n"
f"border: 2px solid  rgb{dark_general_button_border};\n"
"}\n"
"QPushButton:focus:pressed{\n"
f"background-color: rgb{dark_general_button_pressed_background};\n"
"border-radius: 15px;\n"
f"border: 2px solid  rgb{dark_general_button_border};\n"
f"color: rgb{dark_light_font};\n"  #ll
"}")

    def DarkInfoValue():
        return ("QLabel{\n"
f"background-color: rgb{dark_info_value_background};\n"
f"color: rgb{dark_light_font};\n" #ll
"border-radius: 10px;\n"
"padding-left: 7px}")

    def DarkSelectedMissionWidget():
        return (f"background-color: rgb{dark_selected_mission_widget};\n"
"border-radius: 10px;")

    def DarkMissionSelectButton():
        return ("QPushButton{\n"
f"background-color: rgb{dark_general_button_background};\n"
"border-radius: 25px;\n"
"border-bottom: none;\n"
f"color: rgb{dark_light_font};\n"  #ll
"}\n"
"QPushButton:hover{\n"
f"background-color: rgb{dark_general_button_background};\n"
"border-radius: 25px;\n"
f"border: 3px solid  rgb{dark_general_button_border};\n"
"}\n"
"QPushButton:focus:pressed{\n"
f"background-color: rgb{dark_general_button_pressed_background};\n"
"border-radius: 25px;\n"
f"border: 3px solid  rgb{dark_general_button_border};\n"
f"color: rgb{dark_light_font};\n"  #ll
"}")

    def DarkDisabeleMissionWidget():
        return (f"background-color: rgb{dark_main_background};\n"
"border-radius: 10px;")

    def DarkMenuWidget():
        return(f"background-color: rgb{dark_menu_background};")

    def DarkThemeButton():
        return("QPushButton{\n"
"background-color: none;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: none;\n"
"border: none;\n"
"}\n"
"QPushButton:focus:pressed{\n"
f"background-color: rgb{dark_menu_button_hover_background};\n"
"border-radius: 10px;\n"
f"border: 2px solid  rgb{dark_menu_button_hover_background};\n"
"}")

    def DarkHomeIcon():
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(dark_home), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def DarkPIDIcon():
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(dark_pid), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def DarkCodeIcon():
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(dark_code), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def DarkMissionsIcon():
        icon = QtGui.QPixmap(dark_missions)
        return icon

    def DarkSunIcon():
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(dark_theme), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def DarkPidButton():
        return("QPushButton{\n"
        f"background-color: rgb{dark_pid_button_background};\n"
        "border-radius: 10px;\n"
        "border-bottom: none;\n"
        f"color: rgb{dark_light_font};\n"
        "}\n"
        "QPushButton:hover{\n"
        f"background-color: rgb{dark_pid_button_hover_background};\n"
        "border-radius: 10px;\n"
        "}\n"
        "QPushButton:focus:pressed{\n"
        f"background-color: rgb{dark_pid_button_pressed_background};\n"
        "border-radius: 10px;\n"
        f"color: rgb{dark_light_font};\n"
        "}")

    def DarkPidValue():
        return("border-radius: 10px;\n"
        f"background-color: rgb{dark_pid_value_background};\n"
        f"border: 2px solid rgb{dark_pid_value_border};"
        f"color: rgb{dark_dark_font}\n")

    def DarkPidTitle():
        return(f"color: rgb{dark_dark_font};\n"
        "border: none;")