# Ex.23 - Crie uma estrutura para solicitar 10 números para o usuário. Após isso crie duas listas (par e ímpar) e insira os valores pares na lista par, valores ímpares na lista ímpar. Print a lista completa, lista par e lista ímpar.

lista_par = []
lista_impar = []
lista_completa = []

for i in range (10):
    numero = float(input("Digite um número: "))
    if numero %2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
    lista_completa.append(numero)

print(f"Lista completa: {lista_completa}")
print(f"Lista impar: {lista_impar}")
print(f"Lista par: {lista_par}")