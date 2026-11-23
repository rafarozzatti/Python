# Exercícios de Leitura e escrita de arquivos .txt

## Exercício 1

Imagine que existe um arquivo chamado `produtos.txt` com o seguinte conteúdo:

```
Notebook
Mouse
Teclado
Monitor
```

Escreva um código Python que:

1. Abra o arquivo no modo de leitura (`'r'`).
2. Leia todo o conteúdo utilizando `read()`.
3. Armazene o conteúdo em uma variável.
4. Exiba o conteúdo com `print()`.
5. Utilize `with open()` e codificação UTF-8.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-1)

## Exercício 2

Imagine que o arquivo `alunos.txt` contém:

```
Carlos
Mariana
João
Fernanda
```

Escreva um código que:

1. Abra o arquivo no modo de leitura (`'r'`).
2. Leia somente a primeira linha utilizando `readline()`.
3. Armazene o resultado em uma variável.
4. Exiba essa linha com `print()`.
5. Utilize `with open()` e UTF-8.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-2)

## Exercício 3

Imagine que o arquivo `cidades.txt` contém:

```
São Paulo
Rio de Janeiro
Belo Horizonte
Curitiba
```

Escreva um código que:

1. Abra o arquivo no modo de leitura (`'r'`).
2. Leia todas as linhas utilizando `readlines()`.
3. Armazene o resultado em uma variável.
4. Exiba essa variável com `print()`.
5. Utilize `with open()` e UTF-8.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-3)

## Exercício 4

Escreva um código que crie ou sobrescreva o arquivo `funcionarios.txt` com as seguintes informações:

```
Nome: Carlos
Idade: 30
Cargo: Analista
```

Requisitos:

1. Utilize `with open()`.
2. Utilize o modo `'w'`.
3. Utilize `encoding='utf-8'`.
4. Utilize `write()` para escrever as três linhas.
5. Utilize `\n` para separar as linhas.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-4)

## Exercício 5

Imagine que o arquivo `funcionarios.txt` já contém:

```
Nome: Carlos
Idade: 30
Cargo: Analista
```

Escreva um código que adicione a seguinte informação ao final do arquivo, sem apagar o conteúdo existente:

```
Departamento: Tecnologia
```

Requisitos:

1. Utilize `with open()`.
2. Utilize o modo `'a'`.
3. Utilize `encoding='utf-8'`.
4. Utilize `write()` para adicionar a informação.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-5)

## Exercício 6

Escreva um código que:

1. Crie um arquivo chamado `relatorio.txt`.
2. Utilize o modo `'x'`.
3. Utilize `with open()` e `encoding='utf-8'`.
4. Escreva a seguinte mensagem no arquivo:

```
Relatório criado com sucesso!
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-6)

## Exercício 7

Responda com suas palavras:

Imagine que o arquivo `vendas.txt` já existe e contém informações sobre vendas.

Qual modo você utilizaria em cada situação?

**A)** Ler todas as informações do arquivo sem modificá-lo.

**B)** Substituir todo o conteúdo existente por novas informações.

**C)** Adicionar novas informações ao final, preservando o conteúdo anterior.

**D)** Criar um arquivo novo, mas impedir a criação caso já exista um arquivo com esse nome.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-7)

## Exercício 8

Imagine que você precisa criar um arquivo chamado `mensagem.txt` contendo:

```
Análise de Dados
Informações sobre São Paulo
```

Escreva o código para:

1. Abrir o arquivo no modo `'w'`.
2. Utilizar `encoding='utf-8'`.
3. Gravar as duas linhas utilizando `write()`.
4. Separar as linhas utilizando `\n`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-8)

## Exercício 9

Imagine que você precisa:

1. Criar ou sobrescrever o arquivo `resumo.txt`.
2. Gravar nele as seguintes informações:
   - `Produto: Notebook`
   - `Preço: 3500`
3. Depois, abrir o mesmo arquivo novamente no modo de leitura.
4. Ler todo o conteúdo utilizando `read()`.
5. Exibir o conteúdo com `print()`.

Utilize `with open()` e `encoding='utf-8'` nas duas operações.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-9)

## Exercício 10

Imagine que o arquivo `notas.txt` contém:

```
8.5
7.0
9.0
6.5
```

Escreva um código que:

1. Abra o arquivo no modo `'r'`, utilizando UTF-8.
2. Leia todas as linhas com `readlines()`.
3. Armazene o resultado em uma variável.
4. Exiba o conteúdo utilizando `print()`.

**Atenção:** neste exercício, queremos apenas ler e exibir as linhas. Não precisa calcular a média nem converter os valores.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-10)
