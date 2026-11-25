## **Conversões entre tipos**

Agora vamos entender como converter valores de um tipo de dado para outro, combinando as funções que estudamos anteriormente.

As conversões podem acontecer entre diferentes tipos, dependendo do valor que queremos transformar.

### **1. Converter&#x20;**`str`**&#x20;para&#x20;**`int`

Podemos transformar um texto que contém um número inteiro em um valor numérico.

```
numero = '100'

numero_convertido = int(numero)

print(numero_convertido)
print(type(numero_convertido))
```

**Resultado:**

```
100
<class 'int'>
```

Antes da conversão, `'100'` era um texto. Depois, passou a ser um número inteiro.

### **2. Converter&#x20;**`str`**&#x20;para&#x20;**`float`

Também podemos transformar um texto que contém um número decimal em um valor `float`.

```
preco = '29.90'

preco_convertido = float(preco)

print(preco_convertido)
print(type(preco_convertido))
```

**Resultado:**

```
29.9
<class 'float'>
```

### **3. Converter&#x20;**`int`**&#x20;para&#x20;**`float`

Podemos transformar um número inteiro em decimal.

```
quantidade = 10

quantidade_decimal = float(quantidade)

print(quantidade_decimal)
print(type(quantidade_decimal))
```

**Resultado:**

```
10.0
<class 'float'>
```

### **4. Converter&#x20;**`float`**&#x20;para&#x20;**`int`

Também podemos fazer o caminho contrário, transformando um número decimal em inteiro.

```
media = 8.7

media_inteira = int(media)

print(media_inteira)
print(type(media_inteira))
```

**Resultado:**

```
8
<class 'int'>
```

Lembre-se: a conversão elimina as casas decimais, sem arredondar.

### **5. Converter&#x20;**`int`**&#x20;e&#x20;**`float`**&#x20;para&#x20;**`str`

Podemos transformar números em textos.

```
idade = 27
altura = 1.75

idade_texto = str(idade)
altura_texto = str(altura)

print(idade_texto)
print(altura_texto)

print(type(idade_texto))
print(type(altura_texto))
```

**Resultado:**

```
27
1.75
<class 'str'>
<class 'str'>
```

Isso é útil quando precisamos combinar números com mensagens.

```
idade = 27

mensagem = 'Minha idade é ' + str(idade)

print(mensagem)
```

**Resultado:**

```
Minha idade é 27
```

### **6. Converter valores para&#x20;**`bool`

Podemos converter diferentes tipos para valores lógicos.

```
print(bool(0))
print(bool(15))
print(bool(''))
print(bool('Python'))
```

**Resultado:**

```
False
True
False
True
```

Como vimos, zero e textos vazios resultam em `False`. Valores não vazios e números diferentes de zero resultam em `True`.

### **Resumo das conversões**

| Conversão             | Exemplo         | Resultado |
| --------------------- | --------------- | --------- |
| `str` → `int`         | `int('100')`    | `100`     |
| `str` → `float`       | `float('10.5')` | `10.5`    |
| `int` → `float`       | `float(10)`     | `10.0`    |
| `float` → `int`       | `int(10.8)`     | `10`      |
| `int` → `str`         | `str(100)`      | `'100'`   |
| `float` → `str`       | `str(10.5)`     | `'10.5'`  |
| Outros tipos → `bool` | `bool(0)`       | `False`   |
