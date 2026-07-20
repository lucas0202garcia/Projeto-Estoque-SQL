import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

print("Iniciando a extração simulada do ERP...")

# 1. Gerando a Tabela de Produtos (Dimensão)
produtos_data = {
    'id_produto': range(1, 21),
    'nome_produto': [
        'Notebook Pro', 'Mouse Wireless', 'Teclado Mecânico', 'Monitor 24', 'Cabo HDMI',
        'Cadeira Gamer', 'Headset Bluetooth', 'Webcam 1080p', 'SSD 1TB', 'Memória RAM 16GB',
        'Placa de Vídeo', 'Fonte 600W', 'Gabinete ATX', 'Cooler Fan', 'Roteador Wi-Fi',
        'Smartphone X', 'Tablet 10', 'Smartwatch', 'Carregador USB-C', 'Bateria Portátil'
    ],
    'categoria': ['Informática', 'Acessórios', 'Acessórios', 'Monitores', 'Acessórios',
                  'Móveis', 'Acessórios', 'Acessórios', 'Hardware', 'Hardware',
                  'Hardware', 'Hardware', 'Hardware', 'Hardware', 'Redes',
                  'Mobile', 'Mobile', 'Mobile', 'Mobile', 'Mobile'],
    'custo_unitario': [2500.0, 40.0, 150.0, 600.0, 15.0, 500.0, 120.0, 180.0, 200.0, 160.0,
                       1500.0, 220.0, 180.0, 30.0, 130.0, 1800.0, 900.0, 400.0, 50.0, 80.0]
}
df_produtos = pd.DataFrame(produtos_data)
# Calculando preço de venda com uma margem de lucro aleatória entre 30% e 60%
df_produtos['preco_venda'] = df_produtos['custo_unitario'] * np.random.uniform(1.3, 1.6, 20)
df_produtos['preco_venda'] = df_produtos['preco_venda'].round(2)


# 2. Gerando a Tabela de Estoque Atual (Fato)
estoque_data = {
    'id_produto': range(1, 21),
    'quantidade_atual': [random.randint(5, 100) for _ in range(20)],
    'lead_time_dias': [random.randint(2, 15) for _ in range(20)] # Tempo que o fornecedor demora pra entregar
}
df_estoque = pd.DataFrame(estoque_data)


# 3. Gerando Histórico de Vendas dos últimos 90 dias (Fato)
dias_historico = 90
data_final = datetime.today()
data_inicial = data_final - timedelta(days=dias_historico)

vendas_list = []
# Simulando cerca de 1000 transações
for i in range(1, 1001):
    id_prod = random.randint(1, 20)
    qtd_vendida = random.randint(1, 5)
    # Criando datas aleatórias nos últimos 90 dias
    dias_aleatorios = random.randint(0, dias_historico)
    data_venda = data_inicial + timedelta(days=dias_aleatorios)
    
    vendas_list.append({
        'id_venda': i,
        'data_venda': data_venda.strftime('%Y-%m-%d'),
        'id_produto': id_prod,
        'quantidade': qtd_vendida
    })

df_vendas = pd.DataFrame(vendas_list)
# Ordenando as vendas por data
df_vendas = df_vendas.sort_values(by='data_venda')

# Exportando para CSV
df_produtos.to_csv('produtos.csv', index=False)
df_estoque.to_csv('estoque.csv', index=False)
df_vendas.to_csv('vendas.csv', index=False)

print("✅ Sucesso! Arquivos 'produtos.csv', 'estoque.csv' e 'vendas.csv' gerados na pasta.")
