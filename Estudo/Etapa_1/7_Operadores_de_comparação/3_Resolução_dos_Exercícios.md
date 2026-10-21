# Exercícios de Operadores de comparação

## Exercícios — 1

Crie um programa que:

1. Crie a variável `a` com o valor `10`.
2. Crie a variável `b` com o valor `5`.
3. Crie a variável `resultado` para guardar a comparação que verifica se `a` é maior que `b`.
4. Imprima a variável `resultado`.

Resolução:
```python
a = 10
b = 5

resultado = a > b
print(resultado)
```
Saída:
```
True
```

## Exercício 2

Agora vamos praticar o operador `==` (igual a).

Crie um programa que:

1. Crie a variável `produto1` com o valor `25`.
2. Crie a variável `produto2` com o valor `25`.
3. Crie a variável `resultado` para verificar se os dois valores são iguais.
4. Imprima `resultado`.

Resolução:
```python
produto1 = 25
produto2 = 25

resultado = produto1 == produto2
print(resultado)
```
Saída:
```
True
```

## Exercício 3

Agora vamos praticar o operador `!=` (diferente de).

Crie um programa que:

1. Crie a variável `idade1` com o valor `20`.
2. Crie a variável `idade2` com o valor `18`.
3. Crie a variável `resultado` para verificar se as duas idades são diferentes.
4. Imprima `resultado`.

Resolução:
```python
idade1 = 20
idade2 = 18

resultado = idade1 != idade2
print(resultado)
```
Saída:
```
True
```

## Exercício 4

Agora vamos praticar o operador `<` (menor que).

Crie um programa que:

1. Crie a variável `preco1` com o valor `35.50`.
2. Crie a variável `preco2` com o valor `42.90`.
3. Crie a variável `resultado` para verificar se `preco1` é menor que `preco2`.
4. Imprima `resultado`.

Resolução:
```python
preco1 = 35.50
preco2 = 42.90

resultado = preco1 < preco2
print(resultado)
```
Saída:
```
True
```

## Exercício 5

Agora vamos praticar o operador `>=` (maior ou igual a).

Crie um programa que:

1. Crie a variável `nota` com o valor `7`.
2. Crie a variável `nota_minima` com o valor `7`.
3. Crie a variável `resultado` para verificar se `nota` é maior ou igual a `nota_minima`.
4. Imprima `resultado`.

Resolução:
```python
nota = 7
nota_minima = 7

resultado = nota >= nota_minima
print(resultado)
```
Saída:
```
True
```

## Exercício 6

Agora vamos praticar o operador `<=` (menor ou igual a).

Crie um programa que:

1. Crie a variável `quantidade` com o valor `15`.
2. Crie a variável `limite` com o valor `20`.
3. Crie a variável `resultado` para verificar se `quantidade` é menor ou igual a `limite`.
4. Imprima `resultado`.

Resolução:
```python
quantidade = 15
limite = 20

resultado = quantidade <= limite
print(resultado)
```
Saída:
```
True
```

## Exercício 7

Agora vamos combinar dois conceitos que você já aprendeu: operadores de comparação e `input()`.

Crie um programa que:

1. Peça ao usuário para digitar sua idade.
2. Converta a entrada para um número inteiro usando `int()`.
3. Verifique se a idade é maior ou igual a `18`.
4. Armazene o resultado na variável `maioridade`.
5. Imprima a variável `maioridade`.

Exemplo de execução:

```
Digite sua idade: 22
True
```

Resolução:
```python
idade = int(input('Digite sua idade: '))

maioridade = idade >= 18
print(maioridade)
```

## Exercício 8

Agora vamos trabalhar com duas comparações usando variáveis, sem introduzir nenhum conceito novo.

Uma loja quer verificar se um produto está dentro da faixa de preço desejada.

Crie um programa que:

1. Crie a variável `preco` com o valor `80`.
2. Crie a variável `preco_minimo` com o valor `50`.
3. Crie a variável `preco_maximo` com o valor `100`.
4. Crie a variável `acima_minimo` para verificar se `preco` é maior que `preco_minimo`.
5. Crie a variável `abaixo_maximo` para verificar se `preco` é menor que `preco_maximo`.
6. Imprima `acima_minimo` e `abaixo_maximo`, um em cada linha.

Saída esperada:

```
True
True
```

Resolução:
```python
preco = 80
preco_minimo = 50
preco_maximo = 100

acima_minimo = preco > preco_minimo
abaixo_maximo = preco < preco_maximo

print(acima_minimo)
print(abaixo_maximo)
```

## Exercício 9

Agora vamos verificar se dois valores são iguais e se são diferentes, usando o mesmo programa.

Uma loja possui dois registros de estoque.

Crie um programa que:

1. Crie a variável `estoque_a` com o valor `120`.
2. Crie a variável `estoque_b` com o valor `120`.
3. Crie a variável `estoques_iguais` para verificar se os dois valores são iguais.
4. Crie a variável `estoques_diferentes` para verificar se os dois valores são diferentes.
5. Imprima as duas variáveis, uma em cada linha.

Saída esperada:

```
True
False
```

Resolução:
```python
estoque_a = 120
estoque_b = 120

estoque_iguais = estoque_a == estoque_b
estoque_diferentes = estoque_a != estoque_b

print(estoque_iguais)
print(estoque_diferentes)
```

## Exercício 10

Uma empresa quer analisar o valor de uma venda.

Crie um programa que:

1. Crie a variável `venda` com o valor `500`.
2. Crie a variável `meta` com o valor `500`.
3. Crie seis variáveis com os seguintes resultados:
   - `igual`: verifica se `venda` é igual a `meta`.
   - `diferente`: verifica se `venda` é diferente de `meta`.
   - `maior`: verifica se `venda` é maior que `meta`.
   - `menor`: verifica se `venda` é menor que `meta`.
   - `maior_igual`: verifica se `venda` é maior ou igual a `meta`.
   - `menor_igual`: verifica se `venda` é menor ou igual a `meta`.
4. Imprima as seis variáveis, uma em cada linha, nessa ordem.

Saída esperada:

```
True
False
False
False
True
True
```

Resolução:
```python
venda = 500
meta = 500

igual = venda == meta
diferente = venda != meta
maior = venda > meta
menor = venda < meta
maior_igual = venda >= meta
menor_igual = venda <= meta

print(igual)
print(diferente)
print(maior)
print(menor)
print(maior_igual)
print(menor_igual)
```
