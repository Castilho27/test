import pandas as pd
import matplotlib.pyplot as plt

# Lê os dados do arquivo CSV
df = pd.read_csv('Dados/dados.csv')

# Agrupa por marca e soma as quantidades
dados_por_marca = df.groupby('Marca')['Quantidade'].sum().sort_values(ascending=False)

# Configurações do gráfico
plt.figure(figsize=(10, 10))
cores = plt.cm.tab20.colors  # Paleta de cores moderna
explode = [0.1 if i == 0 else 0 for i in range(len(dados_por_marca))]  # Destaque para o maior

# Gráfico de pizza
plt.pie(
    dados_por_marca,
    labels=dados_por_marca.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=cores,
    explode=explode,
    shadow=True
)

plt.title('Participação por Marca - Carros Mais Vendidos no Brasil', fontsize=14)
plt.axis('equal')  # Deixa o gráfico circular

# Salva a imagem do gráfico na mesma pasta que o script
plt.tight_layout()
plt.savefig('grafico_pizza_marcas.png', dpi=300)
plt.show()
