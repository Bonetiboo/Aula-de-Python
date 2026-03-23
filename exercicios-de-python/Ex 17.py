# Ex.17 - Crie um algoritmo para perguntar para o usuário qual o dia da semana, caso seja sábado, escreva "Dia de festa". Caso seja domingo, pergunte sobre a condição física do usuário, se estiver com dores de cabeça, printe "Recuperando, então, precisa descansar." Caso contrário, apenas descanse. Caso não seja sábado ou domingo, mostre "Trabalhando, trabalhando e trabalhando!"

dia = input("Qual o dia da semana?")

if (dia == "domingo"):
    dor = input("Como está a cabeça? (responda: com dor/sem dor):")
    if (dor == "com dor"):
        print("Recuperando, então descanse.")
    else:
        print("Apenas descanse então.")
elif (dia == "sábado"):
    print("Dia de festa.")
else:
    print("Trabalhando, trabalhando e trabalhando.")

    