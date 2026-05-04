# Ex.42 - Crie um algoritmo com lista de notas válidas. Se -1, para a estrutura, se nota < 0 ou nota > 10, continue. Ao final, calcule a média das notas.

lista_notas = []
soma = 0

while True:
    nota = int(input("Digite a nota (caso já tenha colocado todas digite '-1'): "))
    if nota == -1:
        break
    elif nota < 0 or nota > 10:
        continue
    else:
        lista_notas.append(nota)
        print(lista_notas)
        soma += nota

media = soma / len(lista_notas)
print(f"A média das notas é: {media}")
