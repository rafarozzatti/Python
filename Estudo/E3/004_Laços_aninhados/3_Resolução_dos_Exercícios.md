# Exercícios de Laços aninhados

## Vamos praticar — Exercício 1

Crie um programa usando dois laços `for` aninhados para produzir a seguinte saída:

```
1 1 1
2 2 2
3 3 3
```

Regras:

- O laço externo deve percorrer os números de 1 a 3.
- O laço interno deve repetir 3 vezes para cada número externo.
- Cada linha deve exibir o número externo três vezes, separados por espaços.

Resolução:
```python
for i in range(1, 4):
    for j in range(3):
        print(i, end=' ')
    print()
```