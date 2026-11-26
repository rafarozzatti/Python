## **Exercício 1**

```python
idade = int(input('Digite sua idade: '))

if idade < 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
elif idade <= 59:
    print('Adulto')
else:
    print('Idoso')
```

## **Exercício 2**

```python
nota = float(input('Digite sua nota: '))

if nota >= 9:
    print('Excelente')
elif nota >= 7:
    print('Bom')
elif nota >= 5:
    print('Regular')
else:
    print('Insuficiente')
```

## **Exercício 3**

```python
salario = float(input('Digite o salário: '))

if salario < 2000:
    print('Faixa salarial baixa')
elif salario <= 4000:
    print('Faixa salarial intermediária')
else:
    print('Faixa salarial alta')
```

## **Exercício 4**

```python
temperatura = float(input('Digite a temperatura: '))

if temperatura < 15:
    print('Frio')
elif temperatura <= 25:
    print('Agradável')
elif temperatura <= 35:
    print('Quente')
else:
    print('Muito quente')
```

## **Exercício 5**

```python
valor_compra = float(input('Digite o valor da compra: '))

if valor_compra < 100:
    desconto = 0
elif valor_compra < 500:
    desconto = 0.05
else:
    desconto = 0.10

valor_final = valor_compra - (valor_compra * desconto)

print(f'Desconto aplicado: {desconto * 100:.0f}%')
print(f'Valor final: R$ {valor_final:.2f}')
```

## **Exercício 6**

```python
nota = float(input('Digite a nota: '))
frequencia = float(input('Digite a frequência: '))

if nota < 7:
    print('Reprovado por nota')
else:
    if frequencia >= 75:
        print('Aprovado')
    else:
        print('Reprovado por frequência')
```

## **Exercício 7**

```python
estoque = int(input('Digite a quantidade em estoque: '))

if estoque == 0:
    print('Estoque zerado')
elif estoque <= 10:
    print('Estoque baixo')
elif estoque <= 50:
    print('Estoque adequado')
else:
    print('Estoque alto')
```

## **Exercício 8**

```python
idade = int(input('Digite a idade: '))
salario = float(input('Digite o salário: '))
situacao = input('Digite a situação (ativo/inativo): ')

if situacao == 'inativo':
    print('Não elegível')
else:
    if idade >= 18:
        if salario < 3000:
            print('Benefício concedido')
        else:
            print('Não elegível')
    else:
        print('Não elegível')
```

## **Exercício 9**

```python
renda = float(input('Digite a renda mensal: '))
tempo_empresa = int(input('Digite o tempo de empresa em anos: '))

if renda < 2000:
    print('Crédito negado')
else:
    if tempo_empresa >= 2:
        print('Crédito aprovado')
    else:
        print('Crédito em análise')
```

## **Exercício 10**

```python
valor_vendas = float(input('Digite o valor total das vendas: '))
quantidade_vendas = int(input('Digite a quantidade de vendas: '))

if valor_vendas < 5000:
    print('Desempenho abaixo da meta')
else:
    if quantidade_vendas >= 20:
        print('Desempenho excelente')
    else:
        print('Meta atingida')
```
