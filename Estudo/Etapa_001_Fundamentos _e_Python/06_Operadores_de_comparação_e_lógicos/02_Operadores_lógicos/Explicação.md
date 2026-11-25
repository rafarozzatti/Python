## **Operadores lógicos (**`and`**,&#x20;**`or`**&#x20;e&#x20;**`not`**)**

Os **operadores lógicos** são utilizados para combinar ou inverter condições.

Assim como os operadores de comparação, eles retornam valores booleanos: `True` ou `False`.

Python possui três operadores lógicos principais:

- `and`
- `or`
- `not`

### **1. Operador&#x20;**`and`**&#x20;(E)**

O `and` retorna `True` somente quando **todas as condições são verdadeiras**.

```
idade = 25
renda = 3000

resultado = idade >= 18 and renda >= 2000

print(resultado)
```

Resultado:

```
True
```

As duas condições são verdadeiras:

- `idade >= 18` → `True`
- `renda >= 2000` → `True`

Se uma das condições for falsa, o resultado será `False`.

```
idade = 25
renda = 1500

resultado = idade >= 18 and renda >= 2000

print(resultado)
```

Resultado:

```
False
```

### **2. Operador&#x20;**`or`**&#x20;(OU)**

O `or` retorna \`True quando **pelo menos uma das condições é verdadeira**.

```
idade = 17
autorizacao = True

resultado = idade >= 18 or autorizacao == True

print(resultado)
```

Resultado:

```
True
```

A primeira condição é falsa, mas a segunda é verdadeira. Portanto, o resultado é `True`.

Somente quando todas as condições forem falsas o resultado será `False`.

### **3. Operador&#x20;**`not`**&#x20;(NÃO)**

O `not` inverte o resultado de uma condição:

- `not True` → `False`
- `not False` → `True`

Exemplo:

```
ativo = True

resultado = not ativo

print(resultado)
```

Resultado:

```
False
```

Como `ativo` é `True`, o `not` inverte o resultado para `False`.

### **4. Tabela-verdade**

A tabela abaixo resume o funcionamento dos operadores:

| Condição A | Condição B | `and` | `or`  |
| ---------- | ---------- | ----- | ----- |
| True       | True       | True  | True  |
| True       | False      | False | True  |
| False      | True       | False | True  |
| False      | False      | False | False |

Para o `not`:

| Condição | `not` |
| -------- | ----- |
| True     | False |
| False    | True  |

**Resumo:**

- `and`: todas as condições precisam ser verdadeiras.
- `or`: pelo menos uma condição precisa ser verdadeira.
- `not`: inverte o resultado da condição.
