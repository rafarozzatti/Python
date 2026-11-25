## **Operadores de comparação**

Os **operadores de comparação** são utilizados para comparar dois valores. O resultado de uma comparação sempre será um valor booleano (`True` ou `False`).

Eles são muito utilizados para verificar se uma condição é verdadeira ou falsa.

### **Operadores disponíveis**

| Operador | Significado      | Exemplo    | Resultado |
| -------- | ---------------- | ---------- | --------- |
| `==`     | Igual a          | `10 == 10` | `True`    |
| `!=`     | Diferente de     | `10 != 5`  | `True`    |
| `>`      | Maior que        | `10 > 5`   | `True`    |
| `<`      | Menor que        | `10 < 5`   | `False`   |
| `>=`     | Maior ou igual a | `10 >= 10` | `True`    |
| `<=`     | Menor ou igual a | `5 <= 10`  | `True`    |

### **Exemplos em Python**

**Exemplo 1 — Igualdade (**`==`**)**

Verifica se dois valores são iguais.

```
idade = 25

resultado = idade == 25

print(resultado)
```

Resultado:

```
True
```

**Exemplo 2 — Diferença (**`!=`**)**

Verifica se dois valores são diferentes.

```
idade = 25

resultado = idade != 18

print(resultado)
```

Resultado:

```
True
```

**Exemplo 3 — Maior e menor**

```
nota = 7

print(nota > 5)
print(nota < 5)
```

Resultado:

```
True
False
```

**Exemplo 4 — Maior ou igual e menor ou igual**

```
idade = 18

print(idade >= 18)
print(idade <= 18)
```

Resultado:

```
True
True
```

### **Atenção:&#x20;**`=`**&#x20;é diferente de&#x20;**`==`

- `=` é utilizado para atribuir um valor a uma variável.
- `==` é utilizado para comparar dois valores.

```
idade = 25       # Atribuição

print(idade == 25)  # Comparação
```

Resultado:

```
True
```

**Resumo:** os operadores de comparação verificam relações entre valores e retornam `True` ou `False`.
