# Ex.30 - Crie um programa para gerar uma tabuada, a partir de duas variáveis (número e limite).

numero = int(input("Digite um número para descobrir sua tabuada: "))
limite = 0

while limite <= 9:
    resultado = numero * (limite + 1)
    limite += 1
    print(f"A tabuada de {numero} vezes {limite} é igual à: {resultado}")
