# Ex.44 - Filtrar palavras com letra proibida. Se aparecer palavras com x, não mostrar palavra na lista.

lista = []

while True:
    palavra = input("Digite uma palavra que não contenha x, se conter x, não aparecerá na lista: ")
    if "x" in palavra:
        continue
    else:
        lista.append(palavra)
        print(lista)