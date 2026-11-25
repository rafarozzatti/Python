## **Adição, subtração, multiplicação e divisão**

Os operadores aritméticos são utilizados para realizar operações matemáticas em Python.

Os quatro operadores básicos são:

| Operação      | Operador | Exemplo  |
| ------------- | -------- | -------- |
| Adição        | `+`      | `10 + 5` |
| Subtração     | `-`      | `10 - 5` |
| Multiplicação | `*`      | `10 * 5` |
| Divisão       | `/`      | `10 / 5` |

### **1. Adição (**`+`**)**

Utilizada para somar dois ou mais valores.

```
numero1 = 10
numero2 = 5

resultado = numero1 + numero2

print(resultado)
```

**Resultado:**

```
15
```

### **2. Subtração (**`-`**)**

Utilizada para calcular a diferença entre valores.

```
numero1 = 10
numero2 = 5

resultado = numero1 - numero2

print(resultado)
```

**Resultado:**

```
5
```

Também podemos obter resultados negativos:

```
resultado = 5 - 10

print(resultado)
```

**Resultado:**

```
-5
```

### **3. Multiplicação (**`*`**)**

Utilizada para multiplicar valores.

```
numero1 = 10
numero2 = 5

resultado = numero1 * numero2

print(resultado)
```

**Resultado:**

```
50
```

### **4. Divisão (**`/`**)**

Utilizada para dividir um valor por outro.

```
numero1 = 10
numero2 = 5

resultado = numero1 / numero2

print(resultado)
```

**Resultado:**

```
2.0
```

**Uma característica importante:** o operador `/` sempre retorna um resultado do tipo `float`, mesmo quando a divisão é exata.

Outro exemplo:

```
resultado = 9 / 3

print(resultado)
print(type(resultado))
```

**Resultado:**

```
3.0
<class 'float'>
```

Se tentarmos dividir um número por zero, o Python gera um erro chamado `ZeroDivisionError`.

```
resultado = 10 / 0
```

**Resultado:**

```
ZeroDivisionError: division by zero
```

Isso acontece porque não existe divisão por zero na matemática.

### **Resumo**

| Operador | Nome          | Exemplo  | Resultado |
| -------- | ------------- | -------- | --------- |
| `+`      | Adição        | `10 + 5` | `15`      |
| `-`      | Subtração     | `10 - 5` | `5`       |
| `*`      | Multiplicação | `10 * 5` | `50`      |
| `/`      | Divisão       | `10 / 5` | `2.0`     |
