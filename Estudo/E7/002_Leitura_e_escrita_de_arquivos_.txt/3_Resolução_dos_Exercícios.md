## Exercício 1

```python
with open('produtos.txt', 'r', encoding='utf-8') as arquivo:

    leitura = arquivo.read()

    print(leitura)
```

## Exercício 2

```python
with open('alunos.txt', 'r', encoding='utf-8') as arquivo:

    leitura = arquivo.readline()

    print(leitura)
```

## Exercício 3

```python
with open('cidades.txt', 'r', encoding='utf-8') as arquivo:

    leitura = arquivo.readlines()

    print(leitura)
```

## Exercício 4

```python
with open('funcionarios.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Nome: Rafael\n')
    arquivo.write('Idade: 27\n')
    arquivo.write('Cargo: Analista de dados\n')
```

## Exercício 5

```python
with open('funcionarios.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Departamento: Tecnologia')
```

## Exercício 6

```python
with open('relatorio.txt', 'x', encoding='utf-8') as arquivo:
    arquivo.write('Relatório criado com sucesso!')
```

## Exercício 7

```
A) 'r' — leitura.

B) 'w' — escrita, substituindo o conteúdo.

C) 'a' — adiciona conteúdo ao final.

D) 'x' — cria um arquivo novo, sem sobrescrever um existente.
```

## Exercício 8

```python
with open('mensagem.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Análise de Dados\n')
    arquivo.write('Informações sobre São Paulo')
```

## Exercício 9

```python
with open('resumo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Produto: Notebook\n')
    arquivo.write('Preço: 3500')

with open('resumo.txt', 'r', encoding='utf-8') as arquivo:
    leitura = arquivo.read()

    print(leitura)
```

## Exercício 10

```python
with open('notas.txt', 'r', encoding='utf-8') as arquivo:
    leitura = arquivo.readlines()

    print(leitura)
```
