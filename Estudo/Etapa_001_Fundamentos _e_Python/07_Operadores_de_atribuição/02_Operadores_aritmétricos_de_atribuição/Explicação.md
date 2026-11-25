## **Operadores&#x20;**`//=`**,&#x20;**`%=`**,&#x20;**`**=`

Esses três operadores seguem a mesma lógica dos anteriores: realizam uma operação matemática e armazenam o resultado na própria variável.

### **1. Divisão inteira com atribuição (**`//=`**)**

Divide o valor atual da variável por outro número, descartando a parte decimal do resultado.

```
numero = 17

numero //= 5

print(numero)
```

Resultado:

```
3
```

Equivalente a:

```
numero = numero // 5
```

### **2. Resto da divisão com atribuição (**`%=`**)**

Armazena o resto da divisão entre o valor atual da variável e outro número.

```
numero = 17

numero %= 5

print(numero)
```

Resultado:

```
2
```

Equivalente a:

```
numero = numero % 5
```

### **3. Potenciação com atribuição (**`**=`**)**

Eleva o valor atual da variável a uma potência e armazena o resultado.

```
numero = 2

numero **= 3

print(numero)
```

Resultado:

```
8
```

Equivalente a:

```
numero = numero ** 3
```

### **Resumo dos operadores de atribuição**

| Operador | Operação         | Exemplo                 | Resultado |
| -------- | ---------------- | ----------------------- | --------- |
| `=`      | Atribuição       | `numero = 10`           | 10        |
| `+=`     | Adição           | `numero += 5`           | 15        |
| `-=`     | Subtração        | `numero -= 3`           | 7         |
| `*=`     | Multiplicação    | `numero *= 3`           | 30        |
| `/=`     | Divisão          | `numero /= 2`           | 5.0       |
| `//=`    | Divisão inteira  | `numero //= 5` (com 17) | 3         |
| `%=`     | Resto da divisão | `numero %= 5` (com 17)  | 2         |
| `**=`    | Potenciação      | `numero **= 3` (com 2)  | 8         |

**Uma observação importante:** os operadores de atribuição modificam o valor da variável. Por exemplo, depois de `numero += 5`, a variável passa a armazenar o novo resultado.
