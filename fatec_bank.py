# -*- coding: utf-8 -*-

# FATEC BANK - PROJETO INTEGRADOR I

import os
import csv

usuarios = {
    "1": {
        "id": "1",
        "nome": "Antonio",
        "senha": "1234",
        "saldo_inicial": 500.00,
        "saldo": 500.00,
        "historico": []
    },

    "2": {
        "id": "2",
        "nome": "Maria",
        "senha": "2345",
        "saldo_inicial": 800.00,
        "saldo": 800.00,
        "historico": []
    },

    "3": {
        "id": "3",
        "nome": "Joao",
        "senha": "3456",
        "saldo_inicial": 350.00,
        "saldo": 350.00,
        "historico": []
    }
}

def carregarMovimentacoes():

    if os.path.exists("movimentacoes.csv"):

        with open("movimentacoes.csv", "r", encoding="utf-8-sig") as arquivo:

            leitor = csv.reader(arquivo, delimiter=";")

            next(leitor, None)

            for linha in leitor:

                id_conta = linha[0]
                operacao = linha[1]
                valor = float(linha[2])
                saldo_anterior = float(linha[3])
                saldo_final = float(linha[4])

                conta = usuarios[id_conta]

                conta["historico"].append(
                    (operacao, valor, saldo_anterior, saldo_final)
                )

                conta["saldo"] = saldo_final

def salvarMovimentacao(conta, operacao, valor, saldo_anterior, saldo_final):

    arquivo_novo = not os.path.exists("movimentacoes.csv")

    with open("movimentacoes.csv", "a", encoding="utf-8") as arquivo:

        if arquivo_novo:
            arquivo.write("conta;operacao;valor;saldo_anterior;saldo_final\n")

        arquivo.write(
            f"{conta['id']};{operacao};{valor:.2f};{saldo_anterior:.2f};{saldo_final:.2f}\n"
        )

    conta["saldo"] = saldo_final
    conta["historico"].append(
        (operacao, valor, saldo_anterior, saldo_final)
    )

def lerValor():
    while True:
        try:
            valor = float(input("Digite o valor (R$): ").replace(",", "."))
            if valor > 0:
                return valor
            print("Digite um valor maior que zero.")
        except ValueError:
            print("Valor invalido. Digite um numero.")


def depositar(conta):

    print("\n===== DEPOSITO =====")

    valor = lerValor()

    if valor > 0:

        saldo_anterior = conta["saldo"]

        saldo_final = round(saldo_anterior + valor, 2)

        salvarMovimentacao(
            conta, "Deposito", valor, saldo_anterior, saldo_final
        )

        print("\nDeposito realizado com sucesso!")
        print(f"Saldo anterior: R$ {saldo_anterior:.2f}")
        print(f"Valor depositado: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo_final:.2f}")

    else:
        print("\nValor invalido! Digite um valor maior que zero.")

    input("\nPressione ENTER para voltar ao menu...")

def sacar(conta):

    print("\n===== SAQUE =====")

    valor = lerValor()

    if valor <= conta["saldo"]:

        saldo_anterior = conta["saldo"]

        saldo_final = round(saldo_anterior - valor, 2)

        salvarMovimentacao(
            conta, "Saque", valor, saldo_anterior, saldo_final
        )

        print("\nSaque realizado com sucesso!")
        print(f"Saldo anterior: R$ {saldo_anterior:.2f}")
        print(f"Valor sacado: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo_final:.2f}")

    else:
        print("\nSaldo insuficiente!")
        print("Operacao nao realizada.")

    input("\nPressione ENTER para voltar ao menu...")

def mostrarSaldo(conta):

    print("\n===== CONSULTA DE SALDO =====")

    print("Usuario:", conta["nome"])

    print(f'Saldo atual: R$ {conta["saldo"]:.2f}')

    input("\nPressione ENTER para voltar ao menu...")

def mostrarHistorico(conta):

    print("\n===== EXTRATO BANCARIO =====")
    print("Usuario:", conta["nome"])
    print(f'Saldo inicial: R$ {conta["saldo_inicial"]:.2f}')

    if len(conta["historico"]) == 0:
        print("Nenhuma movimentacao realizada.")

    else:
        for operacao, valor, saldo_anterior, saldo_final in conta["historico"]:

            print("\nOperacao:", operacao)
            print(f"Saldo anterior: R$ {saldo_anterior:.2f}")
            print(f"Valor movimentado: R$ {valor:.2f}")
            print(f"Saldo final: R$ {saldo_final:.2f}")

    print(f'\nSaldo atual: R$ {conta["saldo"]:.2f}')

    input("\nPressione ENTER para voltar ao menu...")

def fazerLogin():

    print("\n===== FATEC BANK - LOGIN =====")
    print("1 - Antonio")
    print("2 - Maria")
    print("3 - Joao")
    print("0 - Encerrar programa")

    opcao = input("Escolha o usuario: ")

    if opcao == "0":
        return "SAIR"

    if opcao not in usuarios:
        print("\nUsuario invalido!")
        return None

    conta = usuarios[opcao]

    senha = input("Digite a senha: ")

    if senha == conta["senha"]:

        print("\nLogin realizado com sucesso!")
        print("Bem-vindo(a),", conta["nome"])

        return conta

    else:
        print("\nSenha incorreta!")
        return None

def menuConta(conta):

    while True:

        print("\n===== FATEC BANK =====")
        print("Usuario:", conta["nome"])
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Exibir saldo")
        print("4 - Exibir extrato bancario")
        print("5 - Sair da conta")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            depositar(conta)

        elif opcao == "2":
            sacar(conta)

        elif opcao == "3":
            mostrarSaldo(conta)

        elif opcao == "4":
            mostrarHistorico(conta)

        elif opcao == "5":
            print("\nSaindo da conta...")
            break

        else:
            print("\nOpcao invalida!")

def executar():

    while True:

        conta = fazerLogin()

        if conta == "SAIR":
            print("\nPrograma finalizado.")
            break

        if conta is not None:
            menuConta(conta)

carregarMovimentacoes()
executar()