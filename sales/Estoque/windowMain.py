################################################################################
## Form generated from reading UI file 'main2.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(972, 545)
        MainWindow.setStyleSheet(u"background-color: rgb(76, 76, 76);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_10 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.btn_home)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.btn_tables)

        self.btn_pg_venda = QPushButton(self.frame)
        self.btn_pg_venda.setObjectName(u"btn_pg_venda")
        self.btn_pg_venda.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.btn_pg_venda)


        self.verticalLayout_10.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(39, 39, 39);\n"
"")
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_11 = QVBoxLayout(self.pg_table)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tabWidget = QTabWidget(self.pg_table)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_3 = QVBoxLayout(self.tables)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(19)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.td_estoque = QTableWidget(self.tables)
        self.td_estoque.setObjectName(u"td_estoque")
        self.td_estoque.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.td_estoque)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.insert_produto = QPushButton(self.frame_2)
        self.insert_produto.setObjectName(u"insert_produto")
        self.insert_produto.setStyleSheet(u"\n"
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

        self.verticalLayout_4.addWidget(self.insert_produto)

        self.btn_excluir_produto = QPushButton(self.frame_2)
        self.btn_excluir_produto.setObjectName(u"btn_excluir_produto")
        self.btn_excluir_produto.setMaximumSize(QSize(131, 16777215))
        self.btn_excluir_produto.setStyleSheet(u"\n"
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

        self.verticalLayout_4.addWidget(self.btn_excluir_produto)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout = QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_12)

        self.tb_saida = QTableWidget(self.tab_2)
        self.tb_saida.setObjectName(u"tb_saida")
        self.tb_saida.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.tb_saida)


        self.horizontalLayout.addLayout(self.verticalLayout_12)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.insert_saida = QPushButton(self.tab_2)
        self.insert_saida.setObjectName(u"insert_saida")
        font1 = QFont()
        font1.setPointSize(8)
        self.insert_saida.setFont(font1)
        self.insert_saida.setStyleSheet(u"\n"
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

        self.verticalLayout_9.addWidget(self.insert_saida)

        self.btn_extorno = QPushButton(self.tab_2)
        self.btn_extorno.setObjectName(u"btn_extorno")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        self.btn_extorno.setFont(font2)
        self.btn_extorno.setStyleSheet(u"\n"
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

        self.verticalLayout_9.addWidget(self.btn_extorno)

        self.btn_dashboards = QPushButton(self.tab_2)
        self.btn_dashboards.setObjectName(u"btn_dashboards")
        self.btn_dashboards.setFont(font2)
        self.btn_dashboards.setStyleSheet(u"\n"
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

        self.verticalLayout_9.addWidget(self.btn_dashboards)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_9)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_11.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_table)
        self.pg_cadastro_produto = QWidget()
        self.pg_cadastro_produto.setObjectName(u"pg_cadastro_produto")
        self.verticalLayout_15 = QVBoxLayout(self.pg_cadastro_produto)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_17 = QLabel(self.pg_cadastro_produto)
        self.label_17.setObjectName(u"label_17")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(23)
        font3.setBold(True)
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_17)

        self.label_18 = QLabel(self.pg_cadastro_produto)
        self.label_18.setObjectName(u"label_18")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_18)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_22 = QLabel(self.pg_cadastro_produto)
        self.label_22.setObjectName(u"label_22")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(15)
        self.label_22.setFont(font5)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_22)

        self.txt_codigo = QLineEdit(self.pg_cadastro_produto)
        self.txt_codigo.setObjectName(u"txt_codigo")
        self.txt_codigo.setStyleSheet(u"color:rgb(255,255,255);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"")

        self.horizontalLayout_2.addWidget(self.txt_codigo)


        self.verticalLayout_15.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_23 = QLabel(self.pg_cadastro_produto)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font5)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.label_23)

        self.txt_produto_estoque = QLineEdit(self.pg_cadastro_produto)
        self.txt_produto_estoque.setObjectName(u"txt_produto_estoque")
        self.txt_produto_estoque.setStyleSheet(u"color:rgb(255,255,255);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"")

        self.horizontalLayout_14.addWidget(self.txt_produto_estoque)


        self.verticalLayout_15.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_24 = QLabel(self.pg_cadastro_produto)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font5)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.label_24)

        self.txt_quantidade_estoque = QLineEdit(self.pg_cadastro_produto)
        self.txt_quantidade_estoque.setObjectName(u"txt_quantidade_estoque")
        self.txt_quantidade_estoque.setStyleSheet(u"color:rgb(255,255,255);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"")

        self.horizontalLayout_15.addWidget(self.txt_quantidade_estoque)


        self.verticalLayout_15.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_25 = QLabel(self.pg_cadastro_produto)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font5)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.label_25)

        self.txt_preco_unico = QLineEdit(self.pg_cadastro_produto)
        self.txt_preco_unico.setObjectName(u"txt_preco_unico")
        self.txt_preco_unico.setStyleSheet(u"color:rgb(255,255,255);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"")

        self.horizontalLayout_17.addWidget(self.txt_preco_unico)


        self.verticalLayout_15.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_26 = QLabel(self.pg_cadastro_produto)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_18.addWidget(self.label_26)

        self.btn_cadastro_produto = QPushButton(self.pg_cadastro_produto)
        self.btn_cadastro_produto.setObjectName(u"btn_cadastro_produto")
        font6 = QFont()
        font6.setPointSize(13)
        self.btn_cadastro_produto.setFont(font6)
        self.btn_cadastro_produto.setStyleSheet(u"\n"
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

        self.horizontalLayout_18.addWidget(self.btn_cadastro_produto)

        self.label_27 = QLabel(self.pg_cadastro_produto)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_18.addWidget(self.label_27)


        self.verticalLayout_15.addLayout(self.horizontalLayout_18)

        self.Pages.addWidget(self.pg_cadastro_produto)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout = QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(39, 39, 39);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_13 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_2 = QLabel(self.pg_cadastro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_2)

        self.label_4 = QLabel(self.pg_cadastro)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.pg_cadastro)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"color:rgb(255,255,255);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"")

        self.horizontalLayout_8.addWidget(self.txt_nome)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setStyleSheet(u"color:rgb(255,255,255);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"")

        self.horizontalLayout_7.addWidget(self.txt_usuario)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"color:rgb(255,255,255);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"")

        self.horizontalLayout_6.addWidget(self.txt_senha)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.txt_senha2 = QLineEdit(self.pg_cadastro)
        self.txt_senha2.setObjectName(u"txt_senha2")
        self.txt_senha2.setStyleSheet(u"color:rgb(255,255,255);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"")

        self.horizontalLayout_5.addWidget(self.txt_senha2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(11)
        self.cb_perfil.setFont(font7)
        self.cb_perfil.setStyleSheet(u"color:rgb(255,255,255);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"")

        self.horizontalLayout_9.addWidget(self.cb_perfil)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.verticalLayout_13.addLayout(self.verticalLayout_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.btn_cadastro = QPushButton(self.pg_cadastro)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setFont(font6)
        self.btn_cadastro.setStyleSheet(u"\n"
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

        self.horizontalLayout_10.addWidget(self.btn_cadastro)

        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_extorno = QWidget()
        self.pg_extorno.setObjectName(u"pg_extorno")
        self.verticalLayout_14 = QVBoxLayout(self.pg_extorno)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_21 = QLabel(self.pg_extorno)
        self.label_21.setObjectName(u"label_21")
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(20)
        self.label_21.setFont(font8)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_21)

        self.label_13 = QLabel(self.pg_extorno)
        self.label_13.setObjectName(u"label_13")
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(15)
        font9.setBold(True)
        self.label_13.setFont(font9)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_13)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_14 = QLabel(self.pg_extorno)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font5)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.label_14)

        self.txt_pedido_extorno = QLineEdit(self.pg_extorno)
        self.txt_pedido_extorno.setObjectName(u"txt_pedido_extorno")
        self.txt_pedido_extorno.setStyleSheet(u"color:rgb(255,255,255);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"")

        self.horizontalLayout_11.addWidget(self.txt_pedido_extorno)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.pg_extorno)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font5)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.label_15)

        self.txt_quantidade_extorno = QLineEdit(self.pg_extorno)
        self.txt_quantidade_extorno.setObjectName(u"txt_quantidade_extorno")
        self.txt_quantidade_extorno.setStyleSheet(u"color:rgb(255,255,255);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"")

        self.horizontalLayout_12.addWidget(self.txt_quantidade_extorno)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_16 = QLabel(self.pg_extorno)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setFont(font5)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.label_16)

        self.txt_data_extorno = QDateEdit(self.pg_extorno)
        self.txt_data_extorno.setObjectName(u"txt_data_extorno")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_data_extorno.sizePolicy().hasHeightForWidth())
        self.txt_data_extorno.setSizePolicy(sizePolicy2)
        self.txt_data_extorno.setMinimumSize(QSize(0, 18))
        self.txt_data_extorno.setMaximumSize(QSize(16777215, 18))
        font10 = QFont()
        font10.setPointSize(14)
        self.txt_data_extorno.setFont(font10)
        self.txt_data_extorno.setStyleSheet(u"color:rgb(255,255,255);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"")

        self.horizontalLayout_13.addWidget(self.txt_data_extorno)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)


        self.verticalLayout_14.addLayout(self.verticalLayout_8)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_20 = QLabel(self.pg_extorno)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_16.addWidget(self.label_20)

        self.btn_saida = QPushButton(self.pg_extorno)
        self.btn_saida.setObjectName(u"btn_saida")
        self.btn_saida.setFont(font6)
        self.btn_saida.setStyleSheet(u"\n"
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

        self.horizontalLayout_16.addWidget(self.btn_saida)

        self.label_19 = QLabel(self.pg_extorno)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_16.addWidget(self.label_19)


        self.verticalLayout_14.addLayout(self.horizontalLayout_16)

        self.Pages.addWidget(self.pg_extorno)

        self.verticalLayout_10.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"VENDAS", None))
        self.btn_pg_venda.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE USU\u00c1RIO", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"GERENCIAMENTO DO ESTOQUE", None))
        self.insert_produto.setText(QCoreApplication.translate("MainWindow", u"INSERIR PRODUTO", None))
        self.btn_excluir_produto.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR PRODUTO", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"GERENCIAMENTO DAS SA\u00cdDAS", None))
        self.insert_saida.setText(QCoreApplication.translate("MainWindow", u"INSERIR SA\u00cdDA", None))
        self.btn_extorno.setText(QCoreApplication.translate("MainWindow", u"ESTORNO", None))
        self.btn_dashboards.setText(QCoreApplication.translate("MainWindow", u"GERAR GR\u00c1FICOS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"SA\u00cdDAS", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR PRODUTO", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Cadastro de produto", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o \u00danico", None))
        self.label_26.setText("")
        self.btn_cadastro_produto.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR PRODUTO", None))
        self.label_27.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#fff;\">PySystem</span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#fff;\">Gerenciamento de estoque</span></p></body></html>", None))      
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TELA DE CADASTRO", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE USU\u00c1RIO", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o seu Nome:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio:", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seu nome de Usu\u00e1rio", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Senha: ", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua Senha", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.txt_senha2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repita a Senha Novamente", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Perfil:", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Adminstrador", None))

        self.label_10.setText("")
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_11.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">TELA DE ESTORNO DE VENDAS</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"REALIZAR ESTORNO", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Pedido", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Data:", None))
        self.label_20.setText("")
        self.btn_saida.setText(QCoreApplication.translate("MainWindow", u"SOLICITAR ESTORNO", None))
        self.label_19.setText("")
    # retranslateUi