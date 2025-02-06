# Coleções Avançadas em Python

## **1. Counter (Contador de Elementos)**
O `Counter` é uma subclasse de `dict` usada para contar elementos em uma coleção.

### **Sem Counter:**
```python
lista = ['a', 'b', 'a', 'c', 'b', 'a']
contagem = {}
for item in lista:
    if item in contagem:
        contagem[item] += 1
    else:
        contagem[item] = 1
print(contagem)  # {'a': 3, 'b': 2, 'c': 1}
```

### **Com Counter:**
```python
from collections import Counter
lista = ['a', 'b', 'a', 'c', 'b', 'a']
contagem = Counter(lista)
print(contagem)  # Counter({'a': 3, 'b': 2, 'c': 1})
```

---

## **2. defaultdict (Dicionário com Valor Padrão)**
Evita `KeyError` ao acessar chaves inexistentes.

### **Sem defaultdict:**
```python
dicionario = {}
dicionario['chave'] += 1  # Erro se a chave não existir
```

### **Com defaultdict:**
```python
from collections import defaultdict
dicionario = defaultdict(int)  # Valor padrão: 0
dicionario['chave'] += 1
print(dicionario)  # defaultdict(<class 'int'>, {'chave': 1})
```

---

## **3. deque (Fila de Alta Performance)**
O `deque` é uma estrutura de fila eficiente para inserções e remoções em ambos os lados.

### **Sem deque:**
```python
fila = []
fila.append(1)  # Inserção no final
fila.pop(0)  # Remoção do início (lento em listas)
```

### **Com deque:**
```python
from collections import deque
fila = deque()
fila.append(1)  # Inserção no final
fila.appendleft(2)  # Inserção no início
fila.pop()  # Remoção do final
fila.popleft()  # Remoção do início
```

---

## **4. OrderedDict (Dicionário Ordenado)**
Mantém a ordem de inserção das chaves.

### **Sem OrderedDict (Python 3.6+ já mantém ordem por padrão):**
```python
dicionario = {'b': 2, 'a': 1, 'c': 3}
print(dicionario)  # {'b': 2, 'a': 1, 'c': 3} (Ordem pode variar em versões antigas)
```

### **Com OrderedDict:**
```python
from collections import OrderedDict
dicionario = OrderedDict()
dicionario['b'] = 2
dicionario['a'] = 1
dicionario['c'] = 3
print(dicionario)  # OrderedDict([('b', 2), ('a', 1), ('c', 3)])
```

---

## **5. namedtuple (Tuplas Nomeadas)**
Uma alternativa leve para objetos.

### **Sem namedtuple:**
```python
pessoa = ('João', 30)  # Difícil lembrar o que cada índice representa
print(pessoa[0])  # 'João'
```

### **Com namedtuple:**
```python
from collections import namedtuple
Pessoa = namedtuple('Pessoa', ['nome', 'idade'])
pessoa = Pessoa(nome='João', idade=30)
print(pessoa.nome)  # 'João'
print(pessoa.idade)  # 30
```

---

## **Conclusão**
As coleções avançadas do `collections` melhoram a eficiência e a legibilidade do código. Use-as para otimizar suas estruturas de dados!
