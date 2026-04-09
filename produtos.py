print('--- CARDÁPIO DE BEBIDAS ---')
print('1 - Coca-cola (R$ 5.00)')
print('2 - Água (R$ 3.00)')

opcao = int(input('\nDigite o número da opção desejada: '))

if opcao == 1:
    nome_produto = "Coca-cola"
    preco = 5.0
elif opcao == 2:
    nome_produto = "Água"
    preco = 3.0
else:
    nome_produto = None
    print(' Opção inválida! Reinicie o sistema.')

if nome_produto:
    print(f' Você escolheu: {nome_produto}')
    print(f'O valor unitário é: R$ {preco:.2f}')
