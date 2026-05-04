# Ex.26 - Crie um algoritmo para simular um sistema de compras, onde deverá ser solicitado nome 100 vezes. Após isso, crie uma estrutura para quebrar a solicitação de nomes. Após isso, crie uma estrutura para solicitar o preço, com isso, deixe o respectivo nome e preço juntos. Finalmente, mostre o valor total. Finalmente mostre o valor total dos produtos.

lista_produtos = []
valor_total = 0

for i in range(100):
    produto = input("Forneça o nome do produto (caso não haja mais produtos digite 'acabou'): ")
    if produto == "acabou":
        break
    valor = float(input("Forneça o valor do produto: "))
    lista_produtos.append(produto)
    lista_produtos.append(valor)
    valor_total += valor

print(f"Os produtos e seus respectivos preços são: {lista_produtos}")
print(f"Valor final da compra: {valor_total}")