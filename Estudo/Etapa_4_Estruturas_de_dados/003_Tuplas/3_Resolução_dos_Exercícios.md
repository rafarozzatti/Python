## Exercício 1

```python
cores= ("Azul", "Verde", "Vermelho", "Amarelo", "Preto")

print(cores[0])
print(cores[2])
print(cores[-1])
```

## Exercício 2
```python
numeros = (10, 20, 30, 40, 50, 60, 70)

print(numeros[0:3])
print(numeros[3:])
print(numeros[::-1])
```

## Exercício 3
```python
numeros = (5, 10, 5, 20, 5, 30, 10, 5)

print(numeros.count(5))
print(numeros.count(10))
print(numeros.count(30))
```

## Exercício 4
```python
frutas = ("Maçã", "Banana", "Uva", "Laranja", "Morango")

print(frutas.index('Banana'))
print(frutas.index('Laranja'))
print(frutas.index('Morango'))
```

## Exercício 5
```python
numeros = (10, 20, 30, 20, 40, 20, 50)

print(numeros.index(20))
print(numeros.count(20))
```

## Exercício 6
```python
# Tuplas são imutáveis, portanto não permitem alterar, adicionar ou remover elementos depois de criadas.
```

## Exercício 7
```python
# Na lista não ocorreu erro, pois ela é mutável, Já a tupla é imutável, portanto não permite alterar, adicionar ou remover elementos depois de criada.

frutas = ["Maçã", "Banana", "Uva"]
frutas[1] = 'Morango'
print(frutas)

cores = ("Azul", "Verde", "Vermelho")
cores[1] = 'Amarelo'
print(cores)
```

## Exercício 8
```python
numeros = (10,)

print(type(numeros))
```

## Exercício 9
```python
dados = ("Rafael", 27, 1.69, True)

print(dados[0])
print(dados[1])
print(type(dados[2]))
print(type(dados[3]))
print(type(dados))
```

## Exercício 10
```python
numeros = (15, 10, 25, 10, 30, 5, 10)

print(numeros[0])
print(numeros[-1])
print(numeros[2:5])
print(numeros[4:])
print(numeros.count(10))
print(numeros.index(10))
```
