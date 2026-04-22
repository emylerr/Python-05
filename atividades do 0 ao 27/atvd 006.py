#Vogais em palavras
print('-' * 70)
palavras = ('APRENDER', 'PROGRAMAR', 'FACULDADE',
            'PYTHON', 'JAVASCRIPT', 'PRATICAR',
            'JAVA', 'PROGRAMADORA', 'TRABALHO')
for p in palavras:
    print(f'Na palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
    print()
print('-' * 70)