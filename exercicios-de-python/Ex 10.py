# Ex.10 - Cálculo de desconto do INSS. Solicite o salário para o usuário e retorne o valor a ser descontado e o valor a ser recebido. 

# Faixa Salarial (R$)         Alíquota (%)                Parcela a Deduzir (R$)
# Até 1621                       7,%                             -
# 1621 à 2092,84                 9,0%                             24,32
# 2092,84 à 4354,27              12,0%                            111,40
# 4354,27 à 8475,55              14,0%                            198,49

salario = float(input("Insira seu salário:"))
d1 = 0 
d2 = 24.32
d3 = 111.40
d4 = 198.49
c1 = salario - d1
c2 = salario - d2
c3 = salario - d3
c4 = salario - d4

if salario <= 1621:
    print(f"O desconto será de R$0,00 e o salário recebido será {c1}")
elif salario > 1621 and salario <= 2092.84:
    print(f"O desconto será de R$24,32 e o salário recebido será {c2}")
elif salario > 2092.84 and salario <= 4354.27:
    print(f"O desconto será de R$111,40 e o salário recebido será {c3}")
elif salario > 4354.27 and salario <= 8475.55:
    print(f"O desconto será de R$198,49 e o salário recebido será {c4}")
else:
    print("O desconto será contado manualmente.")