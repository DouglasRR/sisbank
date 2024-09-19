def despositar():

    global saldo
    resp = 0

    while resp <= 0:
        resp = float(input("Qual o valor que deseja depositar? \nR: "))

        if not resp <= 0:
            saldo += resp
            transacoes.append(['deposito', resp])

def sacar():
    global LIMITE_DE_SAQUE
    global LIMITE_VALOR_SAQUE
    global saldo
    global saques
    resp = 1

    while resp != 0:
        resp = float(input("Qual o valor que deseja sacar? \nR: "))

        if not resp <= 0:
            if saques <= LIMITE_DE_SAQUE:
                if saques <= LIMITE_VALOR_SAQUE:
                    if resp > saldo:
                        print("Você tentou sacar mais do que tem no saldo. Tente novamente!")
                    else:
                        print(f"\nVocê sacou {saques}°vez, limite é {LIMITE_DE_SAQUE}.\n")
                        saques += 1
                        saldo -= resp
                        transacoes.append(['saque', resp])
                        resp = 0
                else:
                    print("Você só pode sacar até R$ 500,00.")
            else: 
                print("Você já atingiu o limite de saques hoje! Tente novamente amanhã.")
                break

def extrato():
    global transacoes
    global saldo

    print("-----EXTRATO-----")
    for count in range(0, len(transacoes)):
        print(f"{count} - {transacoes[count]}")

    print(f"Seu saldo é R$ {saldo}.")

LIMITE_DE_SAQUE = 3
LIMITE_VALOR_SAQUE = 500
saques = 1
saldo = 0
transacoes = []
usuario = 1

menu = '''
Seja bem vindo ao SisBank!

Qual operação deseja fazer?

[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

    '''

while usuario != 0:

    print(menu)
    print(f"SEU SALDO: R$ {saldo:.2f}")
    usuario = int(input("R: "))

    if usuario == 1:
        despositar()
    
    elif usuario == 2:
        if saldo <= 0:

            print("Você não tem saldo para saque!")

        else:
            sacar()

    elif usuario == 3:
        extrato()

    else:
        if not usuario == 0:
            print("Opção inválida, tente novamente!")
    
