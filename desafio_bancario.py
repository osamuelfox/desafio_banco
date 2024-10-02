menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#Funcao de depositar

def depositando ():

    print(" Deposito ".center(30, '#'))
    print()

    deposito = float(input("Digite o valor que deseja depositar: "))

    if deposito > 0 and deposito < limite:

        global saldo,extrato
        saldo += deposito

        extrato +=  f"Depósito: R$ {deposito:.2f} ,saldo atual: R$ {saldo:.2f}\n"

        print("Operação realizada com sucesso!!!")

    else:

        print("Operação não realizada \nO valor deve ser maior que [0] ou menor que o limite de [500]")

    print()
    print("#".center(30, '#'))




#Funcao de saque

def sacando():

    print(" Saque ".center(30, '#'))
    print()

    global numero_saques,LIMITE_SAQUES,saldo,extrato,limite

    while numero_saques < LIMITE_SAQUES:

        valor_saque = float(input("Digite o valor a ser sacado: "))

        if valor_saque < saldo and valor_saque <= limite:

            saldo -= valor_saque
            numero_saques += 1

            extrato +=  f"Saque: R$ {valor_saque:.2f} ,saldo atual: R$ {saldo:.2f}\n"

            print("Saque realizado com sucesso!!!")

            return menu

        else:
            print("Saldo insuficiente ou quantia não pode ser superior a R$ 500.00")

            return menu

    else:
        print("Você atingiu o limete de saque diario") 


#Menu

while True:

    opcao = input(menu)

    if opcao == "d":
        print()
        depositando()

    elif opcao == "s":
        print()
        sacando()

    elif opcao == "e":
        print(" Extrato ".center(30, '#'))
        print()
        print(extrato)
    
    elif opcao == "q":
        break

    else:
        print("Operacao inalida, por favor selecione novamente a operacao desejada.")