#lista de produtos em ordem
print('-' * 70)
print(f'{"LISTAGEM DE VALORES":^70}')
print('-' * 70)

list = ('Lápis', 1.75,
        'Borracha', 0.90,
        'Caderno', 20.0,
        'Estojo', 14.9,
        'Caneta', 2.5,
        'Régua', 5.0,
        'Mochila', 125.0)

for pos in range(0, len(list)):
    if pos % 2 == 0:
        print(f'{list[pos]:.<62}', end='')
    else:
        print(f'R${list[pos]:>6.2f}')
print('-' * 70)