# Aula 3 — Tipos de dados em Python

## 1. `int` — Números inteiros

O tipo `int` representa números inteiros, ou seja, números sem casas decimais.

Exemplos:

```
idade = 27
quantidade = 10
ano = 2026
temperatura = -5
```

Você pode utilizar números inteiros em cálculos:

```
quantidade = 10
quantidade = quantidade + 5

print(quantidade)
```

Saída:

```
15
```

Observe que não precisamos colocar números inteiros entre aspas.

## 2. `float` — Números decimais

O tipo `float` representa números com casas decimais.

Exemplos:

```
altura = 1.75
preco = 29.90
media = 8.5
```

Em Python, utilizamos ponto (`.`) como separador decimal, e não vírgula.

Veja um exemplo:

```
preco = 29.90
quantidade = 3
total = preco * quantidade

print(total)
```

Saída:

```
89.7
```

Assim como vimos na aula anterior, o Python pode omitir zeros finais ao exibir números decimais.

## 3. `str` — Textos

O tipo `str` representa textos, também chamados de strings.

Podemos utilizar aspas simples ou duplas:

```
nome = 'Rafael'
cidade = "São Paulo"
produto = 'Notebook'
```

Até mesmo números podem ser armazenados como textos quando colocados entre aspas:

```
idade = 27
idade_texto = "27"

print(idade)
print(idade_texto)
```

Saída:

```
27
27
```

A saída parece igual, mas os tipos são diferentes: o primeiro valor é um número inteiro, e o segundo é um texto. Isso faz diferença nos cálculos, como veremos em outra aula.

## 4. `bool` — Valores lógicos

O tipo `bool` possui apenas dois valores possíveis:

- `True` — verdadeiro.
- `False` — falso.

Atenção: em Python, escrevemos a primeira letra em maiúscula.

Exemplo:

```
produto_disponivel = True
pedido_cancelado = False

print(produto_disponivel)
print(pedido_cancelado)
```

Saída:

```
True
False
```

Esses valores são úteis para representar situações como disponibilidade de produtos, aprovação de pedidos e cumprimento de metas.

## 5. Comparando os quatro tipos

| Tipo    | Representa          | Exemplo           |
| ------- | ------------------- | ----------------- |
| `int`   | Número inteiro      | `idade = 27`      |
| `float` | Número decimal      | `preco = 19.90`   |
| `str`   | Texto               | `nome = "Rafael"` |
| `bool`  | Verdadeiro ou falso | `aprovado = True` |

Podemos descobrir o tipo de um valor com `type()`, que será explorado melhor na próxima aula.

```
nome = "Rafael"
idade = 27
altura = 1.69
aprovado = True

print(type(nome))
print(type(idade))
print(type(altura))
print(type(aprovado))
```

Saída:

```
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```
