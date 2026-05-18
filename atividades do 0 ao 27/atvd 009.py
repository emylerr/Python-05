#Valores em ordem sem usar o sort()
print('-' * 70)
lista = []
for cont in range(0,5):
    num = int(input('Digite um número: '))
    if cont == 0 or num > lista[-1]:
        lista.append(num)
        print(f'Valor adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição: {pos}')
                break
            pos += 1
print()
print(f'Os valores em ordem são: {lista}')
print('-' * 70)