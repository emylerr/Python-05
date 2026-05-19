#Extraindo dados de uma lista.
print('-' * 70)
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Você quer digitar +1 valor? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print()
print(f'Você digitou {len(lista)} elementos')

lista.sort(reverse = True)
print(f'Os valores em ordem decrescente são: {lista}')

if 5 in lista:
    print(f'O número 5 faz parte da lista.')
else:
    print(f'O número 5 não foi digitado.')
print('-' * 70)