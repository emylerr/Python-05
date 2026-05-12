#inserir valores
print('-' * 70)
valor = []
maior = menor = 0

for cont in range(0, 5):
    valor.append(int(input(f'Digite um valor na posição {cont}: ')))

    if cont == 0:
        maior = menor = valor[cont]
    else:
        if valor[cont] > maior:
            maior = valor[cont]

        if valor[cont] < menor:
            menor = valor[cont]
print('-' * 70)
print(f'Você digitou os valores: {valor}')
print(f'O maior número encontrado foi {maior} na(s) posição(ões): ', end ='')
for ind, val in enumerate(valor):
    if val == maior:
        print(f'{ind} ', end='')
print()
print(f'O menor número encontrado foi {menor} na(s) posição(ões): ', end ='')
for ind, val in enumerate(valor):
    if val == menor:
        print(f'{ind} ', end='')
print()
print('-' * 70)

#com o index, min e max
'''maior = max(valor)
posmax = valor.index(maior)

menor = min(valor)
posmin = valor.index(menor)

print(f'O maior número encontrado foi {maior} na posição {posmax}.')
print(f'O menor valor encontrado foi {menor} na posição {posmin}.')
print('-' * 70)'''