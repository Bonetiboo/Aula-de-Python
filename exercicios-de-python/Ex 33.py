# Ex.33 - Crie um programa que solicite 5 números inteiros e decremente os valores inseridos pelo usuário.

i = 0
decrementoTotal = 0

while i < 5:
    numeros = int(input("Forneça um número: "))
    decrementoTotal -= numeros
    print(f"O decremento total atual é: {decrementoTotal}") 