## 1. Listas aninhadas

Uma lista aninhada é uma lista que contém outras listas como elementos.

Veja o exemplo:

```
matriz = [    
    [1, 2, 3],    
    [4, 5, 6],    
    [7, 8, 9]
]
```

Temos uma lista principal com três listas dentro dela.

Acessando os elementos

Podemos utilizar dois índices: o primeiro indica a lista interna e o segundo indica o elemento dentro dela.

```
print(matriz[0])
print(matriz[0][1])
print(matriz[1][2])
```

Saída:

```
[1, 2, 3]
2
6
```

Para entender:

- `matriz[0]`: acessa a primeira lista.
- `matriz[0][1]`: acessa o segundo elemento da primeira lista.
- `matriz[1][2]`: acessa o terceiro elemento da segunda lista.

Alterando elementos

Também podemos modificar valores:

```
matriz[1][0] = 10

print(matriz)
```

Saída:

```
[[1, 2, 3], [10, 5, 6], [7, 8, 9]]
```

## 2. Dicionários aninhados

Um dicionário aninhado é um dicionário que contém outros dicionários como valores.

Exemplo:

```
alunos = {    
    "aluno1": {        
        "nome": "Carlos",        
        "idade": 22,        
        "nota": 8.5    
    },    
    "aluno2": {        
        "nome": "Mariana",        
        "idade": 24,        
        "nota": 9.0    
    }
}
```

Nesse exemplo, temos um dicionário principal chamado `alunos`, que contém dois dicionários internos.

Acessando os valores

```
print(alunos["aluno1"])
print(alunos["aluno1"]["nome"])
print(alunos["aluno2"]["nota"])
```

Saída:

```
{'nome': 'Carlos', 'idade': 22, 'nota': 8.5}
Carlos
9.0
```

A lógica é semelhante à das listas aninhadas:

- `alunos["aluno1"]`: acessa o dicionário do primeiro aluno.
- `alunos["aluno1"]["nome"]`: acessa o nome desse aluno.
- `alunos["aluno2"]["nota"]`: acessa a nota do segundo aluno.

Alterando e adicionando valores

Podemos modificar informações existentes:

```
alunos["aluno1"]["nota"] = 9.5
```

E também adicionar novas informações:

```
alunos["aluno1"]["curso"] = "Engenharia"
```

## 3. Listas contendo dicionários

Essa combinação é bastante comum quando trabalhamos com dados.

Imagine uma lista de produtos:

```
produtos = [    
    {"nome": "Notebook", "preco": 3500},    
    {"nome": "Mouse", "preco": 80},    
    {"nome": "Teclado", "preco": 150}
]
```

Cada elemento da lista é um dicionário.

Acessando informações:

```
print(produtos[0])
print(produtos[0]["nome"])
print(produtos[1]["preco"])
```

Saída:

```
{'nome': 'Notebook', 'preco': 3500}
Notebook
80
```

Percorrendo a estrutura com `for`:

```
for produto in produtos:    
    print(produto["nome"], produto["preco"])
```

Saída:

```
Notebook 3500
Mouse 80
Teclado 150
```

Observe que cada repetição acessa um dicionário da lista.

## 4. Dicionários contendo listas

Também podemos fazer o contrário: um dicionário que possui listas como valores.

```
empresa = {    
    "nome": "Empresa ABC",    
    "funcionarios": ["Carlos", "Mariana", "Pedro"],    
    "departamentos": ["RH", "TI", "Financeiro"]
}
```

Acessando os dados:

```
print(empresa["nome"])
print(empresa["funcionarios"])
print(empresa["funcionarios"][1])
```

Saída:

```
Empresa ABC
['Carlos', 'Mariana', 'Pedro']
Mariana
```

## Resumo

| Estrutura                 | Exemplo de acesso            |
| ------------------------- | ---------------------------- |
| Lista de listas           | `matriz[0][1]`               |
| Dicionário de dicionários | `alunos["aluno1"]["nome"]`   |
| Lista de dicionários      | `produtos[0]["nome"]`        |
| Dicionário de listas      | `empresa["funcionarios"][1]` |

Essas quatro combinações são a base para trabalhar com estruturas de dados aninhadas.
