# Ex. 7 Crie uma estrutura para solicitar nome, sobrenome, cpf, endereço e cep
# para o usuário. Ao final, retorne: a) Nome completo b) Nome completo e CPF
# Endereço e CPF

nome = input("Insira seu nome:")
sobrenome = input ("Insira seu sobrenome:")
cpf = int(input("Forneça seu CPF:"))
end = input("Forneça seu endereço:")
n_end = int(input("Forneça o número do endereço:"))
cep = int(input("Forneça seu CEP:"))
nome_completo = nome + " " + sobrenome


print(f"Nome completo: {nome_completo}")
print(f"Nome completo e CPF: {nome_completo} e {cpf}")
print(f"Endereço e CPF: {end} e {cpf}")
