import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Lê o CSV
df = pd.read_csv('Dados/dados.csv', encoding='latin1')

# Converte a data
df['Date'] = pd.to_datetime(df['Date'].str.replace(',', '/'), format='%d/%m/%Y')

# Configura o tamanho do gráfico
plt.figure(figsize=(14, 6))

# Plota a linha de vendas
plt.plot(df['Date'], df['Value'], label='Vendas de Carros', color='blue')

# Títulos e legendas
plt.title('Vendas de Carros no Brasil (1990–2022)')
plt.xlabel('Ano')
plt.ylabel('Número de Carros Vendidos')
plt.grid(True)
plt.legend()

# Deixa o eixo X mais limpo
plt.gca().xaxis.set_major_locator(mdates.YearLocator(2))  # Mostra a cada 2 anos
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

