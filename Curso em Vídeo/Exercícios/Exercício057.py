s = input('Informe seu sexo: [M/F] ')
while s != 'M' and s != 'F':
    s = input('Dados inválidos. Por favor, informe seu sexo: ').upper()
print(f'Sexo {s} registrado com sucesso')