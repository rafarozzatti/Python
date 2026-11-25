## **Exercício 1**

```python
idade = 25
renda = 4000

if idade >= 18:
    if renda >= 3000 and renda <= 10000:
        print('Crédito aprovado')
    else:
        print('Renda fora dos critérios')
else:
    print('Idade insuficiente')
```

## **Exercício 2**

```python
nota = 8
frequencia = 85

if nota >= 5:
    if nota >= 7 and frequencia >= 75:
        print('Aluno aprovado')
    else:
        print('Aluno em recuperação')
else:
    print('Aluno reprovado')
```

## **Exercício 3**

```python
idade = 30
salario = 5000
tempo_empresa = 3

if idade >= 18:
    if salario >= 4000 and tempo_empresa >= 2:
        print('Funcionário atende aos requisitos')
    else:
        if salario < 4000:
            print('Salário insuficiente')
        if tempo_empresa < 2:
            print('Tempo de empresa insuficiente')
else:
    print('Idade insuficiente')
```

## **Exercício 4**

```python
idade = 20
possui_ingresso = False
possui_convite = True

if idade >= 18:
    if possui_ingresso or possui_convite:
        print('Entrada permitida')
    else:
        print('Entrada negada')
else:
    print('Entrada não permitida para menores de idade')
```

## **Exercício 5**

```python
nota = 6
possui_trabalho_extra = True

if nota >= 5:
    if nota >= 7 or possui_trabalho_extra:
        print('Aluno aprovado')
    else:
        print('Aluno em recuperação')
else:
    print('Aluno reprovado')
```

## **Exercício 6**

```python
saldo = 500
possui_limite = True

if saldo > 0:
    if saldo >= 1000 or possui_limite:
        print('Compra autorizada')
    else:
        print('Compra não autorizada')
else:
    print('Saldo não positivo')
```

## **Exercício 7**

```python
idade = 25
bloqueado = False

if idade >= 18:
    if not bloqueado:
        print('Acesso permitido')
    else:
        print('Usuário bloqueado')
else:
    print('Idade insuficiente')
```

## **Exercício 8**

```python
nota = 8
possui_pendencia = False

if nota >= 7:
    if not possui_pendencia:
        print('Aluno aprovado')
    else:
        print('Aluno possui pendências')
else:
    print('Aluno reprovado')
```

## **Exercício 9**

```python
idade = 22
possui_ingresso = False
possui_convite = True
bloqueado = False

if idade >= 18:
    if (possui_ingresso or possui_convite) and not bloqueado:
        print('Entrada permitida')
    else:
        print('Entrada negada')
else:
    print('Entrada negada por idade')
```

## **Exercício 10**

```python
idade = 25
renda = 4000
possui_garantia = True
bloqueado = False

if idade >= 18:
    if (renda >= 3000 or possui_garantia) and not bloqueado:
        print('Crédito aprovado')
    else:
        print('Crédito negado')
else:
    print('Idade insuficiente')
```
