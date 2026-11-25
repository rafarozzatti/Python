# **Resolução dos Exercícios de Identação e Blocos Condicionais**

## **Exercício 1**

```python
idade = 20

if idade >= 18:
    print('Maior de idade')
```

## **Exercício 2**

```python
nota = 8

if nota >= 7:
    print('Aprovado')
else:
    print('Reprovado')
```

## **Exercício 3**

```python
numero = 10

if numero > 0:
    print('Número positivo')
elif numero < 0:
    print('Número negativo')
else:
    print('Zero')
```

## **Exercício 4**

```python
idade = 16

if idade < 18:
    print('Menor de idade')
else:
    print('Maior de idade')

print('Verificação finalizada')
```

## **Exercício 5**

```python
nota = 9

if nota >= 7:
    print('Aprovado')
    print('Parabéns pelo resultado')
else:
    print('Reprovado')
```

## **Exercício 6**

```python
idade = 20
possui_carteira = True

if idade >= 18:
    if possui_carteira:
        print('Pode dirigir')
    else:
        print('Precisa de habilitação')
```

## **Exercício 7**

```python
idade = 16
autorizacao = True

if idade >= 18:
    if autorizacao:
        print('Entrada permitida')
    else:
        print('Entrada não autorizada')
else:
    print('Menor de idade')
```

## **Exercício 8**

```python
nota = 8

if nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('Em recuperação')
else:
    print('Reprovado')

print('Processamento concluído')
```

## **Exercício 9**

```python
saldo = 1000
valor_compra = 300

if saldo >= valor_compra:
    print('Compra autorizada')

    saldo_restante = saldo - valor_compra

    print(saldo_restante)
else:
    print('Saldo insuficiente')
```

## **Exercício 10**

```python
idade = 25
renda = 3500

if idade >= 18:
    if renda >= 3000:
        print('Crédito aprovado')
    else:
        print('Renda insuficiente')
else:
    print('Idade não atende aos critérios')
```