## Funções (Parte 2)


#### Exemplos:

```python
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
# Resultado: Meus cálculos deram 10, 8 e 4.
```