import pandas as pd

# 1. Carrega o arquivo
df = pd.read_csv('Electric_Vehicle_Charging_Stations.csv')

# 2. Configura o Pandas para não esconder nada
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("--- Lendo as 20 primeiras linhas do banco de dados ---")

# 3. Exibe as 20 primeiras observações
print(df.head(40))

print("------------------------------------------------------")
print(f"Total de linhas carregadas: {len(df)}")