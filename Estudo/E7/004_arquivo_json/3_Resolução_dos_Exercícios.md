# Exercício 1

```python
import json

with open('clientes.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

    print(dados)
```

# Exercício 2

```python
import json

with open('clientes.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

    print(dados['nome'])
    print(dados['idade'])
    print(dados['cidade'])
```

# Exercício 3

```python
import json

with open('produtos.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

    for dado in dados:
        print(dado['produto'])
        print(dado['preco'])
```

# Exercício 4

```python
import json

dados = {
    'Nome': 'Mariana',
    'Idade': 25,
    'Cargo': 'Analista de Dados'
}

with open('funcionario.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo)
```

# Exercício 5

```python
import json

dados = {
    'Nome': 'Mariana',
    'Idade': 25,
    'Cargo': 'Analista de Dados'
}

with open('funcionario.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=4)
```

# Exercício 6

```python
import json

empresa = {
    'Nome': 'São Paulo Tecnologia',
    'Cidade': 'São Paulo',
    'País': 'Brasil'
}

with open('empresa.json', 'w', encoding='utf-8') as arquivo:
    json.dump(empresa, arquivo, indent=4, ensure_ascii=False)
```

# Exercício 7

```python
import json

produto = {
    'Nome': 'Notebook',
    'Preço': 3500,
    'Disponível': True
}

texto = json.dumps(produto, indent=4, ensure_ascii=False)

print(texto)
print(type(texto))
```

# Exercício 8

```python
import json

texto = '{"Nome": "Carlos", "idade": 30, "Cidade": "Santos"}'

dados = json.loads(texto)

print(dados['Nome'], dados['Cidade'])
print(type(dados))
```

# Exercício 9

```python
import json

with open('funcionario.json', 'r', encoding='utf-8') as arquivo:
    texto = json.load(arquivo)

texto['Idade'] = 26
texto['Cargo'] = 'Analista de Dados'

with open('funcionario.json', 'w', encoding='utf-8') as arquivo:
    json.dump(texto, arquivo, indent=4, ensure_ascii=False)
```

# Exercício 10

```python
import json

with open('alunos.json', 'r', encoding='utf-8') as arquivo:
    texto = json.load(arquivo)

    for aluno in texto:
        aluno['Nota'] += 1

with open('alunos.json', 'w', encoding='utf-8') as arquivo:
    json.dump(texto, arquivo, indent=4, ensure_ascii=False)
```
