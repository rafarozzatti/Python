## Exercício 1

```python
def mensagem():
    print('Estou aprendendo funções em Python!')

mensagem()
```

## Exercício 2

```python
def saudacao(nome):
    print(f'Olá, {nome}! Seja bem-vindo!')

saudacao('Carlos')
```

## Exercício 3

```python
def apresentar(nome, idade):
    print(f'''Nome: {nome}
Idade: {idade} anos''')

apresentar('Mariana', 25)
```

## Exercício 4

```python
def somar(a, b):
    return a + b

resultado = somar(15, 25)

print(resultado)
```

## Exercício 5

```python
def apresentar(nome, cidade='São Paulo'):
    print(f'Olá {nome}! Você mora em {cidade}')

apresentar('Rafael')
apresentar('Carlos', 'Santos')
```

## Exercício 6

```python
def dados_pessoais (nome, idade, profissao):
    print(f'''{nome}
{idade}
{profissao}''')

dados_pessoais(profissao='Engenheiro', nome='Rafael', idade=27)
```

## Exercício 7

```python
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

resultado = calcular_media(8, 6)

print(resultado)
```

## Exercício 8

```python
def verificar_idade (idade):
    print(f'Você tem {idade} anos')

resultado = verificar_idade(27)

print(resultado)

#Por que aparece None?

#Quando uma função não utiliza return explicitamente, Python retorna automaticamente o valor None.

#No código:
#1. verificar_idade(27) executa o print() dentro da função.
#2. Como não existe return, a função devolve None.
#3. Esse valor é armazenado em resultado.
#4. print(resultado) exibe None.
#Essa é uma diferença importante entre print() e return.
```

## Exercício 9

```python
def classificar_nota (nota):
    if nota >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

resultado1 = classificar_nota(8)
resultado2 = classificar_nota(5)

print(resultado1)
print(resultado2)
```

## Exercício 10

```python
def calcular_desconto(preco, desconto=10):
    preco_final = preco - ((preco * desconto) / 100)
    return preco_final

produto1 = calcular_desconto(200)
produto2 = calcular_desconto(500, 20)

print(produto1)
print(produto2)
```
