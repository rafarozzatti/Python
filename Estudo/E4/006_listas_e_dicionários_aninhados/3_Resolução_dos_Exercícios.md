## Exercício 1

```python
notas = [
    [8 , 7, 9],
    [6, 8, 7],
    [9, 10, 8]
]

print(notas)
print(notas[0])
print(notas[1][1])
print(notas[2][2])
```

## Exercício 2

```python
notas = [
    [8 , 7, 9],
    [6, 8, 7],
    [9, 10, 8]
]

notas[0][0] = 10
notas[1][2] = 9

print(notas)
```

## Exercício 3

```python
notas = [
    [8, 7, 9],
    [6, 8, 7],
    [9, 10, 8]
]

for i in range(3):
    for j in range(3):
        print(notas[i][j])
```

## Exercício 4

```python
alunos = {
    'aluno1' : {
        'nome' : 'Carlos',
        'idade' : 22,
        'nota' : 8.5
    },
    'aluno2' : {
        'nome': 'Mariana',
        'idade' : 24,
        'nota' : 9.0
    }
}

print(alunos)
print(alunos['aluno1']['nome'])
print(alunos['aluno2']['idade'])
print(alunos['aluno1']['nota'])
```

## Exercício 5

```python
alunos = {
    'aluno1' : {
        'nome' : 'Carlos',
        'idade' : 22,
        'nota' : 8.5
    },
    'aluno2' : {
        'nome': 'Mariana',
        'idade' : 24,
        'nota' : 9.0
    }
}

alunos['aluno1']['idade'] = 23
alunos['aluno2']['nota'] = 9.5
alunos['aluno1']['curso'] = 'Engenharia'

print(alunos)
```

## Exercício 6

```python
produtos = [
    {'Produto 1' : 'Notebook', 'preco' : 3500},
    {'Produto 2' : 'Mouse', 'preco' : 80},
    {'Produto 3' : 'Teclado', 'preco' : 150}
]

print(produtos)
print(produtos[0]['Produto 1'])
print(produtos[1]['preco'])
print(produtos[2]['Produto 3'])
```

## Exercício 7

```python
produtos = [
    {'Produto' : 'Notebook', 'preco' : 3500},
    {'Produto' : 'Mouse', 'preco' : 80},
    {'Produto' : 'Teclado', 'preco' : 150}
]

for produto in produtos:
    print(f"Produto: {produto['Produto']} - Preço: {produto['preco']}")
```

## Exercício 8

```python
empresa = {
    'nome' : 'Empresa ABC',
    'funcionarios' : ['Carlos', 'Mariana', 'Pedro'],
    'departamentos' : ['RH', 'TI', 'Financeiro']
}

print(empresa['nome'])
print(empresa['funcionarios'])
print(empresa['funcionarios'][1])
print(empresa['departamentos'][2])
```

## Exercício 9

```python
vendas = [
    {'produto' : 'Notebook', 'quantidade' : 2, 'valor unitario' : 3500},
    {'produto' : 'Mouse', 'quantidade' : 3, 'valor unitario' : 80},
    {'produto' : 'Teclado', 'quantidade' : 1, 'valor unitario' : 150}
]

print(vendas[1]['produto'])

vendas[0]['quantidade'] = 3
vendas[2]['cliente'] = 'Rafael'

print(vendas)
```

## Exercício 10

```python
funcionarios = [
    {'nome' : 'Carlos', 'idade' : 25, 'salario' : 3000},
    {'nome' : 'Mariana', 'idade' : 30, 'salario' : 4500},
    {'nome' : 'Pedro', 'idade' : 28, 'salario' : 3500}
]

for funcionario in funcionarios:
    print(f'''Nome: {funcionario['nome']}
Salário: {funcionario['salario']}''')

funcionarios[0]['salario'] = 3500
funcionarios.append({'nome' : 'Ana', 'idade' : 27, 'salario' : 4000})

print(funcionarios)
```
