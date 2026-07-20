# Projeto-Estoque-SQL
Pipeline de Supply Chain Analytics com Python, SQL (SQLite) e Power BI para prevenção de ruptura de estoque e alertas de compras automatizados.
# 📦 Supply Chain Analytics: Prevenção de Ruptura de Estoque

## 🎯 O Desafio de Negócios
Ruptura de estoque é dinheiro deixado na mesa. Quando um produto acaba antes do fornecedor conseguir repor, a empresa perde vendas e credibilidade. Este projeto simula um ambiente de ERP corporativo para identificar antecipadamente quais produtos (SKUs) correm risco de ruptura, gerando alertas de compra automatizados.

## 🛠️ Arquitetura e Tecnologias
Para resolver este problema de logística, construí um pipeline de dados completo:
* **Python (Pandas):** Construção de um script gerador de dados sintéticos para simular o comportamento de um ERP (Produtos, Estoque Atual e Histórico de Vendas de 90 dias).
* **SQL (SQLite):** Modelagem relacional e estruturação do banco de dados (`estoque_erp.db`).
* **Python (Engine de Regras):** Execução de query SQL avançada com `JOINs`, funções de agregação e lógicas condicionais (`CASE WHEN`) para calcular o giro diário e o status de segurança do estoque cruzado com o *Lead Time* do fornecedor.
* **Power BI:** Conexão direta com a saída dos dados processados para a criação de um Dashboard Tático, filtrando itens de Ação Imediata.

## 🧠 Lógica de Negócios Aplicada
O motor SQL foi programado para calcular:
1. **Média de Venda Diária:** Quantos itens saem por dia, com base nos últimos 90 dias.
2. **Dias de Cobertura:** Divisão do Estoque Atual pela Média de Venda Diária.
3. **Alerta de Ruptura:** Compara os *Dias de Cobertura* com o *Prazo do Fornecedor (Lead Time)*. Se o estoque durar menos tempo do que o fornecedor demora para entregar, o alerta **"🚨 Ruptura Iminente"** é disparado.

## 📊 Dashboard Gerencial
(![Dashboard de Estoque](https://github.com/user-attachments/assets/3a16ae76-6798-4a12-8270-12f2c6eff30f))

## 🚀 Como Executar
1. Rode `gerador_erp.py` para criar os dados em CSV.
2. Rode `cria_banco.py` para injetar os dados no banco SQLite.
3. Rode `analise_estoque.py` para gerar o relatório estratégico de compras.
