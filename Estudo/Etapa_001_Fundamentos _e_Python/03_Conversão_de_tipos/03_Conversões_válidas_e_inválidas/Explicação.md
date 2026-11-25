## **Conversões válidas e inválidas**

Nem todo valor pode ser convertido para qualquer tipo de dado. Algumas conversões funcionam normalmente, enquanto outras geram erros.

Vamos entender a diferença.

### **1. Conversões válidas**

São conversões que o Python consegue realizar.

**Texto numérico para inteiro:**

```
numero = int('100')

print(numero)
```

Resultado:

```
100
```

**Texto numérico decimal para&#x20;**`float`**:**

```
preco = float('19.90')

print(preco)
```

Resultado:

```
19.9
```

**Número para texto:**

```
texto = str(250)

print(texto)
```

Resultado:

```
250
```

**Inteiro para decimal:**

```
numero = float(15)

print(numero)
```

Resultado:

```
15.0
```

### **2. Conversões inválidas**

São conversões que o Python não consegue realizar porque o conteúdo não representa um valor compatível com o tipo desejado.

**Texto que não representa um número inteiro:**

```
numero = int('Python')
```

Resultado:

```
ValueError: invalid literal for int()
```

O erro acontece porque `'Python'` não representa um número inteiro.

**Texto com letras para decimal:**

```
numero = float('abc')
```

Resultado:

```
ValueError: could not convert string to float
```

**Texto com número decimal convertido diretamente para inteiro:**

```
numero = int('10.5')
```

Resultado:

```
ValueError: invalid literal for int()
```

Nesse caso, `'10.5'` é um texto decimal. Para converter corretamente, primeiro precisamos transformá-lo em `float` e depois em `int`:

```
numero = int(float('10.5'))

print(numero)
```

Resultado:

```
10
```

### **3. Atenção: conversão não significa validação do conteúdo**

Uma conversão pode funcionar mesmo quando o resultado não representa o que esperamos.

Por exemplo:

```
valor = bool('False')

print(valor)
```

Resultado:

```
True
```

Isso acontece porque `'False'` é um texto não vazio. O `bool()` não interpreta a palavra como uma resposta lógica; ele verifica se o valor é vazio ou não.

Da mesma forma:

```
valor = bool('0')

print(valor)
```

Resultado:

```
True
```

Já o número zero resulta em `False`:

```
valor = bool(0)

print(valor)
```

Resultado:

```
False
```

### **4. Tabela de conversões**

| Conversão | Exemplo              | Resultado    |
| --------- | -------------------- | ------------ |
| Válida    | `int('100')`         | `100`        |
| Válida    | `float('10.5')`      | `10.5`       |
| Válida    | `str(100)`           | `'100'`      |
| Válida    | `int(float('10.5'))` | `10`         |
| Inválida  | `int('Python')`      | `ValueError` |
| Inválida  | `float('abc')`       | `ValueError` |
| Inválida  | `int('10.5')`        | `ValueError` |
