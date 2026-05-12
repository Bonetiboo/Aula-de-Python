# Ex.50 - Crie uma estrutura com match/case e while, comando = sair - saindo da estrutura. Case = sair - encerrando. Case qualquer outra coisa - comando inválido

while True:
    comando = input("Insira o comando: ")
    match comando:
        case 'sair':
            print('Encerrando...')
            break
        case _:
            print('Comando inválido.')