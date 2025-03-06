def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b

ret = soma_numeros_positivos(2, 4)
print(ret)
ret2 = soma_numeros_positivos(-2, 4)
print(ret)
