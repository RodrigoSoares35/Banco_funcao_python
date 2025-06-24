
def menu():


    menu = """
    ********** Menu **********
    [1]-----------Novo usuário
    [2]-------------Nova conta
    [3]------------- Depositar
    [4]----------------- Sacar
    [5]--------------- Extrato
    [6]----------------- Saldo
    [7]----------Listar contas
    [0]------------------ Sair

    **************************
    Escolha: """
    return input((menu))
   

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print()
        print("Deposito Realizado com Sucesso ✅")
    else:
         print("Valor inválido ❌")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > saldo:
            print("Você não tem saldo suficiente!❌")

    elif valor > limite:
            print(" O valor do saque excede o limite ❌")
        
    elif numero_saques >= limite_saques:
            print(" Número máximo de saques excedido ❌")
    
    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque Realizado com Sucesso ✅")


    else:
            print("O valor informado é inválido ❌")
       
    return saldo, extrato, numero_saques

def imprimir_extrato(saldo, /, *, extrato):
     print("\n================ 🧾EXTRATO  ================")
     print("Não foram realizadas movimentações." if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("==========================================")

def imprimir_saldo(saldo):
     
     print("\n========= Saldo==========")
     print()
     print(f"Saldo da Conta R$:{saldo:.2f}")
     print()
     print("===========================")   

def novo_usuario(usuarios):
    cpf = input("Informe o CPF, Ex:12345678900:\n")
    usuarios = consultar_usuario(cpf, usuarios)

    if usuarios:
        print("Usuário já Cadastrado!")
        return

    nome = input("Informe o nome completo:\n")
    data_nascimento = input("Informe a data de nascimento Ex: dd-mm-aaaa:\n")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado):\n")

    lista_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("----Dados Cadastrados---------")
    print(f"Nome:{nome} \n Data de Nascimento:{data_nascimento} \n Endereço:{endereco}")
    print()
    print("Usuário criado com sucesso!✅")

def consultar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    print("-------Lista de Contas----------")
    print()
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("-------------------------")
        print(linha)
       
       
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário:\n")
    usuario = consultar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso! ✅")
        return {"agencia": agencia,"numero_conta": numero_conta,"usuario": usuario}

    print("\nUsuário não encontrado ")



saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_usuarios = []
lista_contas = []
AGENCIA = "0001"

while True:

    opcao = menu()
    
    if opcao == "1":
           novo_usuario(lista_usuarios)
    
    elif opcao == "2":
          numero_conta = len(lista_contas) + 1
          conta = criar_conta(AGENCIA, numero_conta, lista_usuarios)

          if conta:
                lista_contas.append(conta)

    elif opcao == "3":
        valor = float(input("Informe o valor do depósito R$:\n"))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "4":
        
        valor = float(input("Informe o valor do saque R$:\n"))
        
        saldo, extrato, numero_saques = sacar( saldo=saldo,valor=valor, extrato=extrato,limite=limite,
                               numero_saques=numero_saques, limite_saques=LIMITE_SAQUES )
        

    elif opcao == "5":
         
         imprimir_extrato(saldo, extrato=extrato)
       
    elif opcao == "6":
         
         imprimir_saldo(saldo)

    elif opcao == "7":
        listar_contas(lista_contas)
       
    elif opcao == "0":

       break
    
    else:
        print("Por favor selecione novamente a operação desejada.")

