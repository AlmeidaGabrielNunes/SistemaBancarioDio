saldo = 0 
limite = 500
LIMITE_SAQUE = 3
numero_saque = 0
extrato = ''

menu = """"
[1] Sacar 
[2] Depositar
[3] Extrato
[0] Sair
"""

while True:
    opcao = int(input(menu))
    if opcao == 1:
        saque = float(input("Quanto gostaria de sacar? "))
        if saque <= 500:
            if saque <= saldo and LIMITE_SAQUE > numero_saque:
                saldo -= saque
                numero_saque += 1
                extrato += f"Saque no valor de R${saque}.       Saldo: R${saldo}  \n" 
                print("Retire o valor no local indicado.")
            else:
                if saque > saldo:
                    print("Saldo insuficiente!!")
                else: 
                    print("Excedeu o limite de saques!")
        else:
            print("O limite máximo de saque é o valor de R$500,00")
    elif opcao == 2:
        deposito = float(input("Quanto gostaria de depositar?"))
        saldo += deposito
        extrato += f"Deposito no valor de R${deposito}.    Saldo: R${saldo} \n"
        print("Depósito realizado com sucesso!")
    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
    elif opcao == 0:
        break
    else:
        print("Valor de operaçõ inválido. Digite novamente")