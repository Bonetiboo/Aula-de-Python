# Ex.37 - Crie um programa que solicite nome, curso e idade de 3 pessoas, armazene cada pessoa como uma lista dentro de outra lista_completa.

listaTotal = []

i = 0

while i < 3:
    nome = input("Digite seu nome: ")
    curso = input("Digite seu curso: ")
    idade = int(input("Digite sua idade: "))
    listaIndividual = [nome, curso, idade]
    listaTotal.append(listaIndividual)
    i += 1
    
print(f"A lista de usuários com seus respectivos nomes, cursos e idades são: {listaTotal}")