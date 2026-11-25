# **Resolução dos Exercícios de Condições Simples e Compostas**

## **Exercício 1**

```python
idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Maior de idade')
```

## **Exercício 2**

```python
numero = int(input('Digite um número: '))

if numero < 0:
    print('Número negativo')
```

## **Exercício 3**

```python
idade = int(input('Digite sua idade: '))
habilitacao = input('Possui habilitação? (True/False): ') == 'True'

if idade >= 18 and habilitacao:
    print('Pode dirigir')
```

## **Exercício 4**

```python
valor_compra = float(input('Digite o valor da compra: '))
cliente_vip = input('É cliente VIP? (True/False): ') == 'True'

if cliente_vip or valor_compra > 500:
    print('Desconto disponível')
```

## **Exercício 5**

```python
nota = float(input('Digite a nota: '))
frequencia = float(input('Digite a frequência (%): '))

if nota >= 7 and frequencia >= 75:
    print('Aprovado')
```

## **Exercício 6**

```python
idade = int(input('Digite sua idade: '))
autorizacao = input('Possui autorização? (True/False): ') == 'True'

if idade >= 18 or autorizacao:
    print('Entrada permitida')
```

## **Exercício 7**

```python
tempo_empresa = float(input('Digite o tempo de empresa (anos): '))
salario = float(input('Digite o salário: '))

if tempo_empresa > 2 and salario > 3000:
    print('Elegível ao benefício')
```

## **Exercício 8**

```python
numero = int(input('Digite um número: '))

if numero > 10 and numero < 100:
    print('Número dentro do intervalo')
```

## **Exercício 9**

```python
valor_compra = float(input('Digite o valor da compra: '))
cliente_vip = input('É cliente VIP? (True/False): ') == 'True'

if cliente_vip or (valor_compra > 500 and valor_compra < 1000):
    print('Benefício disponível')
```

## **Exercício 10**

```python
idade = int(input('Digite sua idade: '))
experiencia = input('Possui experiência? (True/False): ') == 'True'

if (idade >= 18 and idade <= 35 and experiencia) or (idade > 35 and experiencia):
    print('Candidato atende aos critérios')
```