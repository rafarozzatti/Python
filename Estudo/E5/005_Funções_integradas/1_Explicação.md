# **1.&#x20;**`len()`**&#x20;— Quantidade de elementos**

A função `len()` retorna a quantidade de elementos de uma estrutura.

Pode ser utilizada com listas, tuplas, conjuntos, dicionários e strings.

**Exemplo com lista:**

```
produtos = ['Notebook', 'Mouse', 'Teclado']

quantidade = len(produtos)

print(quantidade)
```

Saída:

```
3
```

**Exemplo com string:**

```
nome = 'Rafael'

print(len(nome))
```

Saída:

```
6
```

# **2.&#x20;**`sum()`**&#x20;— Soma dos valores**

A função `sum()` calcula a soma dos elementos de uma lista ou outra estrutura numérica iterável.

**Exemplo:**

```
notas = [7, 8, 9, 6, 10]

total = sum(notas)

print(total)
```

Saída:

```
40
```

Também podemos combinar `sum()` com `len()` para calcular médias:

```
notas = [7, 8, 9, 6, 10]

media = sum(notas) / len(notas)

print(media)
```

Saída:

```
8.0
```

# **3.&#x20;**`min()`**&#x20;— Menor valor**

A função `min()` retorna o menor elemento de uma estrutura.

**Exemplo:**

```
precos = [150, 80, 350, 200, 120]

menor_preco = min(precos)

print(menor_preco)
```

Saída:

```
80
```

Também funciona com valores informados diretamente:

```
print(min(10, 5, 20, 3))
```

Saída:

```
3
```

# **4.&#x20;**`max()`**&#x20;— Maior valor**

A função `max()` faz o contrário de `min()`: retorna o maior elemento.

**Exemplo:**

```
precos = [150, 80, 350, 200, 120]

maior_preco = max(precos)

print(maior_preco)
```

Saída:

```
350
```

Também podemos utilizar diretamente:

```
print(max(10, 5, 20, 3))
```

Saída:

```
20
```

# **5.&#x20;**`sorted()`**&#x20;— Ordenar elementos**

A função `sorted()` organiza os elementos de uma estrutura e retorna uma **nova lista ordenada**.

**Exemplo:**

```
numeros = [8, 3, 10, 1, 5]

ordenados = sorted(numeros)

print(ordenados)
```

Saída:

```
[1, 3, 5, 8, 10]
```

Observe que a lista original não é modificada:

```
numeros = [8, 3, 10, 1, 5]

ordenados = sorted(numeros)

print(numeros)
print(ordenados)
```

Saída:

```
[8, 3, 10, 1, 5]
[1, 3, 5, 8, 10]
```

**Ordenação decrescente**

Podemos utilizar o parâmetro `reverse=True` para ordenar do maior para o menor:

```
numeros = [8, 3, 10, 1, 5]ordenados = sorted(numeros, reverse=True)print(ordenados)
```

Saída:

```
[10, 8, 5, 3, 1]
```

**Diferença entre&#x20;**`sorted()`**&#x20;e&#x20;**`sort()`

Você já estudou o método `sort()` nas listas. É importante entender a diferença:

| `sorted()`                        | `sort()`                  |
| --------------------------------- | ------------------------- |
| Função integrada                  | Método de lista           |
| Retorna uma nova lista            | Modifica a lista original |
| Funciona com diferentes iteráveis | Funciona com listas       |

Exemplo:

```
numeros = [5, 2, 8, 1]

resultado = numeros.sort()

print(numeros)
print(resultado)
```

Saída:

```
[1, 2, 5, 8]
None
```

O `sort()` modifica a lista original e não retorna uma nova lista. Por isso, `resultado` recebe `None`.

# **6.&#x20;**`round()`**&#x20;— Arredondar números**

A função `round()` arredonda um número.

**Exemplo:**

```
preco = 19.6789

print(round(preco))
```

Saída:

```
20
```

Por padrão, arredonda para um número inteiro.

**Definindo casas decimais**

Podemos informar um segundo parâmetro para definir quantas casas decimais queremos:

```
preco = 19.6789

print(round(preco, 2))
```

Saída:

```
19.68
```

Outro exemplo:

```
media = 8.56789

print(round(media, 1))
print(round(media, 3))
```

Saída:

```
8.6
8.568
```

Isso é bastante útil para apresentar médias, preços e indicadores com uma quantidade definida de casas decimais.

# **7.&#x20;**`enumerate()`**&#x20;— Índice e valor**

Essa função já estudamos anteriormente. Vamos apenas relembrar.

A função `enumerate()` permite percorrer uma estrutura recebendo simultaneamente o índice e o valor de cada elemento.

**Exemplo:**

```
produtos = ['Notebook', 'Mouse', 'Teclado']

for indice, produto in enumerate(produtos):    
    print(indice, produto)
```

Saída:

```
0 Notebook
1 Mouse
2 Teclado
```

**Começando a contagem em outro número**

Podemos utilizar o parâmetro `start`:

```
produtos = ['Notebook', 'Mouse', 'Teclado']

for indice, produto in enumerate(produtos, start=1):    
    print(indice, produto)
```

Saída:

```
1 Notebook
2 Mouse
3 Teclado
```

# **8.&#x20;**`zip()`**&#x20;— Percorrer duas ou mais estruturas juntas**

Essa é a função nova mais importante deste conteúdo.

A função `zip()` permite percorrer duas ou mais estruturas simultaneamente, relacionando os elementos que ocupam a mesma posição.

Imagine que temos duas listas:

```
nomes = ['Carlos', 'Ana', 'Pedro']
idades = [25, 30, 28]
```

Queremos relacionar cada nome com sua idade.

Podemos utilizar `zip()`:

```
nomes = ['Carlos', 'Ana', 'Pedro']
idades = [25, 30, 28]

for nome, idade in zip(nomes, idades):    
    print(nome, idade)
```

Saída:

```
Carlos 25
Ana 30
Pedro 28
```

Observe o funcionamento:

| Posição | Lista `nomes` | Lista `idades` |
| ------- | ------------- | -------------- |
| 0       | Carlos        | 25             |
| 1       | Ana           | 30             |
| 2       | Pedro         | 28             |

O `zip()` relaciona os elementos de acordo com suas posições.

**Utilizando três listas**

Também podemos relacionar três ou mais listas:

```
nomes = ['Carlos', 'Ana', 'Pedro']
idades = [25, 30, 28]
cidades = ['São Paulo', 'Santos', 'Campinas']

for nome, idade, cidade in zip(nomes, idades, cidades):    
    print(nome, idade, cidade)
```

Saída:

```
Carlos 25 São Paulo
Ana 30 Santos
Pedro 28 Campinas
```

**E se as listas tiverem tamanhos diferentes?**

O `zip()` para quando termina a estrutura mais curta.

Exemplo:

```
nomes = ['Carlos', 'Ana', 'Pedro']
idades = [25, 30]

for nome, idade in zip(nomes, idades):    
    print(nome, idade)
```

Saída:

```
Carlos 25
Ana 30
```

Pedro não aparece porque não existe uma terceira idade correspondente.

**Transformando o resultado em uma lista**

Também podemos utilizar `list()` para visualizar os pares produzidos pelo `zip()`:

```
nomes = ['Carlos', 'Ana', 'Pedro']
idades = [25, 30, 28]

resultado = list(zip(nomes, idades))

print(resultado)
```

Saída:

```
[('Carlos', 25), ('Ana', 30), ('Pedro', 28)]
```

Cada par é representado por uma tupla.

# **9. Resumo para suas anotações**

| Função        | Utilidade                                    |
| ------------- | -------------------------------------------- |
| `len()`       | Retorna a quantidade de elementos            |
| `sum()`       | Soma os valores                              |
| `min()`       | Retorna o menor valor                        |
| `max()`       | Retorna o maior valor                        |
| `sorted()`    | Retorna uma nova lista ordenada              |
| `round()`     | Arredonda números                            |
| `enumerate()` | Retorna índice e valor                       |
| `zip()`       | Relaciona elementos de estruturas diferentes |
