# Ex.34 - Cadastro de alunos: crie um algoritmo que solicite 3 nomes e 3 idades. Deixe a informação em uma lista no formato nome - idade.

listaCompleta = []

i=0

while i<3:
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    listaIndividual = [nome, idade]
    listaCompleta.append(listaIndividual)
    i+=1
    
print(listaCompleta)