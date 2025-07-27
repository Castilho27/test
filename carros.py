import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os

# Mostra os arquivos dentro da pasta Dados
print(os.listdir("Dados"))

# Lê o arquivo CSV corretamente
df = pd.read_csv('Dados/dados.csv', encoding='latin1')

# Mostra as primeiras 5 linhas
print(df.head())

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Value'], label='Vendas de Carros', color='blue')
plt.title('Vendas de Carros no Brasil (1990–2022)')
plt.xlabel('Data')
plt.ylabel('Número de Carros Vendidos')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
