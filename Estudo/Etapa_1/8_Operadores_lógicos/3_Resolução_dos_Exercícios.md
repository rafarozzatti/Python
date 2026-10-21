# Exercícios de Operadores lógicos

## Exercício 1

Vamos começar apenas com o operador `and`.

Crie um programa que:

1. Crie a variável `a` com o valor `10`.
2. Crie a variável `b` com o valor `20`.
3. Crie a variável `resultado` para verificar se `a` é menor que `b` E `b` é maior que `15`.
4. Imprima a variável `resultado`.

A saída esperada é:

```
True
```

Resolução:
```python
a = 10
b = 20

resultado = a < b and b > 15
print(resultado)
```

## Exercício 2

Agora vamos continuar com `and`, mas o resultado será diferente.

Crie um programa que:

1. Crie a variável `preco` com o valor `80`.
2. Crie a variável `limite` com o valor `100`.
3. Crie a variável `resultado` para verificar se `preco` é menor que `limite` e se `preco` é maior que `90`.
4. Imprima `resultado`.

Saída esperada:

```
False
```

Resolução:
```python
preco = 80
limite = 100

resultado = preco < limite and preco > 90
print(resultado)
```

## Exercício 3

Agora vamos praticar o `or`, que retorna `True` quando pelo menos uma das condições é verdadeira.

Crie um programa que:

1. Crie a variável `idade` com o valor `17`.
2. Crie a variável `resultado` para verificar se `idade` é menor que `18` ou se `idade` é maior que `60`.
3. Imprima `resultado`.

Saída esperada:

```
True
```

Resolução:
```python
idade = 17

resultado = idade < 18 or idade > 60
print(resultado)
```

## Exercício 4

Crie um programa que:

1. Crie a variável `temperatura` com o valor `25`.
2. Crie a variável `resultado` para verificar se `temperatura` é menor que `10` ou se `temperatura` é maior que `30`.
3. Imprima `resultado`.

Saída esperada:

```
False
```

Resolução:
```python
temperatura = 25

resultado = temperatura < 10 or temperatura > 30
print(resultado)
```

## Exercício 5

Agora vamos praticar o `not`, que inverte o resultado lógico:

- `not True` → `False`
- `not False` → `True`

Crie um programa que:

1. Crie a variável `numero` com o valor `10`.
2. Crie a variável `resultado` para verificar se não é verdade que `numero` é igual a `10`.
3. Imprima `resultado`.

Saída esperada:

```
False
```

Resolução:
```python
numero = 10

resultado = not (numero == 10)
print(resultado)
```

## Exercício 6

Agora vamos combinar os operadores que já estudamos.

Crie um programa que:

1. Crie a variável `idade` com o valor `25`.
2. Crie a variável `resultado` para verificar se `idade` é maior que `18` e menor que `30`, ou se `idade` é igual a `50`.
3. Imprima `resultado`.

Saída esperada:

```
True
```

Resolução:
```python
idade = 25

resultado = (idade > 18 and idade < 30) or idade == 50
print(resultado)
```

## Exercício 7

Crie um programa que:

1. Crie a variável `saldo` com o valor `150`.
2. Crie a variável `resultado` para verificar se `saldo` é maior ou igual a `100` e se não é verdade que `saldo` é igual a `200`.
3. Imprima `resultado`.

Saída esperada:

```
True
```

Resolução:
```python
saldo = 150

resultado = saldo >= 100 and not (saldo == 200)
print(resultado)
```

## Exercício 8

Crie um programa que:

1. Crie a variável `nota` com o valor `6`.
2. Crie a variável `resultado` para verificar se `nota` é maior ou igual a `7` ou se `nota` é maior ou igual a `5` e menor que `7`.
3. Imprima `resultado`.

Saída esperada:

```
True
```

Resolução:
```python
nota = 6

resultado = nota >= 7 or (nota >= 5 and nota < 7)
print(resultado)
```

## Exercício 9

Crie um programa que:

1. Crie a variável `numero` com o valor `15`.
2. Crie a variável `resultado` para verificar se `numero` não é menor que `10` e se `numero` é diferente de `20`.
3. Imprima `resultado`.

Saída esperada:

```
True
```

Resolução:
```python
numero = 15

resultado = not (numero < 10) and numero != 20
print(resultado)
```

## Exercício 10

Vamos juntar tudo o que você estudou: `and`, `or` e `not`.

Crie um programa que:

1. Crie a variável `idade` com o valor `35`.
2. Crie a variável `tem_ingresso` com o valor `False`.
3. Crie a variável `resultado` para verificar se:
   - `idade` é maior ou igual a `18`; e
   - `tem_ingresso` é verdadeiro ou não é verdade que `idade` é maior que `60`.
4. Imprima `resultado`.

Saída esperada:

```
True
```

Resolução:
```python
idade = 35
tem_ingresso = False

resultado = idade >= 18 and (tem_ingresso == True or not (idade > 60))
print(resultado)
```
