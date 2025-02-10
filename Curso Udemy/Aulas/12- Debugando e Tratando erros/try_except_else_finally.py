try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
print()


try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')
print()


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por zero'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')
print(dividir(num1, num2))
print()


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')
print(dividir(num1, num2))
