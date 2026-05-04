# Ex.41 - Crie um algoritmo para solicitar nome, porém, mande apenas os nomes com caracteres >= 3 para a lista de nomes.

lista_nomes = []

while True:
    nome = input("Digite um nome: ")
    if len(nome) >= 3:
        lista_nomes.append(nome)
        print(lista_nomes)