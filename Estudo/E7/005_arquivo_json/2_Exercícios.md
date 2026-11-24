# Exercícios de Arquivo JSON

## Exercício 1

Considere o arquivo `clientes.json`:

```
{
    "nome": "Carlos",
    "idade": 30,
    "cidade": "São Paulo"
}
```

Escreva um código Python que:

1. Importe o módulo `json`.
2. Abra o arquivo `clientes.json` no modo de leitura.
3. Utilize `json.load()` para carregar os dados.
4. Exiba o conteúdo completo utilizando `print()`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-1)

## Exercício 2

Considere o mesmo arquivo `clientes.json`:

```
{
    "nome": "Carlos",
    "idade": 30,
    "cidade": "São Paulo"
}
```

Utilize `json.load()` para ler o arquivo e exiba separadamente:

1. Nome do cliente.
2. Idade.
3. Cidade.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-2)

## Exercício 3

Considere o arquivo `produtos.json`:

```
[
    {
        "produto": "Notebook",
        "preco": 3500
    },
    {
        "produto": "Mouse",
        "preco": 80
    },
    {
        "produto": "Teclado",
        "preco": 150
    }
]
```

Escreva um código que:

1. Importe o módulo `json`.
2. Abra o arquivo `produtos.json`.
3. Utilize `json.load()` para carregar os dados.
4. Percorra os registros com `for`.
5. Exiba o nome e o preço de cada produto.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-3)

## Exercício 4

Crie um dicionário chamado `funcionario` com os seguintes dados:

- Nome: Mariana
- Idade: 25
- Cargo: Analista de Dados

Depois:

1. Importe o módulo `json`.
2. Abra um arquivo chamado `funcionario.json` no modo de escrita (`'w'`).
3. Utilize `json.dump()` para salvar o dicionário no arquivo.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-4)

## Exercício 5

Vamos continuar utilizando o dicionário do exercício anterior.

Crie um arquivo chamado `funcionario.json` e salve os mesmos dados utilizando `json.dump()`.

Desta vez, utilize o parâmetro `indent=4` para organizar o conteúdo do arquivo e facilitar sua leitura.

O resultado esperado no arquivo é:

```
{
    "Nome": "Mariana",
    "Idade": 25,
    "Cargo": "Analista de Dados"
}
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-5)

## Exercício 6

Crie um dicionário chamado `empresa` com os seguintes dados:

- Nome: São Paulo Tecnologia
- Cidade: São Paulo
- País: Brasil

Salve essas informações no arquivo `empresa.json` utilizando:

- `json.dump()`
- `indent=4`
- `ensure_ascii=False`

O objetivo é preservar os caracteres especiais, como o `ã`, diretamente no arquivo JSON.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-6)

## Exercício 7

Crie um dicionário chamado `produto` com os seguintes dados:

- Nome: Notebook
- Preço: 3500
- Disponível: `True`

Depois:

1. Utilize `json.dumps()` para converter o dicionário em uma string JSON.
2. Armazene o resultado na variável `texto`.
3. Exiba o conteúdo de `texto`.
4. Exiba o tipo de dado de `texto` utilizando `type()`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-7)

## Exercício 8

Considere a seguinte string:

```
texto = '{"Nome": "Carlos", "Idade": 30, "Cidade": "Santos"}'
```

Escreva um código que:

1. Importe o módulo `json`.
2. Utilize `json.loads()` para converter a string em uma estrutura Python.
3. Armazene o resultado na variável `dados`.
4. Exiba o nome e a cidade utilizando as chaves do dicionário.
5. Exiba o tipo de dado de `dados` com `type()`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-8)

## Exercício 9

Considere o arquivo `funcionario.json`:

```
{
    "Nome": "Mariana",
    "Idade": 25,
    "Cargo": "Analista"
}
```

Escreva um código que:

1. Leia o arquivo utilizando `json.load()`.
2. Altere a idade de Mariana para `26`.
3. Altere o cargo para `Analista de Dados`.
4. Salve as alterações no mesmo arquivo utilizando `json.dump()`.
5. Utilize `indent=4` e `ensure_ascii=False`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-9)

## Exercício 10

Considere o arquivo `alunos.json`:

```
[
    {
        "Nome": "Carlos",
        "Nota": 7.5
    },
    {
        "Nome": "Mariana",
        "Nota": 8.0
    },
    {
        "Nome": "João",
        "Nota": 6.5
    }
]
```

Escreva um código que:

1. Leia o arquivo utilizando `json.load()`.
2. Percorra os alunos com `for`.
3. Aumente a nota de cada aluno em 1 ponto.
4. Salve os dados atualizados no mesmo arquivo utilizando `json.dump()`.
5. Utilize `indent=4` e `ensure_ascii=False`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-10)
