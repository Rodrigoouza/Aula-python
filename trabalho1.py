# Dados de Login
senha_correta = "P@$$w0rd"
login_sucesso = False
saldo = 2500.00  
 
print("=== FASE 1: VALIDAÇÃO DE ACESSO ===")
 
 
for tentativa in range(1, 4):
    senha_digitada = input("Digite a senha de acesso: ")
   
    if senha_digitada == senha_correta:
        print("\nBem-vindo ao sistema! Acesso concedido.")
        login_sucesso = True
        break  
       
   
    tentativas_restantes = 3 - tentativa
   
    if tentativas_restantes > 0:
        print(f"Senha incorreta! Restam {tentativas_restantes} tentativa(s).")
        continue  
    else:
        print("Acesso Bloqueado!")
 
 
if login_sucesso:
    while True:
        print("\n" + "="*25)
        print("     MENU PRINCIPAL     ")
        print("="*25)
        print("1: Exibir Saldo")
        print("2: Depositar")
        print("3: Sacar")
        print("4: Sair")
        print("-"*25)
       
        opcao = input("Escolha uma opção: ")
       
        if opcao == "1":
            print(f"\n[Saldo] Seu saldo atual é: R$ {saldo:.2f}")
           
        elif opcao == "2":
            try:
                valor_deposito = float(input("\nDigite o valor que deseja depositar: R$ "))
                if valor_deposito > 0:
                    saldo += valor_deposito  
                    print(f"[Depósito] R$ {valor_deposito:.2f} depositados com sucesso!")
                else:
                    print("[Erro] O valor do depósito deve ser maior que zero.")
            except ValueError:
                print("[Erro] Por favor, digite um valor numérico válido.")
               
        elif opcao == "3":
            try:
                valor_saque = float(input("\nDigite o valor que deseja sacar: R$ "))
                if valor_saque > 0:
                    if valor_saque <= saldo:
                        saldo -= valor_saque  
                        print(f"[Saque] R$ {valor_saque:.2f} retirados com sucesso!")
                    else:
                        print(f"[Erro] Saldo insuficiente! Seu saldo atual é de R$ {saldo:.2f}")
                else:
                    print("[Erro] O valor do saque deve ser maior que zero.")
            except ValueError:
                print("[Erro] Por favor, digite um valor numérico válido.")
               
        elif opcao == "4":
            print("\nSaindo... Obrigado por utilizar o nosso sistema!")
            break  
           
        else:
            print("\nOpção inválida! Por favor, escolha um número de 1 a 4.")