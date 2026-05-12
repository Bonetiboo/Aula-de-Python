# Ex.51 - Crie um algoritmo para solicitar temperatura em celsius e transformar em fahrenheit.

def conversao_de_temp (a):
    tempc = a
    tempf = (tempc * 9/5) + 32
    return tempf

print(conversao_de_temp(-40))