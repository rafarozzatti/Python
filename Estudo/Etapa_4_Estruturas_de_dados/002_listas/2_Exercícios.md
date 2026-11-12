# Exercícios de Listas

## Exercício 1

Crie uma lista chamada `frutas` contendo os seguintes elementos:

```
"Maçã", "Banana", "Uva", "Laranja", "Morango"
```

Depois, escreva um programa que exiba exatamente:

```
Maçã
Uva
Morango
```

Regras:

1. Utilize a lista `frutas`.
2. O primeiro elemento deve ser acessado com índice positivo.
3. O segundo elemento solicitado deve ser acessado com índice positivo.
4. O terceiro elemento solicitado deve ser acessado com índice negativo.
5. Utilize três comandos `print()`.

### Exercício 2do elementos

Considere a lista:

```
numeros = [10, 20, 30, 40, 50]
```

Altere os seguintes elementos:

- Substitua o `20` por `25`.
- Substitua o `40` por `45`.

Depois, exiba a lista completa:

```
[10, 25, 30, 45, 50]
```

Regras:

1. Utilize a lista `numeros`.
2. Faça as alterações diretamente na lista, utilizando os índices.
3. Não crie uma segunda lista.

### Exercício 3

Considere:

```
produtos = ["Notebook", "Mouse", "Teclado"]
```

Utilize o método `append()` para adicionar os seguintes produtos, nessa ordem:

- Monitor
- Headset

Depois, exiba a lista completa.

Saída esperada:

```
["Notebook", "Mouse", "Teclado", "Monitor", "Headset"]
```

### Exercício 4

Considere:

```
numeros = [1, 2, 3]
```

Utilize o método `extend()` para adicionar os números `4`, `5` e `6` à lista.

Saída esperada:

```
[1, 2, 3, 4, 5, 6]
```

Regra: utilize apenas uma chamada de `extend()` para adicionar os três números.

### Exercício 5

Considere:

```
nomes = ["Ana", "Carlos", "Pedro", "Mariana"]
```

Utilize `insert()` para adicionar o nome `"Rafael"` na posição de índice `2`.

Depois, exiba a lista completa.

Saída esperada:

```
["Ana", "Carlos", "Rafael", "Pedro", "Mariana"]
```

### Exercício 6

Considere:

```
numeros = [10, 20, 30, 40, 50]
```

Utilize `pop()` para remover o elemento que está no índice `2`.

Depois, exiba a lista completa.

Saída esperada:

```
[10, 20, 40, 50]
```

Regra: remova o elemento utilizando seu índice, não seu valor.

### Exercício 7

Considere:

```
frutas = ["Maçã", "Banana", "Uva", "Laranja", "Morango"]
```

Utilize `remove()` para remover o elemento `"Uva"`.

Depois, exiba a lista completa.

Saída esperada:

```
["Maçã", "Banana", "Laranja", "Morango"]
```

Regra: remova o elemento utilizando seu valor, não seu índice.

### Exercício 8

Considere:

```
numeros = [8, 3, 10, 1, 5, 2]
```

Utilize `sort()` para organizar os números em ordem crescente.

Depois, exiba a lista completa.

Saída esperada:

```
[1, 2, 3, 5, 8, 10]
```

### Exercício 9

Considere:

```
nomes = ["Carlos", "Ana", "Rafael", "Bruno", "Mariana"]
```

Utilize `sort()` para organizar os nomes em ordem alfabética decrescente (Z até A).

Depois, exiba a lista completa.

Saída esperada:

```
["Rafael", "Mariana", "Carlos", "Bruno", "Ana"]
```

### Exercício 10

Considere:

```
produtos = ["Notebook", "Mouse", "Teclado", "Monitor"]
```

Realize as seguintes operações, nesta ordem:

1. Adicione `"Headset"` ao final da lista utilizando `append()`.
2. Adicione `"Webcam"` e `"Microfone"` utilizando uma única chamada de `extend()`.
3. Insira `"Gabinete"` na posição de índice `2`, utilizando `insert()`.
4. Remova `"Mouse"` utilizando `remove()`.
5. Remova o último elemento utilizando `pop()`.
6. Organize a lista em ordem alfabética utilizando `sort()`.

Ao final, exiba a lista completa.

Saída esperada:

```
["Gabinete", "Headset", "Monitor", "Notebook", "Teclado", "Webcam"]
```
