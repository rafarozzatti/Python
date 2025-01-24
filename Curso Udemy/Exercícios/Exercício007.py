cont = 0
while True:
    for c in range(20):
        if cont == 5:
            break
        if c % 3 == 0 and c > 0:
            print(c)
            cont += 1
        