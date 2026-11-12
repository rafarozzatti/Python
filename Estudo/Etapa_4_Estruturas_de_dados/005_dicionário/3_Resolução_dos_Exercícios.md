## Exercício 1

```python
produto = {
    'nome' : 'Notebook',
    'preco' : 3500,
    'quantidade' : 10,
    'disponivel' : True
}

print(produto)
print(type(produto))
print(produto['nome'])
print(produto['preco'])
```

## Exercício 2

```python
aluno = {
    "nome": "Carlos",
    "idade": 22,
    "curso": "Engenharia"
}

print(aluno.get('nome'))
print(aluno.get('idade'))
print(aluno.get('nota'))
print(aluno.get('nota', 'Não informada'))
```

## Exercício 3

```python
funcionario = {
    "nome": "Mariana",
    "idade": 25,
    "cargo": "Assistente"
}

funcionario['salario'] = 2800
funcionario['idade'] = 26
funcionario['cargo'] = 'Analista'

print(funcionario)
```

## Exercício 4

```python
produto = {
    "nome": "Monitor",
    "preco": 1200,
    "estoque": 15
}

produto.update({
    'preco' : 1350,
    'marca' : 'Samsung',
    'estoque' : 20,
    'garantia' : 12
})

print(produto)
```

## Exercício 5

```python
carro = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2022,
    "cor": "Prata",
    "preco": 120000
}

ano_removido = carro.pop('ano')
cor_removida = carro.pop('cor')
quilometragem_removida = carro.pop('quilometragem', 'Não informado')

print(ano_removido)
print(cor_removida)
print(quilometragem_removida)
print(carro)
```

## Exercício 6

```python
funcionario = {
    "nome": "Pedro",
    "idade": 30,
    "cargo": "Gerente",
    "departamento": "Vendas"
}

ultimo_item = funcionario.popitem()
del funcionario['idade']

print(ultimo_item)
print(funcionario)
```

## Exercício 7

```python
estoque = {
    "produto1": "Teclado",
    "produto2": "Mouse",
    "produto3": "Monitor",
    "produto4": "Headset"
}

print(estoque)

estoque.clear()

print(estoque)
print(type(estoque))
```

## Exercício 8

```python
aluno = {
    "nome": "Lucas",
    "idade": 23,
    "curso": "Medicina",
    "periodo": "Noturno"
}

print('nome' in aluno)
print('nota' in aluno)
print('idade' not in aluno)
print('matricula' not in aluno)
```

## Exercício 9

```python
vendas = {
    "Janeiro": 15000,
    "Fevereiro": 18000,
    "Março": 22000,
    "Abril": 17000
}

print(vendas.keys())
print(vendas.values())
print(vendas.items())
```

## Exercício 10

```python
notas = {
    "Matemática": 8.5,
    "Português": 7.0,
    "História": 9.0,
    "Geografia": 6.5
}

for chave in notas.keys():
    print(chave)
print()

for valor in notas.values():
    print(valor)
print()

for chave, valor in notas.items():
    print(f'Matéria: {chave} - Nota: {valor:.1f}')
```
