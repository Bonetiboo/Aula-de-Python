# Ex.35 - Crie uma estrutura que solicite itens de compra de forma que só seja possível sair da estrutura de repetição, caso o usuário digite sair. Coloque os itens em uma lista.

listaDeCompras = []

produto = input("Digite o produto (caso não haja mais produtos digite 'sair'): ")

while produto != "sair":
    produto = input("Digite o próximo produto: ")
    listaDeCompras.append(produto)

print(listaDeCompras)