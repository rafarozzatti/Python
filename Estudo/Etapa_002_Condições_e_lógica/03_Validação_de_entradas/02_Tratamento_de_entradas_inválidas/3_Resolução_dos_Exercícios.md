## **Exercício 1**

```python
idade = int(input('Digite sua idade: '))

if idade < 0:
    print('Erro: idade inválida')
else:
    print('Idade registrada')
```

## **Exercício 2**

```python
preco = float(input('Digite o preço do produto: '))

if preco <= 0:
    print('Erro: preço inválido')
else:
    print('Preço registrado')
```

## **Exercício 3**

```python
quantidade = int(input('Digite a quantidade de produtos: '))

if quantidade <= 0:
    print('Erro: quantidade inválida')
else:
    print('Quantidade registrada')
```

## **Exercício 4**

```python
nota = float(input('Digite sua nota: '))

if nota < 0 or nota > 10:
    print('Erro: nota inválida')
else:
    print('Nota registrada')
```

## **Exercício 5**

```python
salario = float(input('Digite o salário: '))

if salario <= 0:
    print('Erro: salário inválido')
else:
    print('Salário registrado')
```

## **Exercício 6**

```python
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

if numero2 == 0:
    print('Erro: não é possível dividir por zero')
else:
    resultado = numero1 / numero2
    print(f'Resultado: {resultado}')
```

## **Exercício 7**

```python
valor_compra = float(input('Digite o valor da compra: '))
desconto = float(input('Digite o percentual de desconto: '))

if valor_compra <= 0:
    print('Erro: valor da compra inválido')
elif desconto < 0 or desconto > 100:
    print('Erro: percentual de desconto inválido')
else:
    valor_desconto = valor_compra * (desconto / 100)
    valor_final = valor_compra - valor_desconto

    print(f'Valor final: R$ {valor_final:.2f}')
```

## **Exercício 8**

```python
estoque = int(input('Digite a quantidade em estoque: '))
retirada = int(input('Digite a quantidade que será retirada: '))

if estoque <= 0 or retirada <= 0:
    print('Erro: quantidade inválida')
elif retirada > estoque:
    print('Erro: estoque insuficiente')
else:
    estoque_restante = estoque - retirada
    print(f'Estoque restante: {estoque_restante}')
```

## **Exercício 9**

```python
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if nome.strip() == '':
    print('Erro: nome não informado')
elif idade < 0:
    print('Erro: idade inválida')
else:
    print('Cadastro realizado com sucesso')
```

## **Exercício 10**

```python
preco = float(input('Digite o preço do produto: '))
quantidade = int(input('Digite a quantidade comprada: '))
desconto = float(input('Digite o percentual de desconto: '))

if preco <= 0:
    print('Erro: preço inválido')
elif quantidade <= 0:
    print('Erro: quantidade inválida')
elif desconto < 0 or desconto > 100:
    print('Erro: percentual de desconto inválido')
else:
    total = preco * quantidade
    valor_desconto = total * (desconto / 100)
    valor_final = total - valor_desconto

    print(f'Valor total: R$ {total:.2f}')
    print(f'Valor do desconto: R$ {valor_desconto:.2f}')
    print(f'Valor final: R$ {valor_final:.2f}')
```
