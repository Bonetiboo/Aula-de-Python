# Estrutura de repetição

# [] - lista
# () - dupla
# {} - dicionário

# var iteradora: i = o, i = 1, i = 2 e etc.

# += somar uma variável à outra
# -= subtrair uma variável à outra

# for é de repetição. Range é a quantidade de coisas, no caso 5 coisas, independentemente de qual tipo de variável seja.
# append é utilizado para preencher a lista, ou seja, quando colocarmos o nome ele inclui ele na lista.

# Exemplo 1:

lista = [] 

for i in range (5): 
     nome = input("") 
     lista.append(nome) 
     print(lista)

# Exemplo 2:

soma = 0

for numero in range (1, 4): 
     soma += numero
     print(soma)

# Exemplo 3:

subtração = 0

for numero1 in range (1, 5):
     subtração -= numero1
     print(subtração)

# Exemplo 4:

lista_nomes = ["ana", "laura", "pedro", "jose"]
# print(lista_nomes[0])  deverá aparecer a ana, pois ela é o de índice 0
# print(lista_nomes[1])  deverá aparecer a laura, pois ela é o de índice 1
# print(lista_nomes[2])  deverá aparecer a pedro, pois ela é o de índice 2
# print(lista_nomes[3])  deverá aparecer a jose, pois ela é o de índice 3

for n in lista_nomes:
     print(n)

# Exemplo 5:

lista_nomes_numeros = ["ana", "laura", "pedro", "jose", 1, 2, 3]

for nn in lista_nomes_numeros:
     print(nn)

# Exemplo 6:

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

maior = numeros[0]

for ns in numeros: # esse for ns in numeros diz que ele deve passar por cada um dos índices da lista "numeros" e tornar o valor da variável iteradora ns como o índice atual. 
     if ns > maior:
          maior = ns

print(f"O maior número da lista é {maior}")

# Exemplo 7: 

for nn in range (1, 5):
     if nn == 3:
          continue # ou seja, ignore o 3, apenas continue sem considerar o 3.
     print(nn)

# Exemplo 8:

for nn in range (1, 5):
     if nn == 3:
          break # ou seja, pare a estrutura de repetição.
     print(nn)

