# Ex.16 - Solicite valor e se a pessoa é vip ou não. Se valor maior ou igual a 200, crie estrutura de condição aninhada para verificar se a pessoa é vip, se for, ofereça 20% de desconto sobre o valor e mostre o valor a ser descontado e o valor final considerando o desconto. Se não for vip, ofereça o desconto de 10%.

valor = float(input("Digite o valor do produto:"))

if valor >= 200:
    (vip := input("Você é VIP? (responda com sim ou não):"))
    if vip == "sim":
        print(f"Você recebeu um desconto de 20%, ou seja {valor/5}, no total ficaria {valor - (valor/5)}")
    else:
        print(f"Você recebeu um desconto de 10%, ou seja {valor/10}, no total ficaria {valor - (valor/10)}")
else:
    print(f"Você não recebeu descontos e o valor total é {valor}.")
