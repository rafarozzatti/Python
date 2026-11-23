# Exercícios de Arquivos CSV

## Exercício 1

Imagine que existe um arquivo chamado `produtos.csv` com o seguinte conteúdo:

```
Produto,Preco,Estoque
Notebook,3500,10
Mouse,80,50
Teclado,150,25
```

Escreva um código que:

1. Importe o módulo `csv`.
2. Abra o arquivo no modo `'r'`, utilizando UTF-8.
3. Utilize `csv.reader()` para ler o arquivo.
4. Percorra todas as linhas com `for`.
5. Exiba cada linha com `print()`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-1)

## Exercício 2

Imagine que o arquivo `alunos.csv` contém:

```
Nome,Idade,Nota
Carlos,20,8.5
Mariana,22,9.0
João,19,7.5
```

Escreva um código que:

1. Importe `csv`.
2. Abra o arquivo no modo `'r'`, com UTF-8.
3. Utilize `csv.reader()`.
4. Utilize `next()` para ignorar o cabeçalho.
5. Percorra e exiba somente os registros dos alunos com `for`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-2)

## Exercício 3

Imagine que o arquivo `funcionarios.csv` contém:

```
Nome,Idade,Salario
Carlos,30,3500
Mariana,25,4200
João,28,3900
```

Escreva um código que:

1. Leia o arquivo utilizando `csv.reader()`.
2. Ignore o cabeçalho com `next()`.
3. Percorra os registros com `for`.
4. Exiba somente o nome e o salário de cada funcionário.

**Dica:** lembre-se de que o primeiro índice é `0`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-3)

## Exercício 4

Considere o arquivo `alunos.csv`:

```
Nome,Idade,Curso
Carlos,22,Engenharia
Mariana,24,Administração
João,21,Análise de Dados
```

Utilize `csv.DictReader()` para ler o arquivo e exiba cada registro completo.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-4)

## Exercício 5

Utilize o mesmo arquivo `alunos.csv`.

Agora, leia os registros com `csv.DictReader()` e exiba somente:

- Nome do aluno.
- Curso.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-5)

## Exercício 6

Crie um arquivo chamado `vendas.csv` utilizando `csv.writer()`.

O arquivo deverá conter:

**Cabeçalho:**

- Produto
- Quantidade
- Valor

**Registros:**

- Notebook, 2, 3500
- Mouse, 5, 80

Utilize `writerow()` para escrever o cabeçalho e cada registro.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-6)

## Exercício 7

Crie um arquivo chamado `estoque.csv` com o seguinte conteúdo:

| Produto | Quantidade |
| ------- | ---------- |
| Teclado | 10         |
| Monitor | 5          |
| Mouse   | 20         |

Utilize `csv.writer()` e `writerows()` para escrever o cabeçalho e os registros.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-7)

## Exercício 8

Crie um arquivo chamado `funcionarios.csv` utilizando `csv.DictWriter()`.

O arquivo deverá conter as colunas:

- Nome
- Cargo
- Salario

E os seguintes registros:

- Carlos, Analista, 3500
- Mariana, Gerente, 5200

Utilize:

1. `fieldnames` para definir os nomes das colunas.
2. `writeheader()` para escrever o cabeçalho.
3. `writerow()` para adicionar cada funcionário.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-8)

## Exercício 9

Considere o arquivo produtos.csv:
Produto;Quantidade;Preco
Notebook;2;3500
Mouse;5;80
Teclado;3;150


Utilize csv.reader() para:
1. Abrir o arquivo.
2. Ignorar o cabeçalho.
3. Percorrer os registros.
4. Exibir o nome do produto e seu preço.
Atenção: o arquivo utiliza ponto e vírgula (;) como delimitador, e não vírgula.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-9)

## Exercício 10

Considere o arquivo `clientes.csv`:

```
Nome,Email,Cidade
Carlos,carlos@email.com,São Paulo
Mariana,,Rio de Janeiro
João,joao@email.com,
```

Utilize `csv.DictReader()` para:

1. Ler o arquivo.
2. Percorrer os registros.
3. Verificar se o campo `Email` está vazio.
4. Exibir o nome dos clientes que não possuem email.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-10)
