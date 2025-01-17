l = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'''Você digitou os valores {l}
O valor 9 apareceu {l.count(9)} vezes
O valor 3 aparaceu na {l.index(3) + 1}ª posição
Os valores pares digitados foram ''', end='')
for n in l:
    if n % 2 == 0:
        print(f'{n}', end=' ')