# Tuplas em Python

## 1. O que são tuplas?

Tuplas são estruturas utilizadas para armazenar vários valores em uma única variável, assim como as listas.

A principal diferença é que tuplas são imutáveis, ou seja, depois de criadas, não podemos alterar, adicionar ou remover seus elementos.

Veja a comparação:

Lista:

```
frutas = ["Maçã", "Banana", "Uva"]
```

Tupla:

```
frutas = ("Maçã", "Banana", "Uva")
```

Observe a diferença:

- Listas utilizam colchetes `[]`.
- Tuplas utilizam parênteses `()`.

## 2. Criando tuplas

Podemos criar tuplas contendo diferentes tipos de dados:

```
dados = ("Rafael", 27, 1.69, True)

print(dados)
```

Saída:

```
("Rafael", 27, 1.69, True)
```

Também podemos criar uma tupla com apenas um elemento.

Nesse caso, precisamos colocar uma vírgula depois do elemento:

```
numeros = (10,)

print(type(numeros))
```

Saída:

```
<class 'tuple'>
```

Sem a vírgula, o Python interpreta os parênteses apenas como agrupamento:

```
numeros = (10)

print(type(numeros))
```

Saída:

```
<class 'int'>
```

## 3. Acessando elementos

Assim como nas listas e strings, podemos acessar os elementos de uma tupla utilizando índices positivos e negativos.

Considere:

```
frutas = ("Maçã", "Banana", "Uva", "Laranja")
```

| Elemento | Índice positivo | Índice negativo |
| -------- | --------------- | --------------- |
| Maçã     | 0               | -4              |
| Banana   | 1               | -3              |
| Uva      | 2               | -2              |
| Laranja  | 3               | -1              |

Exemplo:

```
print(frutas[0])
print(frutas[2])
print(frutas[-1])
```

Saída:

```
Maçã
Uva
Laranja
```

## 4. Fatiamento de tuplas

Também podemos utilizar fatiamento, assim como fizemos com strings e listas.

```
numeros = (10, 20, 30, 40, 50)

print(numeros[0:3])
print(numeros[2:])
print(numeros[::-1])
```

Saída:

```
(10, 20, 30)
(30, 40, 50)
(50, 40, 30, 20, 10)
```

Observe que o resultado continua sendo uma tupla, representada por parênteses.

## 5. Imutabilidade das tuplas

Essa é a característica mais importante desse conteúdo.

Observe:

```
frutas = ("Maçã", "Banana", "Uva")

frutas[1] = "Morango"
```

Esse código gera um erro:

```
TypeError: 'tuple' object does not support item assignment
```

Isso acontece porque não podemos substituir elementos de uma tupla.

Também não podemos utilizar métodos como `append()`, `insert()` ou `remove()` diretamente em uma tupla.

## 6. Métodos `count()` e `index()`

Apesar de serem imutáveis, as tuplas possuem alguns métodos úteis.

`count()` — conta quantas vezes um elemento aparece.

```
numeros = (10, 20, 10, 30, 10, 40)

print(numeros.count(10))
```

Saída:

```
3
```

`index()` — retorna o índice da primeira ocorrência de um elemento.

```
frutas = ("Maçã", "Banana", "Uva", "Laranja")

print(frutas.index("Uva"))
```

Saída:

```
2
```

Se o elemento aparecer mais de uma vez, `index()` retorna a posição da primeira ocorrência.

## Resumo — Tuplas

| Operação        | Exemplo                | Função                         |
| --------------- | ---------------------- | ------------------------------ |
| Criação         | `tupla = (10, 20, 30)` | Cria uma tupla                 |
| Acesso          | `tupla[0]`             | Acessa um elemento             |
| Índice negativo | `tupla[-1]`            | Acessa o último elemento       |
| Fatiamento      | `tupla[0:2]`           | Extrai parte da tupla          |
| `count()`       | `tupla.count(10)`      | Conta ocorrências              |
| `index()`       | `tupla.index(20)`      | Localiza a primeira ocorrência |

Lembre-se: listas podem ser modificadas; tuplas não podem.
