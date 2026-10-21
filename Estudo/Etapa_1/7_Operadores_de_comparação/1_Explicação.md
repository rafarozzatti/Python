# 7. Operadores de comparação em Python

Os operadores de comparação são usados para comparar dois valores. O resultado da comparação será sempre um valor booleano: `True` (verdadeiro) ou `False` (falso).

Vamos estudar os seis operadores do nosso plano.

## 1. Conhecendo os operadores

| Operador | Significado      | Exemplo    | Resultado |
| -------- | ---------------- | ---------- | --------- |
| `==`     | Igual a          | `10 == 10` | `True`    |
| `!=`     | Diferente de     | `10 != 5`  | `True`    |
| `>`      | Maior que        | `10 > 5`   | `True`    |
| `<`      | Menor que        | `3 < 8`    | `True`    |
| `>=`     | Maior ou igual a | `10 >= 10` | `True`    |
| `<=`     | Menor ou igual a | `5 <= 3`   | `False`   |

Observe que `5 <= 3` retorna `False`, porque 5 não é menor nem igual a 3.

## 2. Exemplos práticos

### Operador `==` — Igual a

Verifica se dois valores são iguais.

```
numero1 = 10numero2 = 10print(numero1 == numero2)
```

Resultado:

```
True
```

Como os dois valores são iguais, o resultado é `True`.

### Operador `!=` — Diferente de

Verifica se dois valores são diferentes.

```
numero1 = 10numero2 = 5print(numero1 != numero2)
```

Resultado:

```
True
```

Como os valores são diferentes, o resultado é `True`.

### Operadores `>` e `<` — Maior e menor que

```
idade = 27print(idade > 18)print(idade < 18)
```

Resultado:

```
True
False
```

A primeira comparação é verdadeira, porque 27 é maior que 18. A segunda é falsa, porque 27 não é menor que 18.

### Operadores `>=` e `<=` — Maior ou igual e menor ou igual

A diferença é que esses operadores também consideram a igualdade.

```
nota = 7print(nota >= 7)print(nota <= 7)
```

Resultado:

```
True
True
```

As duas comparações são verdadeiras porque a nota é exatamente 7.

## 3. Cuidado com `=` e `==`

Essa diferença é muito importante:

- `=` atribui um valor a uma variável.
- `==` compara dois valores.

Exemplo:

```
numero = 10print(numero == 10)
```

Resultado:

```
True
```

Primeiro, atribuímos o valor `10` à variável. Depois, verificamos se ela é igual a `10`.

## 4. Comparações com `input()`

Também podemos comparar valores digitados pelo usuário. Lembre-se de que `input()` retorna um texto, então podemos converter a entrada para número com `int()`.

```
idade = int(input('Digite sua idade: '))print(idade >= 18)
```

Se o usuário digitar `20`, o resultado será:

```
True
```

Se digitar `15`, o resultado será:

```
False
```

Ainda não precisamos usar `if`. Por enquanto, vamos apenas realizar comparações e observar os resultados.
