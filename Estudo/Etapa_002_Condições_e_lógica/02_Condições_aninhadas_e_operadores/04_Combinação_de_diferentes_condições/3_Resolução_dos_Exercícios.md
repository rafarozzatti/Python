## **Exercício 1**

```python
salario = 2500
tempo_empresa = 3
cargo = 'Gerente'

if (salario >= 3000 and tempo_empresa >= 2) or cargo == 'Gerente':
    print('Benefício concedido')
else:
    print('Benefício não concedido')
```

## **Exercício 2**

```python
idade = 25
autorizado = True
bloqueado = False

if idade >= 18 and autorizado and not bloqueado:
    print('Acesso permitido')
else:
    print('Acesso negado')
```

## **Exercício 3**

```python
funcionario_ativo = True
setor = 'TI'

setores_autorizados = ['TI', 'Financeiro', 'RH']

if funcionario_ativo and setor in setores_autorizados:
    print('Acesso permitido')
else:
    print('Acesso negado')
```

## **Exercício 4**

```python
usuario = 'Carlos'
usuario_ativo = True

usuarios_bloqueados = ['João', 'Pedro', 'Marcos']

if usuario_ativo and usuario not in usuarios_bloqueados:
    print('Acesso permitido')
else:
    print('Acesso negado')
```

## **Exercício 5**

```python
idade = 20
nota = 8
possui_bolsa = False

if idade >= 18:
    if nota >= 7 or possui_bolsa:
        print('Atende aos critérios')
    else:
        print('Não atende aos critérios')
else:
    print('Idade insuficiente')
```

## **Exercício 6**

```python
idade = 30
renda = 2500
possui_garantia = True
bloqueado = False

if idade >= 18:
    if (renda >= 3000 or possui_garantia) and not bloqueado:
        print('Crédito aprovado')
    else:
        print('Crédito negado')
else:
    print('Idade insuficiente')
```

## **Exercício 7**

```python
idade = 25
cargo = 'Analista'
ativo = True

cargos_autorizados = ['Analista', 'Coordenador', 'Gerente']

if idade >= 18 and ativo:
    if cargo in cargos_autorizados:
        print('Acesso autorizado')
    else:
        print('Cargo não autorizado')
else:
    print('Não atende aos requisitos')
```

## **Exercício 8**

```python
nota = 6
frequencia = 80
trabalho_extra = True

if nota >= 5:
    if (nota >= 7 or trabalho_extra) and frequencia >= 75:
        print('Aluno aprovado')
    else:
        print('Aluno reprovado')
else:
    print('Aluno reprovado')
```

## **Exercício 9**

```python
idade = 22
setor = 'Financeiro'
ativo = True
bloqueado = False

setores_autorizados = ['TI', 'Financeiro', 'RH']

if idade >= 18:
    if ativo and not bloqueado and setor in setores_autorizados:
        print('Acesso permitido')
    else:
        print('Acesso negado')
else:
    print('Acesso negado por idade')
```

## **Exercício 10**

```python
idade = 30
renda = 4000
tempo_empresa = 3
cargo = 'Analista'
bloqueado = False

cargos_autorizados = ['Analista', 'Coordenador', 'Gerente']

if idade >= 18:
    if renda >= 3000 and tempo_empresa >= 2:
        if cargo in cargos_autorizados and not bloqueado:
            print('Crédito aprovado')
        else:
            print('Crédito negado')
    else:
        print('Crédito negado')
else:
    print('Crédito negado')
```
