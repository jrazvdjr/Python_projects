menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "d":
       valor = float(input("Deposite o valor que você deseja: "))
       if valor > 0:
           saldo += valor
           extrato += f"Depósito : R${valor:.2f}\n"
       else:
           print("Opreção falhou! Valor informado é inválido.")   

    
    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = saldo > limite

        excedeu_saques = numero_saques > LIMITE_SAQUES 

        if excedeu_saldo:
            print("Operação Falhou! Saldo indisponível.")

        elif excedeu_limite:
            print("Operação Falhou! Você excedeu o limite de saques")

        elif excedeu_saques:
            print("Operação Falhou! Número máximo de saques excedido") 

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"  
            numero_saques += 1 
        else:
            print("Valor informado é inválido!")             

    elif opcao == "e":
        print("====================Extrato====================")
        print("Não foi realizado nenhuma trasação" if not extrato else extrato)
        print(f"\n Saldo R$ {saldo:.2f}")
        print("=================================================")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação. ")    
