# Exercícios de Formatação de textos com f-strings

## Exercício 1

Crie um programa que:

1. Crie a variável `nome` com o texto `"Carlos"`.
2. Crie a variável `idade` com o valor `30`.
3. Utilize `print()` com uma f-string para exibir a frase abaixo, substituindo as variáveis pelos seus valores:

Saída esperada:

```
Meu nome é Carlos e tenho 30 anos.
```

Resolução:
```python
nome = 'Carlos'
idade = 30

print(f'Meu nome é {nome} e tenho {idade} anos.')
```

## Exercício 2

Crie um programa que:

1. Crie a variável `preco` com o valor `45`.
2. Crie a variável `quantidade` com o valor `3`.
3. Utilize uma f-string com `print()` para exibir o resultado da multiplicação dessas duas variáveis na frase abaixo.

Saída esperada:

```
O valor total é R$ 135.
```

Resolução:
```python
preco = 45
quantidade = 3

print(f'O valor total é R$ {preco * quantidade}')
```

## Exercício 3

Crie um programa que:

1. Crie a variável `preco` com o valor `19.5`.
2. Utilize uma f-string para exibir o preço com duas casas decimais.

Saída esperada:

```
Preço: R$ 19.50
```

Resolução:
```python
preco = 19.5

print(f'Preço: R$ {preco:.2f}')
```

## Exercício 4

Crie um programa que:

1. Crie a variável `media` com o valor `7.456`.
2. Utilize uma f-string para exibir a média com duas casas decimais.

Saída esperada:

```
A média é 7.46
```

Resolução:
```python
media = 7.456

print(f'A média é {media:.2f}')
```

## Exercício 5

Crie um programa que:

1. Crie a variável `produto` com o texto `"Mouse"`.
2. Crie a variável `preco` com o valor `79.9`.
3. Crie a variável `quantidade` com o valor `2`.
4. Utilize uma única f-string com `print()` para exibir o nome do produto, o preço com duas casas decimais e a quantidade.

Saída esperada:

```
Produto: Mouse | Preço: R$ 79.90 | Quantidade: 2
```

Resolução:
```python
produto = 'Mouse'
preco = 79.9
quantidade = 2

print(f'Produto: {produto} | Preço: R$ {preco:.2f} | Quantidade: {quantidade}')
```

## Exercício 6

Crie um programa que:

1. Crie a variável `preco` com o valor `12.5`.
2. Crie a variável `quantidade` com o valor `4`.
3. Utilize uma f-string para exibir o valor total da compra, calculando `preco * quantidade` diretamente dentro das chaves.
4. Exiba o total com duas casas decimais.

Saída esperada:

```
Total da compra: R$ 50.00
```

Resolução:
```python
preco = 12.5
quantidade = 4

print(f'Total da compra: R$ {(preco * quantidade):.2f}')
```

## Exercício 7

Crie um programa que:

1. Crie a variável `a` com o valor `15`.
2. Crie a variável `b` com o valor `4`.
3. Utilize duas f-strings com `print()` para exibir:
   - A soma de `a` e `b`.
   - A divisão de `a` por `b`, com duas casas decimais.

Saída esperada:

```
Soma: 19
Divisão: 3.75
```

Resolução:
```python
a = 15
b = 4

print(f'Soma: {a + b}')
print(f'Divisão: {(a / b):.2f}')
```

## Exercício 8

Crie um programa que:

1. Crie a variável `produto` com o texto `"Caderno"`.
2. Crie a variável `preco` com o valor `8.75`.
3. Crie a variável `quantidade` com o valor `6`.
4. Utilize uma f-string para exibir uma frase com o nome do produto, a quantidade e o valor total (`preco * quantidade`), formatado com duas casas decimais.

Saída esperada:

```
Comprei 6 unidades de Caderno por R$ 52.50
```

Resolução:
```python
produto = 'Caderno'
preco = 8.75
quantidade = 6

print(f'Comprei {quantidade} unidades de {produto} por R$ {(preco * quantidade):.2f}')
```

## Exercício 9

Crie um programa que:

1. Crie a variável `nome` com o texto `"Ana"`.
2. Crie a variável `nota1` com o valor `8.5`.
3. Crie a variável `nota2` com o valor `7.25`.
4. Utilize uma f-string para exibir o nome e a média das duas notas, com duas casas decimais.

Para calcular a média, some as duas notas e divida o resultado por `2`.

Saída esperada:

```
Aluna: Ana | Média: 7.88
```

Resolução:
```python
nome = 'Ana'
nota1 = 8.5
nota2 = 7.25

print(f'Aluna: {nome} | Média: {((nota1 + nota2) / 2):.2f}')
```

## Exercício 10

Vamos reunir tudo o que você aprendeu neste assunto.

Crie um programa que:

1. Crie a variável `produto` com o texto `"Monitor"`.
2. Crie a variável `preco` com o valor `899.9`.
3. Crie a variável `quantidade` com o valor `2`.
4. Crie a variável `desconto` com o valor `50`.
5. Utilize uma f-string para exibir:
   - O nome do produto.
   - O preço unitário com duas casas decimais.
   - A quantidade comprada.
   - O total da compra após subtrair o desconto.

O cálculo do total deve considerar `preco * quantidade - desconto`.

Saída esperada:

```
Produto: Monitor
Preço unitário: R$ 899.90
Quantidade: 2
Total com desconto: R$ 1749.80
```

Resolução:
```python
produto = 'Monitor'
preco = 899.9
quantidade = 2
desconto = 50

print(f'''Produto: {produto}
Preço unitário: R$ {preco:.2f}
Quantidade: {quantidade}
Total com desconto: R$ {(preco * quantidade - desconto):.2f}''')
```
