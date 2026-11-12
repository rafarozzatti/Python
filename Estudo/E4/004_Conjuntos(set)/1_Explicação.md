# Conjuntos (`set`)

## 1. O que são conjuntos?

Conjuntos são estruturas utilizadas para armazenar vários elementos, com duas características principais:

- Não permitem elementos duplicados.
- Não possuem ordem definida nem índices.

Exemplo:

```
numeros = {10, 20, 30, 10, 20}

print(numeros)
print(type(numeros))
```

Saída:

```
{10, 20, 30}
<class 'set'>
```

Observe que os valores repetidos foram eliminados automaticamente.

## 2. Criando conjuntos

Utilizamos chaves `{}` para criar conjuntos:

```
frutas = {"Maçã", "Banana", "Uva"}
```

Para criar um conjunto vazio, utilizamos `set()`:

```
numeros = set()

print(numeros)
print(type(numeros))
```

Saída:

```
set()
<class 'set'>
```

Atenção: `{}` cria um dicionário vazio (`dict`), não um conjunto.

## 3. Verificando elementos (`in` e `not in`)

Utilizamos esses operadores para verificar se determinado elemento existe ou não no conjunto.

```
frutas = {"Maçã", "Banana", "Uva"}

print("Banana" in frutas)
print("Morango" not in frutas)
```

Saída:

```
True
True
```

- `in`: verifica se o elemento existe.
- `not in`: verifica se o elemento não existe.

## 4. Adicionando elementos (`add()`)

Adiciona um único elemento ao conjunto.

```
frutas = {"Maçã", "Banana"}

frutas.add("Uva")

print(frutas)
```

Saída:

```
{"Maçã", "Banana", "Uva"}
```

Se o elemento já existir, nada acontece. Não são criadas duplicatas.

## 5. Adicionando vários elementos (`update()`)

Adiciona vários elementos de uma vez.

Podemos passar uma lista, tupla ou outro conjunto.

```
numeros = {10, 20, 30}

numeros.update([40, 50, 60])

print(numeros)
```

Saída:

```
{10, 20, 30, 40, 50, 60}
```

Também podemos adicionar elementos utilizando uma tupla:

```
numeros.update((70, 80))
```

## 6. Removendo elementos (`remove()`)

Remove um elemento específico.

```
frutas = {"Maçã", "Banana", "Uva"}

frutas.remove("Banana")

print(frutas)
```

Saída:

```
{"Maçã", "Uva"}
```

Importante: se o elemento não existir, `remove()` gera um erro chamado `KeyError`.

## 7. Removendo elementos (`discard()`)

Também remove um elemento específico, mas possui uma diferença importante em relação ao `remove()`.

```
frutas = {"Maçã", "Banana", "Uva"}

frutas.discard("Banana")
frutas.discard("Morango")

print(frutas)
```

Saída:

```
{"Maçã", "Uva"}
```

A diferença:

| Método      | Elemento não existe |
| ----------- | ------------------- |
| `remove()`  | Gera `KeyError`     |
| `discard()` | Não gera erro       |

## 8. Esvaziando um conjunto (`clear()`)

Remove todos os elementos do conjunto, mas mantém a variável.

```
numeros = {10, 20, 30}

numeros.clear()

print(numeros)
print(type(numeros))
```

Saída:

```
set()
<class 'set'>
```

A variável continua sendo um conjunto, mas agora está vazia.

## 9. União de conjuntos (`union()`)

Combina os elementos de dois conjuntos, eliminando duplicatas.

```
conjunto_a = {10, 20, 30}
conjunto_b = {30, 40, 50}

resultado = conjunto_a.union(conjunto_b)

print(resultado)
```

Saída:

```
{10, 20, 30, 40, 50}
```

O número `30` aparece apenas uma vez.

Importante: `union()` retorna um novo conjunto, sem modificar os originais.

## 10. Interseção de conjuntos (`intersection()`)

Retorna somente os elementos que existem nos dois conjuntos.

```
conjunto_a = {10, 20, 30, 40}
conjunto_b = {30, 40, 50, 60}

resultado = conjunto_a.intersection(conjunto_b)

print(resultado)
```

Saída:

```
{30, 40}
```

Os números `30` e `40` são os únicos presentes nos dois conjuntos.

## 11. Diferença entre conjuntos (`difference()`)

Retorna os elementos que existem no primeiro conjunto, mas não existem no segundo.

```
conjunto_a = {10, 20, 30, 40}
conjunto_b = {30, 40, 50, 60}

resultado = conjunto_a.difference(conjunto_b)

print(resultado)
```

Saída:

```
{10, 20}
```

Se invertermos os conjuntos:

```
resultado = conjunto_b.difference(conjunto_a)

print(resultado)
```

Saída:

```
{50, 60}
```

Atenção: a ordem dos conjuntos importa!

## 12. Diferença simétrica (`symmetric_difference()`)

Retorna os elementos que existem em apenas um dos conjuntos, excluindo aqueles que aparecem nos dois.

```
conjunto_a = {10, 20, 30, 40}
conjunto_b = {30, 40, 50, 60}

resultado = conjunto_a.symmetric_difference(conjunto_b)

print(resultado)
```

Saída:

```
{10, 20, 50, 60}
```

Observe que `30` e `40` foram excluídos porque aparecem nos dois conjuntos.

## 13. Subconjuntos (`issubset()`)

Verifica se todos os elementos de um conjunto estão presentes em outro.

```
conjunto_a = {10, 20}
conjunto_b = {10, 20, 30, 40}

print(conjunto_a.issubset(conjunto_b))
```

Saída:

```
True
```

Isso acontece porque todos os elementos de A também estão em B.

## 14. Superconjuntos (`issuperset()`)

Faz a verificação inversa: verifica se um conjunto contém todos os elementos de outro.

```
conjunto_a = {10, 20, 30, 40}
conjunto_b = {10, 20}

print(conjunto_a.issuperset(conjunto_b))
```

Saída:

```
True
```

A contém todos os elementos de B.

## 15. Conjuntos disjuntos (`isdisjoint()`)

Verifica se dois conjuntos não possuem nenhum elemento em comum.

```
conjunto_a = {10, 20, 30}
conjunto_b = {40, 50, 60}

print(conjunto_a.isdisjoint(conjunto_b))
```

Saída:

```
True
```

Como não existe nenhum elemento em comum, o resultado é `True`.

Se os conjuntos tivessem algum elemento em comum, o resultado seria `False`.

## 16. Operações utilizando símbolos

Além dos métodos, Python permite realizar operações entre conjuntos utilizando símbolos.

| Operação            | Método                   | Símbolo |
| ------------------- | ------------------------ | ------- |
| União               | `union()`                | `\\|`   |
| Interseção          | `intersection()`         | `&`     |
| Diferença           | `difference()`           | `-`     |
| Diferença simétrica | `symmetric_difference()` | `^`     |

Exemplo:

```
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)
```

Saída:

```
{1, 2, 3, 4, 5}
{3}
{1, 2}
{1, 2, 4, 5}
```

# Resumo dos métodos de conjuntos

| Método                   | Finalidade                                        |
| ------------------------ | ------------------------------------------------- |
| `add()`                  | Adiciona um elemento                              |
| `update()`               | Adiciona vários elementos                         |
| `remove()`               | Remove um elemento (gera erro se não existir)     |
| `discard()`              | Remove um elemento (não gera erro se não existir) |
| `clear()`                | Remove todos os elementos                         |
| `union()`                | Une conjuntos                                     |
| `intersection()`         | Retorna elementos em comum                        |
| `difference()`           | Retorna elementos exclusivos do primeiro conjunto |
| `symmetric_difference()` | Retorna elementos exclusivos de cada conjunto     |
| `issubset()`             | Verifica se é subconjunto                         |
| `issuperset()`           | Verifica se é superconjunto                       |
| `isdisjoint()`           | Verifica se não existem elementos em comum        |
