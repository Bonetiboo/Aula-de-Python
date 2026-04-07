# Ex.27 - Crie um algoritmo para solicitar nome e nota para 4 alunos. Insira em uma estrutura com lista dentro de lista (nome, nota). Após isso, crie uma estrutura para mostrar os alunos com nota maior ou igual à 6, mostrando o respectivo nome e nota. Crie também uma estrutura para mostrar os alunos com nota menor do que 6, mostrando o respectivo nome e nota.

lista_aprovados = []
lista_reprovados = []

for i in range (4):
    nome = input("Forneça o nome: ")
    nota = float(input("Forneça a nota: "))
    lista_nome_nota = [nome, nota]
    if nota >= 6:
        lista_aprovados.append(lista_nome_nota)
    if nota < 6:
        lista_reprovados.append(lista_nome_nota)
    
print(f"O(s) aprovado(s) é(são): {lista_aprovados}.")
print(f"E o(s) reprovado(s) é(são): {lista_reprovados}.")
