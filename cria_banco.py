import sqlite3
import pandas as pd

print("Iniciando a criação do Banco de Dados SQL...")

# 1. Cria a conexão e o arquivo do banco de dados (estoque_erp.db)
conexao = sqlite3.connect('estoque_erp.db')

# 2. Lê os arquivos CSV que geramos na Sprint 1
df_produtos = pd.read_csv('produtos.csv')
df_estoque = pd.read_csv('estoque.csv')
df_vendas = pd.read_csv('vendas.csv')

# 3. Envia os dados para o SQLite, criando as tabelas automaticamente
# O if_exists='replace' garante que se rodarmos o script de novo, ele recria as tabelas limpas
df_produtos.to_sql('produtos', conexao, if_exists='replace', index=False)
df_estoque.to_sql('estoque', conexao, if_exists='replace', index=False)
df_vendas.to_sql('vendas', conexao, if_exists='replace', index=False)

print("✅ Banco de dados 'estoque_erp.db' estruturado e populado com sucesso!")

# Fecha a conexão por segurança
conexao.close()
