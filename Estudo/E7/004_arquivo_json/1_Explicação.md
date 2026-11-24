## 1. O que é JSON?

JSON significa *JavaScript Object Notation*. É um formato utilizado para armazenar e trocar dados entre sistemas.

É muito comum encontrar arquivos JSON em:

- APIs.
- Sistemas web.
- Aplicações.
- Bancos de dados.
- Processos de integração de dados.

Um arquivo chamado `clientes.json`, por exemplo, pode armazenar:

```
{
    "nome": "Carlos",
    "idade": 30,
    "cidade": "São Paulo"
}
```

Observe que a estrutura utiliza pares de chave e valor, semelhante aos dicionários do Python.

## 2. Importando o módulo json

Para trabalhar com arquivos JSON, utilizamos:

```
import json
```

O módulo `json` já faz parte da biblioteca padrão do Python. Portanto, não precisamos instalar nada com `pip`.

## 3. Lendo arquivos JSON — `json.load()`

Imagine que temos o arquivo `clientes.json`:

```
{
    "nome": "Carlos",
    "idade": 30,
    "cidade": "São Paulo"
}
```

Podemos ler seu conteúdo assim:

```
import json

with open('clientes.json', 'r', encoding='utf-8') as arquivo:    
    dados = json.load(arquivo)
    
    print(dados)
```

Resultado:

```
{'nome': 'Carlos', 'idade': 30, 'cidade': 'São Paulo'}
```

**O que aconteceu?**

- `open()` abriu o arquivo.
- `json.load()` leu o conteúdo JSON e o converteu para uma estrutura Python.
- A variável `dados` recebeu um dicionário.

Uma diferença importante em relação ao CSV: o JSON consegue preservar estruturas mais complexas, como listas e dicionários aninhados.

## 4. Acessando informações do JSON

Como o conteúdo foi convertido em um dicionário, podemos acessar os valores pelas chaves:

```
print(dados['nome'])
print(dados['idade'])
print(dados['cidade'])
```

Resultado:

```
Carlos
30
São Paulo
```

Também podemos alterar os valores normalmente:

```
dados['idade'] = 31

print(dados['idade'])
```

Resultado:

```
31
```

## 5. JSON contendo uma lista de registros

É bastante comum encontrar arquivos JSON contendo vários registros.

Exemplo de `produtos.json`:

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

Nesse caso, o conteúdo será convertido em uma **lista de dicionários**.

Podemos percorrer os registros com `for`:

```
import json

with open('produtos.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

for produto in dados:
    print(produto['produto'], produto['preco'])
```

Resultado:

```
Notebook 3500
Mouse 80
Teclado 150
```

Perceba que utilizamos conhecimentos que já estudamos: listas, dicionários, `for` e acesso por chaves.

## 6. Escrevendo arquivos JSON — `json.dump()`

Agora vamos aprender a criar arquivos JSON.

Imagine que temos um dicionário:

```
dados = {
    'nome': 'Mariana',
    'idade': 25,
    'cidade': 'Santos'
}
```

Para salvar essas informações em um arquivo JSON, utilizamos `json.dump()`:

```
import json

dados = {
    'nome': 'Mariana',
    'idade': 25,
    'cidade': 'Santos'
}

with open('clientes.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo)
```

O arquivo `clientes.json` será criado com o conteúdo:

```
{"nome": "Mariana", "idade": 25, "cidade": "Santos"}
```

## 7. Organizando o JSON com `indent`

Podemos utilizar o parâmetro `indent` para deixar o arquivo mais organizado e fácil de ler.

```
json.dump(dados, arquivo, indent=4)
```

Resultado no arquivo:

```
{
    "nome": "Mariana",
    "idade": 25,
    "cidade": "Santos"
}
```

O número `4` representa a quantidade de espaços utilizados na indentação.

## 8. Convertendo caracteres especiais com `ensure_ascii`

Por padrão, o Python pode representar caracteres especiais utilizando códigos Unicode.

Para preservar visualmente os caracteres, como acentos, podemos utilizar:

```
json.dump(dados, arquivo, indent=4, ensure_ascii=False)
```

Assim, palavras como `São Paulo` permanecem legíveis no arquivo.

## 9. Convertendo JSON em texto e texto em JSON

Além de trabalhar diretamente com arquivos, podemos converter dados em memória.

Existem duas funções importantes:

**`json.dumps()`**

Converte uma estrutura Python em uma string JSON.

```
import json

dados = {
    'nome': 'Carlos',
    'idade': 30
}

texto = json.dumps(dados, indent=4, ensure_ascii=False)

print(texto)
print(type(texto))
```

Resultado:

```
{
    "nome": "Carlos",
    "idade": 30
}
<class 'str'>
```

**`json.loads()`**

Faz o caminho contrário: converte uma string JSON em uma estrutura Python.

```
texto = '{"nome": "Carlos", "idade": 30}'

dados = json.loads(texto)

print(dados['nome'])
print(type(dados))
```

Resultado:

```
Carlos
<class 'dict'>
```

## 10. Diferença entre as quatro funções

Esta tabela é importante para não confundir os métodos:

| Função         | Finalidade                         |
| -------------- | ---------------------------------- |
| `json.load()`  | Lê JSON de um arquivo              |
| `json.dump()`  | Escreve JSON em um arquivo         |
| `json.loads()` | Converte uma string JSON em Python |
| `json.dumps()` | Converte Python em uma string JSON |

**Resumo para memorizar**

Arquivo → Python **`load()`**

---

Python → Arquivo **`dump()`**

---

String → Python **`loads()`**

---

Python → String **`dumps()`**

## 11. Tipos de dados suportados pelo JSON

O JSON possui equivalentes para os principais tipos de dados do Python:

| Python          | JSON    |
| --------------- | ------- |
| `dict`          | Objeto  |
| `list`          | Array   |
| `str`           | String  |
| `int` / `float` | Número  |
| `True`          | `true`  |
| `False`         | `false` |
| `None`          | `null`  |

Uma observação: dentro de arquivos JSON, os valores booleanos são escritos em letras minúsculas (`true` e `false`), diferentemente do Python.

---
