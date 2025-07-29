import pandas as pd
import matplotlib.pyplot as plt

# Lê os dados do arquivo CSV corrigido
df = pd.read_csv('Dados/carros.csv')

# Garante que os nomes das colunas estejam limpos
df.columns = df.columns.str.strip()

# Agrupa por marca e soma a quantidade de vendas
dados_por_marca = df.groupby('Marca')['Quantidade'].sum().sort_values(ascending=False)

# Configurações do gráfico de pizza
plt.figure(figsize=(10, 10))
cores = plt.cm.tab20.colors  # Paleta com boa variedade de cores
explode = [0.1 if i == 0 else 0 for i in range(len(dados_por_marca))]  # Destaque para a maior fatia

# Gera o gráfico de pizza
plt.pie(
    dados_por_marca,
    labels=dados_por_marca.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=cores,
    explode=explode,
    shadow=True
)

# Título e ajuste visual
plt.title('Participação de Mercado por Marca - Carros Mais Vendidos no Brasil', fontsize=14)
plt.axis('equal')  # Deixa o gráfico redondinho
plt.tight_layout()

# Salva o gráfico em PNG na pasta do script
plt.savefig('grafico_pizza_marcas.png', dpi=300)

# Exibe o gráfico na tela
plt.show()

