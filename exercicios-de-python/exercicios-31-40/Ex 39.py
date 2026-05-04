# Ex.39 - Crie um algoritmo usando while true para simular um menu iterativo. Se opção for "1": printe olá, se opção for igual a 2, print sair.

while True:
    opcao = int(input("Escolha a sua opção entre 1 e 2: "))
    if opcao == 1:
        print("Olá")
        break    
    if opcao == 2:
        print("Sair")
        break