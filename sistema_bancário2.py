from datetime import datetime

# Definição das funções
def depositar(saldo, extrato, transacoes_realizadas, LIMITE_TRANSACOES):
    if transacoes_realizadas >= LIMITE_TRANSACOES:
        print("Você atingiu o limite de transações diárias!")
        return saldo, extrato, transacoes_realizadas

    try:
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append(f"{data_hora} - Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            transacoes_realizadas += 1
        else:
            print("Valor inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

    return saldo, extrato, transacoes_realizadas


def sacar(saldo, extrato, saques_diarios, LIMITE_SAQUES, limite_saque, transacoes_realizadas, LIMITE_TRANSACOES):
    if transacoes_realizadas >= LIMITE_TRANSACOES:
        print("Você atingiu o limite de transações diárias!")
        return saldo, extrato, saques_diarios, transacoes_realizadas

    if saques_diarios >= LIMITE_SAQUES:
        print("Limite diário de saques atingido!")
        return saldo, extrato, saques_diarios, transacoes_realizadas

    try:
        valor = float(input("Digite o valor do saque: "))
        if valor <= 0:
            print("Valor inválido. Tente novamente.")
        elif valor > saldo:
            print("Saldo insuficiente!")
        elif valor > limite_saque:
            print(f"Limite máximo por saque é R$ {limite_saque:.2f}.")
        else:
            saldo -= valor
            saques_diarios += 1
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append(f"{data_hora} - Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            transacoes_realizadas += 1
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

    return saldo, extrato, saques_diarios, transacoes_realizadas


def exibir_extrato(saldo, extrato):
    print("\n===== EXTRATO =====")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for item in extrato:
            print(item)
    print(f"Saldo atual: R$ {saldo:.2f}")


def main():
    saldo = 0.0
    extrato = []
    limite_saque = 500.00
    saques_diarios = 0
    LIMITE_SAQUES = 3
    LIMITE_TRANSACOES = 10
    transacoes_realizadas = 0

    while True:
        print("\n===== MENU =====")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo, extrato, transacoes_realizadas = depositar(saldo, extrato, transacoes_realizadas, LIMITE_TRANSACOES)
        elif opcao == "2":
            saldo, extrato, saques_diarios, transacoes_realizadas = sacar(
                saldo, extrato, saques_diarios, LIMITE_SAQUES, limite_saque, transacoes_realizadas, LIMITE_TRANSACOES
            )
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "4":
            print("Saindo do sistema. Obrigado por utilizar nossos serviços!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
