import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# Lê o CSV
df = pd.read_csv('Dados/dados.csv', encoding='latin1')

# Converte a data
df['Date'] = pd.to_datetime(df['Date'].str.replace(',', '/'), format='%d/%m/%Y')

# Define estilo do seaborn e remove bordas
sns.set_style('whitegrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

# Cria a figura
plt.figure(figsize=(16, 8))

# Cor principal
cor_linha = '#007ACC'

# Linha e sombreamento
plt.plot(df['Date'], df['Value'], color=cor_linha, linewidth=2.8, label='Vendas de Carros')
plt.fill_between(df['Date'], df['Value'], color=cor_linha, alpha=0.1)

# Destaques: Máximo e mínimo
max_val = df.loc[df['Value'].idxmax()]
min_val = df.loc[df['Value'].idxmin()]

plt.scatter([max_val['Date']], [max_val['Value']], color='red', zorder=5)
plt.scatter([min_val['Date']], [min_val['Value']], color='green', zorder=5)

plt.text(max_val['Date'], max_val['Value'], f'Máx: {int(max_val["Value"]):,}', 
         fontsize=11, color='red', ha='left', va='bottom')
plt.text(min_val['Date'], min_val['Value'], f'Mín: {int(min_val["Value"]):,}', 
         fontsize=11, color='green', ha='left', va='top')

# Títulos e rótulos
plt.title('Vendas de Carros no Brasil (1990–2022)', fontsize=20, fontweight='bold', color='#333333')
plt.xlabel('Ano', fontsize=14)
plt.ylabel('Número de Carros Vendidos', fontsize=14)

# Eixo X mais limpo e rotacionado
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.YearLocator(2))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)

# Grid mais sutil
plt.grid(alpha=0.25)

# Legenda elegante
plt.legend(fontsize=13, loc='upper left', frameon=False)

# Layout final
plt.tight_layout()
plt.show()

