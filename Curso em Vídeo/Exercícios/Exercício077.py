l = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in l:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for le in p:
        if le.lower() in 'aeiou':
            print(f'{le}',end=' ')
