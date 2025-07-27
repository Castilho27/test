import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# Lê o CSV
df = pd.read_csv('Dados/dados.csv', encoding='latin1')

# Converte a data
df['Date'] = pd.to_datetime(df['Date'].str.replace(',', '/'), format='%d/%m/%Y')

# Define o estilo seaborn para o fundo
sns.set_style('whitegrid')

plt.figure(figsize=(16, 7))

# Plota a linha com pontos e estilo mais elegante
plt.plot(df['Date'], df['Value'], 
         label='Vendas de Carros', 
         color='#1f77b4',       # Azul moderno
         linewidth=2.5,         # Linha mais grossa
         marker='o',            # Pontos nos dados
         markersize=6, 
         markerfacecolor='white', 
         markeredgewidth=1.5,
         markeredgecolor='#1f77b4')

# Títulos e legendas com fontes maiores
plt.title('Vendas de Carros no Brasil (1990–2022)', fontsize=18, fontweight='bold')
plt.xlabel('Ano', fontsize=14)
plt.ylabel('Número de Carros Vendidos', fontsize=14)
plt.legend(fontsize=12)

# Ajusta o eixo X
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.YearLocator(2))  # Marca a cada 2 anos
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)

# Grid mais suave
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
