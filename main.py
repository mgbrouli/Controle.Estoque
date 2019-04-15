bebidas = []
pereciveis = []
naoPereciveis = []


def cadastro():
    while True:
        lista = {}
        lista.clear()
        lista['produto'] = str(input('Digite o nome do produto: '))
        lista['quantidade'] = int(input('Quantidade: '))
        pb = float(input('Preço bruto R$: '))
        lista['pBruto'] = pb
        pcent = int(input('Porcentagem do lucro: '))
        lista['porcentagem'] = pcent
        lista['lucro'] = ((pb*pcent)/100)+pb
        print('''Qual o tipo de produto
         [1] Bebidas Alcoolicas.
         [2] Produtos perecivel.
         [3] Produtos Não pereciveis.
         ''')
        tipo = int(input('Digite aqui a opção desejada: '))
        if tipo == 1:
            bebidas.append(lista.copy())
        elif tipo == 2:
            pereciveis.append(lista.copy())
        elif tipo == 3:
            lista['validade'] = int(input('Data de validade (digite apenas o mes): '))
            naoPereciveis.append(lista.copy())
        resp = str(input('Quer continuar o cadastro [S/N]: ')).upper().strip()[0]
        while resp not in 'SN':
            resp = str(input('Quer continuar o cadastro [S/N]: ')).upper().strip()[0]
        if resp == 'N':
            break


def alterar():
    print('''Qual o tipo de produto
             [1] Bebidas Alcoolicas.
             [2] Produtos perecivel.
             [3] Produtos Não pereciveis.
             ''')
    resp = int(input('Digite sua opção em numeros: '))
    while resp >= 4:
        resp = int(input('Digite sua opção em numeros: '))
    if resp == 1:
        for i in bebidas:
            for k, v in i.items():
                print(f'{k}: {v}')
    elif resp == 2:
        for i in pereciveis:
            for k, v in i.items():
                print(f'{k}: {v}')
    elif resp == 3:
        for i in naoPereciveis:
            for k, v in i.items():
                print(f'{k}: {v}')


print('--'*30)
print(f'{">>>PROGRAMA DE CONTROLE DE ESTOQUE v1.0<<<":^60}')
print(f'{"crado por Welligton":^60}')
print('--'*30)
while True:
    print('''\033[1;33mEscolha sua opção digitando as opções em valor numerico:\033[m 
    \033[1;32m[1]\033[m Para cadastrar produtos: 
    \033[1;32m[2]\033[m Para Alterar o produtos cadastrados:
    \033[1;32m[0]\033[m Para sair do programa:\033[m  
    ''')
    print('--' * 30)
    opcao = int(input('\033[1;33mDigite aqui a opção: \033[m'))
    while opcao >= 3:
        opcao = int(input('\033[1;33mDigite aqui a opção: \033[m'))
    if opcao == 0:
        break
    elif opcao == 1:
        cadastro()
    elif opcao == 2:
        alterar()






print(bebidas)
print(pereciveis)
print(naoPereciveis)
