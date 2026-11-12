# Exercícios de Dicionário

## Exercício 1/10 — Criando dicionários

Crie um dicionário chamado `produto` com as seguintes informações:

| Chave          | Valor        |
| -------------- | ------------ |
| `"nome"`       | `"Notebook"` |
| `"preco"`      | `3500`       |
| `"quantidade"` | `10`         |
| `"disponivel"` | `True`       |

Depois:

1. Imprima o dicionário completo.
2. Imprima o tipo de dado da variável `produto` utilizando `type()`.
3. Imprima separadamente o nome do produto.
4. Imprima separadamente o preço do produto.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-1)

## Exercício 2

Considere o seguinte dicionário:

```
aluno = {    
    "nome": "Carlos",    
    "idade": 22,    
    "curso": "Engenharia"}
```

Faça o seguinte:

1. Imprima o valor da chave `"nome"` utilizando `get()`.
2. Imprima o valor da chave `"idade"` utilizando `get()`.
3. Tente acessar a chave `"nota"` utilizando `get()`.
4. Acesse a chave `"nota"` novamente, mas defina `"Não informada"` como valor padrão.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-2)

## Exercício 3

Considere o dicionário:

```
funcionario = {    
    "nome": "Mariana",    
    "idade": 25,    
    "cargo": "Assistente"}
```

Faça o seguinte:

1. Adicione a chave `"salario"` com o valor `2800`.
2. Altere a `"idade"` para `26`.
3. Altere o `"cargo"` para `"Analista"`.
4. Imprima o dicionário completo.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-3)

## Exercício 4

Considere o dicionário:

```
produto = {    
    "nome": "Monitor",    
    "preco": 1200,    
    "estoque": 15}
```

Faça o seguinte:

1. Utilize `update()` para alterar o preço para `1350`.
2. Utilize `update()` para adicionar a chave `"marca"` com o valor `"Samsung"`.
3. Utilize `update()` novamente para alterar o estoque para `20` e adicionar a chave `"garantia"` com o valor `12`.
4. Imprima o dicionário completo.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-4)

## Exercício 5

Considere o dicionário:

```
carro = {    
    "marca": "Toyota",    
    "modelo": "Corolla",    
    "ano": 2022,    
    "cor": "Prata",    
    "preco": 120000}
```

Faça o seguinte:

1. Remova a chave `"ano"` utilizando `pop()` e armazene o valor removido em uma variável chamada `ano_removido`.
2. Remova a chave `"cor"` utilizando `pop()` e armazene o valor removido em `cor_removida`.
3. Tente remover a chave `"quilometragem"` utilizando `pop()`, definindo `"Não informado"` como valor padrão.
4. Imprima os três resultados das remoções.
5. Imprima o dicionário atualizado.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-5)

## Exercício 6

Considere o dicionário:

```
funcionario = {    
    "nome": "Pedro",    
    "idade": 30,    
    "cargo": "Gerente",    
    "departamento": "Vendas"}
```

Faça o seguinte:

1. Utilize `popitem()` para remover o último par inserido e armazene o resultado em `ultimo_item`.
2. Utilize `del` para remover a chave `"idade"`.
3. Imprima `ultimo_item`.
4. Imprima o dicionário atualizado.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-6)

## Exercício 7

Considere o dicionário:

```
estoque = {    
    "produto1": "Teclado",    
    "produto2": "Mouse",    
    "produto3": "Monitor",    
    "produto4": "Headset"}
```

Faça o seguinte:

1. Imprima o dicionário original.
2. Utilize `clear()` para remover todos os elementos.
3. Imprima o dicionário novamente.
4. Imprima o tipo de dado da variável `estoque` utilizando `type()`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-7)

## Exercício 8

Considere o dicionário:

```
aluno = {    
    "nome": "Lucas",    
    "idade": 23,    
    "curso": "Medicina",    
    "periodo": "Noturno"}
```

Faça o seguinte:

1. Verifique se a chave `"nome"` existe.
2. Verifique se a chave `"nota"` existe.
3. Verifique se a chave `"idade"` não existe.
4. Verifique se a chave `"matricula"` não existe.
5. Imprima os quatro resultados.

Utilize `in` e `not in`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-8)

## Exercício 9

Considere o dicionário:

```
vendas = {    
    "Janeiro": 15000,    
    "Fevereiro": 18000,    
    "Março": 22000,    
    "Abril": 17000}
```

Faça o seguinte:

1. Imprima todas as chaves utilizando `keys()`.
2. Imprima todos os valores utilizando `values()`.
3. Imprima todos os pares de chave e valor utilizando `items()`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-9)

## Exercício 10

Considere o dicionário:

```
notas = {    
    "Matemática": 8.5,    
    "Português": 7.0,    
    "História": 9.0,    
    "Geografia": 6.5}
```

Faça o seguinte:

1. Utilize `for` para percorrer e imprimir todas as chaves.
2. Utilize outro `for` para percorrer e imprimir todos os valores.
3. Utilize um terceiro `for` com `items()` para imprimir cada matéria junto com sua nota, no formato:

```
Matéria: Matemática - Nota: 8.5
Matéria: Português - Nota: 7.0
Matéria: História - Nota: 9.0
Matéria: Geografia - Nota: 6.5
```

[Resolução](3_Resolução_dos_Exercícios.md#exercício-10)