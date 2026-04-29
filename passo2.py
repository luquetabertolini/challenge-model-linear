import pandas as pd

# 1. Carregar o arquivo
df = pd.read_csv('Electric_Vehicle_Charging_Stations.csv')

# 2. Selecionar a variável quantitativa discreta
# Vamos analisar quantos carregadores de 'Nível 2' as estações costumam ter
coluna_discreta = 'EV Level2 EVSE Num'

# 3. Criar a Tabela de Frequência
# Contamos quantas vezes cada número (0, 1, 2, 4...) aparece
df_frequencia = df[coluna_discreta].value_counts().reset_index()
df_frequencia.columns = [coluna_discreta, 'fi']  # fi = Frequência Absoluta

# 4. Ordenar pelo valor da variável (importante para discretas)
df_frequencia = df_frequencia.sort_values(by=coluna_discreta).reset_index(drop=True)

# 5. Cálculos Estatísticos
total = df_frequencia['fi'].sum()

# Frequência Relativa (fi / n)
df_frequencia['ri'] = df_frequencia['fi'] / total

# Frequência Relativa Percentual (ri * 100)
df_frequencia['ri%'] = (df_frequencia['ri'] * 100).round(2)

# Frequência Acumulada (Fi)
df_frequencia['Fi'] = df_frequencia['fi'].cumsum()

# Frequência Acumulada Relativa (Ri%)
df_frequencia['Ri%'] = df_frequencia['ri%'].cumsum().round(2)

print(f"Tabela de Frequência para: {coluna_discreta}")
print(df_frequencia)