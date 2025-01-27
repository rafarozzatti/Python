def aumentar(preço = 0, taxa = 0, formato = False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)
    
def diminuir(preço = 0, taxa = 0, formato = False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)
    
def dobro(preço = 0, formato = False):
    res = preço * 2
    return res if formato is False else moeda(res)
    
def metade(preço = 0, formato = False):
    res = preço / 2
    return res if formato is False else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço = 0, taxaa = 10, taxar = 5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'''Preço analizado: \t{moeda(preço)}
Dobro do preço: \t{dobro(preço, True)}
Metade do preço: \t{metade(preço, True)}
{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}
{taxar}% de redução: \t{diminuir(preço, taxar, True)}
''')
    print('-' * 35)