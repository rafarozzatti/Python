## Condições

#### Exemplos:

```python
tempo = int(input('Quantos anos tem seu carro?' ))
if tempo <= 3:
    print('carro novo')
# Se o tempo for menor ou igual a 3, imprime 'carro novo'
else:
    print('carro velho')
# Se não, imprime 'carro velho'
print('--FIM--')
```

```python
tempo = int(input('Quantos anos tem seu carro?' ))
print('carro novo' if tempo <= 3 else 'carro velho')
# Versão simplificada do exemplo acima
print('--FIM--')
```