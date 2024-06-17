import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import openpyxl


def carregar_dados_vendas(caminho_arquivo):
    workbook = openpyxl.load_workbook(caminho_arquivo)
    folha = workbook.active
    dados = list(folha.values)
    cabecalhos = dados[0]
    dados_vendas = dados[1:]

    vendas_por_loja = {}
    for linha in dados_vendas:
        nome_loja = linha[11]  
        if nome_loja and nome_loja.strip(): 
            if nome_loja not in vendas_por_loja:
                vendas_por_loja[nome_loja] = []
            vendas_por_loja[nome_loja].append(linha)

    return cabecalhos, dados_vendas, vendas_por_loja

def criar_treeview_loja(parent, nome_loja, cabecalhos, dados_vendas, linha, coluna):
    frame = ctk.CTkFrame(parent)
    frame.grid(row=linha, column=coluna, padx=10, pady=10, sticky="nsew")

    label = ctk.CTkLabel(frame, text=nome_loja, font=ctk.CTkFont(size=20, weight="bold"))
    label.pack(pady=5)

    colunas = cabecalhos
    treeview = ttk.Treeview(frame, columns=colunas, show='headings')
    treeview.pack(fill='both', expand=True, padx=0, pady=5)

    largura_coluna = 120  
    for col in colunas:
        treeview.heading(col, text=col)
        treeview.column(col, width=largura_coluna)

    for linha in dados_vendas:
        treeview.insert('', tk.END, values=linha)


    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    return frame


planilha = 'sales.xlsx'


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Dados de Vendas por Loja")
root.geometry("1920x1080")


for i in range(3):  
    root.grid_rowconfigure(i, weight=1)
for j in range(2):  
    root.grid_columnconfigure(j, weight=1)


cabecalhos, dados_vendas_completos, vendas_por_loja = carregar_dados_vendas(planilha)


criar_treeview_loja(root, "Todos os Dados", cabecalhos, dados_vendas_completos, 0, 0)


linha, coluna = 0, 1  
for index, (nome_loja, dados_vendas) in enumerate(vendas_por_loja.items()):
    criar_treeview_loja(root, nome_loja, cabecalhos, dados_vendas, linha, coluna)
    coluna += 1
    if coluna > 1:
        coluna = 0
        linha += 1


root.mainloop()
