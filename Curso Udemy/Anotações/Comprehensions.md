# Comprehensions em Python

## **O que são comprehensions?**

Comprehensions são uma forma concisa e eficiente de criar estruturas de dados como listas, dicionários e conjuntos em Python. Elas tornam o código mais legível e expressivo.

---

## **1. List Comprehension**

A **List Comprehension** é uma maneira compacta de criar listas a partir de iteráveis.

### **Sem List Comprehension:**

```python
# Criando uma lista com os quadrados de 0 a 9
quadrados = []
for x in range(10):
    quadrados.append(x ** 2)
print(quadrados)
```

### **Com List Comprehension:**

```python
quadrados = [x ** 2 for x in range(10)]
print(quadrados)
```

**Saída:**

```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### **Com List Comprehension e Condição:**

```python
# Criando uma lista apenas com os números pares de 0 a 9
pares = [x for x in range(10) if x % 2 == 0]
print(pares)
```

**Saída:**

```
[0, 2, 4, 6, 8]
```

---

## **2. Dictionary Comprehension**

A **Dictionary Comprehension** permite criar dicionários de forma mais simples e direta.

### **Sem Dictionary Comprehension:**

```python
quadrados_dict = {}
for x in range(5):
    quadrados_dict[x] = x ** 2
print(quadrados_dict)
```

### **Com Dictionary Comprehension:**

```python
quadrados_dict = {x: x ** 2 for x in range(5)}
print(quadrados_dict)
```

**Saída:**

```
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### **Com Dictionary Comprehension e Condição:**

```python
# Criando um dicionário apenas com números ímpares
impares_dict = {x: x ** 2 for x in range(10) if x % 2 != 0}
print(impares_dict)
```

**Saída:**

```
{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
```

---

## **3. Set Comprehension**

A **Set Comprehension** é usada para criar conjuntos de maneira eficiente.

### **Sem Set Comprehension:**

```python
quadrados_set = set()
for x in range(10):
    quadrados_set.add(x ** 2)
print(quadrados_set)
```

### **Com Set Comprehension:**

```python
quadrados_set = {x ** 2 for x in range(10)}
print(quadrados_set)
```

**Saída:**

```
{0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
```

### **Com Set Comprehension e Condição:**

```python
# Criando um conjunto apenas com números múltiplos de 3
multiplos_de_3 = {x for x in range(20) if x % 3 == 0}
print(multiplos_de_3)
```

**Saída:**

```
{0, 3, 6, 9, 12, 15, 18}
```

---

## **4. Generator Comprehension**

A **Generator Comprehension** funciona de maneira semelhante à List Comprehension, mas em vez de criar uma lista, ela gera um iterador eficiente.

### **Sem Generator Comprehension:**

```python
def gerar_quadrados():
    for x in range(10):
        yield x ** 2
quadrados_gen = gerar_quadrados()
print(list(quadrados_gen))
```

### **Com Generator Comprehension:**

```python
quadrados_gen = (x ** 2 for x in range(10))
print(list(quadrados_gen))
```

**Saída:**

```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---

## **Conclusão**

As comprehensions são uma forma poderosa de escrever código mais conciso e eficiente. Dependendo do caso, você pode usar:

- **List Comprehension** para criar listas rapidamente.
- **Dictionary Comprehension** para criar dicionários de forma compacta.
- **Set Comprehension** para criar conjuntos sem elementos duplicados.
- **Generator Comprehension** para criar iteradores eficientes sem consumir muita memória.