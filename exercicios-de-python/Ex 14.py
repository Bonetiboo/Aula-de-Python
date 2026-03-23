# Ex.14: Solicite nota, se nota for maior ou igual a 6, crie condição aninhada para verificar se nota é maior ou igual a 9, se for, aprovado com excelência. Caso nota não for maior ou igual a 9, Aprovado. Caso contrário, reprovado.

nota = float(input("Forneça a nota obtida:"))

if (nota >= 6):
    if (nota >= 9):
        print("Aprovado com excelência.")
    else:
        print("Aprovado")
else:
    print("Reprovado.")