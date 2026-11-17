## Exercício 1

```python
def calcular_total(numeros):
    soma = sum(numeros)

    return soma

preco = [50, 100, 150, 200]

total = calcular_total(preco)

print(total)
```

## Exercício 2

```python
def mostrar_produtos(lista):
    for produto in lista:
        print(produto)

produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor']

mostrar_produtos(produtos)
```

## Exercício 3

```python
def adicionar_produto(produtos, novo_produto):
    produtos.append(novo_produto)

lista = ['Notebook', 'Mouse']

adicionar_produto(lista, 'Teclado')

print(lista)
```

## Exercício 4

```python
def remover_produto(produtos, produto_remover):
    produtos.remove(produto_remover)

lista = ['Notebook', 'Mouse', 'Teclado', 'Monitor']

remover_produto(lista, 'Mouse')

print(lista)
```

## Exercício 5

```python
def mostrar_funcionario(funcionario):
    print(f'''Nome: {funcionario['nome']}
Cargo: {funcionario['cargo']}''')

funcionario = {
    'nome': 'Carlos',
    'cargo': 'Analista de Dados',
    'salario': 3500
}

mostrar_funcionario(funcionario)
```

## Exercício 6

```python
def atualizar_salario(funcionario, novo_salario):
    funcionario['salario'] = novo_salario

funcionario = {
    'nome' : 'Ana',
    'cargo' : 'Desenvolvedora',
    'salario' : 4000
}

atualizar_salario(funcionario, 5000)

print(funcionario)
```

## Exercício 7

```python
def criar_produto(nome, preco, quantidade):
    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }

    return produto

produto = criar_produto('Notebook', 3500, 10)

print(produto)
```

## Exercício 8

```python
def analisar_notas(notas):
    soma = sum(notas)
    media =  soma / len(notas)

    return soma, media

lista = [7, 8, 9, 6, 10]

soma, media = analisar_notas(lista)

print(soma)
print(media)
```

## Exercício 9

```python
def mostrar_produtos(produtos):
    for produto in produtos:
        print(f"Produto: {produto['nome']} | Preço: {produto['preco']}")

produtos = [
    {'nome': 'Notebook', 'preco': 3500},
    {'nome': 'Mouse', 'preco': 80},
    {'nome': 'Teclado', 'preco': 150}
]

mostrar_produtos(produtos)
```

## Exercício 10

```python
def aumentar_salario(funcionarios):
    for funcionario in funcionarios:
        funcionario['salario'] += 500

funcionarios = [
    {'nome': 'Carlos', 'salario': 3000},
    {'nome': 'Ana', 'salario': 4000},
    {'nome': 'Pedro', 'salario': 3500}
]

aumentar_salario(funcionarios)

print(funcionarios)
```
