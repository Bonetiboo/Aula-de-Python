# Ex.6 - Dada a equação a² = b² + c², solicite ao usuário o valor de a, c e calcule
# o valor de b

a = float(input("Forneça o valor da hipotenusa do triângulo:"))
c = float(input("Forneça o valor de um dos catetos do triângulo:")) 
b = ((a ** 2) - (c ** 2)) ** 0.5

print(f"O valor do outro cateto é: {b}")
