import pandas as pd

# 1. Carregar o arquivo
df = pd.read_csv('Electric_Vehicle_Charging_Stations.csv')

# --- EXERCÍCIO A: VARIÁVEL QUANTITATIVA DISCRETA ---
# Variável: Número de carregadores rápidos (EV DC Fast Count)
col_discreta = 'EV DC Fast Count'
tab_discreta = df[col_discreta].value_counts().sort_index().reset_index()
tab_discreta.columns = [col_discreta, 'fi']
tab_discreta['ri%'] = (tab_discreta['fi'] / tab_discreta['fi'].sum() * 100).round(2)

print("TABELA A: VARIÁVEL DISCRETA (DC Fast Count)")
print(tab_discreta)
print("-" * 30)


# --- EXERCÍCIO B: VARIÁVEL QUANTITATIVA CONTÍNUA ---
# Variável: EV Level2 EVSE Num (Agrupada em classes/faixas)
bins = [0, 2, 4, 10, 50]
labels = ['0-2', '3-4', '5-10', '11-50']
df['Classe_Level2'] = pd.cut(df['EV Level2 EVSE Num'], bins=bins, labels=labels, include_lowest=True)

tab_continua = df['Classe_Level2'].value_counts().sort_index().reset_index()
tab_continua.columns = ['Intervalo (Level 2)', 'fi']
tab_continua['ri%'] = (tab_continua['fi'] / tab_continua['fi'].sum() * 100).round(2)
tab_continua['Fi'] = tab_continua['fi'].cumsum()

print("TABELA B: VARIÁVEL CONTÍNUA (Intervalos de Level 2)")
print(tab_continua)

# --- INSIGHTS DO EXERCÍCIO B ---
# Insight 1: # A coluna 'Fi' (Frequência Acumulada) mostra que a imensa maioria das estações foca em baixa capacidade (até 4 carregadores).
# Insight 2: # A frequência relativa (ri%) indica que estações de alta densidade (11-50 carregadores) são exceções, representando uma parcela mínima da rede.x