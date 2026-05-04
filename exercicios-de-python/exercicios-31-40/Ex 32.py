# Ex.32 - Crie um programa que socilite 5 nomes e insira em uma lista.

listaDeNomes = []

while len(listaDeNomes) < 5:
    nome = input("Forneça um nome: ")
    listaDeNomes.append(nome)
print(f"A lista completa de nomes é: {listaDeNomes}")