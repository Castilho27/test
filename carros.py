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
