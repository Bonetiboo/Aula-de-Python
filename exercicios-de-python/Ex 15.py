# Ex.15 - Solicite número e verifique se é maior do que zero, se for, crie uma estrutura de condição aninhada para verificar se este número é par, se for, printe positivo e par. Se não for, positivo e ímpar. Se número for igual a zero, printe zero.  Caso contrário, negativo.

numero = int(input("Digite qualquer número inteiro:"))

if (numero > 0):
    if (numero % 2 == 0):
        print("Seu número é par e positivo.")
    else:
        print("Seu número é ímpar e positivo.")
elif (numero == 0):
    print("Seu número é 0.")
else:
    print("Seu número é negativo.")
    