# Ex.18 - Crie um algoritmo para solicitar a escolha do menu do café da manhã. Opções: ovos, panquecas, wafles e frutas.
# Acompanhamentos: bacon, queijo, pão, presunto, manteiga e limão. Tipos de frutas: abacaxi, maçã, banana e uvas.

opção = input(
    "Qual a sua opção de café da manhã? As opções são: ovo, panqueca, wafle e frutas. O que deseja? "
)

ovo = "ovo"
panqueca = "panqueca"
wafle = "wafle"
bacon = "bacon"
queijo = "queijo"
pão = "pão"
presunto = "presunto"
manteiga = "manteiga"
limão = "limão"
abacaxi = "abacaxi"
maca = "maçã"
banana = "banana"
uva = "uvas"
frutas = "frutas"

if opção == "ovo":
    acompanhamento = input(
        "Qual acompanhamento gostaria para seu ovo? As opções são: bacon, queijo, pão e presunto. O que deseja? "
    )
    if acompanhamento == bacon:
        print("O cliente gostaria de ovo com bacon.")
    elif acompanhamento == queijo:
        print("O cliente gostaria de ovo com queijo.")
    elif acompanhamento == pão:
        print("O cliente gostaria de pão com ovo.")
    elif acompanhamento == presunto:
        print("O cliente gostaria de ovo com presunto.")
    else:
        print("O cliente prefere ovo sem acompanhamentos.")
elif opção == panqueca:
    print("O cliente quer panquecas.")
elif opção == wafle:
    print("O cliente quer wafles.")
elif opção == frutas:
    tiposDeFrutas = input(
        "Qual tipo de fruta gostaria? As opções são: abacaxi, maçã, banana e uvas. O que deseja? "
    )
    if tiposDeFrutas == abacaxi:
        print("O cliente gostaria de abacaxi.")
    elif tiposDeFrutas == maca:
        print("O cliente gostaria de maçã.")
    elif tiposDeFrutas == banana:
        print("O cliente gostaria de banana.")
    else:
        print("O cliente gostaria de uvas.")
else:
    print("O cliente não quer café da manhã.")
