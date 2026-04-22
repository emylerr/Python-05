#números por extenso
print('-' * 70)
cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte')
while True:
    num = int(input('Me fale um número entre 0 e 20: '))

    if 0 <= num <= 20:
        print(f'Você me informou o número \033[32m{cont[num]}\033[m.')
        resp = ' '
        while resp not in 'SsNn':
            resp = str(input('Você quer continuar digitando mais números? [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break
    else:
        print('Tente novamente.', end='')
        
print('Programa\033[31m encerrado\033[m.')
print('-' * 70)