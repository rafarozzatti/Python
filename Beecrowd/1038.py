x, y = input().split()
x = int(x)
y = float(y)
if x == 1:
    valor = 4
elif x == 2:
    valor = 4.5
elif x == 3:
    valor = 5
elif x == 4:
    valor = 2
elif x == 5:
    valor = 1.5
total = y * valor
print(f'Total: R$ {total:.2f}')
