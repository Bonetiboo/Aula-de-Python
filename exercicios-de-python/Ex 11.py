# Ex.11 - Classificação de crédito: solicite renda mensal e score de crédito.
# Crie as seguintes regras:

# Aprovado - renda => 3000 and score >= 700
# Análise manual - renda => 2000 and score >= 600 
# Caso constrário - Negado

rm = float(input("Insira sua renda mensal:"))
sc = float(input("Insira seu score de crédito:"))

if rm >= 3000 and sc >= 700:
    print("Aprovado.")
elif rm >= 2000 and sc >= 600:
    print("Uma análise manual será realizada.")
else:
    print("Negado.")

