import pandas as pd

try:
    df = pd.read_csv('Dados/carros.csv', skip_blank_lines=True, encoding='utf-8')
    print(df.head())
except Exception as e:
    print("Erro ao ler o arquivo:", e)
