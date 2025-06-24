
def menu():


    menu = """
    ********** Menu **********

    [1]------------- Depositar
    [2]----------------- Sacar
    [3]--------------- Extrato
    [4]----------------- Saldo
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

    elif numero_saques >= LIMITE_SAQUES:
            print(" Número máximo de saques excedido ❌")

    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque Realizado com Sucesso ✅")

    else:
            print("O valor informado é inválido ❌")
       
    return saldo, extrato

def imprimir_extrato(saldo, /, *, extrato):
     print("\n================ 🧾EXTRATO  ================")
     print("Não foram realizadas movimentações." if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("==========================================")
    

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = menu()

    if opcao == "1":
        valor = float(input("Informe o valor do depósito R$: "))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "2":
        
        valor = float(input("Informe o valor do saque R$: "))
        
        saldo, extrato = sacar( saldo=saldo,valor=valor, extrato=extrato,limite=limite,
                               numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        

    elif opcao == "3":
         
         imprimir_extrato(saldo, extrato=extrato)
       
    elif opcao == "4":
         print("\n========= Saldo==========")
         print()
         print(f"Saldo da Conta R$:{saldo:.2f}")
         print()
         print("===========================")

    elif opcao == "0":

        break
    
    else:
        print("Por favor selecione novamente a operação desejada.")

