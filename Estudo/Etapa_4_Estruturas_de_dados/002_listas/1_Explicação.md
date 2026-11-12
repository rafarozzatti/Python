# Listas em Python

## 1. O que são listas?

Uma lista permite armazenar vários valores dentro de uma única variável.

Por exemplo, imagine que queremos armazenar nomes de pessoas.

Sem listas, precisaríamos criar várias variáveis:

```
nome1 = "Rafael"
nome2 = "Ana"
nome3 = "Carlos"
```

Com uma lista, podemos fazer isso de maneira mais organizada:

```
nomes = ["Rafael", "Ana", "Carlos"]
```

Observe algumas características:

- Listas são criadas utilizando colchetes `[]`.
- Os elementos são separados por vírgulas.
- Uma lista pode armazenar textos, números e até diferentes tipos de dados.
- Os elementos possuem índices, assim como acontece com strings.

Exemplo:

```
dados = ["Rafael", 27, 1.69, True]
```

## 2. Acessando elementos de uma lista

Assim como nas strings, podemos acessar os elementos utilizando índices.

Considere:

```
frutas = ["Maçã", "Banana", "Uva", "Laranja"]
```

| Elemento | Índice positivo | Índice negativo |
| -------- | --------------- | --------------- |
| Maçã     | 0               | -4              |
| Banana   | 1               | -3              |
| Uva      | 2               | -2              |
| Laranja  | 3               | -1              |

Exemplos:

```
frutas = ["Maçã", "Banana", "Uva", "Laranja"]

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

Também podemos acessar uma parte da lista utilizando fatiamento:

```
print(frutas[0:2])
```

Saída:

```
["Maçã", "Banana"]
```

## 3. Alterando elementos de uma lista

Uma característica importante das listas é que podemos modificar seus elementos depois de criá-las.

Exemplo:

```
frutas = ["Maçã", "Banana", "Uva"]

frutas[1] = "Morango"

print(frutas)
```

Saída:

```
["Maçã", "Morango", "Uva"]
```

Nesse caso, substituímos o elemento que estava no índice `1`.

## 4. Adicionando elementos

Agora vamos conhecer três métodos para adicionar elementos.

`append()` — adiciona um elemento ao final da lista.

```
frutas = ["Maçã", "Banana"]

frutas.append("Uva")

print(frutas)
```

Saída:

```
["Maçã", "Banana", "Uva"]
```

`extend()` — adiciona vários elementos ao final da lista.

```
frutas = ["Maçã", "Banana"]

frutas.extend(["Uva", "Laranja"])

print(frutas)
```

Saída:

```
["Maçã", "Banana", "Uva", "Laranja"]
```

A diferença entre `append()` e `extend()` é importante:

```
numeros = [1, 2]

numeros.append([3, 4])

print(numeros)
```

Resultado:

```
[1, 2, [3, 4]]
```

Já com `extend()`:

```
numeros = [1, 2]

numeros.extend([3, 4])

print(numeros)
```

Resultado:

```
[1, 2, 3, 4]
```

`insert()` — adiciona um elemento em uma posição específica.

Estrutura:

```
lista.insert(indice, elemento)
```

Exemplo:

```
frutas = ["Maçã", "Uva"]

frutas.insert(1, "Banana")

print(frutas)
```

Saída:

```
["Maçã", "Banana", "Uva"]
```

O elemento `Banana` foi inserido no índice `1`, e os outros elementos foram deslocados.

## 5. Removendo elementos

Também temos métodos específicos para remover elementos.

`pop()` — remove um elemento pelo índice.

```
frutas = ["Maçã", "Banana", "Uva"]

frutas.pop(1)

print(frutas)
```

Saída:

```
["Maçã", "Uva"]
```

Se não informarmos um índice, `pop()` remove o último elemento:

```
frutas.pop()
```

`remove()` — remove um elemento pelo seu valor.

```
frutas = ["Maçã", "Banana", "Uva"]

frutas.remove("Banana")

print(frutas)
```

Saída:

```
["Maçã", "Uva"]
```

Atenção à diferença:

| Método     | Remove utilizando |
| ---------- | ----------------- |
| `pop()`    | Índice            |
| `remove()` | Valor             |

## 6. Ordenando listas com `sort()`

O método `sort()` organiza os elementos da lista em ordem crescente.

Exemplo com números:

```
numeros = [5, 2, 8, 1, 3]

numeros.sort()

print(numeros)
```

Saída:

```
[1, 2, 3, 5, 8]
```

Com textos:

```
nomes = ["Carlos", "Ana", "Rafael", "Bruno"]

nomes.sort()

print(nomes)
```

Saída:

```
["Ana", "Bruno", "Carlos", "Rafael"]
```

Para ordenar em ordem decrescente, podemos utilizar `reverse=True`:

```
numeros = [5, 2, 8, 1, 3]

numeros.sort(reverse=True)

print(numeros)
```

Saída:

```
[8, 5, 3, 2, 1]
```

## Resumo dos métodos

| Método     | Função                             |
| ---------- | ---------------------------------- |
| `append()` | Adiciona um elemento ao final      |
| `extend()` | Adiciona vários elementos          |
| `insert()` | Adiciona em uma posição específica |
| `pop()`    | Remove pelo índice                 |
| `remove()` | Remove pelo valor                  |
| `sort()`   | Ordena os elementos                |
