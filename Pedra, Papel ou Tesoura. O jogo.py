import random
#Ta travando muito,so quero fazer um jogo de pedra,papel e tesoura
escolhas_computador = ["pedra", "papel", "tesoura"]
sair = False
while sair != 'sair':
    resultadopc = random.choice(escolhas_computador)
    sair = usuario = input("Escolha entre 'pedra', 'papel' ou 'tesoura' ou digite 'sair' para sair.")
    print("Computador escolheu:", resultadopc)
    print("Voce escolheu:", usuario)
    if usuario == resultadopc:
        print("EMPATE!")
    elif usuario == 'pedra' and resultadopc == 'tesoura':
        print("VOCE GANHOU!!")
    elif usuario == 'papel' and resultadopc == 'pedra':
        print("VOCE GANHOU!!")
    elif usuario == 'tesoura' and resultadopc == 'papel':
        print("VOCE GANHOU!!")
    else:
           print("COMPUTADOR GANHOU!")
input()