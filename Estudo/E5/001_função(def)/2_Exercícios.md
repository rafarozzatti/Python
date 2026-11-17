# Exercícios de Função(def)

## Exercício 1

Crie uma função chamada `mensagem` que:

1. Exiba a mensagem `"Estou aprendendo funções em Python!"`.
2. Seja executada por meio de uma chamada da função.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-1)

## Exercício 2

Crie uma função chamada `saudacao` que receba um parâmetro chamado `nome`.

A função deverá exibir:

```
Olá, Carlos! Seja bem-vindo!
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-2)

## Exercício 3

Crie uma função chamada `apresentar` que receba dois parâmetros:

- `nome`
- `idade`

A função deverá exibir:

```
Nome: Mariana
Idade: 25 anos
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-3)

## Exercício 4

Agora vamos praticar o conceito de retorno.

Crie uma função chamada `somar` que:

1. Receba dois parâmetros: `a` e `b`.
2. Some os dois valores.
3. Utilize `return` para devolver o resultado.

Depois:

- Chame a função passando os valores `15` e `25`.
- Armazene o resultado em uma variável chamada `resultado`.
- Utilize `print()` para exibir essa variável.

Saída esperada:

```
40
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-4)

## Exercício 5

Crie uma função chamada `apresentar` que:

1. Receba um parâmetro `nome`.
2. Receba um segundo parâmetro `cidade`, com valor padrão `'São Paulo'`.
3. Utilize `print()` para exibir: `Olá, [nome]! Você mora em [cidade].`

Depois, faça duas chamadas:

- Uma passando apenas o nome `'Rafael'`.
- Outra passando o nome `'Carlos'` e a cidade `'Santos'`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-5)

## Exercício 6

Crie uma função chamada `dados_pessoais` que receba três parâmetros:

- `nome`
- `idade`
- `profissao`

A função deve exibir os três dados em linhas separadas.

Depois, chame a função utilizando **argumentos nomeados**, nesta ordem:

- `profissao='Engenheiro'`
- `nome='Rafael'`
- `idade=27`

[Resolução](3_Resolução_dos_Exercícios.md#exercício-6)

## Exercício 7

Crie uma função chamada `calcular_media` que:

1. Receba dois parâmetros: `nota1` e `nota2`.
2. Crie uma variável local chamada `media`, calculando a média das duas notas.
3. Utilize `return` para devolver a média.

Depois, chame a função passando as notas `8` e `6`, armazene o resultado em uma variável chamada `resultado` e exiba essa variável com `print()`.

Saída esperada:

```
7.0
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-7)

## Exercício 8

Crie uma função chamada `verificar_idade` que:

1. Receba um parâmetro chamado `idade`.
2. Utilize `print()` para exibir: `Você tem [idade] anos.`
3. Não utilize `return`.

Depois, chame a função passando o valor `27` e armazene o resultado em uma variável chamada `resultado`.

Por fim, utilize `print(resultado)`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-8)

## Exercício 9

Crie uma função chamada `classificar_nota` que:

1. Receba um parâmetro chamado `nota`.
2. Se a nota for maior ou igual a 7, retorne `'Aprovado'`.
3. Caso contrário, retorne `'Reprovado'`.

Depois, faça duas chamadas:

- Uma passando `8`.
- Outra passando `5`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-9)

## Exercício 10

Vamos juntar vários conceitos que estudamos.

Crie uma função chamada `calcular_desconto` que:

1. Receba dois parâmetros: `preco` e `desconto`.
2. O parâmetro `desconto` deve ter valor padrão de `10` (10%).
3. Calcule o valor do desconto sobre o preço.
4. Retorne o preço final após aplicar o desconto.

Depois, faça duas chamadas:

- Produto de R$ 200, utilizando o desconto padrão.
- Produto de R$ 500, utilizando desconto de 20%.

Armazene os resultados em variáveis e exiba ambos com `print()`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-10)
