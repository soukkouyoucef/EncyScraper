# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ency Web Scraper InterfaceyKIvnz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os 
savingToPath = os.getcwd()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(703, 468)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(61, 56, 70, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 84, 105, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(76, 70, 87, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(31, 28, 35, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(41, 37, 47, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(30, 28, 35, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        MainWindow.setPalette(palette)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setWindowTitle(u"Ency Web Scraper")
        icon = QIcon()
        icon.addFile(u"icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TOP_FRAME = QFrame(self.centralwidget)
        self.TOP_FRAME.setObjectName(u"TOP_FRAME")
        self.TOP_FRAME.setFrameShape(QFrame.StyledPanel)
        self.TOP_FRAME.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.TOP_FRAME)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Title_Frame = QFrame(self.TOP_FRAME)
        self.Title_Frame.setObjectName(u"Title_Frame")
        self.Title_Frame.setFrameShape(QFrame.StyledPanel)
        self.Title_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Title_Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Title_Text = QLabel(self.Title_Frame)
        self.Title_Text.setObjectName(u"Title_Text")
        font = QFont()
        font.setFamily(u"Liberation Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Title_Text.setFont(font)
        self.Title_Text.setScaledContents(True)
        self.Title_Text.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Title_Text)


        self.verticalLayout_2.addWidget(self.Title_Frame)

        self.Select_Module_Frame = QFrame(self.TOP_FRAME)
        self.Select_Module_Frame.setObjectName(u"Select_Module_Frame")
        font1 = QFont()
        font1.setPointSize(15)
        self.Select_Module_Frame.setFont(font1)
        self.Select_Module_Frame.setFrameShape(QFrame.StyledPanel)
        self.Select_Module_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Select_Module_Frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Text1 = QLabel(self.Select_Module_Frame)
        self.Text1.setObjectName(u"Text1")
        font2 = QFont()
        font2.setFamily(u"Liberation Serif")
        font2.setPointSize(16)
        self.Text1.setFont(font2)
        self.Text1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.Text1)

        self.Select_Modules_Dropdown = QComboBox(self.Select_Module_Frame)
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.addItem("")
        self.Select_Modules_Dropdown.setObjectName(u"Select_Modules_Dropdown")
        font3 = QFont()
        font3.setFamily(u"Liberation Serif")
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setWeight(75)
        self.Select_Modules_Dropdown.setFont(font3)
        self.Select_Modules_Dropdown.setEditable(False)
        self.Select_Modules_Dropdown.setMaxVisibleItems(7)
        self.Select_Modules_Dropdown.setFrame(True)

        self.horizontalLayout_4.addWidget(self.Select_Modules_Dropdown)


        self.verticalLayout_2.addWidget(self.Select_Module_Frame)

        self.Save_location_and_donwload_button = QFrame(self.TOP_FRAME)
        self.Save_location_and_donwload_button.setObjectName(u"Save_location_and_donwload_button")
        self.Save_location_and_donwload_button.setFrameShape(QFrame.StyledPanel)
        self.Save_location_and_donwload_button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Save_location_and_donwload_button)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Saving_Path_Frame = QFrame(self.Save_location_and_donwload_button)
        self.Saving_Path_Frame.setObjectName(u"Saving_Path_Frame")
        self.Saving_Path_Frame.setFrameShape(QFrame.StyledPanel)
        self.Saving_Path_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Saving_Path_Frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Text2 = QLabel(self.Saving_Path_Frame)
        self.Text2.setObjectName(u"Text2")
        font4 = QFont()
        font4.setFamily(u"Liberation Serif")
        font4.setPointSize(12)
        self.Text2.setFont(font4)
        self.Text2.setMidLineWidth(0)
        self.Text2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.Text2)

        self.Path_Text = QLabel(self.Saving_Path_Frame)
        self.Path_Text.setObjectName(u"Path_Text")
        self.Path_Text.setFont(font4)
        self.Path_Text.setLineWidth(1)
        self.Path_Text.setMargin(0)
        self.Path_Text.setIndent(0)

        self.horizontalLayout_5.addWidget(self.Path_Text)


        self.horizontalLayout_2.addWidget(self.Saving_Path_Frame)

        self.frame_5 = QFrame(self.Save_location_and_donwload_button)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Download_Button = QPushButton(self.frame_5)
        self.Download_Button.setObjectName(u"Download_Button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Download_Button.sizePolicy().hasHeightForWidth())
        self.Download_Button.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setFamily(u"Liberation Serif")
        font5.setPointSize(17)
        self.Download_Button.setFont(font5)
        self.Download_Button.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u"download-icon-white-png-29.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.Download_Button.setIcon(icon1)
        self.Download_Button.setIconSize(QSize(32, 32))
        self.Download_Button.setAutoDefault(False)
        self.Download_Button.setFlat(False)

        self.gridLayout.addWidget(self.Download_Button, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.Save_location_and_donwload_button)


        self.verticalLayout.addWidget(self.TOP_FRAME)

        self.BOTTOM_FRAME = QFrame(self.centralwidget)
        self.BOTTOM_FRAME.setObjectName(u"BOTTOM_FRAME")
        self.BOTTOM_FRAME.setFrameShape(QFrame.StyledPanel)
        self.BOTTOM_FRAME.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.BOTTOM_FRAME)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Telemetry = QFrame(self.BOTTOM_FRAME)
        self.Telemetry.setObjectName(u"Telemetry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Telemetry.sizePolicy().hasHeightForWidth())
        self.Telemetry.setSizePolicy(sizePolicy1)
        self.Telemetry.setFrameShape(QFrame.StyledPanel)
        self.Telemetry.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Telemetry)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Telemetry_Text_Frame = QFrame(self.Telemetry)
        self.Telemetry_Text_Frame.setObjectName(u"Telemetry_Text_Frame")
        self.Telemetry_Text_Frame.setFrameShape(QFrame.StyledPanel)
        self.Telemetry_Text_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Telemetry_Text_Frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Text3 = QLabel(self.Telemetry_Text_Frame)
        self.Text3.setObjectName(u"Text3")
        font6 = QFont()
        font6.setFamily(u"Liberation Serif")
        font6.setPointSize(15)
        self.Text3.setFont(font6)
        self.Text3.setLineWidth(0)
        self.Text3.setMidLineWidth(0)
        self.Text3.setAlignment(Qt.AlignCenter)
        self.Text3.setIndent(0)

        self.horizontalLayout_7.addWidget(self.Text3)

        self.File_Being_Downloaded = QLabel(self.Telemetry_Text_Frame)
        self.File_Being_Downloaded.setObjectName(u"File_Being_Downloaded")
        self.File_Being_Downloaded.setFont(font6)

        self.horizontalLayout_7.addWidget(self.File_Being_Downloaded)


        self.verticalLayout_4.addWidget(self.Telemetry_Text_Frame)

        self.Progress_Bar_Frame = QFrame(self.Telemetry)
        self.Progress_Bar_Frame.setObjectName(u"Progress_Bar_Frame")
        self.Progress_Bar_Frame.setFrameShape(QFrame.StyledPanel)
        self.Progress_Bar_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Progress_Bar_Frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Progress_Bar = QProgressBar(self.Progress_Bar_Frame)
        self.Progress_Bar.setObjectName(u"Progress_Bar")
        self.Progress_Bar.setValue(0)

        self.horizontalLayout_6.addWidget(self.Progress_Bar)

        self.abortButton = QPushButton(self.Progress_Bar_Frame)
        self.abortButton.setObjectName(u"abortButton")
        font7 = QFont()
        font7.setFamily(u"Liberation Serif")
        font7.setPointSize(13)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.abortButton.setFont(font7)
        self.abortButton.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u"cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.abortButton.setIcon(icon2)
        self.abortButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.abortButton)


        self.verticalLayout_4.addWidget(self.Progress_Bar_Frame)


        self.verticalLayout_3.addWidget(self.Telemetry)

        self.frame_6 = QFrame(self.BOTTOM_FRAME)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Feedback_Text = QLabel(self.frame_6)
        self.Feedback_Text.setObjectName(u"Feedback_Text")
        font8 = QFont()
        font8.setFamily(u"Liberation Serif")
        font8.setPointSize(23)
        self.Feedback_Text.setFont(font8)
        self.Feedback_Text.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Feedback_Text)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.BOTTOM_FRAME)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Select_Modules_Dropdown.setCurrentIndex(0)
        self.Download_Button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.Title_Text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#f6f5f4;\">Ency Web Scraper</span></p></body></html>", None))
        self.Text1.setText(QCoreApplication.translate("MainWindow", u"Choose a subject :", None))
        self.Select_Modules_Dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Mal﻿adies infectieuses", None))
        self.Select_Modules_Dropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"Gastro-ent\u00e9rologie", None))
        self.Select_Modules_Dropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"Cardiologie", None))
        self.Select_Modules_Dropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"Neurologie", None))
        self.Select_Modules_Dropdown.setItemText(4, QCoreApplication.translate("MainWindow", u"Onco-H\u00e9matologie", None))
        self.Select_Modules_Dropdown.setItemText(5, QCoreApplication.translate("MainWindow", u"Pneumologie-Phtisiologie", None))
        self.Select_Modules_Dropdown.setItemText(6, QCoreApplication.translate("MainWindow", u"Gyn\u00e9cologie", None))
        self.Select_Modules_Dropdown.setItemText(7, QCoreApplication.translate("MainWindow", u"Orthop\u00e9die", None))
        self.Select_Modules_Dropdown.setItemText(8, QCoreApplication.translate("MainWindow", u"P\u00e9diatrie", None))
        self.Select_Modules_Dropdown.setItemText(9, QCoreApplication.translate("MainWindow", u"Urologie-Nephrologie", None))
        self.Select_Modules_Dropdown.setItemText(10, QCoreApplication.translate("MainWindow", u"Endocrinologie ", None))
        self.Select_Modules_Dropdown.setItemText(11, QCoreApplication.translate("MainWindow", u"Psychiatrie", None))
        self.Select_Modules_Dropdown.setItemText(12, QCoreApplication.translate("MainWindow", u"Rhumatologie", None))
        self.Select_Modules_Dropdown.setItemText(13, QCoreApplication.translate("MainWindow", u"Urgences m\u00e9dico-chirurgicales", None))
        self.Select_Modules_Dropdown.setItemText(14, QCoreApplication.translate("MainWindow", u"Ophtalmologie", None))
        self.Select_Modules_Dropdown.setItemText(15, QCoreApplication.translate("MainWindow", u"Dermatologie", None))
        self.Select_Modules_Dropdown.setItemText(16, QCoreApplication.translate("MainWindow", u"\u00c9pid\u00e9miologie", None))
        self.Select_Modules_Dropdown.setItemText(17, QCoreApplication.translate("MainWindow", u"M\u00e9decine de travail", None))
        self.Select_Modules_Dropdown.setItemText(18, QCoreApplication.translate("MainWindow", u"M\u00e9decine l\u00e9gale", None))
        self.Select_Modules_Dropdown.setItemText(19, QCoreApplication.translate("MainWindow", u"ORL", None))
        self.Select_Modules_Dropdown.setItemText(20, QCoreApplication.translate("MainWindow", u"Th\u00e9rapeutique", None))
        self.Select_Modules_Dropdown.setItemText(21, QCoreApplication.translate("MainWindow", u"\u00c9conomie", None))
        self.Select_Modules_Dropdown.setItemText(22, QCoreApplication.translate("MainWindow", u"Droit et d\u00e9ontologie m\u00e9dicale ", None))
        self.Select_Modules_Dropdown.setItemText(23, QCoreApplication.translate("MainWindow", u"Psychologie m\u00e9dicale", None))

        self.Select_Modules_Dropdown.setCurrentText(QCoreApplication.translate("MainWindow", u"Maladies infectieuses", None))
        self.Text2.setText(QCoreApplication.translate("MainWindow", u"Saving to :", None))
        self.Path_Text.setText(QCoreApplication.translate("MainWindow", savingToPath, None))
        self.Download_Button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.Text3.setText(QCoreApplication.translate("MainWindow", u"Getting :", None))
        self.File_Being_Downloaded.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.abortButton.setText(QCoreApplication.translate("MainWindow", u"Abort", None))
        self.Feedback_Text.setText("Waiting ...")
        pass
    # retranslateUi

