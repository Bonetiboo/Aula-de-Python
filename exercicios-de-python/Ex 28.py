# Ex.28 - Crie um algoritmo para simular sistemas com menu. O usuário pode cadastrar, listar ou sair da estrutura. 
# 
# Se opção 1, solicite nome, idade, cidade e deixe estas informações em uma estrutura de lista dentro de lista. 
# Se opção 2, printe o respectivo nome, idade e cidade da pessoa.
# Se opção 3, crie uma estrutura para sair do código.

lista_total = []

for i in range (100):
    menu = input("Deseja cadastrar, listar ou sair? ")
    if menu == "cadastrar":
        for k in range (1):
            nome = input("Forneça seu nome: ")
            idade = int(input("Forneça sua idade: "))
            cidade = input("Forneça a cidade em que você mora: ")
            lista_pessoal = [nome, idade, cidade]
            lista_total.append(lista_pessoal)
            break
    elif menu == "listar":
        print(f"A lista atual de usuários é: {lista_total}")
    else:
        print("Volte sempre.")
        break
