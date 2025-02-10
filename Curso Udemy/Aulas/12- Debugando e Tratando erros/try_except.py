try:
    geek()
except:
    print('Deu algum problema')
print()

try:
    len(5)
except:
    print('Deu algum problema')
print()

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')
print()

try:
    len(5)
except TypeError:
    print('Você está utilizando uma função inexistente')
print()

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')
print()

try:
    len(5)
except NameError as erra:
    print(f'A aplicação gerou o seguinte erro: {erra}')
except TypeError as errb:
    print(f'A aplicação gerou o seguinte erro: {errb}')
print()

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    

dic = {"nome": "geek"}
print(pega_valor(dic, "nome"))