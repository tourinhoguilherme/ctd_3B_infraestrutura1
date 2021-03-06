# encoding:UTF-8
import random
import sys

userScore = 0
pcScore = 0
totalScore = 0
winUser = 0
winPc = 0
tie = 0


def get_int():
    userdata = input("Digite um número, ou 's' para sair do programa ")
    if userdata == 's':
        print("Nos vemos!")
        sys.exit()
    try:
        user_num = int(userdata)
        return user_num
    except ValueError:
        print("Precisa de um número para continuar: ")
        return(get_int())


def percent():
    if totalScore > 0:
        x = ((totalScore - pcScore) / totalScore) * 100
        return x
    elif totalScore == 0:
        x = 0
        return x


while True:
    aleatorio = random.randrange(0, 5)
    escolhaPc = ""
    again = ""
    print("1)Pedra")
    print("2)Papel")
    print("3)Tesoura")
    print("4)Lagarto")
    print("5)Spock")
    print("6)Show Scores")
    opcao = get_int()

    if opcao == 1:
        escolhaUsuario = "pedra"
    elif opcao == 2:
        escolhaUsuario = "papel"
    elif opcao == 3:
        escolhaUsuario = "tesoura"
    elif opcao == 4:
        escolhaUsuario = "lagarto"
    elif opcao == 5:
        escolhaUsuario = "spock"
    elif opcao == 6:
        print("Pontuações: ")
        print("Usuário: ", userScore)
        print("Pc: ", pcScore)
        print("Empates:", tie)
        print("Porcentagem de vitórias: ", percent(), "% ")
        break
    else:
        print("Opção Invalida")
        continue

    print("Você escolheu: ", escolhaUsuario)

    if aleatorio == 0:
        escolhaPc = "pedra"
    elif aleatorio == 1:
        escolhaPc = "papel"
    elif aleatorio == 2:
        escolhaPc = "tesoura"
    elif aleatorio == 3:
        escolhaPc = "lagarto"
    elif aleatorio == 4:
        escolhaPc = "spock"
    print("PC escolheu: ", escolhaPc)
    print("...")

    if escolhaPc == "pedra" and escolhaUsuario == "papel":
        print("Ganhou, papel cobre pedra")
        winUser += 1
    elif escolhaPc == "papel" and escolhaUsuario == "tesoura":
        print("Ganhou, tesoura corta papel")
        winUser += 1
    elif escolhaPc == "tesoura" and escolhaUsuario == "pedra":
        print("Ganhou, pedra amassa tesoura")
        winUser += 1
    elif escolhaPc == "lagarto" and escolhaUsuario == "pedra":
        print("Ganhou, pedra esmaga a lagarto")
        winUser += 1
    elif escolhaPc == "lagarto" and escolhaUsuario == "tesoura":
        print("Ganhou, tesoura decapita a Lagarto")
        winUser += 1
    elif escolhaPc == "tesoura" and escolhaUsuario == "spock":
        print("Ganhou, Spock quebra tesoura")
        winUser += 1
    elif escolhaPc == "spock" and escolhaUsuario == "lagarto":
        print("Ganhou, lagarto envenena a Spock")
        winUser += 1
    elif escolhaPc == "papel" and escolhaUsuario == "lagarto":
        print("Ganhou, lagarto come papel")
        winUser += 1
    elif escolhaPc == "spock" and escolhaUsuario == "papel":
        print("Ganhou, papel refuta a Spock")
        winUser += 1
    elif escolhaPc == "pedra" and escolhaUsuario == "spock":
        print("Ganhou, Spock vaporiza pedra")
        winUser += 1
    elif escolhaUsuario == "pedra" and escolhaPc == "papel":
        print("Perdeu, papel cobre pedra")
        winPc += 1
    elif escolhaUsuario == "papel" and escolhaPc == "tesoura":
        print("Perdeu, tesoura corta papel")
        winPc += 1
    elif escolhaUsuario == "tesoura" and escolhaPc == "pedra":
        print("Perdeu, pedra amassa tesoura")
        winPc += 1
    elif escolhaUsuario == "lagarto" and escolhaPc == "pedra":
        print("Perdeu, pedra esmaga a lagarto")
        winPc += 1
    elif escolhaUsuario == "lagarto" and escolhaPc == "tesoura":
        print("Perdeu, tesoura decapita a Lagarto")
        winPc += 1
    elif escolhaUsuario == "tesoura" and escolhaPc == "spock":
        print("Perdeu, Spock quebra tesoura")
        winPc += 1
    elif escolhaUsuario == "spock" and escolhaPc == "lagarto":
        print("Perdeu, lagarto envenena a Spock")
        winPc += 1
    elif escolhaUsuario == "papel" and escolhaPc == "lagarto":
        print("Perdeu, lagarto come papel")
        winPc += 1
    elif escolhaUsuario == "spock" and escolhaPc == "papel":
        print("Perdeu, papel refuta a Spock")
        winPc += 1
    elif escolhaUsuario == "pedra" and escolhaPc == "spock":
        print("Perdeu, Spock vaporiza pedra")
        winPc += 1
    elif escolhaPc == escolhaUsuario:
        print("Empate")
        tie += 1

    while again == "":
        again = input("Vamos jogar de novo? s/n: ")
        if 's' in again:
            print("Usuário: ", userScore)
            print("Pc: ", pcScore)
            print("Empates:", tie)
            break
        elif 'n' in again:
            print("Nos vemos!")
            sys.exit()
        else:
            print("Valor Invalido")
            again = ""
            continue

    userScore = userScore + winUser
    pcScore = pcScore + winPc
    totalScore = userScore + pcScore + tie
