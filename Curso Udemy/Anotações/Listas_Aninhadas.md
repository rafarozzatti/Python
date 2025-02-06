# Listas Aninhadas em Python

## **O que são listas aninhadas?**

Listas aninhadas são listas dentro de listas. Elas permitem representar estruturas complexas, como tabelas e matrizes.

---

## **1. Criando listas aninhadas**

### **Sem List Comprehension:**

```python
# Criando uma matriz 3x3 sem List Comprehension
matriz = []
for i in range(3):
    linha = []
    for j in range(1, 4):
        linha.append(j)  # Adiciona números de 1 a 3 na linha
    matriz.append(linha)
print(matriz)  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
```

### **Com List Comprehension:**

```python
# Criando uma matriz 3x3 com List Comprehension
matriz = [[j for j in range(1, 4)] for i in range(3)]
print(matriz)  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
```

---

## **2. Percorrendo listas aninhadas**

### **Sem List Comprehension:**

```python
# Percorrendo uma matriz com loops aninhados
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
valores = []
for linha in matriz:
    for elemento in linha:
        valores.append(elemento)  # Adiciona os elementos a uma nova lista
print(valores)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### **Com List Comprehension:**

```python
# Criando uma única lista a partir da matriz
lista_unica = [elemento for linha in matriz for elemento in linha]
print(lista_unica)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## **3. Criando matrizes personalizadas**

### **Sem List Comprehension:**

```python
# Criando uma matriz identidade 3x3 sem List Comprehension
identidade = []
for i in range(3):
    linha = []
    for j in range(3):
        if i == j:
            linha.append(1)  # Adiciona 1 na diagonal principal
        else:
            linha.append(0)  # Adiciona 0 nas outras posições
    identidade.append(linha)
print(identidade)  # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

### **Com List Comprehension:**

```python
# Criando uma matriz identidade 3x3 com List Comprehension
identidade = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print(identidade)  # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

---

## **Quando usar listas aninhadas?**

✅ **Casos ideais para uso:**
- Quando há necessidade de representar dados em formato tabular (matrizes, tabelas, grades, etc.).
- Para armazenar múltiplos conjuntos de dados relacionados em uma única estrutura.
- Quando se deseja melhorar a organização e legibilidade do código para manipulação de dados estruturados.

❌ **Evite usar listas aninhadas quando:**
- A estrutura de dados for muito complexa e difícil de acessar ou modificar.
- Outras estruturas de dados, como dicionários ou DataFrames (pandas), forem mais adequadas.
- O desempenho for uma preocupação, pois listas aninhadas podem ser menos eficientes do que outras alternativas para grandes volumes de dados.

---

## **Conclusão**

Listas aninhadas são úteis para representar estruturas complexas, como matrizes e tabelas. O uso de comprehensions pode tornar o código mais conciso e legível, mas loops tradicionais ainda são úteis para compreensão e manipulação detalhada.