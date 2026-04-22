#tabela do brasileirão 2026
print('-' * 70)
times = ('Palmeiras', 'São Paulo', 'Fluminense', 'Flamengo',
         'Bahia', 'Athletico-PR', 'Coritiba', 'Atlético-MG',
         'Bragantino', 'Botafogo', 'Grêmio', 'Vasco da Gama',
         'Internacional', 'EC Vitória', 'Santos', 'Corinthians',
         'Chapecoense', 'Remo', 'Cruzeiro', 'Mirassol')
print(f'Colocação dos times do Brasileirão Série A 2026: {times}')
print('-' * 70)

print(f'Os 05 primeiros colocados são {times[:5]}')
print('-' * 70)

print(f'Os ultimos 04 colocados são: {times[-4:]}')
print('-' * 70)

print(f'Os times em ordem alfabética são: {sorted(times)}')
print('-' * 70)

print(f'A Chapecoense está na {times.index('Chapecoense')+1}ª posição')
print('-' * 70)