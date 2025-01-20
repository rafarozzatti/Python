## Dicionários


#### Exemplos:

```python
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
# Resultado: Pedro
```

```python
dados = {'nome':'Pedro', 'idade':25}
print(dados['idade'])
# Resultado: 25
```

```python
dados = {'nome':'Pedro', 'idade':25}
dados['sexo'] = 'M'
# Resultado: adiciona o sexo no dicionário dados
```

```python
dados = {'nome':'Pedro', 'idade':25}
del dados['idade']
# Resultado: deleta a idade do dicionário dados
```

```python
filme = {'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'}
print(filme.values())
# Resultado: Star Wars, 1977, George Lucas
```

```python
filme = {'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'}
print(filme.keys())
# Resultado: titulo, ano, diretor
```

```python
filme = {'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'}
print(filme.items())
# Resultado: imprime tudo
```