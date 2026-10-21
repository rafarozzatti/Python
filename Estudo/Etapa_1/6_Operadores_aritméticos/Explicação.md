Vamos nessa! Vamos estudar Operadores aritméticos em Python, seguindo nosso método: explicação com exemplos e resultados, depois 10 exercícios em ordem crescente de dificuldade, corrigidos um por vez.

# 6. Operadores aritméticos em Python

Os operadores aritméticos permitem realizar cálculos no Python, como somar preços, calcular médias, dividir quantidades e calcular descontos.

## 1. Os 7 operadores aritméticos

# +

Adição

Soma dois valores.

`10 + 3` → `13`

# -

Subtração

Subtrai o segundo valor do primeiro.

`10 - 3` → `7`

# \*

Multiplicação

Multiplica os valores.

`10 * 3` → `30`

# /

Divisão

Divide os valores e retorna um resultado do tipo `float`.

`10 / 3` → `3.333333...`

# //

Divisão inteira

Arredonda o quociente para baixo, em direção a menos infinito.

`10 // 3` → `3`

# %

Módulo (resto da divisão)

Retorna o resto da divisão.

`10 % 3` → `1`

# \*\*

Potenciação

Eleva um número a uma potência.

`2 ** 3` → `8`, pois \\(2 \times 2 \times 2 = 8\\).

## 2. Entendendo melhor `//` e `%`

Esses dois operadores podem parecer semelhantes no começo, mas têm funções diferentes.

Imagine que você tem 10 unidades de um produto e quer montar caixas com 3 unidades em cada uma.

```
quantidade = 10por_caixa = 3caixas_completas = quantidade // por_caixasobras = quantidade % por_caixaprint(caixas_completas)print(sobras)
```

Resultado:

```
3
1
```

- `10 // 3` retorna `3`: você consegue montar três caixas completas.
- `10 % 3` retorna `1`: sobra uma unidade.

Esse tipo de cálculo é útil em controle de estoque, logística e distribuição de produtos.

## 3. Utilizando operadores com variáveis

Você pode armazenar os resultados em variáveis, como já fez nos exercícios anteriores.

```
numero1 = 10numero2 = 3soma = numero1 + numero2subtracao = numero1 - numero2multiplicacao = numero1 * numero2divisao = numero1 / numero2divisao_inteira = numero1 // numero2resto = numero1 % numero2potencia = numero1 ** numero2print(soma)print(subtracao)print(multiplicacao)print(divisao)print(divisao_inteira)print(resto)print(potencia)
```

Saída:

```
13
7
30
3.3333333333333335
3
1
1000
```

Repare que cada operador executa uma operação diferente com os mesmos dois números.

## 4. Ordem das operações

Python segue uma ordem de prioridade para realizar os cálculos.

Veja:

```
resultado1 = 2 + 3 * 4resultado2 = (2 + 3) * 4print(resultado1)print(resultado2)
```

Saída:

```
14
20
```

No primeiro caso, a multiplicação é feita antes da adição: \\(2 + 12 = 14\\).

No segundo, os parênteses têm prioridade: \\(5 \times 4 = 20\\).

Uma regra prática: use parênteses quando quiser deixar explícita a ordem de um cálculo, principalmente em fórmulas mais complexas.

Atenção também à divisão por zero: expressões como `10 / 0`, `10 // 0` e `10 % 0` geram erro.
