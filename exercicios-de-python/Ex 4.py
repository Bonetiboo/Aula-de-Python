# Ex. 4 - Crie um algoritmo para solicitar a distância e tempo para o usuário e
# retorne a velocidade média em km/h

d = float(input("Forneça a distância percorrida em metros:"))
t = float(input("Forneça o tempo utilizado para percorrer a distância em segundos:"))

ms = d / t 
kmh = ms * 3.6

print("A velocidade média em km/h é:", kmh)