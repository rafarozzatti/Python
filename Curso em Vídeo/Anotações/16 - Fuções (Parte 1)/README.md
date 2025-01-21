## Funções (Parte 1)

#### Exemplos:

```python
def lin():
    print('-' * 30)


lin()
print('APRENDA PYTHON')
lin()
# Resultado: Imprime 30 linhas antes e depois do frase 'APRENDA PYTHON '
```

```python
def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


título('APRENDA PYTHON')
título('CURSO EM VÍDEO')
# Resultado: Imprime 30 linhas antes e depois das duas frases
```

```python
def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 7)
# Resultado: Imprime o resultado da soma de 4 + 5 e 8 + 7
```

```python
def contador(* num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 6, 2)
# Resultado: cria uma tupla para cada contador
```

```python
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores  = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
# Resultado: dobra os valores da lista
```