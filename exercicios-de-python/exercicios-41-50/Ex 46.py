# Ex.46 - Crie uma estrutura com try/except para converter temperatura celcius em fahrenheit. fahreinheit = (celcius * 9/5) + 32

try:
    tempc = float(input("Forneça a temperatura em celcius: "))
    tempf = (tempc * 9/5) + 32
    print(f"A temperatura em fahreinheit é: {tempf}")
except ValueError:
    print("O valor fornecido não é numérico")