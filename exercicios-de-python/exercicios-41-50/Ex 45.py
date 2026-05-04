# Ex.45 - Crie um programa ao qual ao selecionar opção 1, solicitar e enviar nomes para uma lista_nomes, opção 2, solicitar e enviar cpfs para uma lista_cpfs e ao digitar opção 3, solicitar e enviar idade para a lista_idade. Crie também uma estrutura para juntar todas as listas.

lista_nomes = []
lista_cpfs = []
lista_idade = []
lista_total = [lista_nomes, lista_cpfs, lista_idade]

while True:
    opcao = input("Digite entre 'NOME', 'CPF', 'IDADE' ou 'SAIR': ")
    if opcao == "NOME":
        nome = input("Digite o nome: ")
        lista_nomes.append(nome)
    if opcao == "CPF":
        cpf = int(input("Digite seu CPF: "))
        lista_cpfs.append(cpf)
    if opcao == "IDADE":
        idade = int(input("Digite sua idade: "))
        lista_idade.append(idade)
    if opcao == "SAIR":
        break
    print(lista_total)