cont = media = 0
while True:
    n = float(input())
    if n < 0 or n > 10:
        print('nota invalida')
    else:
        media +=n
        cont += 1
    if cont == 2:
        break
print(f'media = {(media/cont):.2f}')
