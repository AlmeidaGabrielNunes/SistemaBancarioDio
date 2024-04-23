#Transformar sacar, extrato  e depositar em funções. Também precisamos criar usario e criar conta corrente (vinculando com o usuario). 

#função saque deve receber os argumentos aponas por nome (keyword only). SUgestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_asques. Sugestão
#de retorno: saldo e extrato. 

#funçao deposito deve receber os argumentos por posição; Argumentos sugeridos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato
#funçao extrato deve receber por posição e por nome. Arugmentos posiconais: saldo. Arugmentos nomeados: extrato

#criar usuário: o programa deve criar uma lista para guardar as info. nome, data de nascimento, cpf e edenreço. O enderçeo é uma string. Deve ser amarzenado somente os numeros do cpf.
#n podemos cadastrar 2 usaurios com o mesmo cpf. 

#criar conta corrente: composta por agencia, numero da conta e usuario. O numero da conta é sequencia, niciando em 1. O unumero da agencia é fixo 0001. O Usuario pode ter mais de uma conta
#mas uma conta pertence a somente um usuario
#um usuario pode ter mais de uma conta

#Dica: fitlre a lista de usaurios busncado o numero do cpf informado para cada usuario da lista. 

saldo = 0 
limite = 500
LIMITE_SAQUE = 3
numero_saque = 0
registro_extrato = ''

def saque(*, saldo, valor, numero_saque, LIMITE_SAQUE, registro_extrato):
    if valor <= 500:
            if valor <= saldo and LIMITE_SAQUE > numero_saque:
                saldo -= valor
                numero_saque += 1
                registro_extrato += f"Saque no valor de R${valor}.  \n" 
                print("Retire o valor no local indicado.")
            else:
                if valor > saldo:
                    print("Saldo insuficiente!!")
                else: 
                    print("Excedeu o limite de saques!")
    else:
            print("O limite máximo de saque é o valor de R$500,00")
    return saldo, registro_extrato, numero_saque


def depositar(saldo, valor, registro_extrato, /):
    saldo += valor
    registro_extrato += f"Deposito no valor de R${valor}.\n"
    print("Depósito realizado com sucesso!")
    return saldo, registro_extrato

def extrato(saldo,/, *, registro_extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not registro_extrato else registro_extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")





menu = """"
[1] Sacar 
[2] Depositar
[3] Extrato
[0] Sair
"""

while True:
    opcao = int(input(menu))
    if opcao == 1:
        valor = float(input("Quanto gostaria de sacar? "))
        saldo, registro_extrato, numero_saque = saque(saldo=saldo, valor=valor, numero_saque=numero_saque, LIMITE_SAQUE=LIMITE_SAQUE, registro_extrato=registro_extrato )
    elif opcao == 2:
        valor = float(input("Quanto gostaria de depositar?"))
        saldo, registro_extrato = depositar(saldo, valor, registro_extrato)
    elif opcao == 3:
        extrato(saldo, registro_extrato=registro_extrato)
    elif opcao == 0:
        break
    else:
        print("Valor de operaçõ inválido. Digite novamente")