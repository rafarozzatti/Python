# Função `filter()` em Python

A função `filter()` é usada para filtrar elementos de um iterável (como listas ou tuplas) com base em uma condição especificada por uma função.

---

## **1. Sem `filter()` (Usando Loop `for`)**
```python
# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Criando uma nova lista apenas com os números pares
pares = []
for num in numeros:
    if num % 2 == 0:  # Verifica se o número é par
        pares.append(num)

print(pares)  # Saída: [2, 4, 6, 8, 10]
```

## **2. Com `filter()` (Código mais curto e eficiente)**
```python
# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando filter() para obter apenas os números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)  # Saída: [2, 4, 6, 8, 10]
```

---

## **Quando Usar `filter()`?** ✅
- Quando precisar **filtrar elementos** de um iterável com base em uma condição.
- Para tornar o código mais **conciso e legível**, evitando loops `for` desnecessários.
- Se quiser um código mais **eficiente**, pois `filter()` usa iteração interna otimizada.

## **Quando Evitar `filter()`?** ❌
- Se a condição for muito complexa, pois pode tornar o código menos legível.
- Quando precisar modificar os elementos filtrados, pois `filter()` apenas seleciona elementos.
- Se for necessário converter os dados para outro formato (nesse caso, `map()` pode ser mais adequado).

---

## **Exemplo com Função Normal**
```python
# Função que verifica se um número é maior que 5
def maior_que_cinco(x):
    return x > 5

# Lista de números
numeros = [1, 3, 5, 7, 9, 11]

# Filtrando apenas os números maiores que 5
resultado = list(filter(maior_que_cinco, numeros))

print(resultado)  # Saída: [7, 9, 11]
```

---

## **Exemplo com Strings**
```python
# Lista de nomes
nomes = ["Ana", "Bruno", "Carlos", "Beatriz", "Amanda"]

# Filtrando apenas os nomes que começam com a letra "A"
nomes_com_a = list(filter(lambda nome: nome.startswith("A"), nomes))

print(nomes_com_a)  # Saída: ['Ana', 'Amanda']
```

---

## **Conclusão**
A função `filter()` é útil para selecionar elementos que atendem a uma condição específica, tornando o código mais limpo e eficiente. No entanto, se a lógica for muito complexa, um loop `for` pode ser mais legível. 
