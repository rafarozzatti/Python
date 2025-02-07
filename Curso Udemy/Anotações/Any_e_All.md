# Funções `any()` e `all()` em Python

As funções `any()` e `all()` são usadas para verificar condições dentro de iteráveis (listas, tuplas, conjuntos, etc.).

---

## **1. Função `any()`** ✅
A função `any()` retorna `True` se **pelo menos um** elemento de um iterável for avaliado como `True`.

### **Exemplo sem `any()` (Usando Loop)**
```python
valores = [0, 0, 1, 0]
algum_verdadeiro = False
for valor in valores:
    if valor:
        algum_verdadeiro = True
        break
print(algum_verdadeiro)  # True
```

### **Exemplo com `any()` (Mais Simples)**
```python
valores = [0, 0, 1, 0]
print(any(valores))  # True
```

### **Quando usar `any()`?** ✅
- Para verificar rapidamente se **pelo menos um** elemento é verdadeiro.
- Quando precisar simplificar a verificação de condições em listas e outros iteráveis.

### **Quando evitar `any()`?** ❌
- Se precisar verificar todos os elementos (nesse caso, `all()` pode ser mais adequado).
- Quando quiser contar quantos são `True`, pois `any()` apenas verifica a existência de pelo menos um.

---

## **2. Função `all()`** ✅
A função `all()` retorna `True` apenas se **todos os** elementos do iterável forem avaliados como `True`.

### **Exemplo sem `all()` (Usando Loop)**
```python
valores = [1, 2, 3, 4]
todos_verdadeiros = True
for valor in valores:
    if not valor:
        todos_verdadeiros = False
        break
print(todos_verdadeiros)  # True
```

### **Exemplo com `all()` (Mais Simples)**
```python
valores = [1, 2, 3, 4]
print(all(valores))  # True
```

### **Quando usar `all()`?** ✅
- Para verificar se **todos os** elementos de um iterável são verdadeiros.
- Em validação de dados onde todos os requisitos precisam ser atendidos.

### **Quando evitar `all()`?** ❌
- Se precisar saber **quantos** são verdadeiros, pois `all()` apenas retorna `True` ou `False`.
- Se precisar verificar apenas a existência de pelo menos um verdadeiro (use `any()` nesse caso).

---

## **3. Exemplo Comparativo: `any()` vs `all()`**
```python
valores = [0, 1, 2, 3]

print(any(valores))  # True (porque há pelo menos um valor verdadeiro)
print(all(valores))  # False (porque há pelo menos um valor falso - o 0)
```

---

## **Conclusão**
As funções `any()` e `all()` tornam a verificação de condições mais simples e legível. Utilize `any()` quando precisar saber se **ao menos um** elemento é verdadeiro e `all()` quando precisar garantir que **todos** são verdadeiros.
