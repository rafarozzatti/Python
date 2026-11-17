# Exercícios de Funções com Listas e Dicionários

## Exercício 1

Crie uma função chamada `calcular_total` que:

1. Receba uma lista de números como parâmetro.
2. Calcule a soma de todos os elementos.
3. Retorne o resultado utilizando `return`.

Depois:

- Crie uma lista chamada `precos` com os valores `[50, 100, 150, 200]`.
- Chame a função passando essa lista.
- Armazene o resultado em uma variável chamada `total`.
- Exiba o resultado com `print()`.

Saída esperada:

```
500
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-1)

## Exercício 2

Crie uma função chamada `mostrar_produtos` que:

1. Receba uma lista de produtos como parâmetro.
2. Utilize um `for` para percorrer a lista.
3. Exiba cada produto utilizando `print()`.

Depois, crie a lista:

```
produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor']
```

Chame a função passando essa lista.

Saída esperada:

```
Notebook
Mouse
Teclado
Monitor
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-2)

## Exercício 3

Crie uma função chamada `adicionar_produto` que:

1. Receba dois parâmetros: `produtos` e `novo_produto`.
2. Utilize `append()` para adicionar o novo produto à lista.

Depois:

- Crie a lista `['Notebook', 'Mouse']`.
- Chame a função passando a lista e o produto `'Teclado'`.
- Exiba a lista original utilizando `print()`.

Saída esperada:

```
['Notebook', 'Mouse', 'Teclado']
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-3)

## Exercício 4

Crie uma função chamada `remover_produto` que:

1. Receba dois parâmetros: `produtos` e `produto_remover`.
2. Utilize `remove()` para remover o produto informado da lista.

Depois:

- Crie a lista `['Notebook', 'Mouse', 'Teclado', 'Monitor']`.
- Chame a função para remover `'Mouse'`.
- Exiba a lista após a alteração.

Saída esperada:

```
['Notebook', 'Teclado', 'Monitor']
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-4)

## Exercício 5

Crie uma função chamada `mostrar_funcionario` que:

1. Receba um dicionário chamado `funcionario`.
2. Exiba o nome e o cargo do funcionário.

Depois, crie este dicionário:

```
funcionario = {    'nome': 'Carlos',    'cargo': 'Analista de Dados',    'salario': 3500}
```

Chame a função passando o dicionário como argumento.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-5)

## Exercício 6

Crie uma função chamada `atualizar_salario` que:

1. Receba dois parâmetros: `funcionario` e `novo_salario`.
2. Atualize o valor da chave `'salario'` do dicionário com o novo salário.

Depois:

- Crie um dicionário com nome `'Ana'`, cargo `'Desenvolvedora'` e salário `4000`.
- Chame a função para atualizar o salário para `5000`.
- Exiba o dicionário atualizado.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-6)

## Exercício 7

Crie uma função chamada `criar_produto` que:

1. Receba três parâmetros: `nome`, `preco` e `quantidade`.
2. Crie um dicionário contendo essas três informações.
3. Retorne o dicionário criado.

Depois:

- Chame a função passando `'Notebook'`, `3500` e `10`.
- Armazene o retorno em uma variável chamada `produto`.
- Exiba essa variável.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-7)

## Exercício 8

Crie uma função chamada `analisar_notas` que:

1. Receba uma lista de notas como parâmetro.
2. Calcule a soma das notas.
3. Calcule a média das notas.
4. Retorne a soma e a média.

Depois:

- Crie a lista `[7, 8, 9, 6, 10]`.
- Chame a função passando essa lista.
- Armazene os dois valores retornados em variáveis chamadas `soma` e `media`.
- Exiba os dois resultados.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-8)

## Exercício 9

Considere a seguinte lista:

```
produtos = [    {'nome': 'Notebook', 'preco': 3500},    {'nome': 'Mouse', 'preco': 80},    {'nome': 'Teclado', 'preco': 150}]
```

Crie uma função chamada `mostrar_produtos` que:

1. Receba a lista `produtos` como parâmetro.
2. Utilize um `for` para percorrer a lista.
3. Exiba o nome e o preço de cada produto.

A saída deverá ser:

```
Produto: Notebook | Preço: 3500
Produto: Mouse | Preço: 80
Produto: Teclado | Preço: 150
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-9)

## Exercício 10

Considere a lista:

```
funcionarios = [    {'nome': 'Carlos', 'salario': 3000},    {'nome': 'Ana', 'salario': 4000},    {'nome': 'Pedro', 'salario': 3500}]
```

Crie uma função chamada `aumentar_salarios` que:

1. Receba a lista `funcionarios` como parâmetro.
2. Percorra a lista utilizando `for`.
3. Aumente o salário de cada funcionário em 500.

Depois:

- Chame a função passando a lista.
- Exiba a lista após as alterações.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-10)
