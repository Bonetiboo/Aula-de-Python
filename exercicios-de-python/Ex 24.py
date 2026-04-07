# Ex.24 - Crie um algoritmo para cadastro de alunos, onde deve ser solicitado nome e idade 5 vezes, porém, a informação deve aparecer na lista dentro de lista, ou seja, [nome1, idade1], [nome2, idade2], [...], e assim por diante. Print lista final.

lista = []

for i in range (5):
    nome = input("Forneça o nome: ")
    idade = int(input("Forneça a idade: "))
    
    nome_idade = [nome, idade]
    lista.append(nome_idade)

print(lista)