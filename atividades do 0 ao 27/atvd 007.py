#inserir valores
print('-' * 70)
valor = list()
maior = menor = 0
posmax = posmin = 0

for cont in range(0, 5):
    valor.append(int(input(f'Digite um valor na posição {cont}: ')))

    if cont == 0:
        maior = menor = valor[cont]
        posmax = posmin = cont
    else:
        if valor[cont] > maior:
            maior = valor[cont]
            posmax = cont

        if valor[cont] < menor:
            menor = valor[cont]
            posmin = cont
print('-' * 70)
print(f'Você digitou os valores: {valor}')
print(f'O maior número encontrado foi {maior} na posição {posmax}')
print(f'O menor valor encontrado foi {menor} na posição {posmin}')
print('-' * 70)

#com o index, min e max
'''maior = max(valor)
posmax = valor.index(maior)

menor = min(valor)
posmin = valor.index(menor)

print(f'O maior número encontrado foi {maior} na posição {posmax}.')
print(f'O menor valor encontrado foi {menor} na posição {posmin}.')
print('-' * 70)'''