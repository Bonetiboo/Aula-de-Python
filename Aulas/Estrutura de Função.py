# Exemplo 1

comando = 'start'

if comando == 'start':
    print("Iniciando!")
elif comando == "stop":
    print("Parando!")
else:
    print("Entrada inválida!")

# Match/Case

comando = input("Digite uma entrada: ")

match comando:
    case 'start':
        print("Iniciando!")
    case 'stop':
        print('Parando!')
    case _:
        print('Entrada inválida!')

# Exemplo 2

opcao = input("Digite um número: ")

match opcao:
    case '1':
        print('Cadastrar!')
    case '2':
        print('Listar!')
    case _:
        print("Entrada inválida!")

# Exemplo 3

dados = ("produto", 'arroz', 10)

match dados:
    case ('produto', nome, qtd):
        print(f"{nome} - {qtd}")
    case _:
        print("Entrada inválida!")

numero = int(input("Entre com um número: "))

match numero:
    case _ if (numero %2 == 0):
        print('Par!')
    case _:
        print('Impar!')

######################

# Função def

def nome(parametros): # O que será feito com os parâmetros
    return 'alguma coisa'

def somar(a, b):
    soma = a + b
    sub = a - b
    div = a / b
    mult = a * b
    return soma, sub, div, mult

a, b, c, d = somar(20, 40)
print(a)
print(b)
print(c)
print(d)

# Função def para dataframes

import pandas as pd

dados = {
    'nome': ['ana', 'carlos','letícia', 'ronaldo', 'marcos',],
    'idade': [35, 18, 23, 57, 55],
    'salario': [1618, 15387, 3700, 2500, 250000]

}

df = pd.DataFrame(dados)

# Exemplo 1

def mostrar_dataframe():
    print(df)

mostrar_dataframe()

# Exemplo 2

def mostrar_linhas_especificas():
    print(df.head())

mostrar_linhas_especificas()

# Exemplo 3

def mostrar_informacoes():
    print(df.info)

mostrar_informacoes()

# Exemplo 4

def media_idade():
    print("Média das idades: ", df['idade'].mean)

media_idade()

# Exemplo 5

def min_max_mean_salario():
    print(df['salario'].min())
    print(df['salario'].max())
    print(df['salario'].mean())

min_max_mean_salario()

# Exemplo 6

def filtro_idade():
    print(df['idade'] > 30)

filtro_idade()

# Exemplo 7

def adicionar_bonus():
    df['Bonus'] = df['salario'] * 1.1

adicionar_bonus()

# Exemplo 8

def ordenar_salario():
    print(df.sort_values('salario', ascending=False))
    
ordenar_salario()

# Exemplo 9

def contar_registros():
    print("Quantidade de registros: ", len(df))
    
contar_registros()

# Exemplo 10

def estatistica():
    print(df.describe())
    
estatistica()

# Exemplo 11

def registros_NaN():
    print(df['nome'].value_counts())
    
registros_NaN()