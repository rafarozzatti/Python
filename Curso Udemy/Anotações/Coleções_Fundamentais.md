# Coleções Fundamentais em Python

Python possui diversas estruturas de dados nativas que facilitam a manipulação de coleções de dados. As principais são:

- **Listas** (`list`)
- **Tuplas** (`tuple`)
- **Conjuntos** (`set`)
- **Dicionários** (`dict`)

---

## 1. Listas (`list`)

Listas são coleções ordenadas e mutáveis, permitindo elementos duplicados.

```python
# Criando uma lista
frutas = ["maçã", "banana", "uva"]

# Acessando elementos
print(frutas[0])  # "maçã"

# Adicionando elementos
frutas.append("laranja")

# Removendo elementos
frutas.remove("banana")

# Percorrendo uma lista
for fruta in frutas:
    print(fruta)
```

**Quando usar listas?**
✅ Quando for necessário um conjunto ordenado de elementos mutáveis.
❌ Evite listas se os dados forem imutáveis ou não ordenados.

---

## 2. Tuplas (`tuple`)

Tuplas são semelhantes a listas, mas imutáveis (não podem ser alteradas após a criação).

```python
# Criando uma tupla
coordenadas = (10, 20)

# Acessando elementos
print(coordenadas[0])  # 10
```

**Quando usar tuplas?**
✅ Quando os dados são fixos e não precisam ser modificados.
❌ Se precisar modificar os elementos, use listas.

---

## 3. Conjuntos (`set`)

Conjuntos armazenam elementos únicos e não mantêm ordem.

```python
# Criando um conjunto
numeros = {1, 2, 3, 4, 4, 5}  # Elementos duplicados serão removidos
print(numeros)  # {1, 2, 3, 4, 5}

# Adicionando elementos
numeros.add(6)

# Removendo elementos
numeros.discard(2)
```

**Quando usar conjuntos?**
✅ Para armazenar elementos únicos e evitar duplicatas.
❌ Se precisar de ordem ou acessar elementos por índice, use listas.

---

## 4. Dicionários (`dict`)

Dicionários armazenam pares chave-valor, permitindo acesso rápido aos dados.

```python
# Criando um dicionário
pessoa = {"nome": "Carlos", "idade": 30}

# Acessando valores
print(pessoa["nome"])  # "Carlos"

# Adicionando chaves
pessoa["profissão"] = "Engenheiro"

# Removendo chaves
pessoa.pop("idade")

# Iterando sobre chaves e valores
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
```

**Quando usar dicionários?**
✅ Quando precisar associar chaves a valores para busca eficiente.
❌ Se os dados forem apenas sequenciais, listas são melhores.

---

## Conclusão

Essas coleções são fundamentais em Python e atendem a diferentes necessidades. Escolher a estrutura correta melhora a eficiência e clareza do código.