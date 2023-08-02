def withdraw(*, user, account, valor):
    global numero_saques, extrato, LIMITE_DE_SAQUES

    excedeu_saldo = valor > account["balance"]
    excedeu_limite = valor > limite
    excedeu_limite_daques = numero_saques > LIMITE_DE_SAQUES

    if excedeu_saldo:
        print('Opção falhou! Você não tem saldo suficiente em conta')
    elif excedeu_limite:
        print('Opção falhou! Você excedeu o limite por saque')
    elif excedeu_limite_daques:
        print('Opção falhou! Número máximo de saques excedido')
    elif valor > 0:
        account["balance"] -= valor
        extrato += f'{user["name"]} realizou um Saque de R$ {valor:.2f}\n'
        numero_saques += 1
    else:
        print('Operação falhou! Valor informado é inválido')


def deposit(*, user, account, valor):
    global extrato

    if valor > 0:
        account["balance"] += valor
        extrato += f'{user["name"]} realizou um Depósito de R$ {valor:.2f}\n'
    else:
        print('Operação falhou! O valor informado é inválido')


def statement(*, user, account, show_transactions=True):
    global extrato

    print('\n================ Extrato =================')
    if show_transactions:
        print('Não foram realizadas operações' if not extrato else extrato)
    print(f'\nTitular: {user["name"]}')
    print(f'CPF: {user["cpf"]}')
    print(f'Idade: {user["age"]}')
    print(f'Número da Conta: {account["account_number"]}')
    print(f'Saldo: R$ {account["balance"]:.2f}')


def register_user(name, cpf, age):
    user = {
        "name": name,
        "cpf": cpf,
        "age": age
    }
    return user


def register_account(account_number, user_id, initial_balance):
    account = {
        "account_number": account_number,
        "user_id": user_id,
        "balance": initial_balance
    }
    return account


users = []
accounts = []

limite = 500
extrato = ''
numero_saques = 1
LIMITE_DE_SAQUES = 3

menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Cliente
[5] Cadastrar Conta
[0] Sair

'''

while True:
    opcao = input(menu)

    if opcao == '1':
        cpf = input('Digite o CPF do cliente: ')
        valor = float(input('Digite o valor a ser depositado: '))

        user = next((u for u in users if u["cpf"] == cpf), None)
        if not user:
            print('Cliente não cadastrado!')
            continue

        account = next((a for a in accounts if a["user_id"] == cpf), None)
        if not account:
            print('Conta não encontrada para o cliente!')
            continue

        deposit(user=user, account=account, valor=valor)

    elif opcao == '2':
        cpf = input('Digite o CPF do cliente: ')
        valor = float(input('Informe o valor do saque: '))

        user = next((u for u in users if u["cpf"] == cpf), None)
        if not user:
            print('Cliente não cadastrado!')
            continue

        account = next((a for a in accounts if a["user_id"] == cpf), None)
        if not account:
            print('Conta não encontrada para o cliente!')
            continue

        withdraw(user=user, account=account, valor=valor)

    elif opcao == '3':
        cpf = input('Digite o CPF do cliente: ')

        user = next((u for u in users if u["cpf"] == cpf), None)
        if not user:
            print('Cliente não cadastrado!')
            continue

        account = next((a for a in accounts if a["user_id"] == cpf), None)
        if not account:
            print('Conta não encontrada para o cliente!')
            continue

        show_transactions = input("Deseja mostrar as transações? (S/N): ")
        if show_transactions.lower() == "s":
            statement(user=user, account=account, show_transactions=True)
        else:
            statement(user=user, account=account, show_transactions=False)

    elif opcao == '4':
        name = input('Digite o nome do cliente: ')
        cpf = input('Digite o CPF do cliente: ')
        age = int(input('Digite a idade do cliente: '))
        user = register_user(name, cpf, age)
        users.append(user)
        print(f'Cliente {user["name"]} cadastrado com sucesso!')

    elif opcao == '5':
        account_number = input('Digite o número da conta: ')
        user_id = input('Digite o CPF do cliente vinculado à conta: ')
        initial_balance = float(input('Digite o saldo inicial da conta: '))

        user = next((u for u in users if u["cpf"] == user_id), None)
        if not user:
            print('Cliente não cadastrado! Crie um cliente antes de criar uma conta.')
            continue

        account = register_account(account_number, user_id, initial_balance)
        accounts.append(account)
        print(f'Conta {account["account_number"]} cadastrada com sucesso!')

    elif opcao == '0':
        print('Você saiu')
        break
    else:
        print('Opção inválida \nPor favor digite novamente a opção desejada')

