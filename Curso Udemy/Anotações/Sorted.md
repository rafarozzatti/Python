# Função `sorted()` em Python

A função `sorted()` é usada para ordenar iteráveis, como listas e tuplas, de maneira crescente ou decrescente.

---

## **1. Sem `sorted()` (Usando Loop `for`)**
```python
# Lista de números desordenados
numeros = [5, 2, 9, 1, 5, 6]
numeros_ordenados = []

# Loop para ordenar os números manualmente
while numeros:
    menor = min(numeros)  # Encontra o menor elemento
    numeros_ordenados.append(menor)  # Adiciona à nova lista ordenada
    numeros.remove(menor)  # Remove o menor da lista original

print(numeros_ordenados)  # Saída: [1, 2, 5, 5, 6, 9]
```

**Saída:**
```
[1, 2, 5, 5, 6, 9]
```

## **2. Com `sorted()` (Mais simples e eficiente)**
```python
# Lista de números desordenados
numeros = [5, 2, 9, 1, 5, 6]

# Ordenação direta com sorted()
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)  # Saída: [1, 2, 5, 5, 6, 9]
```

**Saída:**
```
[1, 2, 5, 5, 6, 9]
```

---

## **Ordenando de Forma Decrescente**
```python
# Lista de números desordenados
numeros = [5, 2, 9, 1, 5, 6]

# Ordenação decrescente
numeros_ordenados = sorted(numeros, reverse=True)
print(numeros_ordenados)  # Saída: [9, 6, 5, 5, 2, 1]
```

**Saída:**
```
[9, 6, 5, 5, 2, 1]
```

---

## **Ordenando uma Lista de Tuplas por um Critério Específico**
```python
# Lista de produtos com preços
produtos = [('Celular', 1500), ('Notebook', 3500), ('Fone', 200)]

# Ordenação baseada no segundo elemento da tupla (preço)
ordenado_por_preco = sorted(produtos, key=lambda x: x[1])
print(ordenado_por_preco)  
# Saída: [('Fone', 200), ('Celular', 1500), ('Notebook', 3500)]
```

**Saída:**
```
[('Fone', 200), ('Celular', 1500), ('Notebook', 3500)]
```

---

## **Ordenando por Tamanho da String**
```python
# Lista de palavras
palavras = ['banana', 'maçã', 'uva', 'abacaxi']

# Ordenação baseada no tamanho da string
ordenado_por_tamanho = sorted(palavras, key=len)
print(ordenado_por_tamanho)  
# Saída: ['uva', 'maçã', 'banana', 'abacaxi']
```

**Saída:**
```
['uva', 'maçã', 'banana', 'abacaxi']
```

---

## **Quando Usar `sorted()`?** ✅
- Quando for necessário ordenar listas, tuplas ou qualquer iterável de forma rápida.
- Se precisar ordenar com base em um critério personalizado usando `key`.
- Para manter a lista original inalterada (ao contrário de `.sort()`, que modifica a lista original).

## **Quando Evitar `sorted()`?** ❌
- Se precisar ordenar grandes quantidades de dados frequentemente (nesse caso, estruturas otimizadas como heaps podem ser melhores).
- Quando a lista pode ser modificada diretamente com `.sort()`, evitando criação de uma nova lista.

---

## **Conclusão**
A função `sorted()` é uma maneira eficiente e flexível de ordenar iteráveis, permitindo critérios personalizados com `key` e controle da ordem com `reverse=True`. Para ordenações simples, é a melhor opção!
