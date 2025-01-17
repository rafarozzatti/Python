t = ('zero' ,'um', 'dois', 'três', 'Quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezessies', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n < 0 or n > 20:
        print('Tente novamente.', end=' ')
    else:
        break
print(f'Você digitou o número {t[n]}')