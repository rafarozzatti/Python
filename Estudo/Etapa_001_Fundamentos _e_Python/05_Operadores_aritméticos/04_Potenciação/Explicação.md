## **Potenciação (**`**`**)**

O operador `**` é utilizado para realizar operações de potenciação, ou seja, elevar um número a uma determinada potência.

Na matemática, por exemplo:

\\[ 2^3 = 2 \times 2 \times 2 = 8 \\]

Em Python, utilizamos dois asteriscos (`**`) para representar essa operação.

### **1. Exemplo básico**

```
resultado = 2 ** 3

print(resultado)
```

**Resultado:**

```
8
```

Nesse exemplo:

- `2` é a base.
- `3` é o expoente.
- `8` é o resultado.

### **2. Outros exemplos**

```
print(5 ** 2)
print(3 ** 3)
print(10 ** 2)
print(2 ** 4)
```

**Resultado:**

```
25
27
100
16
```

### **3. Potência com expoente zero**

Qualquer número diferente de zero elevado a zero resulta em 1.

```
print(5 ** 0)
print(10 ** 0)
print(100 ** 0)
```

**Resultado:**

```
1
1
1
```

### **4. Potência com expoente negativo**

Também podemos utilizar expoentes negativos.

Nesse caso, o resultado corresponde ao inverso da potência positiva.

\\[ 2^{-3} = \frac{1}{2^3} = \frac{1}{8} \\]

```
resultado = 2 ** -3

print(resultado)
```

**Resultado:**

```
0.125
```

### **5. Potência com números decimais**

O operador também funciona com valores `float`.

```
base = 2.5
expoente = 2

resultado = base ** expoente

print(resultado)
```

**Resultado:**

```
6.25
```

### **Resumo**

| Operação          | Exemplo    | Resultado |
| ----------------- | ---------- | --------- |
| Potência simples  | `2 ** 3`   | `8`       |
| Expoente 2        | `5 ** 2`   | `25`      |
| Expoente 0        | `10 ** 0`  | `1`       |
| Expoente negativo | `2 ** -3`  | `0.125`   |
| Base decimal      | `2.5 ** 2` | `6.25`    |
