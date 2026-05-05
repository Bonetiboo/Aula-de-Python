# Ex.47 - Crie uma estrutura com try/except a qual calcule e traga um erro para calcular a área de um retângulo e círculo com estrutura de input para o usuário. Além disso, o usuário deve escolher a figura geométrica.

try:
    area = int(input("Digite 1 para retângulo e 2 para círculo: "))
    if area == 1:
        base = float(input("Forneça o tamanho da base: "))
        altura = float(input("Forneça a altura: "))
        arear = base * altura
        print(f"A área do retângulo é: {arear}")
    elif area == 2:
        raio = float(input("Forneça o raio: "))
        areac = 3.14 * raio ** 2
        print(f"A área do círculo é: {areac}")
except ValueError:
    print("O valor fornecido não é válido.")