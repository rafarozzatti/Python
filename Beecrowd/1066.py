contpar = contimpar = contpos = contneg = 0
for i in range(1, 6):
    n = int(input())
    if n > 0:
        contpos += 1
    elif n < 0:
        contneg += 1

    if n % 2 == 0:
        contpar += 1
    else:
        contimpar += 1
print(f'''{contpar} valor (es) par (es)
{contimpar} valor (es) impar (es)
{contpos} valor (es) positivo (s)
{contneg} valor (es) negativo (s)''')
