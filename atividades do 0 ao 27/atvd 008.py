#varios valores e nenhum igual.
print('-' * 70)
valor = list()
while True:
    n = int(input('Digite um valor: '))
    
    if n not in valor:
        valor.append(n)
        print(f'Valor\033[32m adicionado\033[m...')
    else:
        print(f'Valor\033[33m duplicado\033[m, não irei adicionar!')

    #sim ou não
    resp = str(input('Você quer digitar +1 valor? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print()
valor.sort()
print(f'Você digitou os valores: {valor}')
print('-' * 70)