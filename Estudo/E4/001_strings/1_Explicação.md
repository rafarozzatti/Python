# Strings em Python

## 1. O que são Strings?

Strings são sequências de caracteres, ou seja, textos formados por letras, números, espaços e símbolos.

Em Python, criamos uma string utilizando aspas simples ou duplas:

```
nome = 'Rafael'
curso = "Python"
```

Podemos exibir essas strings com `print()`:

```
print(nome)
print(curso)
```

Saída:

```
Rafael
Python
```

## 2. Índices de Strings

Cada caractere de uma string possui uma posição, chamada de índice.

Em Python, a contagem dos índices começa em 0, e não em 1.

Observe:

```
palavra = "PYTHON"
```

Posições dos caracteres

# P

# Y

# T

# H

# O

# N

0

1

2

3

4

5

Cada caractere possui seu próprio índice.

Podemos acessar um caractere específico utilizando colchetes `[]`:

```
palavra = "PYTHON"

print(palavra[0])
print(palavra[2])
print(palavra[5])
```

Saída:

```
P
T
N
```

Observe:

- `palavra[0]` retorna o primeiro caractere.
- `palavra[2]` retorna o terceiro caractere.
- `palavra[5]` retorna o sexto caractere.

Atenção: o índice 2 representa o terceiro caractere, porque a contagem começa em zero.

## 3. Índices negativos

Python também permite acessar os caracteres começando pelo final da string.

Nesse caso, utilizamos índices negativos:

```
palavra = "PYTHON"

print(palavra[-1])
print(palavra[-2])
print(palavra[-3])
```

Saída:

```
N
O
H
```

Veja como funciona:

Índices positivos e negativos

P

Y

T

H

O

N

0

1

2

3

4

5

-6

-5

-4

-3

-2

-1

Os índices negativos começam em -1, no último caractere.

## 4. E se utilizarmos um índice que não existe?

Se tentarmos acessar uma posição que não existe na string, Python apresentará um erro chamado `IndexError`.

Exemplo:

```
palavra = "PYTHON"
print(palavra[6])
```

Resultado:

```
IndexError: string index out of range
```

Isso acontece porque a palavra possui seis caracteres, cujos índices vão de 0 até 5.

## Fatiamento de strings

O fatiamento permite extrair uma parte de uma string, em vez de acessar apenas um caractere.

A estrutura é:

```
variavel[inicio:fim]
```

- `inicio`: índice em que o trecho começa (incluído).
- `fim`: índice em que o trecho termina (não incluído).

Por exemplo:

```
palavra = "Python"
print(palavra[0:3])
```

Saída:

```
Pyt
```

Isso acontece porque o Python começa no índice `0` e vai até o índice `2`. O índice `3` não é incluído.

Também podemos omitir alguns valores:

```
palavra = "Python"

print(palavra[:3])  # Do início até o índice 2
print(palavra[2:])  # Do índice 2 até o final
print(palavra[:])   # String inteira
```

Saída:

```
Pyt
thon
Python
```

## Fatiamento em passo:

```
variavel[inicio:fim:passo]
```

O passo determina de quantos em quantos caracteres o Python deve avançar.

Exemplo:

```
palavra = "Python"
print(palavra[0:6:2])
```

Saída:

```
Pto
```

Isso acontece porque o Python começa no índice 0 e avança de dois em dois: índices 0, 2 e 4.
