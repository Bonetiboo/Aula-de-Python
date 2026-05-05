# Ex.48 - Crie um algoritmo com try/except para mostrar as respectivas informações não numéricas (linha a linha).
#
# Por exemplo:
#
# Produto: notebook - Ano: 2022
# Produto: mouse - Ano: 2022
#
# E assim por diante.

import pandas as pd

dados = {
    'produto': ['notebook', 'mouse','teclado', 'monitor', 'webcam'],
    'vendas': [1200, 300, 450, 800, 80],
    'lucro': [300, 50, 80, 200, 40],
    'ano': ['2022','2022','2022','2022','2022']
}

dataframe = pd.DataFrame(dados)

for coluna in dados:
    try:
        if dataframe[coluna] == str:
            print(dataframe[coluna])
        else:
            continue
    except ValueError:
        print(f"A coluna {coluna} é numérica")