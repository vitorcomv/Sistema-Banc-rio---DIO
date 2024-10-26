menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[Q] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu).strip().upper()
    
    if opcao == "1":
        deposito = float(input("Digite o valor do depósito: "))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("Depósito realizado com sucesso!")
            print(f"Saldo atual: R${saldo:.2f}")
        else:
            print("Erro! O valor do depósito precisa ser maior que zero.")
        
    elif opcao == "2":
        
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saque diário atingido. Aguarde o próximo dia útil!")
        else:
            saque = float(input("Digite o valor do saque: "))
        
            if saque > 0 and saque <= saldo and saque <= limite:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!")
                print(f"Saldo atual: R${saldo:.2f}")
            elif saque > limite:
                print("Erro! O valor do saque excede o limite de R$500. Tente um valor menor.")
            else:
                print("Erro! Saldo insuficiente para saque.")
            
        
    elif opcao == "3":
        print("\n================== Extrato ==================")
        
        if extrato:
            print(extrato)
        else:
            print("Nenhuma transação realizada.")
        print(f"Saldo atual: R$ {saldo:.2f}\n")
        print("===============================================")
        
    elif opcao == "Q":
        print("Saindo... Obrigado por utilizar nosso sistema.")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")