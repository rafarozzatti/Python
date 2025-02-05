# Lambda

### **Cenário: Ordenando uma lista de tuplas**
Imagine que temos uma lista de produtos e seus preços, e queremos ordená-los pelo preço:  

#### **Usando `def` (função normal):**
```python
# Definição da função para ordenar por preço
def ordenar_por_preco(produto):
    return produto[1]  # Retorna o preço

# Lista de produtos com preços
produtos = [('Celular', 1500), ('Notebook', 3500), ('Fone de Ouvido', 200)]

# Ordenação da lista usando a função definida
produtos_ordenados = sorted(produtos, key=ordenar_por_preco)

# Impressão da lista ordenada
print(produtos_ordenados)
```
**Saída:**
```
[('Fone de Ouvido', 200), ('Celular', 1500), ('Notebook', 3500)]
```

#### **Usando `lambda` (mais curto e direto):**
```python
# Lista de produtos com preços
produtos = [('Celular', 1500), ('Notebook', 3500), ('Fone de Ouvido', 200)]

# Ordenação da lista usando lambda
produtos_ordenados = sorted(produtos, key=lambda produto: produto[1])

# Impressão da lista ordenada
print(produtos_ordenados)
```
**Saída:**
```
[('Fone de Ouvido', 200), ('Celular', 1500), ('Notebook', 3500)]
```

### **Por que usar `lambda` aqui?**
- Evita ter que criar uma função com `def` só para um uso simples.
- Deixa o código mais curto e direto.
- Útil quando você precisa de uma função rápida dentro de outra função, como `sorted()`, `map()`, `filter()`, etc.

Ótima questão! A principal utilidade de `lambda` é quando você precisa passar uma função como argumento para outra função. Isso acontece muito em funções como `sorted()`, `map()`, `filter()` e `reduce()`.  

Aqui estão alguns exemplos para ilustrar melhor:  

---

## **1️⃣ Usando `lambda` com `map()`**
O `map()` aplica uma função a cada item de um iterável (como uma lista).  

🔹 **Sem `lambda` (usando `def`):**  
```python
# Definição da função para calcular o quadrado de um número
def quadrado(x):
    return x ** 2

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicação da função quadrado usando map()
resultado = list(map(quadrado, numeros))

# Impressão do resultado
print(resultado)  # [1, 4, 9, 16, 25]
```
🔹 **Com `lambda` (mais curto e direto):**  
```python
# Lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicação de lambda diretamente no map()
resultado = list(map(lambda x: x ** 2, numeros))

# Impressão do resultado
print(resultado)  # [1, 4, 9, 16, 25]
```
✅ **Por que usar `lambda`?**  
Evita a necessidade de criar a função `quadrado()`, já que só vamos usá-la dentro do `map()`.

---

## **2️⃣ Usando `lambda` com `filter()`**
O `filter()` filtra os elementos de um iterável com base em uma condição.

🔹 **Sem `lambda`:**  
```python
# Definição da função para verificar se um número é maior que 10
def maior_que_10(x):
    return x > 10

# Lista de números
numeros = [5, 10, 15, 20, 25]

# Aplicação da função no filter()
resultado = list(filter(maior_que_10, numeros))

# Impressão do resultado
print(resultado)  # [15, 20, 25]
```
🔹 **Com `lambda`:**  
```python
# Lista de números
numeros = [5, 10, 15, 20, 25]

# Aplicação de lambda diretamente no filter()
resultado = list(filter(lambda x: x > 10, numeros))

# Impressão do resultado
print(resultado)  # [15, 20, 25]
```
✅ **Por que usar `lambda`?**  
A função `maior_que_10()` só é usada no `filter()`, então `lambda` deixa o código mais compacto.

---

## **3️⃣ Usando `lambda` com `sorted()`**
O `sorted()` pode ordenar com base em critérios personalizados.

🔹 **Ordenar palavras pelo tamanho (sem `lambda`):**  
```python
# Definição da função para obter o tamanho da palavra
def tamanho(palavra):
    return len(palavra)

# Lista de palavras
palavras = ["banana", "maçã", "uva", "abacaxi"]

# Ordenação da lista usando a função definida
ordenadas = sorted(palavras, key=tamanho)

# Impressão da lista ordenada
print(ordenadas)  # ['uva', 'maçã', 'banana', 'abacaxi']
```
🔹 **Com `lambda`:**  
```python
# Lista de palavras
palavras = ["banana", "maçã", "uva", "abacaxi"]

# Ordenação usando lambda
ordenadas = sorted(palavras, key=lambda palavra: len(palavra))

# Impressão da lista ordenada
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

