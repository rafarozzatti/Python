def notas(* n, sit=False):
    d = {}
    d['total'] = len(n)
    d['maior'] = max(n)
    d['menor'] = min(n)
    d['média'] = sum(n) / len(n)
    if sit:
        if d['média'] >= 7:
            d['situação'] = 'BOA'
        elif d['média'] >= 5:
            d['situação'] = 'RAZOÁVEL'
        else:
            d['situação'] = 'RUIM'
    return d


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)