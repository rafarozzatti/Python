# Aula 4 — `type()` e conversão de tipos

## 1. A função `type()`

A função `type()` permite descobrir o tipo de dado armazenado em uma variável.

```
idade = 27
preco = 19.90
nome = "Rafael"
ativo = True

print(type(idade))
print(type(preco))
print(type(nome))
print(type(ativo))
```

Saída:

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

Lembre-se:

| Tipo    | Significado         |
| ------- | ------------------- |
| `int`   | Número inteiro      |
| `float` | Número decimal      |
| `str`   | Texto               |
| `bool`  | Verdadeiro ou falso |

## 2. `int()` — Converter para inteiro

A função `int()` converte um valor compatível para um número inteiro.

Exemplo com texto numérico:

```
numero = "25"
numero_convertido = int(numero)

print(numero_convertido)
print(type(numero_convertido))
```

Saída:

```
25
<class 'int'>
```

Também podemos converter um número decimal:

```
preco = 19.90
preco_inteiro = int(preco)

print(preco_inteiro)
```

Saída:

```
19
```

Atenção: `int()` elimina a parte decimal, não arredonda o número. Por exemplo, `int(19.90)` resulta em `19`.

Um texto como `"vinte"` não pode ser convertido diretamente para inteiro e causará um erro.

## 3. `float()` — Converter para decimal

A função `float()` converte um valor compatível para um número decimal.

```
preco = "49.90"
preco_convertido = float(preco)

print(preco_convertido)
print(type(preco_convertido))
```

Saída:

```
49.9
<class 'float'>
```

Observe que o Python pode retirar o zero final ao exibir o valor.

Também podemos converter um inteiro:

```
numero = 10
numero_decimal = float(numero)

print(numero_decimal)
```

Saída:

```
10.0
```

## 4. `str()` — Converter para texto

A função `str()` converte valores em textos.

```
idade = 27
idade_texto = str(idade)

print(idade_texto)
print(type(idade_texto))
```

Saída:

```
27
<class 'str'>
```

Apesar de aparecer `27` na tela, agora o valor é um texto, e não um número inteiro.

Isso é útil, por exemplo, quando precisamos juntar informações numéricas com textos.

## 5. `bool()` — Converter para lógico

A função `bool()` converte um valor para `True` ou `False`.

Veja alguns exemplos:

```
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))
```

Saída:

```
True
False
False
True
```

A regra básica é:

- O número `0` resulta em `False`.
- Outros números, como `1`, `-1` e `10`, resultam em `True`.
- Um texto vazio (`""`) resulta em `False`.
- Um texto não vazio, como `"Python"` ou `"False"`, resulta em `True`.

Importante: `bool("False")` resulta em `True`, pois `"False"` é um texto não vazio. O Python não interpreta o significado da palavra; ele verifica se o texto está vazio.

## Resumo para suas anotações

| Função    | Exemplo        | Resultado  |
| --------- | -------------- | ---------- |
| `type()`  | `type(25)`     | Tipo `int` |
| `int()`   | `int("25")`    | `25`       |
| `float()` | `float("3.5")` | `3.5`      |
| `str()`   | `str(25)`      | `"25"`     |
| `bool()`  | `bool(0)`      | `False`    |
