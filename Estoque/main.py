from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication,QMainWindow,QWidget, QMessageBox)
from login import Ui_Login
from windowMain import Ui_MainWindow
import sys
import subprocess
import time as t
from database import *


class Login(QWidget,Ui_Login):
    def __init__(self):
        super(Login,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Login No Sistema')
        self.tentativas = 3

        self.btn_entrar.clicked.connect(self.open_system)

    def open_system (self):

        self.users = Database()
        self.users.connect()

        autenticado = self.users.check_user(self.txt_login.text().upper(), self.txt_password.text().upper())

        if autenticado == 'Adminstrador' or autenticado == 'Usuário':
            self.w = MainWindow(autenticado)
            self.w.show()
            self.close()

        else:
            if self.tentativas > 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle('Usuário Inválido')
                msg.setText(f"Usuário Não registrado\n \n Tentativas: {self.tentativas}")
                self.tentativas -=1
                msg.exec()
            
            elif self.tentativas == 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle('Sistema Bloqueado')
                msg.setText("O sistema foi Bloqueado, numeros de tentativas excedidas")
                msg.exec()
                t.sleep(3)
                sys.exit()

        self.users.close_connection()

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,user):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Sistema de Vendas')
        

        if user.lower() == 'Usuário':
            self.btn_pg_cadastro.setVisible(False)
        
        else:
            self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
            self.btn_pg_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
            self.btn_tables.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
            self.btn_dashboards.clicked.connect(self.graficos)
            self.btn_cadastro.clicked.connect(self.subscribe_user)
            self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
            self.btn_tables.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))

    def graficos(self):
        subprocess.Popen(['streamlit', 'run', r'Estoque\dashs.py'])

    def subscribe_user(self):

        if self.txt_senha.text() != self.txt_senha2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senhas Diferentes")
            msg.setText("A senha não é igual")
            msg.exec()
            return None
        
        name = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db = Database()
        db.connect()
        db.insert_user(name,user,password,access)
        db.close_connection()

        msgs = QMessageBox()
        msgs.setIcon(QMessageBox.Information)
        msgs.setWindowTitle('Cadastrado Efetivado')
        msgs.setText("Usuário Cadastrado")
        msgs.exec()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
    