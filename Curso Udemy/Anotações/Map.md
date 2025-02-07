# Função `map()` em Python

A função `map()` é usada para aplicar uma função a cada elemento de um iterável (como listas ou tuplas), retornando um iterador com os resultados.

---

## **1. Sem `map()` (Usando Loop `for`)**
```python
# Lista de números
numeros = [1, 2, 3, 4, 5]

# Criando uma nova lista para armazenar os quadrados dos números
quadrados = []
for num in numeros:
    quadrados.append(num ** 2)  # Calcula o quadrado e adiciona à lista

# Exibindo o resultado
print(quadrados)  # [1, 4, 9, 16, 25]
```

## **2. Com `map()` (Código mais curto e eficiente)**
```python
# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usando a função map() para calcular o quadrado de cada número
quadrados = list(map(lambda x: x ** 2, numeros))

# Exibindo o resultado
print(quadrados)  # [1, 4, 9, 16, 25]
```

---

## **Quando Usar `map()`?** ✅
- Quando precisar aplicar a **mesma função** a todos os elementos de um iterável.
- Para manter o código mais **conciso** e evitar loops explícitos.
- Se quiser um código mais **eficiente**, pois `map()` usa iteração interna otimizada.

## **Quando Evitar `map()`?** ❌
- Se a função aplicada for muito complexa, pois `map()` pode tornar o código menos legível.
- Quando precisar modificar elementos **baseados em múltiplas variáveis**, pois `map()` aceita apenas funções puras.
- Se precisar de **listas mutáveis**, pois `map()` retorna um iterador e não modifica a lista original.

---

## **Exemplo com Função Normal**
```python
# Definição de uma função que dobra o valor
def dobrar(x):
    return x * 2

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usando map() para dobrar cada número na lista
dobrados = list(map(dobrar, numeros))

# Exibindo o resultado
print(dobrados)  # [2, 4, 6, 8, 10]
```

## **Exemplo com Múltiplas Listas**
```python
# Duas listas de números
numeros1 = [1, 2, 3]
numeros2 = [4, 5, 6]

# Usando map() para somar os elementos correspondentes das duas listas
soma = list(map(lambda x, y: x + y, numeros1, numeros2))

# Exibindo o resultado
print(soma)  # [5, 7, 9]
```

---

## **Conclusão**
A função `map()` é uma ferramenta poderosa para transformar coleções de dados de forma eficiente e concisa. No entanto, para transformações mais complexas, list comprehensions ou loops `for` podem ser mais legíveis.
