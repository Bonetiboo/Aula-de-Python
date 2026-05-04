# Ex.36 - Crie um programa que socilite 5 números inteiros, armazene em uma lista o seu valor ao quadrado. [numero, numero**2]

listaTotal = []

i = 0

while i < 5:
    numeroBase = int(input("Forneça um número: "))
    numeroAoQuadrado = numeroBase ** 2
    listaIndividual = [numeroBase, numeroAoQuadrado]
    listaTotal.append(listaIndividual)
    i += 1

print(listaTotal)