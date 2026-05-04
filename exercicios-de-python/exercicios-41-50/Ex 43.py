# Ex.43 - Crie um sistema com menu simples. 1 - adicionar número, 2 - remover o número anterior, 3 - mostrar lista, 4 - sair

lista = []

while True:
    opcao_menu = int(input("Digite uma opção do menu entre 1, 2, 3 e 4: "))
    if opcao_menu == 1:
        numero = int(input("Digite um número para ser adicionado à lista: "))
        lista.append(numero)
    if opcao_menu == 2:
        lista.pop()
    if opcao_menu == 3:
        print(lista)
    if opcao_menu == 4:
        break