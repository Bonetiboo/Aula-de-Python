# Ex.13 - Solicite idade, se idade for maior ou igual a 18, crie uma estrutura de condição aninhada para verificar se idade é maior ou igual a 60, se for, mostre que é idoso, senão, mostre que é adulto. Se idade for maior ou igual a 12, mostre que é adolescente, caso contrário, criança.

idade = int(input("Digite a sua idade:"))

if (idade >= 18):
    if (idade >= 60):
        print("Você é idoso.")
    else:
        print("Você é adulto.")
else:
    if(idade >= 12):
        print("Você é adolescente.")
    else:
        print("Você é criança.")
