# Ex.38 - Crie um programa que solicite números para o usuário, pare quando digitar 0, armazene números em uma lista. Mostre a lista completa, e a soma dos valores.

listaCompleta = []
somaCompleta = 0

numeros = float(input("Digite um número qualquer, caso queira parar digite 0: "))
listaCompleta.append(numeros)
somaCompleta += numeros

while numeros != 0:
    numeros = float(input("Digite o próximo número: "))
    listaCompleta.append(numeros)
    somaCompleta += numeros

print(f"A lista completa de números e a soma de todos eles é respectivamente: {listaCompleta} e {somaCompleta}")