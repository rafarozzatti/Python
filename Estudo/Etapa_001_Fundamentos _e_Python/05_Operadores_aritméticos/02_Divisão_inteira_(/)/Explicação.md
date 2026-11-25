## **Divisão inteira (**`//`**)**

O operador `//` realiza uma divisão e retorna o resultado sem a parte decimal.

Diferentemente do operador `/`, que retorna um valor `float`, o `//` realiza o arredondamento para baixo (*floor division*).

### **1. Divisão inteira com resultado exato**

```
numero1 = 10
numero2 = 2

resultado = numero1 // numero2

print(resultado)
```

**Resultado:**

```
5
```

### **2. Divisão inteira com resultado decimal**

Quando a divisão não é exata, o Python retorna o inteiro inferior mais próximo, considerando a reta numérica.

```
numero1 = 10
numero2 = 3

resultado = numero1 // numero2

print(resultado)
```

**Resultado:**

```
3
```

Observe a diferença:

```
print(10 / 3)
print(10 // 3)
```

**Resultado:**

```
3.3333333333333335
3
```

### **3. Divisão inteira com números negativos**

A divisão inteira também funciona com números negativos.

```
print(-10 // 3)
print(10 // -3)
```

**Resultado:**

```
-4
-4
```

Isso acontece porque o resultado é arredondado para baixo, e não simplesmente porque a parte decimal é removida.

### **4. Tipo do resultado**

O tipo retornado depende dos tipos utilizados na operação.

```
print(type(10 // 2))
print(type(10.0 // 2))
```

**Resultado:**

```
<class 'int'>
<class 'float'>
```

Portanto, quando os dois operandos são inteiros, o resultado também é inteiro. Se algum deles for `float`, o resultado será `float`.

### **Comparação entre&#x20;**`/`**&#x20;e&#x20;**`//`

| Operador | Função          | Exemplo   | Resultado  |
| -------- | --------------- | --------- | ---------- |
| `/`      | Divisão comum   | `10 / 3`  | `3.333...` |
| `//`     | Divisão inteira | `10 // 3` | `3`        |

**Aplicação prática:** imagine que temos 17 produtos e queremos montar caixas com 5 produtos cada.

```
produtos = 17
por_caixa = 5

caixas_completas = produtos // por_caixa

print(caixas_completas)
```

**Resultado:**

```
3
```

Conseguimos montar 3 caixas completas.
