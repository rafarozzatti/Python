# 8. Operadores lógicos em Python

Os operadores lógicos permitem combinar condições ou inverter um resultado. Eles trabalham com valores booleanos: `True` e `False`.

Vamos aprender os três operadores do nosso plano: `and`, `or` e `not`.

## 1. Operador `and` — E

O `and` retorna `True` somente quando as duas condições são verdadeiras.

| Condição 1 | Condição 2 | Resultado |
| ---------- | ---------- | --------- |
| `True`     | `True`     | `True`    |
| `True`     | `False`    | `False`   |
| `False`    | `True`     | `False`   |
| `False`    | `False`    | `False`   |

Exemplo:

```
idade = 25resultado = idade >= 18 and idade <= 60print(resultado)
```

Saída:

```
True
```

Entendendo o código:

- `idade >= 18` → `True`, porque 25 é maior ou igual a 18.
- `idade <= 60` → `True`, porque 25 é menor ou igual a 60.
- `True and True` → `True`.

As duas condições precisam ser verdadeiras para o resultado ser `True`.

## 2. Operador `or` — OU

O `or` retorna `True` quando pelo menos uma das condições é verdadeira. Só retorna `False` quando as duas são falsas.

| Condição 1 | Condição 2 | Resultado |
| ---------- | ---------- | --------- |
| `True`     | `True`     | `True`    |
| `True`     | `False`    | `True`    |
| `False`    | `True`     | `True`    |
| `False`    | `False`    | `False`   |

Exemplo:

```
nota = 8resultado = nota >= 7 or nota == 10print(resultado)
```

Saída:

```
True
```

Entendendo o código:

- `nota >= 7` → `True`, porque 8 é maior que 7.
- `nota == 10` → `False`, porque 8 não é igual a 10.
- `True or False` → `True`.

Como pelo menos uma condição é verdadeira, o resultado final é `True`.

## 3. Operador `not` — NÃO

O `not` inverte o resultado lógico: transforma `True` em `False` e `False` em `True`.

| Condição | Resultado de `not` |
| -------- | ------------------ |
| `True`   | `False`            |
| `False`  | `True`             |

Exemplo:

```
estoque = 0resultado = not (estoque > 0)print(resultado)
```

Saída:

```
True
```

Entendendo o código:

- `estoque > 0` → `False`, porque o estoque é zero.
- `not False` → `True`.

Os parênteses deixam claro que primeiro fazemos a comparação e depois invertemos seu resultado.

## 4. Resumo para suas anotações

| Operador | Significado | Quando retorna `True`?                            |
| -------- | ----------- | ------------------------------------------------- |
| `and`    | E           | Quando todas as condições são verdadeiras         |
| `or`     | OU          | Quando pelo menos uma condição é verdadeira       |
| `not`    | NÃO         | Quando inverte uma condição falsa para verdadeira |

Esses operadores serão muito importantes quando chegarmos a `if`, `elif` e `else`. Por enquanto, vamos praticá-los sem usar estruturas condicionais.
