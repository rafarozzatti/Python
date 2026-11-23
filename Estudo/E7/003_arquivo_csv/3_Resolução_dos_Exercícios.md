## Exercício 1

```python
import csv

with open('produtos.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)
```

## Exercício 2

```python
import csv

with open('produtos.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)

    next(leitor)

    for linha in leitor:
        print(linha)
```

## Exercício 3

```python
import csv

with open('funcionarios.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)

    next(leitor)

    for linha in leitor:
        print(linha[0], linha[2])
```

## Exercício 4

```python
import csv

with open('alunos.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)
```

## Exercício 5

```python
import csv

with open('alunos.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha['Nome'], linha['Curso'])
```

## Exercício 6

```python
import csv

with open('vendas.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(['Produto', 'Quantidade', 'Valor'])
    escritor.writerow(['Notebook', 2, 3500])
    escritor.writerow(['Mouse', 5, 80])
```

## Exercício 7

```python
import csv

with open('estoque.csv', 'w', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)

    dados = [        
        ['Produto', 'Quantidade'],        
        ['Teclado', 10],        
        ['Monitor', 5],        
        ['Mouse', 20]    
    ]    
    
    escritor.writerows(dados)
```

## Exercício 8

```python
import csv

with open('funcionarios.csv', 'w', encoding='utf-8') as arquivo:
    campos = ['Nome', 'Cargo', 'Salario']    
    
    escritor = csv.DictWriter(arquivo, fieldnames=campos)    
    
    escritor.writeheader()    
    
    escritor.writerow({        
        'Nome': 'Carlos',        
        'Cargo': 'Analista',        
        'Salario': 3500    
    })    
    
    escritor.writerow({        
        'Nome': 'Mariana',        
        'Cargo': 'Gerente',        
        'Salario': 5200    
    })
```

## Exercício 9

```python
import csv

with open('produtos.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo, delimiter=';')

    next(leitor)

    for registro in leitor:
        print(registro[0], registro[2])
```

## Exercício 10

```python
import csv

with open('clientes.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for i in leitor:
        if i['Email'] == '':
            print(i['Nome'])
```
