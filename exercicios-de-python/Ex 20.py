# Ex.20 - Crie um programa que imprima quais são os números pares de 1 à 50 e calcule a soma dos valores pares.

soma = 0

for n150 in range (0, 51):
    if n150 %2 == 0:
        print(f"O número {n150} é par.")
    else:
        continue
    soma += n150
print(soma)