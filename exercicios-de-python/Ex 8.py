# Ex. Desafio - Para a equação de 2º abaixo, determine os valores de x1 e x2:
# 10x² + 3x +1

a = 10
b = 3
c = 1

delta = (b**2) - (4 * a * c)
x1 = ((((-1 * b) + (delta ** 0.5))) / (2*a))
x2 = ((((-1 * b) - (delta ** 0.5))) / (2*a))

print(x1)
print(x2)