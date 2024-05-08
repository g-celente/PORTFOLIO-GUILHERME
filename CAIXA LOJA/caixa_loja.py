produtos = {
    "arroz": 29.99,
    "feijão": 19.99,
    "tomate": 8.99,
    "patinho": 19.99,
    "frango": 19.99,
    "batata": 5.99
} #criar um excel que integre junto com o python para que consiga acessar uma quantidade enorme de produtos, preço, quantia e etc..

def soma (preco_total,quantia_dinheiro):
    troco = preco_total - quantia_dinheiro
    return troco
    #criar função que possa gerar recibos de vendas, relatório de vendas, gerenciar transações e etc...

def cadastrar (produtos,preco_produto,listaProdutos):
    listaProdutos[produtos] = preco_produto
    return listaProdutos
    #criar função que acesse diretamente o excel criado para que ele consiga adicionar e modificar itens dentro do Excel


def funcao_produtos(listaProdutos):
    for produto in listaProdutos:
        produtosz = produto.capitalize()
        preco_produto = listaProdutos[produto]
        print(F"- {produtosz} : R$ {preco_produto:.2f}")

while True:
    print(20*"-", "Supermercado Guanabara", 20*"-")

    escolha = int(input("Escolha uma opção abaixo:\n 1 - Caixa\n 2 - Cadastrar Produto\n 3 - Produtos Cadastrados\n 4 -  Sair\n Digite a opção: "))

    if escolha == 1:
        print("Função Caixa Acionada!")

        while True:
            compra = 0
            produto = input("Digite o nome do produto (digite s para finalizar): ").lower()

            if produto == "s":
                break

            if produto not in produtos:
                print("Produto inválido, tente novamente...")
                continue

            else:
                compra += produtos[produto]

        while True:   
            forma_pagamento = int(input("Formas de Pagamento\n 1 - Dinheiro\n 2 - Cartão\n Escolha uma das opções: "))

            if forma_pagamento == 1:
                quantia_dinheiro = int(input("Qual a quantia em dinheiro? R$ ")) 
                print(f"O Total da compra é igual a: R$ {compra}")
                print(f"O Valor do troco é igual a: R$ {soma(compra,quantia_dinheiro)}")
    
    elif escolha == 2:
        print("Função Cadastrar Acionada!")

        while True:
            produto_novo = input("Digite o nome do produto: ").lower()

            if produto_novo in produtos:
                print("Produto já cadastrado, tente novamente...")
                continue
            else:
                preco_produto = int(input("Digite o preço do Produto: R$ "))
                cadastrar(produto_novo,preco_produto,produtos)
                funcao_produtos(produtos)
    elif escolha == 3:
        print("Função Verificar Produtos Acionada!")
        funcao_produtos(produtos)

    elif escolha == 4:
        print("Obrigado por usar o Caixa Guanabara!")
        break
    else:
        print("Opção inválida, tente novamente...")
        continue

#garantir que as informações dos clientes através de cartão de crédito estejam seguras 
#criar chatbot para auxílio aos clientes de alguma forma
#garantir que o python faça backups semanalmente para que nada seja perdido ao longo do tempo