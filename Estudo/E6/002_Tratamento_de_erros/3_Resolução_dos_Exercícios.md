## Exercício 1

```python
try:
    numero = int(input('Digite um número: '))

except ValueError:
    print('Digite um número inteiro válido.')

else:
    print(numero)
```

## Exercício 2

```python
try:
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite um número: '))

    divisao = numero1 / numero2

except ZeroDivisionError:
    print('Não é possível dividir por zero.')

else:
    print(divisao)
```

## Exercício 3

```python
try:
    numero = int(input('Digite um número: '))

except ValueError as erro:
    print(erro)

else:
    print(numero)
```

## Exercício 4

```python
try:
    lista = [10, 20, 30]

    numero = int(input('Digite o índice da lista: '))

    indice = lista[numero]

except IndexError:
    print('Índice inexistente.')

else:
    print(indice)
```

## Exercício 5

```python
try:
    pessoas = {
        'nome' : 'Carlos',
        'idade' : 25
    }

    chave = input('Digite o nome da chave que deseja consultar: ')

    resultado = pessoas[chave]

except KeyError:
    print('Essa chave não existe no dicionário.')

else:
    print(resultado)
```

## Exercício 6

```python
try:
    arquivo = open('dados.txt', 'r')

except FileNotFoundError:
    print('Arquivo não encontrado.')

else:
    print('Arquivo encontrado com sucesso.')
```

## Exercício 7

```python
try:
    numero = int(input('Digite um número: '))

except ValueError:
    print('Digite um número inteiro válido.')

else:
    print(numero)

finally:
    print('Programa finalizado.')
```

## Exercício 8

```python
try:
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite um número: '))

    divisao = numero1 / numero2

except ValueError:
    print('Digite apenas números inteiros.')

except ZeroDivisionError:
    print('Não é possível dividir por zero.')

else:
    print(divisao)
```

## Exercício 9

```python
try:
    produtos = {
        'Notebook' : 3500,
        'Mouse' : 80,
        'Teclado' : 150
    }

    nome = input('Digite o nome do produto: ')

    valor_produto = produtos[nome]

except KeyError as erro:
    print(erro)

else:
    print(valor_produto)

finally:
    print('Consulta finalizada.')
```

## Exercício 10

```python
try:
    nota1 = float(input('Digite a nota: '))
    nota2 = float(input('Digite a nota: '))
    nota3 = float(input('Digite a nota: '))

    media = (nota1 + nota2 + nota3) / 3

except ValueError:
    print('Digite apenas valores numéricos.')

else:
    print(media)

finally:
    print('Cálculo finalizado.')
```
