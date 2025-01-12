## Manipulando Textos

#### Exemplos de Fatiamento:

```python
frase = 'Curso em Vídeo Python'
print(frase(9))
# Resultado: Imprime a letra 'V'
```

```python
frase = 'Curso em Vídeo Python'
print(frase(9:13))
# Resultado: Imprime as letras 'Víde'
```

```python
frase = 'Curso em Vídeo Python'
print(frase(9:21))
# Resultado: Imprime as letras 'Vídeo Python'
```

```python
frase = 'Curso em Vídeo Python'
print(frase(9:21:2))
# Resultado: Imprime as letras 'VdoPto'
```

```python
frase = 'Curso em Vídeo Python'
print(frase(:5))
# Resultado: Imprime as letras 'Curso'
```

```python
frase = 'Curso em Vídeo Python'
print(frase(15:))
# Resultado: Imprime as letras 'Python'
```

```python
frase = 'Curso em Vídeo Python'
print(frase(9::3))
# Resultado: Imprime as letras 'VePh'
```

#### Exemplos de Análise:

```python
frase = 'Curso em Vídeo Python'
len(frase)
# Resultado: Imprime '21'(conta os números de caracteres)
```

```python
frase = 'Curso em Vídeo Python'
frase.count('o')
# Resultado: Imprime '3'(conta a quantidade de letras 'o'(somente as minúsculas))
```

```python
frase = 'Curso em Vídeo Python'
frase.count('O')
# Resultado: Imprime '0'(conta a quantidade de letras 'O'(somente as maiúsculas))
```

```python
frase = 'Curso em Vídeo Python'
frase.count('o',0,13)
# Resultado: Imprime '1'(conta a quantidade de letras 'o')
```

```python
frase = 'Curso em Vídeo Python'
frase.find('deo')
# Resultado: Imprime '11'(indica onde foi encontrado 'deo'))
```

```python
frase = 'Curso em Vídeo Python'
frase.find('Android')
# Resultado: Imprime '-1'(indica onde foi encontrado 'Android', o -1 indica que não foi encontrado))
```

```python
frase = 'Curso em Vídeo Python'
print('Curso' in frase)
# Resultado: Imprime 'True'(A condição é verdadeira, pois 'Curso' existe em frase))
```

#### Exemplos de Transformação:

```python
frase = 'Curso em Vídeo Python'
frase.replace('Python','Android')
# Resultado: Troca 'Python' por 'Android'
```

```python
frase = 'Curso em Vídeo Python'
frase.upper()
# Resultado: Passa todas as letras minúsculas para maiúsculas
```

```python
frase = 'Curso em Vídeo Python'
frase.lower()
# Resultado: Passa todas as letras maiúsculas para minúsculas
```

```python
frase = 'Curso em Vídeo Python'
frase.capitalize()
# Resultado: Passa todas as letras maiúsculas para minúsculas, exceto a primeira
```

```python
frase = 'Curso em Vídeo Python'
frase.title()
# Resultado: Passa todas as primeiras letras de cada palavra para maiúsculas
```

```python
frase = '   Aprenda Python  '
frase.strip()
# Resultado: Remove todos os espaços em branco antes da primeira palavra e depois da última palavra
```

```python
frase = '   Aprenda Python  '
frase.rstrip()
# Resultado: Remove somente os espaços em branco depois da última palavra
```

```python
frase = '   Aprenda Python  '
frase.lstrip()
# Resultado: Remove somente os espaços em branco antes da primeira palavra
```

#### Exemplo de Divisão:

```python
frase = 'Curso em Vídeo Python'
frase.split()
# Resultado: Divide a lista em várias listas, assim cada palavra fica em uma lista
```

#### Exemplo de Junção:

```python
frase = 'Curso em Vídeo Python'
'-'.join(frase)
# Resultado: Juntas as listas em uma só, com '-' entre cada palavras
```