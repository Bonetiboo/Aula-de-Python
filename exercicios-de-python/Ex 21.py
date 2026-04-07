# Ex.21 - Escreva um programa que identifique quais valores são ímpares em uma range de 1 a 51 e calcule a média destes valores.

soma = 0

for n151 in range (0, 52):
    if n151 %2 != 0:
        print(f"O número {n151} é impar")
    soma += n151

média = soma/26

print(média)