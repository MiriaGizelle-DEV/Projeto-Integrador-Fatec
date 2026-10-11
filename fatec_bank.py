```python
# -*- coding: utf-8 -*-

# ==================================================
# FATEC BANK
# SISTEMA DE CONTROLE FINANCEIRO MULTIUSUARIO
# PROJETO INTEGRADOR I - FATEC
# ==================================================


# 1 - CADASTRO DOS TRES USUARIOS
# Cada usuario possui nome, senha, saldo inicial,
# saldo atual e historico de movimentacoes.

usuarios = {
    "1": {
        "nome": "Antonio",
        "senha": "1234",
        "saldo_inicial": 500.00,
        "saldo": 500.00,
        "historico": []
    },

    "2": {
        "nome": "Maria",
        "senha": "2345",
        "saldo_inicial": 800.00,
        "saldo": 800.00,
        "historico": []
    },

    "3": {
        "nome": "Joao",
        "senha": "3456",
        "saldo_inicial": 350.00,
        "saldo": 350.00,
        "historico": []
    }
}


# ==================================================
# 2 - FUNCAO PARA LER UM VALOR POSITIVO
# ==================================================

def lerValor():
    while True:
        try:
            valor = float(
                input("Digite o valor (R$): ").replace(",", ".")
            )

            # O valor deve ser maior que zero.
            if valor > 0:
                return valor
            else:
                print("Digite um valor maior que zero.")

        except ValueError:
            print("Valor invalido. Digite um numero.")


# ==================================================
# 3 - PROCESSO PARA REALIZAR DEPOSITO
# ==================================================

def depositar(conta):
    print("\n===== DEPOSITO =====")

    valor = lerValor()

    # Guarda o saldo antes do deposito.
    saldo_anterior = conta["saldo"]

    # Acrescenta o deposito ao saldo.
    conta["saldo"] = round(saldo_anterior + valor, 2)

    # Guarda o saldo depois do deposito.
    saldo_final = conta["saldo"]

    # Registra a operacao no historico.
    # Guarda: tipo, valor, saldo anterior e saldo final.
    conta["historico"].append(
        ("Deposito", valor, saldo_anterior, saldo_final)
    )

    print("\nDeposito realizado com sucesso!")

    print(f"Saldo anterior: R$ {saldo_anterior:.2f}")
    print(f"Valor depositado: R$ {valor:.2f}")
    print(f"Saldo atual: R$ {saldo_final:.2f}")

    input("\nPressione ENTER para voltar ao menu...")


# ==================================================
# 4 - PROCESSO PARA REALIZAR SAQUE
# ==================================================

def sacar(conta):
    print("\n===== SAQUE =====")

    valor = lerValor()

    # Verifica se existe saldo suficiente.
    if valor <= conta["saldo"]:

        # Guarda o saldo antes do saque.
        saldo_anterior = conta["saldo"]

        # Desconta o valor sacado.
        conta["saldo"] = round(saldo_anterior - valor, 2)

        # Guarda o saldo depois do saque.
        saldo_final = conta["saldo"]

        # Registra o saque no historico.
        conta["historico"].append(
            ("Saque", valor, saldo_anterior, saldo_final)
        )

        print("\nSaque realizado com sucesso!")

        print(f"Saldo anterior: R$ {saldo_anterior:.2f}")
        print(f"Valor sacado: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo_final:.2f}")

    else:
        # Se nao houver saldo, o saque nao e realizado.
        print("\nSaldo insuficiente!")
        print("Operacao nao realizada.")

    input("\nPressione ENTER para voltar ao menu...")


# ==================================================
# 5 - PROCESSO PARA CONSULTAR SALDO
# ==================================================

def mostrarSaldo(conta):
    print("\n======================================")
    print("       FATEC BANK - CONSULTA")
    print("======================================")

    print("Usuario:", conta["nome"])

    print("-------------------------------------")

    print(f'Saldo atual: R$ {conta["saldo"]:.2f}')

    print("======================================")

    input("\nPressione ENTER para voltar ao menu...")


# ==================================================
# 6 - PROCESSO PARA CONSULTAR EXTRATO BANCARIO
# ==================================================

def mostrarHistorico(conta):
    print("\n======================================")
    print("       FATEC BANK - EXTRATO")
    print("======================================")

    print("Usuario:", conta["nome"])

    print("-------------------------------------")

    # Mostra o saldo inicial da conta.
    print(
        f'Saldo inicial: R$ {conta["saldo_inicial"]:.2f}'
    )

    print("-------------------------------------")

    # Verifica se existem movimentacoes.
    if len(conta["historico"]) == 0:
        print("Nenhuma movimentacao realizada.")

    else:
        # Percorre cada movimentacao do historico.
        for tipo, valor, saldo_anterior, saldo_final in conta["historico"]:

            print("\nOperacao:", tipo)

            print(
                f"Saldo anterior: R$ {saldo_anterior:.2f}"
            )

            print(
                f"Valor movimentado: R$ {valor:.2f}"
            )

            print(
                f"Saldo final: R$ {saldo_final:.2f}"
            )

            print("--------------------------------------")

    # Exibe o saldo atualizado da conta.
    print(
        f'\nSaldo atual: R$ {conta["saldo"]:.2f}'
    )

    print("======================================")

    input("\nPressione ENTER para voltar ao menu...")


# ==================================================
# 7 - FUNCAO PARA REALIZAR LOGIN
# ==================================================

def fazerLogin():
    print("\n======================================")
    print("              FATEC BANK")
    print("======================================")
    print("                LOGIN")
    print("======================================")

    print("1 - Antonio")
    print("2 - Maria")
    print("3 - Joao")
    print("0 - Encerrar programa")

    print("======================================")

    opcao = input("Escolha o usuario: ").strip()

    # Verifica se o usuario deseja encerrar.
    if opcao == "0":
        return "SAIR"

    # Verifica se o usuario existe.
    if opcao not in usuarios:
        print("\nUsuario invalido!")
        return None

    # Solicita a senha do usuario selecionado.
    senha = input("Digite a senha: ").strip()

    # Recupera os dados do usuario.
    conta = usuarios[opcao]

    # Compara a senha digitada com a cadastrada.
    if senha == conta["senha"]:
        print("\nLogin realizado com sucesso!")
        print("Bem-vindo(a),", conta["nome"])
        return conta

    else:
        print("\nSenha incorreta!")
        return None


# ==================================================
# 8 - PROCESSO DO MENU PRINCIPAL
# ==================================================

def menuConta(conta):

    # Mantem o menu em funcionamento.
    while True:
        print("\n======================================")
        print("              FATEC BANK")
        print("======================================")

        print("Usuario:", conta["nome"])

        print("--------------------------------------")

        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Exibir Saldo")
        print("4 - Exibir Extrato Bancario")
        print("5 - Sair da Conta")

        print("======================================")

        opcao = input("Escolha uma opcao: ").strip()

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

            # Interrompe o menu e retorna ao login.
            break

        else:
            print("\nOpcao invalida!")


# ==================================================
# 9 - PROCESSO PRINCIPAL DO PROGRAMA
# ==================================================

def executar():
    while True:

        # Solicita o login.
        conta = fazerLogin()

        # Encerra o programa.
        if conta == "SAIR":
            print("\nPrograma finalizado.")
            break

        # Se o login estiver correto, abre o menu.
        elif conta is not None:
            menuConta(conta)


# ==================================================
# 10 - INICIO DO PROGRAMA
# ==================================================

# Chama a sub-rotina principal.
executar()
```
