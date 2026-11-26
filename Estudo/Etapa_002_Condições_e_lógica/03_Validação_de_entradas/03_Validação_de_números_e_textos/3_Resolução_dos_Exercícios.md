# **Resolução dos exercícios — Validação de números e textos**

## **Exercício 1**

```python
numero = int(input('Digite um número inteiro: '))

if numero >= 1 and numero <= 50:
    print('Número aceito')
else:
    print('Número fora do intervalo')
```

## **Exercício 2**

```python
preco = float(input('Digite o preço do produto: '))

if preco > 0:
    print('Preço válido')
else:
    print('Preço inválido')
```

## **Exercício 3**

```python
nota = float(input('Digite sua nota: '))

if nota >= 0 and nota <= 10:
    print('Nota válida')
else:
    print('Nota inválida')
```

## **Exercício 4**

```python
nome = input('Digite seu nome: ')

if nome == '':
    print('Nome não informado')
else:
    print('Nome informado')
```

## **Exercício 5**

```python
nome = input('Digite seu nome: ')

if nome.strip() == '':
    print('Nome não informado')
else:
    print('Nome informado')
```

## **Exercício 6**

```python
senha = input('Digite sua senha: ')

if len(senha) >= 8:
    print('Senha aceita')
else:
    print('Senha muito curta')
```

## **Exercício 7**

```python
email = input('Digite seu e-mail: ')

if '@' in email:
    print('E-mail contém @')
else:
    print('E-mail não contém @')
```

## **Exercício 8**

```python
codigo = input('Digite o código de identificação: ')

if len(codigo) == 6:
    print('Código aceito')
else:
    print('Código inválido')
```

## **Exercício 9**

```python
nome = input('Digite seu nome completo: ')

if ' ' in nome:
    print('Nome completo informado')
else:
    print('Informe nome e sobrenome')
```

## **Exercício 10**

```python
nome = input('Digite o nome do funcionário: ')
idade = int(input('Digite a idade: '))
salario = float(input('Digite o salário: '))

if nome.strip() != '' and idade >= 18 and idade <= 65 and salario > 0:
    print('Cadastro válido')
else:
    print('Cadastro inválido')
```
