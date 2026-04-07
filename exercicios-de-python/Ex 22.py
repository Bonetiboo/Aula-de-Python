# Ex.22 - Crie um algoritmo para solicitar 5 valores não inteiros, insira em uma lista. Após isso, crie uma estrutura para somar e retornar a média dos elementos desta lista.

soma = 0
valores = []

for i in range (5):
    valor = float(input("Digite um valor: "))
    valores.append(valor)
    print(valores)

    soma += valor # vai somando o valor diretamente na soma
    print(soma)

média = soma / len(valores)

print(média)
