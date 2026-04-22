#números aleatórios
from random import randint

print('-' * 70)
num = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
print(f'Os números sorteados foram: ', end='')

for n in num:
    print(f'{n}', end='')
print(f'\nO maior valor sorteado foi: {max(num)}')
print(f'O mnenor valor sorteado foi: {min(num)}')
print('-' * 70)