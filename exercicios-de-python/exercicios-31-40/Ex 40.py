# Ex.40 - Crie um algoritmo usando while true para ignorar valores negativos. Se o número for 0, quebre a estrutura de repetição, caso contrário envie cada número para uma lista.

lista = []

while True:
    numeros = int(input("Digite um número qualquer que não seja 0 ou negativo: "))
    if numeros > 0:
        lista.append(numeros)
        print(lista)
    if numeros == 0:
        break
    if numeros < 0:
        continue