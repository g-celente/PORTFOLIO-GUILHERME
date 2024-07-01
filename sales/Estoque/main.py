from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from login import Ui_Login
from windowMain import Ui_MainWindow
import sys
import subprocess
import time as t
from database import *
import openpyxl

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

        if autenticado.lower() == 'adminstrador' or autenticado.lower() == 'usuário':
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
            self.btn_pg_venda.setVisible(False)
            self.insert_produto.setVisible(False)
        
        
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_pg_venda.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        self.btn_tables.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
        self.btn_dashboards.clicked.connect(self.subprocess_dash)
        self.btn_cadastro.clicked.connect(self.subscribe_user)
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(self.show_table)
        self.btn_tables.clicked.connect(self.table_estoque)
        self.insert_saida.clicked.connect(self.subprocess_cadastro)
        self.btn_extorno.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_extorno))
        self.btn_saida.clicked.connect(self.estorno)
        self.insert_produto.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_produto))
        self.btn_cadastro_produto.clicked.connect(self.cadastrar_produto)

    def subprocess_dash(self):
        subprocess.Popen(['streamlit', 'run', r'sales\Estoque\dashs.py'])
    
    def subprocess_cadastro(self):
        subprocess.Popen(['python', r'sales\Cadastro\teste.py'])
    
    def message_Warning(self,texto, mensagem):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle(texto)
        msg.setText(mensagem)
        msg.exec()

    def message_Information(self, texto,mensagem):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(texto)
        msg.setText(mensagem)
        msg.exec()

    def estorno(self):
        pedido = self.txt_pedido_extorno.text()
        quantidade_extorno = self.txt_quantidade_extorno.text()
        vazio = ''

        if pedido == vazio or quantidade_extorno == vazio:
            self.message_Warning('Erro', 'Por Favor, insira todos os campos')
            return None

        df_sales = pd.read_excel(r'sales\sales.xlsx')
        df_estoque = pd.read_excel(r'sales\estoque.xlsx')

        try:
            venda_filtrada = df_sales[df_sales['Pedido'] == int(pedido)]
        except:
            self.message_Warning('Erro', 'Por favor insira números inteiros no pedido')
            return None

        if venda_filtrada.empty:
            self.message_Warning('Erro', 'Pedido não encontrado no estoque')
            return None

        quantidadePedido = venda_filtrada['Quantidade'].values[0]
        quantidade = int(quantidade_extorno)

        if quantidade > quantidadePedido:
            self.message_Warning('Erro', 'A quantidade inserida é maior\n que a quantidade do pedido')
            return None

        produto = venda_filtrada['Produto'].values[0]
        df_estoque.loc[df_estoque['Produto'] == produto, 'Quantidade'] += quantidade

        if quantidade == quantidadePedido:
            try:
                df_sales = df_sales[df_sales['Pedido'] != int(pedido)]
            except:
                self.message_Warning('Erro', 'Por favor insira números inteiros no pedido')
                return None
        else:
            try:
                df_sales.loc[df_sales['Pedido'] == int(pedido), 'Quantidade'] -= quantidade
            except:
                self.message_Warning('Erro', 'Por favor insira números inteiros no pedido')
                return None
            
        df_sales.to_excel(r'sales\sales.xlsx', index=False)
        df_estoque.to_excel(r'sales\estoque.xlsx', index=False)

        self.message_Information('Estorno Realizado', 'Extorno Realizado com Sucesso!')
    
    def show_table(self):
        df = pd.read_excel(r'sales\sales.xlsx')
        colunas_desejadas = ['Pedido', 'Quantidade', 'Produto', 'Preco', 'Faturamento', 'Data']
        df = df[colunas_desejadas]
        values = df.values.tolist() 

        self.tb_saida.clearContents()
        self.tb_saida.setRowCount(len(values))
        self.tb_saida.setColumnCount(len(df.columns))

        self.tb_saida.setHorizontalHeaderLabels(df.columns)

        for row_index, row_data in enumerate(values):
            for column_index, cell_data in enumerate(row_data):
                self.tb_saida.setItem(row_index, column_index, QTableWidgetItem(str(cell_data)))

    def table_estoque(self):
        df = pd.read_excel(r'sales\estoque.xlsx')
        values = df.values.tolist()

        self.td_estoque.clearContents()
        self.td_estoque.setRowCount(len(values))
        self.td_estoque.setColumnCount(len(df.columns))

        self.td_estoque.setHorizontalHeaderLabels(df.columns)

        for row_index, row_data in enumerate(values):
            for column_index, cell_data in enumerate(row_data):
                self.td_estoque.setItem(row_index, column_index, QTableWidgetItem(str(cell_data)))

        for linha in range(1,6):
            self.td_estoque.resizeColumnsToContents()

    def cadastrar_produto(self):
        df_estoque = pd.read_excel(r'sales\estoque.xlsx')
        df_produtos = df_estoque['Produto']
        df_produtos.values.tolist()
        codigo = self.txt_codigo.text()
        produto = self.txt_produto_estoque.text()
        quantidade_estoque = self.txt_quantidade_estoque.text()
        preco_unico = self.txt_preco_unico.text()
        vazio = ''

        if codigo == vazio or produto == vazio or quantidade_estoque == vazio or preco_unico == vazio:
            self.message_Warning('Erro', 'Por favor, insira todos os valores!')
            return None
        
        else: 
            if produto in df_produtos.values:
                self.message_Warning('Erro', 'Produto já está cadastrado no sistema!')
                return None
            
            arquivo = r'sales\estoque.xlsx'
            workbook = openpyxl.load_workbook(arquivo)
            folha = workbook.active

            try:
                quantidade = int(quantidade_estoque)
                preco = int(preco_unico)
            except:
                self.message_Warning('Erro', 'Por favor, insira números inteiros na Quantidade e Preço')
                return None
            
            faturamento = quantidade*preco
            info_produto = [codigo,produto,quantidade,preco, faturamento]
            folha.append(info_produto)
            workbook.save(arquivo)
            self.message_Information('Sucesso', 'Produto cadastrado com Sucesso!')
            

    def subscribe_user(self):

        if self.txt_senha.text() != self.txt_senha2.text():
            self.message_Warning('Senhas diferentes', 'As senhas não são iguais!')
            return None
        
        else:
            name = self.txt_nome.text()
            user = self.txt_usuario.text()
            password = self.txt_senha.text()
            access = self.cb_perfil.currentText()
            
            db = Database()
            db.connect()
            try:
                db.insert_user(name, user, password, access)
                self.message_Information('Cadastro Efetivado', 'Cadastro Realizado com Sucesso!')
            except sqlite3.IntegrityError:
                self.message_Information('Usuário Cadastrado', f'O Usuário {name} já está cadastrado!')
            finally:
                db.close_connection()
            
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
    