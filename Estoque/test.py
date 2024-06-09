import random
from datetime import datetime, timedelta

# Produtos e preços fixos
products = [
    (1, 'Calça', 9.99),
    (2, 'Camisa', 19.99),
    (3, 'Jaqueta', 29.99)
]

# Estados brasileiros
estados_brasileiros = [
    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal",
    "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul",
    "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
    "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina",
    "São Paulo", "Sergipe", "Tocantins"
]

# Lojas Renner
lojas_renner = ["RennerMG", "RennerRJ", "RennerSP"]

# Função para gerar uma data aleatória dentro de um mês específico
def random_date_in_month(year, month):
    start_date = datetime(year, month, 1)
    end_date = (start_date + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Geração de dados
data = []
for i in range(1, 301):
    product_id, product_name, price = random.choice(products)
    quantity = random.randint(1, 30)
    month = random.randint(1, 12)
    sale_date = random_date_in_month(2023, month).strftime('%Y-%m-%d')
    estado = random.choice(estados_brasileiros)
    if estado in lojas_renner:
        store = random.choice(lojas_renner)
    else:
        store = estado
    loja_renner_aleatoria = random.choice(lojas_renner)
    data.append((product_id, product_name, quantity, sale_date, price, store, loja_renner_aleatoria))

# Conversão para instruções SQL de inserção
insert_statements = "INSERT INTO sales (product_id, product_name, quantity, sale_date, price, store, loja_renner_aleatoria) VALUES\n"
for record in data:
    insert_statements += f"({record[0]}, '{record[1]}', {record[2]}, '{record[3]}', {record[4]}, '{record[5]}', '{record[6]}'),\n"

# Remover a última vírgula e nova linha, e adicionar um ponto e vírgula no final
insert_statements = insert_statements.rstrip(",\n") + ";"

# Escrever em um arquivo
with open("insert_sales.sql", "w") as file:
    file.write(insert_statements)

# Imprimir o resultado (opcional)
print(insert_statements)