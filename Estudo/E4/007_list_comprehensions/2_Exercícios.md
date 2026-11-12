# Exercícios de List Comprehensions

## Exercícios — 1

Vamos começar com um exercício básico.

Crie uma lista chamada `numeros` utilizando List Comprehension, contendo os números inteiros de 1 até 10.

Depois, imprima a lista.

Regra: utilize a estrutura básica, sem condições e sem `append()`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-1)

## Exercício 2

Crie uma lista chamada `dobros` utilizando List Comprehension.

Utilize os números de 1 até 10 e multiplique cada um por 2.

A saída esperada é:

```
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-2)

## Exercício 3

Crie uma lista chamada `pares` utilizando List Comprehension.

Requisitos:

- Percorra os números de 1 até 20.
- Adicione somente os números pares.
- Utilize a condição `if` dentro da List Comprehension.

Saída esperada:

```
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-3)

## Exercício 4

Crie uma lista chamada `impares` utilizando List Comprehension.

Requisitos:

- Percorra os números de 1 até 30.
- Adicione somente os números ímpares.
- Utilize a condição `if`.

Saída esperada:

```
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-4)

## Exercício 5

Crie uma lista chamada `quadrados` utilizando List Comprehension.

Requisitos:

- Utilize os números de 1 até 10.
- Eleve cada número ao quadrado utilizando o operador `**`.

Saída esperada:

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-5)

## Exercício 6

Crie uma lista chamada `dobros_pares` utilizando List Comprehension.

Requisitos:

- Percorra os números de 1 até 20.
- Considere somente os números pares.
- Multiplique cada número selecionado por 2.

Saída esperada:

```
[4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-6)

## Exercício 7

Agora vamos praticar uma estrutura diferente.

Crie uma lista chamada `classificacao` utilizando List Comprehension.

Requisitos:

- Percorra os números de 1 até 10.
- Se o número for par, adicione `"Par"` à lista.
- Caso contrário, adicione `"Ímpar"`.

Saída esperada:

```
['Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par']
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-7)

## Exercício 8

Crie uma lista chamada `nomes_maiusculos` utilizando List Comprehension.

Utilize esta lista como origem:

```
nomes = ["carlos", "mariana", "pedro", "ana"]
```

Requisitos:

1. Percorra todos os nomes.
2. Transforme cada nome em letras maiúsculas utilizando o método `upper()`.
3. Adicione os nomes transformados à nova lista.

Saída esperada:

```
['CARLOS', 'MARIANA', 'PEDRO', 'ANA']
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-8)

## Exercício 9

Agora vamos combinar List Comprehension com uma condição aplicada a textos.

Utilize a seguinte lista:

```
nomes = ["Carlos", "Mariana", "Pedro", "Ana", "Roberto", "João"]
```

Crie uma lista chamada `nomes_grandes` que contenha somente os nomes com mais de 5 caracteres.

Requisitos:

- Utilize List Comprehension.
- Utilize o `if` para filtrar os nomes.
- Utilize `len()` para verificar o tamanho de cada nome.
- Mantenha os nomes na escrita original.

Saída esperada:

```
['Mariana', 'Roberto']
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-9)

## Exercício 10

Vamos reunir os principais conceitos estudados.

Considere a seguinte lista:

```
vendas = [150, 80, 250, 40, 300, 120, 60, 500]
```

Crie uma nova lista chamada `vendas_altas` utilizando List Comprehension.

Requisitos:

1. Selecione somente as vendas maiores que `100`.
2. Aplique um aumento de 10% em cada venda selecionada.
3. Armazene os resultados na nova lista.
4. Exiba a lista `vendas_altas`.

Saída esperada:

```
[165.0, 275.0, 330.0, 132.0, 550.0]
```

Dica: você precisará combinar uma expressão matemática com uma condição `if`, como fizemos no exercício 6.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-10)
