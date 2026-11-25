## **Funções&#x20;**`int()`**,&#x20;**`float()`**,&#x20;**`str()`**&#x20;e&#x20;**`bool()`

Em Python, podemos converter um valor de um tipo de dado para outro.

Por exemplo, transformar um número inteiro em texto ou um número decimal em inteiro.

Para isso, utilizamos as funções de conversão:

- `int()`: converte um valor para inteiro.
- `float()`: converte um valor para decimal.
- `str()`: converte um valor para texto.
- `bool()`: converte um valor para lógico (`True` ou `False`).

### **1. Função&#x20;**`int()`

A função `int()` converte um valor para número inteiro.

```
numero = int(10.8)

print(numero)
print(type(numero))
```

**Resultado:**

```
10
<class 'int'>
```

Observe que a conversão de um número decimal para inteiro elimina a parte decimal. Ela não arredonda o número.

Outro exemplo:

```
numero = int(25.9)

print(numero)
```

**Resultado:**

```
25
```

### **2. Função&#x20;**`float()`

A função `float()` converte um valor para número decimal.

```
numero = float(10)

print(numero)
print(type(numero))
```

**Resultado:**

```
10.0
<class 'float'>
```

Mesmo que o valor original seja inteiro, após a conversão ele passa a ser decimal.

Também podemos converter textos numéricos:

```
preco = float('29.90')

print(preco)
print(type(preco))
```

**Resultado:**

```
29.9
<class 'float'>
```

### **3. Função&#x20;**`str()`

A função `str()` converte um valor para texto.

```
numero = 100

texto = str(numero)

print(texto)
print(type(texto))
```

**Resultado:**

```
100
<class 'str'>
```

Visualmente, o resultado continua sendo `100`, mas agora é um texto, não um número.

Outro exemplo:

```
preco = 29.90

texto = str(preco)

print(texto)
print(type(texto))
```

**Resultado:**

```
29.9
<class 'str'>
```

Essa conversão pode ser útil quando precisamos juntar informações numéricas com textos.

### **4. Função&#x20;**`bool()`

A função `bool()` converte um valor para verdadeiro (`True`) ou falso (`False`).

A regra principal é:

- Valores considerados vazios ou zero resultam em `False`.
- Valores diferentes de zero ou não vazios resultam em `True`.

**Exemplos com números:**

```
print(bool(0))
print(bool(1))
print(bool(-5))
print(bool(10.5))
```

**Resultado:**

```
False
True
True
True
```

**Exemplos com textos:**

```
print(bool(''))
print(bool('Python'))
print(bool('0'))
```

**Resultado:**

```
False
True
True
```

Observe que `'0'` resulta em `True`, pois é um texto que contém um caractere. Ele não é o número zero.

**Exemplos com outros valores:**

```
print(bool(None))
print(bool([]))
print(bool([1, 2, 3]))
```

**Resultado:**

```
False
False
True
```

Aqui, `None` representa ausência de valor, `[]` representa uma lista vazia e `[1, 2, 3]` representa uma lista preenchida.

### **Resumo das funções**

| Função    | Conversão    | Exemplo              |
| --------- | ------------ | -------------------- |
| `int()`   | Para inteiro | `int(10.8)` → `10`   |
| `float()` | Para decimal | `float(10)` → `10.0` |
| `str()`   | Para texto   | `str(100)` → `'100'` |
| `bool()`  | Para lógico  | `bool(0)` → `False`  |
