## Interrompendo Repetições While

## Exemplo:

```python
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
# o código lê os números até que digite 999, aí o comando break faz sair do loop
```