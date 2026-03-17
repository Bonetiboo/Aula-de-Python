# Ex. 5 - Crie um algoritmo para solicitar a massa para o usuário e retorne a energia,
# dada a equação de Einstein para energia. E = mc²

m = float(input("Forneça a massa do corpo em kg:"))
e = m * 299792458 ** 2

print("A energia do corpo é:", e)