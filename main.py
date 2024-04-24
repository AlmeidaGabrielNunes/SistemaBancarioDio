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


def criar_usuario(usuarios):
    cpf = input("Digite somente os numeros de seu CPF: \n") #problema de int é que desconsidera o 0. Então 098 será armazenado como 98.  
    usuario = filtrar_usuario(cpf, usuarios) #vai buscar a função filtrar_usuario, para confirmar se ja tem algum usuario com esse cpf
    if usuario:
        print(" \n  Este CPF já está vinculado à um usuário")
        return #return encerra a função aqui 
    nome = input("Digite seu nome completo: \n")
    nascimento = input("Digite sua data de nascimento(dd-mm-aaaa): \n")
    endereço = input("Digite seu endereço: \n")
    usuarios.append({"cpf": cpf, "nome": nome, "nascimento": nascimento, "endereço": endereço}) #está adicionando à lista usuarios o dicionario com dados do usuario
    print(" USUÁRIO CRIADO!!")
    
def filtrar_usuario(cpf, usuarios): #parametros são o cpf e a lista com os usuários, já que vai checar se o primeiro está dentro do segundo
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] #cria uma variavel para apresentar à pessoa, caso ja tenha criado um usuário. 
    # o for vai caminhar pela lista usuarios e se encontrar algum dicionario com o "cpf" igual ao cpf que estão tentando criar a conta, 
    return usuarios_filtrados[0] if usuarios_filtrados else None #aqui vai retornar o valor listado no usuarios_filtrados, caso tenha. se não, vai retornar "nada"


### A FUNÇÃO criar_usuario VAI CHAMAR A FUNÇÃO filtrar_usuario LOGO APÓS O USUARIO ENTRAR COM O CPF
### A VARIAVEL usuario CRIADO ALI, SÓ VAI TER UM VALOR CASO NO FILTRO TENHA ACHADO UM OUTRO USUARIO VINCULADO AO CPF
### É ISSO QUE ESTÁ SENDO CHECADO COM O IF. SE EXISTIR, ELE AVISA NA TELA E ENCERRA A FUNÇÃO, RETORNADO PARA O MENU

def criar_conta(usuario, numero_conta, agencia):
    numero_conta = numero_conta + 1
    agencia = agencia
    print("Conta Criada com Sucesso!!")
    return ({"usuario": usuario, "numero_conta": numero_conta, "agencia": agencia})


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

def main():
    saldo = 0 
    limite = 500
    LIMITE_SAQUE = 3
    numero_saque = 0
    registro_extrato = ''
    usuarios =[]
    contas = [] 
    AGENCIA = "0001"
    numero_conta = 0 

    menu = """"
    [1] Criar Usuário
    [2] Criar Conta
    [3] Sacar 
    [4] Depositar
    [5] Extrato
    [6] Verificar Contas
    [0] Sair
    """  

    while True:
        opcao = int(input(menu))
        if opcao == 1:
            criar_usuario(usuarios) #como parametro, está a lista onde serão armazenados os usuarios 
        elif opcao == 2:
            user = input("Digite seu CPF: \n")
            checagem =  [usuario for usuario in usuarios if usuario["cpf"] == user]
            if checagem:
                conta = criar_conta(checagem, numero_conta, AGENCIA)
                contas.append(conta)
            else:
                print("Precisa criar um usuário antes!")
        elif opcao == 3:
            valor = float(input("Quanto gostaria de sacar? "))
            saldo, registro_extrato, numero_saque = saque(saldo=saldo, valor=valor, numero_saque=numero_saque, LIMITE_SAQUE=LIMITE_SAQUE, registro_extrato=registro_extrato )
        elif opcao == 4:
            valor = float(input("Quanto gostaria de depositar?"))
            saldo, registro_extrato = depositar(saldo, valor, registro_extrato)
        elif opcao == 5:
            extrato(saldo, registro_extrato=registro_extrato)
        elif opcao == 6:
            print(contas)
        elif opcao == 0:
            break
        else:
            print("Valor de operaçõ inválido. Digite novamente")

main()