# Exercícios break e continue

## Exercício 1

Crie um programa em Python que percorra os números de 1 até 10, mas interrompa o laço quando encontrar o número 6.

O programa deve imprimir cada número antes do 6 e, depois que o laço terminar, imprimir a mensagem `Laço encerrado`.

Saída esperada:

```
1
2
3
4
5
Laço encerrado
```

Sua tarefa: escreva o código completo usando `for`, `range()` e `break`.

Resolução:
```python
for i in range(1, 11):
    if i == 6:
        break
    print(i)

print('Laço encerrado')
```

## Exercício 2

Crie um programa que percorra os números de 1 até 10, mas não imprima os números pares.

O programa deve imprimir apenas os números ímpares.

Saída esperada:

```
1
3
5
7
9
```

Sua tarefa: use `for`, `range()`, `if` e `continue`.

Resolução:
```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```

## Exercício 3

Crie um programa que peça números inteiros ao usuário repetidamente.

- Se o usuário digitar `0`, o programa deve interromper a repetição usando `break`.
- Se digitar qualquer outro número, o programa deve exibi-lo.
- Ao terminar, deve imprimir `Programa encerrado`.

Exemplo de execução:

```
Digite um número: 8
Você digitou: 8
Digite um número: 3
Você digitou: 3
Digite um número: 0
Programa encerrado
```

Sua tarefa: escreva o código completo usando `while`, `input()`, `if` e `break`.

Resolução:
```python
while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    print(f'Você digitou: {num}')

print('Programa encerrado')
```

## Exercício 4

Crie um programa que peça 5 números inteiros ao usuário.

- Se o número for negativo, use `continue` para ignorá-lo, sem imprimi-lo.
- Se for zero ou positivo, imprima o número.
- O programa deve solicitar os 5 números, mesmo que alguns sejam negativos.

Exemplo de execução:

```
Digite um número: 4
4
Digite um número: -2
Digite um número: 0
0
Digite um número: -7
Digite um número: 9
9
```

Sua tarefa: use `while`, um contador, `if` e `continue`.

Resolução:
```python
cont = 0

while cont <= 4:
    num = int(input('Digite um número: '))
    cont += 1
    if num < 0:
        continue
    print(num)
```

## Exercício 5

Crie um programa que percorra os números de 1 até 20 e siga estas regras:

- Se o número for par, ignore-o usando `continue`.
- Se o número for maior que 13, encerre o laço usando `break`.
- Imprima os números restantes.

A saída esperada é:

```
1
3
5
7
9
11
13
```

Sua tarefa: escreva o código usando `for`, `range()`, `if`, `continue` e `break`.

Resolução:
```python
for i in range(1, 21):
    if i > 13:
        break
    if i % 2 == 0:
        continue
    print(i)
```

## Exercício 6

Crie um programa que percorra os números de 1 até 100 e encontre o primeiro número divisível por 7 e por 5 ao mesmo tempo.

Regras:

- Use `for` e `range()`.
- Quando encontrar o número, imprima-o.
- Use `break` para encerrar a busca assim que encontrá-lo.

Resolução:
```python
for i in range(1, 101):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
        break
```

## Exercício 7

Crie um programa que solicite 10 números inteiros ao usuário.

Regras:

- Se o número for negativo, ignore-o usando `continue`.
- Se o número for zero ou positivo, conte-o como válido.
- Ao final, exiba quantos números válidos foram digitados.

Exemplo de execução:

```
Digite um número: 5
Digite um número: -2
Digite um número: 0
Digite um número: 8
Digite um número: -1
Digite um número: 3
Digite um número: 7
Digite um número: -4
Digite um número: 2
Digite um número: 9

Quantidade de números válidos: 7
```

Sua tarefa: use `while`, um contador para controlar as 10 entradas, outro contador para os números válidos e `continue`.

Resolução:
```python
cont = contnum = 0

while cont <= 9:
    num = int(input('Digite um número: '))
    cont += 1
    if num < 0:
        continue

    contnum += 1

print(f'Quantidade de números válidos: {contnum}')
```

## Exercício 8

Crie um programa que peça ao usuário uma senha. A senha correta será `python123`.

Regras:

- O usuário terá no máximo 3 tentativas.
- Se digitar a senha correta, exiba `Acesso permitido` e encerre o laço usando `break`.
- Se errar, exiba `Senha incorreta`.
- Se errar nas três tentativas, exiba `Acesso bloqueado`.

Exemplo de execução com acerto:

```
Digite a senha: abc
Senha incorreta
Digite a senha: python123
Acesso permitido
```

Sua tarefa: use `while`, um contador de tentativas, `if` e `break`.

Resolução:
```python
cont = 0

while cont <= 2:
    senha = input('Digite a senha: ')
    if senha == 'python123':
        print('Acesso permitido')
        break
    print('Senha incorreta')
    cont += 1
    if cont == 3:
        print('Acesso bloqueado')
```

## Exercício 9

Crie um programa que solicite 8 notas ao usuário.

Regras:

- Se a nota for menor que 0 ou maior que 10, ignore-a usando `continue`.
- Para as notas válidas, some os valores e conte quantas notas válidas foram informadas.
- Ao final, calcule e exiba a média das notas válidas.

Exemplo: se as entradas forem `8`, `11`, `6`, `-1`, `10`, `7`, `5`, `12`, o programa deverá considerar apenas `8`, `6`, `10`, `7` e `5`.

A média será:

```
Média das notas válidas: 7.2
```

Sua tarefa: use `for`, `range()`, `continue`, um acumulador para a soma e um contador para as notas válidas.

Resolução:
```python
cont = soma = 0

for i in range(1, 9):
    nota = float(input(f'Digite a {i}º nota: '))
    if nota < 0  or nota > 10:
        continue
    cont += 1
    soma += nota

media = soma / cont

print(f'Média das notas válidas: {media:.1f}')
```

## Exercício 10

Crie um programa que peça números inteiros ao usuário até que ele digite `0`.

Regras:

- Se o número for negativo, ignore-o usando `continue`.
- Se o número for positivo, some-o e conte-o.
- Se o usuário digitar `0`, encerre o laço usando `break`.
- Ao final, exiba a quantidade de números positivos e a soma deles.

Exemplo de execução:

```
Digite um número: 5
Digite um número: -3
Digite um número: 8
Digite um número: 0

Quantidade de positivos: 2
Soma dos positivos: 13
```

Sua tarefa: use `while True`, `if`, `continue`, `break`, um contador e um acumulador.

Resolução:
```python
cont = soma = 0

while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    if num < 0:
        continue
    cont += 1
    soma += num

print(f'''Quantidade de positivos: {cont}
Soma dos positivos: {soma}''')
```
