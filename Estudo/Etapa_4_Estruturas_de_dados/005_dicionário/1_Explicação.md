Vamos começar! Agora estudaremos Dicionários (`dict`) em Python.

Assim como fizemos com listas, tuplas e conjuntos, primeiro vou explicar o conteúdo completo, com exemplos e saídas. Depois começaremos os 10 exercícios, um de cada vez.

# Aula — Dicionários (`dict`)

## 1. O que são dicionários?

Dicionários são estruturas que armazenam dados em pares de chave e valor (key-value).

Cada informação possui uma chave que permite acessar seu respectivo valor.

Exemplo:

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27,    
    "altura": 1.69,    
    "estudante": True
}

print(pessoa)
print(type(pessoa))
```

Saída:

```
{'nome': 'Rafael', 'idade': 27, 'altura': 1.69, 'estudante': True}
<class 'dict'>
```

Observe:

| Chave         | Valor      |
| ------------- | ---------- |
| `"nome"`      | `"Rafael"` |
| `"idade"`     | `27`       |
| `"altura"`    | `1.69`     |
| `"estudante"` | `True`     |

Algumas características dos dicionários:

- Armazenam dados em pares de chave e valor.
- As chaves não podem se repetir.
- Os valores podem se repetir.
- Podem armazenar diferentes tipos de dados.
- São mutáveis, ou seja, podemos adicionar, alterar e remover informações.
- Mantêm a ordem de inserção dos elementos.

## 2. Criando dicionários

Utilizamos `{}` para criar um dicionário, separando cada chave do seu valor com `:`.

```
produto = {    
    "nome": "Notebook",    
    "preco": 3500,    
    "quantidade": 10
}
```

Também podemos criar um dicionário vazio:

```
dados = {}

print(dados)
print(type(dados))
```

Saída:

```
{}
<class 'dict'>
```

Outra maneira de criar um dicionário vazio é utilizando `dict()`:

```
dados = dict()
```

Atenção: `{}` cria um dicionário vazio, enquanto `set()` cria um conjunto vazio.

## 3. Acessando valores

Para acessar um valor, utilizamos sua chave entre colchetes.

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27,    
    "cidade": "São Paulo"
}

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])
```

Saída:

```
Rafael
27
São Paulo
```

Se tentarmos acessar uma chave que não existe, Python apresentará um erro (`KeyError`).

### Método `get()`

Também podemos acessar valores utilizando o método `get()`.

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27
}

print(pessoa.get("nome"))
print(pessoa.get("profissao"))
```

Saída:

```
Rafael
None
```

A diferença é:

- `pessoa["profissao"]`: gera erro se a chave não existir.
- `pessoa.get("profissao")`: retorna `None` se a chave não existir.

Também podemos definir um valor padrão para quando a chave não existir:

```
print(pessoa.get("profissao", "Não informado"))
```

Saída:

```
Não informado
```

## 4. Adicionando elementos

Para adicionar uma informação, basta atribuir um valor a uma nova chave.

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27
}

pessoa["cidade"] = "São Paulo"

print(pessoa)
```

Saída:

```
{'nome': 'Rafael', 'idade': 27, 'cidade': 'São Paulo'}
```

Se a chave não existir, ela será criada.

## 5. Alterando valores

Se a chave já existir, a atribuição altera seu valor.

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27
}

pessoa["idade"] = 28

print(pessoa)
```

Saída:

```
{'nome': 'Rafael', 'idade': 28}
```

Portanto, a mesma sintaxe serve para adicionar e alterar informações.

## 6. Atualizando com `update()`

O método `update()` permite adicionar ou alterar várias informações de uma vez.

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27
}

pessoa.update({    
    "idade": 28,    
    "cidade": "São Paulo"
})

print(pessoa)
```

Saída:

```
{'nome': 'Rafael', 'idade': 28, 'cidade': 'São Paulo'}
```

Observe que:

- `"idade"` já existia, então seu valor foi alterado.
- `"cidade"` não existia, então foi adicionada.

## 7. Removendo elementos

Existem algumas maneiras de remover informações de um dicionário.

### Método `pop()`

Remove uma chave específica e retorna seu valor.

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27,    
    "cidade": "São Paulo"
}

resultado = pessoa.pop("idade")

print(resultado)
print(pessoa)
```

Saída:

```
27
{'nome': 'Rafael', 'cidade': 'São Paulo'}
```

Se a chave não existir, ocorre um erro. Podemos evitar isso informando um valor padrão:

```
resultado = pessoa.pop("profissao", "Não encontrado")

print(resultado)
```

Saída:

```
Não encontrado
```

### Método `popitem()`

Remove e retorna o último par de chave e valor inserido no dicionário.

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27,    
    "cidade": "São Paulo"
}

resultado = pessoa.popitem()

print(resultado)
print(pessoa)
```

Saída:

```
('cidade', 'São Paulo')
{'nome': 'Rafael', 'idade': 27}
```

### Palavra-chave `del`

Remove uma chave específica.

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27,    
    "cidade": "São Paulo"
}

del pessoa["idade"]

print(pessoa)
```

Saída:

```
{'nome': 'Rafael', 'cidade': 'São Paulo'}
```

A diferença é que `del` não retorna o valor removido.

## 8. Limpando o dicionário com `clear()`

O método `clear()` remove todos os elementos do dicionário.

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27
}

pessoa.clear()

print(pessoa)
```

Saída:

```
{}
```

A variável continua existindo, mas o dicionário fica vazio.

## 9. Verificando se uma chave existe

Podemos utilizar `in` e `not in` para verificar se uma chave está presente.

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27
}

print("nome" in pessoa)
print("cidade" in pessoa)
print("idade" not in pessoa)
```

Saída:

```
True
False
False
```

Importante: em dicionários, `in` verifica as chaves, não os valores.

Por exemplo:

```
print("Rafael" in pessoa)
```

Retorna `False`, porque `"Rafael"` é um valor, não uma chave.

## 10. Conhecendo as chaves com `keys()`

O método `keys()` retorna todas as chaves do dicionário.

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27,    
    "cidade": "São Paulo"
}

print(pessoa.keys())
```

Saída:

```
dict_keys(['nome', 'idade', 'cidade'])
```

## 11. Conhecendo os valores com `values()`

O método `values()` retorna todos os valores.

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27,    
    "cidade": "São Paulo"
}

print(pessoa.values())
```

Saída:

```
dict_values(['Rafael', 27, 'São Paulo'])
```

## 12. Conhecendo os pares com `items()`

O método `items()` retorna os pares de chave e valor.

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27,    
    "cidade": "São Paulo"
}

print(pessoa.items())
```

Saída:

```
dict_items([('nome', 'Rafael'), ('idade', 27), ('cidade', 'São Paulo')])
```

Cada par é apresentado como uma tupla.

## 13. Percorrendo dicionários com `for`

Podemos utilizar o `for` para percorrer as informações de um dicionário.

### Percorrendo as chaves

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27,    
    "cidade": "São Paulo"
}

for chave in pessoa:    
    print(chave)
```

Saída:

```
nome
idade
cidade
```

Também podemos utilizar `keys()`:

```
for chave in pessoa.keys():    
    print(chave)
```

### Percorrendo os valores

```
for valor in pessoa.values():   
    print(valor)
```

Saída:

```
Rafael
27
São Paulo
```

### Percorrendo chaves e valores

Utilizamos `items()` para obter os dois ao mesmo tempo.

```
for chave, valor in pessoa.items():    
    print(chave, ":", valor)
```

Saída:

```
nome : Rafael
idade : 27
cidade : São Paulo
```

## 14. Descobrindo a quantidade de elementos com `len()`

A função `len()` retorna a quantidade de pares de chave e valor.

```
pessoa = {    
    "nome": "Rafael",    
    "idade": 27,    
    "cidade": "São Paulo"
}

print(len(pessoa))
```

Saída:

```
3
```

## 15. Dicionários aninhados

Um dicionário pode armazenar outro dicionário como valor. Chamamos isso de dicionário aninhado.

```
alunos = {    
    "aluno1": {        
        "nome": "Rafael",        
        "nota": 8.5    
    },    
    "aluno2": {        
        "nome": "Lucas",        
        "nota": 9.0    
    }
}
    
print(alunos["aluno1"]["nome"])
print(alunos["aluno2"]["nota"])
```

Saída:

```
Rafael
9.0
```

Observe que utilizamos duas chaves para acessar informações internas.

# Resumo dos métodos e operações

| Método / operação | Finalidade                                            |
| ----------------- | ----------------------------------------------------- |
| `dict()`          | Cria um dicionário vazio                              |
| `get()`           | Acessa um valor sem gerar erro se a chave não existir |
| `update()`        | Adiciona ou atualiza informações                      |
| `pop()`           | Remove uma chave específica e retorna seu valor       |
| `popitem()`       | Remove o último par inserido                          |
| `clear()`         | Remove todos os elementos                             |
| `keys()`          | Retorna as chaves                                     |
| `values()`        | Retorna os valores                                    |
| `items()`         | Retorna os pares de chave e valor                     |
| `len()`           | Retorna a quantidade de pares                         |
| `in` / `not in`   | Verifica a existência de uma chave                    |
| `del`             | Remove uma chave específica                           |
