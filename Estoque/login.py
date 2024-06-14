################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(553, 621)
        Login.setStyleSheet(u"background-color: rgb(76, 76, 76);")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 170, 491, 411))
        self.frame.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_login = QLineEdit(self.frame)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setGeometry(QRect(110, 140, 291, 31))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        self.txt_login.setFont(font)
        self.txt_login.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_login.setAlignment(Qt.AlignCenter)
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(112, 220, 291, 31))
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)
        self.btn_entrar = QPushButton(self.frame)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(170, 290, 161, 31))
        self.btn_entrar.setFont(font)
        self.btn_entrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrar.setStyleSheet(u"\n"
"QPushButton{\n"
"       color:rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"       \n"
"       background-color: rgb(255,255,255);\n"
"       color:rgb(0,0,0);\n"
"}\n"
"")
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 20, 201, 191))
        self.label.setPixmap(QPixmap(r"Estoque\imgs\login.png"))
        self.label.setScaledContents(True)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.txt_login.setPlaceholderText(QCoreApplication.translate("Login", u"Digite o usu\u00e1rio", None))
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Login", u"Digite sua senha", None))
        self.btn_entrar.setText(QCoreApplication.translate("Login", u"Entrar", None))
        self.label.setText("")
    # retranslateUi