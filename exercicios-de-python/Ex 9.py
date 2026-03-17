# Ex.9 - Crie um algoritmo para solicitar nome, sobrenome e cpf para o usuário. Se o nome e sobrenome estiver correto, mostre que será verificado o cpf, se nome, sobrenome e cpf estiverem corretos, mostre acesso VIP permitido, se nome ou sobrenome e cpf estiverem corretos mostre que será verificado. Qualquer outra condição, acesso VIP negado.

nome = input("Insira seu nome:")
sobrenome = input("Insira seu sobrenome:")
cpf = input("Insira seu CPF:")

if nome == "Rafael" and sobrenome == "Boneti" and cpf == "10010010010":
    print("Acesso VIP permitido.")

elif nome == "Rafael" or sobrenome == "Boneti" and cpf == "10010010010":
    print("Acesso será verificado manualmente.")

else:
    print("Acesso negado.")