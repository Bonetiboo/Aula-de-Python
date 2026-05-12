# Crie uma estrutura para solicitar o tipo de figura geométrica, após isso, mostre como calcular a área e o perímetro de cada figura geométrica.

print("Caso algum parâmetro não exista, digite 1.")

def calcular_area(figura, a, b, c):
    match (figura):
        case 'círculo':
            area = 2*3.14*a*b*c
            return  area
        case 'quadrado':
            area = a*b*c
            return area
        case 'retângulo':
            area = a*b*c
            return area
        case 'trapézio':
            area = ((a+b) * c) / 2
            return area
        case 'triângulo':
            area = (a*b*c) / 2
            return area
        
print(f'A área é: {(calcular_area((input("Forneça a figura geométrica: ")), (float(input("Forneça a base/base maior/raio: "))), (float(input("Forneça a altura/base menor: "))), (float(input("Forneça a altura: ")))))}')

def calcular_perimetro(figura, a, b, c, d):
    match (figura):
        case 'círculo':
            perimetro = 2*3.14*a*b*c*d
            return  perimetro
        case 'quadrado':
            perimetro = a + b + c + d
            return perimetro
        case 'retângulo':
            perimetro = a + b + c + d
            return perimetro
        case 'trapézio':
            perimetro = a + b + c + d
            return perimetro
        case 'triângulo':
            perimetro = (a + b + c) * d
            return perimetro
        
print(f'O perímetro é: {(calcular_perimetro((input("Forneça a figura geométrica: ")), (float(input("Forneça o primeiro lado: "))), (float(input("Forneça o segundo lado: "))), (float(input("Forneça o terceiro lado: "))), (float(input("Forneça o quarto lado: ")))))}')