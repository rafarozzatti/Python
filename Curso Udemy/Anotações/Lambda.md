# Lambda

## **Cenário: Ordenando uma lista de tuplas**
Imagine que temos uma lista de produtos e seus preços, e queremos ordená-los pelo preço:

### **Usando `def` (função normal):**
```python
def ordenar_por_preco(produto):
    return produto[1]  # Retorna o preço

produtos = [('Celular', 1500), ('Notebook', 3500), ('Fone de Ouvido', 200)]
produtos_ordenados = sorted(produtos, key=ordenar_por_preco)

print(produtos_ordenados)
```
**Saída:**
```
[('Fone de Ouvido', 200), ('Celular', 1500), ('Notebook', 3500)]
```

### **Usando `lambda` (mais curto e direto):**
```python
produtos = [('Celular', 1500), ('Notebook', 3500), ('Fone de Ouvido', 200)]
produtos_ordenados = sorted(produtos, key=lambda produto: produto[1])

print(produtos_ordenados)
```
**Saída:**
```
[('Fone de Ouvido', 200), ('Celular', 1500), ('Notebook', 3500)]
```

## **Por que usar `lambda` aqui?**
- Evita ter que criar uma função com `def` só para um uso simples.
- Deixa o código mais curto e direto.
- Útil quando você precisa de uma função rápida dentro de outra função, como `sorted()`, `map()`, `filter()`, etc.


## **Usando `lambda` em outras funções**
A principal utilidade de `lambda` é quando você precisa passar uma função como argumento para outra função. Isso acontece muito em funções como `sorted()`, `map()`, `filter()` e `reduce()`.

### **1️⃣ Usando `lambda` com `map()`**
O `map()` aplica uma função a cada item de um iterável (como uma lista).

🔹 **Sem `lambda` (usando `def`):**
```python
def quadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
resultado = list(map(quadrado, numeros))

print(resultado)  # [1, 4, 9, 16, 25]
```
🔹 **Com `lambda` (mais curto e direto):**
```python
numeros = [1, 2, 3, 4, 5]
resultado = list(map(lambda x: x ** 2, numeros))

print(resultado)  # [1, 4, 9, 16, 25]
```
✅ **Por que usar `lambda`?**  
Evita a necessidade de criar a função `quadrado()`, já que só vamos usá-la dentro do `map()`.

---

### **2️⃣ Usando `lambda` com `filter()`**
O `filter()` filtra os elementos de um iterável com base em uma condição.

🔹 **Sem `lambda`:**
```python
def maior_que_10(x):
    return x > 10

numeros = [5, 10, 15, 20, 25]
resultado = list(filter(maior_que_10, numeros))

print(resultado)  # [15, 20, 25]
```
🔹 **Com `lambda`:**
```python
numeros = [5, 10, 15, 20, 25]
resultado = list(filter(lambda x: x > 10, numeros))

print(resultado)  # [15, 20, 25]
```
✅ **Por que usar `lambda`?**  
A função `maior_que_10()` só é usada no `filter()`, então `lambda` deixa o código mais compacto.

---

### **3️⃣ Usando `lambda` com `sorted()`**
O `sorted()` pode ordenar com base em critérios personalizados.

🔹 **Ordenar palavras pelo tamanho (sem `lambda`):**
```python
def tamanho(palavra):
    return len(palavra)

palavras = ["banana", "maçã", "uva", "abacaxi"]
ordenadas = sorted(palavras, key=tamanho)

print(ordenadas)  # ['uva', 'maçã', 'banana', 'abacaxi']
```
🔹 **Com `lambda`:**
```python
palavras = ["banana", "maçã", "uva", "abacaxi"]
ordenadas = sorted(palavras, key=lambda palavra: len(palavra))

print(ordenadas)  # ['uva', 'maçã', 'banana', 'abacaxi']
```
✅ **Por que usar `lambda`?**  
Evita criar a função `tamanho()` só para um critério de ordenação.

---

## **Conclusão**
As `lambda` são úteis para funções **simples e curtas**, principalmente quando são usadas **apenas uma vez dentro de outra função**. Mas se a lógica for mais complexa, usar `def` torna o código mais legível.

### **Quando usar `lambda`?**
✅ **Função curta, usada apenas uma vez**  
✅ **Dentro de outra função, como argumento**  
✅ **Para manter o código mais conciso**  

### **Quando evitar `lambda`?**
❌ **Se a função for muito complexa** (difícil de entender e manter)  
❌ **Se precisar reutilizar a função várias vezes** (melhor usar `def`)  
❌ **Se precisar de várias linhas** (lambda só permite **uma expressão**, não múltiplas instruções)  

---

### **Resumo prático**
🔹 **Use `lambda` para funções simples dentro de `map()`, `filter()`, `sorted()`, etc.**  
🔹 **Use `def` quando a função for mais complexa, precisar de múltiplas instruções ou for reutilizada.**