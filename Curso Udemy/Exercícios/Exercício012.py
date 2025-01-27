lista = []
listapar = []
for i in range(0, 10):
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
print(f'''Valores digitados: {lista}
Foram digitados {len(listapar)} números pares
Lista números pares: {listapar}''')
