# Exercícios de Operadores lógicos em condições

## Exercício 1

Crie um programa que:

1. Crie a variável `idade` com o valor `22`.
2. Crie a variável `tem_carteira` com o valor `True`.
3. Utilize um `if` com o operador `and` para verificar se:
   - A idade é maior ou igual a `18`.
   - A pessoa tem carteira.
4. Se as duas condições forem verdadeiras, exiba `Pode dirigir`.

Saída esperada:

```
Pode dirigir
```

## Exercício 2

Crie um programa que:

1. Crie a variável `idade` com o valor `22`.
2. Crie a variável `tem_carteira` com o valor `False`.
3. Utilize `if` e `and` para verificar se a idade é maior ou igual a 18 e se a pessoa tem carteira.
4. Se as duas condições forem verdadeiras, exiba `Pode dirigir`.

Saída esperada: nenhuma mensagem será exibida, porque uma das condições é falsa.

## Exercício 3

Agora vamos praticar o operador `or`, que permite executar o bloco quando pelo menos uma das condições é verdadeira.

Crie um programa que:

1. Crie a variável `dia` com o texto `'domingo'`.
2. Verifique se `dia` é igual a `'sábado'` ou igual a `'domingo'`, utilizando `or`.
3. Se uma das condições for verdadeira, exiba `É fim de semana`.

Saída esperada:

```
É fim de semana
```

## Exercício 4

Crie um programa que:

1. Crie a variável `dia` com o texto `'quarta-feira'`.
2. Verifique se `dia` é igual a `'sábado'` ou igual a `'domingo'`, utilizando `or`.
3. Se uma das condições for verdadeira, exiba `É fim de semana`.

Saída esperada: nenhuma mensagem será exibida, porque as duas condições são falsas.

## Exercício 5

Agora vamos praticar o operador `not`, que inverte o valor lógico de uma condição.

Crie um programa que:

1. Crie a variável `tem_divida` com o valor `False`.
2. Utilize `if` com o operador `not` para verificar se a pessoa não tem dívida.
3. Se a condição for verdadeira, exiba `Pode solicitar crédito`.

Saída esperada:

```
Pode solicitar crédito
```

## Exercício 6

Crie um programa que:

1. Crie a variável `tem_divida` com o valor `True`.
2. Utilize `if` com o operador `not` para verificar se a pessoa não tem dívida.
3. Se a condição for verdadeira, exiba `Pode solicitar crédito`.

Saída esperada: nenhuma mensagem será exibida, porque `not True` resulta em `False`.

## Exercício 7

Agora vamos combinar dois operadores lógicos.

Crie um programa que:

1. Crie a variável `idade` com o valor `17`.
2. Crie a variável `tem_autorizacao` com o valor `True`.
3. Verifique se a idade é maior ou igual a `18` ou se a pessoa tem autorização.
4. Se pelo menos uma das condições for verdadeira, exiba `Entrada permitida`.

Saída esperada:

```
Entrada permitida
```

## Exercício 8`

Crie um programa que:

1. Crie a variável `idade` com o valor `20`.
2. Crie a variável `tem_convite` com o valor `False`.
3. Crie a variável `esta_na_lista` com o valor `True`.
4. Verifique se a pessoa tem pelo menos 18 anos e se tem convite ou está na lista.
5. Se a condição for verdadeira, exiba `Entrada autorizada`.

Para deixar a intenção clara, use parênteses para agrupar a condição do convite ou da lista:

`idade >= 18 and (tem_convite or esta_na_lista)`

Saída esperada:

```
Entrada autorizada
```

## Exercício 9

Crie um programa que:

1. Crie a variável `idade` com o valor `16`.
2. Crie a variável `tem_autorizacao` com o valor `False`.
3. Verifique se a idade é maior ou igual a `18` ou se a pessoa tem autorização.
4. Se pelo menos uma condição for verdadeira, exiba `Entrada permitida`.
5. Caso contrário, exiba `Entrada negada`.

Saída esperada:

```
Entrada negada
```

## Exercício 10

Vamos reunir os operadores `and`, `or` e `not` em um único programa.

Crie um programa que:

1. Crie a variável `idade` com o valor `25`.
2. Crie a variável `tem_emprego` com o valor `True`.
3. Crie a variável `tem_divida` com o valor `False`.
4. Verifique se a pessoa tem pelo menos 18 anos e possui emprego e não tem dívidas.
5. Se todas as condições forem verdadeiras, exiba `Crédito aprovado`.
6. Caso contrário, exiba `Crédito negado`.

Saída esperada:

```
Crédito aprovado
```
