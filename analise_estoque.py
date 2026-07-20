import sqlite3
import pandas as pd

print("Executando a query de inteligência de negócios no SQL...")

# 1. Conecta ao banco de dados que criamos na Sprint 2
conexao = sqlite3.connect('estoque_erp.db')

# 2. A Super Query SQL (Regras de Negócio e JOINs)
query_sql = """
SELECT 
    p.id_produto,
    p.nome_produto,
    p.categoria,
    p.preco_venda,
    e.quantidade_atual,
    e.lead_time_dias,
    SUM(v.quantidade) AS total_vendido_90d,
    
    -- Calcula a média diária de vendas (Total / 90 dias)
    ROUND(CAST(SUM(v.quantidade) AS FLOAT) / 90, 2) AS media_venda_diaria,
    
    -- Calcula quantos dias o estoque atual vai durar
    ROUND(e.quantidade_atual / (CAST(SUM(v.quantidade) AS FLOAT) / 90), 0) AS dias_estoque,
    
    -- Regra de Negócio: Status do Estoque
    CASE 
        WHEN (e.quantidade_atual / (CAST(SUM(v.quantidade) AS FLOAT) / 90)) <= e.lead_time_dias 
            THEN '🚨 Ruptura Iminente'
        WHEN (e.quantidade_atual / (CAST(SUM(v.quantidade) AS FLOAT) / 90)) <= (e.lead_time_dias + 7) 
            THEN '⚠️ Comprar Esta Semana'
        ELSE '✅ Estoque Saudável'
    END AS status_estoque

FROM produtos p
JOIN estoque e ON p.id_produto = e.id_produto
LEFT JOIN vendas v ON p.id_produto = v.id_produto

-- Agrupa por produto para poder somar as vendas corretamente
GROUP BY 
    p.id_produto, 
    p.nome_produto, 
    p.categoria, 
    p.preco_venda, 
    e.quantidade_atual, 
    e.lead_time_dias

-- Ordena para mostrar os problemas primeiro (Rupturas no topo)
ORDER BY dias_estoque ASC;
"""

# 3. O Pandas executa a query lá dentro do banco e traz o resultado como tabela
df_relatorio = pd.read_sql_query(query_sql, conexao)

# 4. Salva a tabela finalizada para usarmos no Power BI
df_relatorio.to_csv('relatorio_gerencial.csv', index=False)

print("✅ Sucesso! Relatório gerado: 'relatorio_gerencial.csv'")

# Fecha a conexão
conexao.close()
