#posições, valores e pares
print('-' * 70)
num1 = int(input('Digite um 1º número: '))
num2 = int(input('Digite um 2º número: '))
num3 = int(input('Digite um 3º número: '))
num4 = int(input('Digite um 4º número: '))
numeros = (num1, num2, num3, num4)

print('-' * 70)
print(f'Você digitou os números: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vez(es)')

if 3 in numeros:
    print(f'E o número 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado.')

print(f'Os números pares são: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end=' ')
print()
print('-' * 70)