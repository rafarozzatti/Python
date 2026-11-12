# Exercícios de String: índices, fatiamentos e métodos

## Exercício 1

Considere a seguinte variável:

```
linguagem = "Python"
```

Escreva um programa que exiba exatamente esta saída:

```
P
t
o
n
```

Regras:

1. Utilize a variável `linguagem`.
2. Utilize os índices positivos para acessar os caracteres `P` e `t`.
3. Utilize índices negativos para acessar os caracteres `o` e `n`.
4. Utilize quatro comandos `print()`.
5. Não escreva os caracteres diretamente dentro do `print()`. Acesse-os pela variável.

Resolução:
```python
linguagem = "Python"

print(linguagem[0])
print(linguagem[2])
print(linguagem[-2])
print(linguagem[-1])
```

## Exercício 2

Considere:

```
frase = "Analise de Dados"
```

Escreva um programa que exiba exatamente:

```
A
D
s
o
```

Regras:

1. Utilize a variável `frase`.
2. Acesse os caracteres utilizando índices positivos e negativos.
3. Utilize quatro comandos `print()`.
4. Não escreva os caracteres diretamente nos comandos `print()`.

Resolução:
```python
frase = "Analise de Dados"

print(frase[0])
print(frase[-5])
print(frase[15])
print(frase[-2])
```

## Exercício 3

Considere:

```
palavra = "Programacao"
```

Responda utilizando comandos `print()` para exibir:

```
P
g
a
o
```

Regras:

1. Utilize a variável `palavra`.
2. Utilize índices positivos para os dois primeiros caracteres solicitados.
3. Utilize índices negativos para os dois últimos.
4. Utilize quatro comandos `print()`.
5. Não escreva os caracteres diretamente nos comandos.

Resolução:
```python
palavra = "Programacao"

print(palavra[0])
print(palavra[3])
print(palavra[-2])
print(palavra[-1])
```

## Exercício 4

Considere:

```
texto = "Desenvolvimento"
```

Escreva um programa que exiba exatamente:

```
D
t
o
```

Regras:

1. Utilize a variável `texto`.
2. O primeiro caractere deve ser acessado com índice positivo.
3. O segundo caractere deve ser acessado com índice negativo.
4. O terceiro caractere solicitado deve ser acessado utilizando o índice `-1`.
5. Utilize três comandos `print()`.

Resolução:
```python
texto = "Desenvolvimento"

print(texto[0])
print(texto[-2])
print(texto[-1])
```

### Exercício 5

Considere:

```
palavra = "Computador"
```

Escreva um programa que exiba exatamente:

```
C
u
d
r
```

Regras:

1. Utilize a variável `palavra`.
2. O primeiro caractere deve ser acessado com índice positivo.
3. O segundo caractere deve ser acessado com índice negativo.
4. O terceiro caractere deve ser acessado com índice positivo.
5. O quarto caractere deve ser acessado com índice negativo.
6. Utilize quatro comandos `print()`.

Resolução:
```python
palavra = "Computador"

print(palavra[0])
print(palavra[-6])
print(palavra[7])
print(palavra[-1])
```

### Exercício 6

Considere:

```
frase = "Analise de Dados"
```

Escreva um programa que exiba exatamente:

```
Analise
Dados
de
```

Regras:

1. Utilize a variável `frase`.
2. Utilize fatiamento nos três comandos `print()`.
3. Não utilize índices individuais para acessar os caracteres.

Resolução:
```python
frase = "Analise de Dados"

print(frase[0:7])
print(frase[11:16])
print(frase[8:10])
```

### Exercício 7

Considere:

```
nome = "Rafael"
```

Escreva um programa que exiba exatamente:

```
Raf
ael;
Rafael
```

Regras:

1. Utilize a variável `nome`.
2. Utilize fatiamento nos três comandos `print()`.
3. Em pelo menos dois comandos, omita um dos índices (`inicio` ou `fim`).

Resolução:
```python
nome = "Rafael"

print(nome[0:3])
print(nome[3:])
print(nome[:])
```

### Exercício 8

Considere:

```
linguagem = "JavaScript"
```

Escreva um programa que exiba exatamente:

```
Java
Script
```

Regras:

1. Utilize a variável `linguagem`.
2. Utilize fatiamento nos dois comandos `print()`.
3. Pelo menos um dos fatiamentos deve utilizar índice negativo.

Resolução:
```python
linguagem = "JavaScript"

print(linguagem[0:4])
print(linguagem[-6:])
```

### Exercício 9

Considere:

```
palavra = "Computador"
```

Escreva um programa que exiba exatamente:

```
Cmu
```

Utilize fatiamento com passo no comando `print()`.

Resolução:
```python
palavra = "Computador"

print(palavra[0:6:2])
```

### Exercício 10

Considere:

```
frase = "Programacao em Python"
```

Escreva um programa que exiba exatamente:

```
Programacao
Python
Pormco
```

Regras:

1. Utilize a variável `frase`.
2. Utilize fatiamento nos três comandos `print()`.
3. O primeiro comando deve extrair `Programacao`.
4. O segundo deve extrair `Python`.
5. O terceiro deve utilizar passo `2` para extrair `Pormco`.

Resolução:
```python
frase = "Programacao em Python"

print(frase[0:11])
print(frase[15:])
print(frase[0:11:2])
```
