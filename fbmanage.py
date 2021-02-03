# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fb_manage_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        # MainWindow.resize(734, 557)
        MainWindow.setFixedSize(734, 557)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(734, 557))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowFilePath("")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 341, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(33)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.MMall_like = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.MMall_like.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MMall_like.setAutoFillBackground(False)
        self.MMall_like.setObjectName("MMall_like")
        self.verticalLayout_5.addWidget(self.MMall_like)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.MMall_open_by_cookie = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.MMall_open_by_cookie.setObjectName("MMall_open_by_cookie")
        self.verticalLayout_6.addWidget(self.MMall_open_by_cookie)
        self.MMall_open_by_folder = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.MMall_open_by_folder.setObjectName("MMall_open_by_folder")
        self.verticalLayout_6.addWidget(self.MMall_open_by_folder)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.MMall_auto_confirm = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.MMall_auto_confirm.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.MMall_auto_confirm.setObjectName("MMall_auto_confirm")
        self.horizontalLayout_2.addWidget(self.MMall_auto_confirm)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.Go_to_MMall = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Go_to_MMall.setObjectName("Go_to_MMall")
        self.verticalLayout_6.addWidget(self.Go_to_MMall)
        self.MMall_auto_invite = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.MMall_auto_invite.setObjectName("MMall_auto_invite")
        self.verticalLayout_6.addWidget(self.MMall_auto_invite)
        self.MMall_auto_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.MMall_auto_add.setObjectName("MMall_auto_add")
        self.verticalLayout_6.addWidget(self.MMall_auto_add)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(370, 0, 341, 421))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(33)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.Seller_Like = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.Seller_Like.setObjectName("Seller_Like")
        self.verticalLayout_8.addWidget(self.Seller_Like)
        self.verticalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Seller_open_by_cookie = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Seller_open_by_cookie.setObjectName("Seller_open_by_cookie")
        self.verticalLayout_10.addWidget(self.Seller_open_by_cookie)
        self.Seller_open_by_folder = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Seller_open_by_folder.setObjectName("Seller_open_by_folder")
        self.verticalLayout_10.addWidget(self.Seller_open_by_folder)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.seller_auto_seemore = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.seller_auto_seemore.setObjectName("seller_auto_seemore")
        self.horizontalLayout_3.addWidget(self.seller_auto_seemore)
        self.seller_auto_confirm = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.seller_auto_confirm.setObjectName("seller_auto_confirm")
        self.horizontalLayout_3.addWidget(self.seller_auto_confirm)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.Go_to_seller = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Go_to_seller.setObjectName("Go_to_seller")
        self.verticalLayout_10.addWidget(self.Go_to_seller)
        self.Seller_auto_invite = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Seller_auto_invite.setObjectName("Seller_auto_invite")
        self.verticalLayout_10.addWidget(self.Seller_auto_invite)
        self.Seller_auto_add = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Seller_auto_add.setObjectName("Seller_auto_add")
        self.verticalLayout_10.addWidget(self.Seller_auto_add)
        self.verticalLayout_2.addLayout(self.verticalLayout_10)
        self.General = QtWidgets.QGroupBox(self.centralwidget)
        self.General.setGeometry(QtCore.QRect(10, 420, 701, 101))
        self.General.setFlat(True)
        self.General.setCheckable(False)
        self.General.setObjectName("General")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.General)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 661, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.Manage_all_acc = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Manage_all_acc.setObjectName("Manage_all_acc")
        self.horizontalLayout.addWidget(self.Manage_all_acc)
        self.Share_post = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Share_post.setObjectName("Share_post")
        self.horizontalLayout.addWidget(self.Share_post)
        self.Generate_Cookie = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Generate_Cookie.setObjectName("Generate_Cookie")
        self.horizontalLayout.addWidget(self.Generate_Cookie)
        self.Live = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Live.setObjectName("Live")
        self.horizontalLayout.addWidget(self.Live)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.MMall_open_by_cookie, self.MMall_open_by_folder)
        MainWindow.setTabOrder(self.MMall_open_by_folder, self.Go_to_MMall)
        MainWindow.setTabOrder(self.Go_to_MMall, self.MMall_auto_invite)
        MainWindow.setTabOrder(self.MMall_auto_invite, self.MMall_auto_add)
        MainWindow.setTabOrder(self.MMall_auto_add, self.Seller_open_by_cookie)
        MainWindow.setTabOrder(self.Seller_open_by_cookie, self.Seller_open_by_folder)
        MainWindow.setTabOrder(self.Seller_open_by_folder, self.Go_to_seller)
        MainWindow.setTabOrder(self.Go_to_seller, self.Seller_auto_invite)
        MainWindow.setTabOrder(self.Seller_auto_invite, self.Seller_auto_add)
        MainWindow.setTabOrder(self.Seller_auto_add, self.Manage_all_acc)
        MainWindow.setTabOrder(self.Manage_all_acc, self.Share_post)
        MainWindow.setTabOrder(self.Share_post, self.Generate_Cookie)
        MainWindow.setTabOrder(self.Generate_Cookie, self.Live)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MMall Facebook Manage"))
        self.label.setText(_translate("MainWindow", "Markarian Mall"))
        self.MMall_open_by_cookie.setText(_translate("MainWindow", "Open Account by Cookie"))
        self.MMall_open_by_folder.setText(_translate("MainWindow", "Open Account by Profile Firefox"))
        self.pushButton.setText(_translate("MainWindow", "Auto See more"))
        self.MMall_auto_confirm.setText(_translate("MainWindow", "Auto Confirm"))
        self.Go_to_MMall.setText(_translate("MainWindow", "Go to MMall Page"))
        self.MMall_auto_invite.setText(_translate("MainWindow", "Auto invite"))
        self.MMall_auto_add.setText(_translate("MainWindow", "Auto Add(15)"))
        self.label_2.setText(_translate("MainWindow", "អ្នកលក់ Seller"))
        self.Seller_open_by_cookie.setText(_translate("MainWindow", "Open Account by Cookie"))
        self.Seller_open_by_folder.setText(_translate("MainWindow", "Open Account by Profile Firefox"))
        self.seller_auto_seemore.setText(_translate("MainWindow", "Auto See more"))
        self.seller_auto_confirm.setText(_translate("MainWindow", "Auto Confirm"))
        self.Go_to_seller.setText(_translate("MainWindow", "Go to MMall Page"))
        self.Seller_auto_invite.setText(_translate("MainWindow", "Auto invite"))
        self.Seller_auto_add.setText(_translate("MainWindow", "Auto Add(15)"))
        self.General.setTitle(_translate("MainWindow", "General"))
        self.pushButton_3.setText(_translate("MainWindow", "Active Account"))
        self.Manage_all_acc.setText(_translate("MainWindow", "Manage All account"))
        self.Share_post.setText(_translate("MainWindow", "Share Post"))
        self.Generate_Cookie.setText(_translate("MainWindow", "Generate Cookie"))
        self.Live.setText(_translate("MainWindow", "Live"))
class MainClass():
    def __init__(self):
        if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())

pp=MainClass()
exit()
