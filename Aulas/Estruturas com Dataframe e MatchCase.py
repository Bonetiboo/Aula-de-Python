import pandas as pd

dados = {
    'produto': ['notebook', 'mouse','teclado', 'monitor', 'webcam'],
    'vendas': [1200, 300, 450, 800, 80],
    'lucro': [300, 50, 80, 200, 40],
    'ano': ['2022','2022','2022','2022','2022']
}

print(dados)

dataframe = pd.DataFrame(dados)

# Cálculo média

media = dataframe['lucro'].mean()
mediana = dataframe['lucro'].median()
min = dataframe['lucro'].min()
max = dataframe['lucro'].max()
print(media)
print(mediana)
print(min)
print(max)

# Verificar as informações do dataframe

dataframe.info()

dataframe["produto"].value_counts()

# Try/Except

try:
    media = dataframe['fiap'].mean()
    print(f'A média de lucro é: {media}')
except KeyError:
    print('Esta coluna não existe!')
    
try:
    dataframe['relação_vendas_lucro'] = dataframe['lucro'] / dataframe['vendas']
    
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
    
else:
    print("A margem foi calculada com sucesso!")
    
try:
    numero = int(input("Insira um número: "))
    
except ValueError:
    print("Valor não numérico!")

try:
    numero2 = int(input("Insira um número: "))
    numero3 = int(input("Insira um segundo número: "))
    
    soma = numero2 + numero3
    sub = numero2 - numero3
    div = numero2 / numero3
    print(soma)
    print(sub)
    print(div)
    
except ValueError:
    print("Valor não numérico!")
    
except ZeroDivisionError:
    print("Erro: divisão por zero!")

for coluna in ['vendas', 'lucro']:
    try:
        media = dataframe[coluna].mean()
        print(f"A média da coluna {coluna} é {media}: ")
    except KeyError:
        print(f"A coluna {coluna} é inexistente.")