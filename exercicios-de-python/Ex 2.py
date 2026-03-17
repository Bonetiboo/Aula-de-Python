# Média final de notas

a = str(input("Nome do aluno:"))

n1t1 = float(input("Forneça a primeira nota do primeiro trimestre:"))
n2t1 = float(input("Forneça a segunda nota do primeiro trimestre:"))
n3t1 = float(input("Forneça a terceira nota do primeiro trimestre:"))

n1t2 = float(input("Forneça a primeira nota do segundo trimestre:"))
n2t2 = float(input("Forneça a segunda nota do segundo trimestre:"))
n3t2 = float(input("Forneça a terceira nota do segundo trimestre:"))

n1t3 = float(input("Forneça a primeira nota do terceiro trimestre:"))
n2t3 = float(input("Forneça a segunda nota do terceiro trimestre:"))
n3t3 = float(input("Forneça a terceira nota do terceiro trimestre:"))

m = (((n1t1 + n2t1 + n3t1) / 3) + ((n1t2 + n2t2 + n3t2) / 3) + ((n1t3 + n2t3 + n3t3) / 3)) / 3

print("A média final do aluno", a, "é", m)