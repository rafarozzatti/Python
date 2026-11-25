## **Exercício 1**

```python
nome = 'Rafael'

if 'a' in nome:
    print('A letra foi encontrada')
else:
    print('A letra não foi encontrada')
```

## **Exercício 2**

```python
frase = 'Estou estudando Python'

if 'Python' in frase:
    print('Palavra encontrada')
else:
    print('Palavra não encontrada')
```

## **Exercício 3**

```python
frutas = ['maçã', 'banana', 'uva', 'laranja']

if 'banana' in frutas:
    print('Fruta encontrada')
else:
    print('Fruta não encontrada')
```

## **Exercício 4**

```python
numeros = [10, 20, 30, 40, 50]

if 25 in numeros:
    print('Número encontrado')
else:
    print('Número não encontrado')
```

## **Exercício 5**

```python
cores = ['azul', 'verde', 'vermelho']

if 'amarelo' not in cores:
    print('Cor não encontrada')
else:
    print('Cor encontrada')
```

## **Exercício 6**

```python
nome = 'Python'

if 'z' not in nome:
    print('A letra não foi encontrada')
else:
    print('A letra foi encontrada')
```

## **Exercício 7**

```python
funcionario_ativo = True
setor = 'Financeiro'

setores_autorizados = ['TI', 'Financeiro', 'RH']

if funcionario_ativo:
    if setor in setores_autorizados:
        print('Acesso permitido')
    else:
        print('Setor não autorizado')
else:
    print('Funcionário inativo')
```

## **Exercício 8**

```python
idade = 20
categoria = 'Estudante'

categorias_desconto = ['Estudante', 'Idoso']

if idade >= 18:
    if categoria in categorias_desconto:
        print('Desconto permitido')
    else:
        print('Sem direito ao desconto')
else:
    print('Idade não atende ao requisito')
```

## **Exercício 9**

```python
usuario_ativo = True
usuario = 'Carlos'

usuarios_bloqueados = ['João', 'Pedro', 'Marcos']

if usuario_ativo:
    if usuario not in usuarios_bloqueados:
        print('Acesso permitido')
    else:
        print('Usuário bloqueado')
else:
    print('Usuário inativo')
```

## **Exercício 10**

```python
idade = 25
cargo = 'Analista'

cargos_autorizados = ['Analista', 'Coordenador', 'Gerente']

if idade >= 18:
    if cargo in cargos_autorizados:
        print('Acesso autorizado')
    else:
        print('Cargo não autorizado')
else:
    print('Idade insuficiente')
```
