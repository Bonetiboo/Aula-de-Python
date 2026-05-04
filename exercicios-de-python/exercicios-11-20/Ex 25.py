# Ex.25 Vamos fazer um algoritmo para cadastro com média. Solicite 3 informações: nome, nota1 e nota2 três vezes. Após isso, calcule a média de cada aluno e retorne uma lista contendo nome, nota1, nota2 e a média de cada aluno.
# Estrutura: lista = [[nome, nota1, nota2, média], [nome, nota1, nota2, média], [...]]
 
lista = []

for i in range (3):
    nome = input("Forneça o nome do aluno: ")
    nota1 = float(input("Fornaça a primeira nota: "))
    nota2 = float(input("Fornaça a segunda nota: "))
    media = (nota1 + nota2) / 2
    nota_media = [nome, nota1, nota2]
    lista.append(nota_media)

print(lista)