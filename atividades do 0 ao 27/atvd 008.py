#varios valores e nenhum igual.
print('-' * 70)
valor = list()
while True:
        ent = input('Digite um valor: ')
        
        #verifica se a entrada é númerica, incluindo o 0
        if ent.isnumeric():
            val = int(ent)
            valor.append(val)
            print(f'Valor adicionado com\033[32m sucesso\033[m...')
            
            resp = ' '
            while resp not in 'SN':
                resp = str(input('Você quer adicionar +1 valor? [S/N]: ')).strip().upper()[0]
            if resp == 'N':
                break
        else:
            print('Não é um número válido')
print()
print(f'Você digitou os valores:\033[31m {valor} \033[m')
print('-' * 70)