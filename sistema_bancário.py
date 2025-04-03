def main():
    saldo = 0.0
    extrato = []
    limite_saque = 500.00
    saques_diarios = 0
    LIMITE_SAQUES = 3

    while True:
        print("\n===== MENU =====")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido. Tente novamente.")

        elif opcao == "2":
            if saques_diarios < LIMITE_SAQUES:
                valor = float(input("Digite o valor do saque: "))
                if valor > saldo:
                    print("Saldo insuficiente!")
                elif valor > limite_saque:
                    print(f"Limite máximo por saque é R$ {limite_saque:.2f}.")
                elif valor > 0:
                    saldo -= valor
                    saques_diarios += 1
                    extrato.append(f"Saque: R$ {valor:.2f}")
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("Valor inválido. Tente novamente.")
            else:
                print("Limite diário de saques atingido!")

        elif opcao == "3":
            print("\n===== EXTRATO =====")
            if not extrato:
                print("Nenhuma movimentação registrada.")
            else:
                for item in extrato:
                    print(item)
            print(f"Saldo atual: R$ {saldo:.2f}")

        elif opcao == "4":
            print("Saindo do sistema. Obrigado por utilizar nossos serviços!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

