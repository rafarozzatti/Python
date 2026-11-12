# Exercícios de Laço while

## Exercício 1

Vamos começar com um exercício simples para praticar a estrutura.

Crie um programa que imprima os números de 1 até 10, utilizando `while`.

A saída esperada é:

```
1
2
3
4
5
6
7
8
9
10
```

Regras:

- Utilize uma variável chamada `contador`.
- Comece com o valor `1`.
- Use `while` para repetir.
- Atualize o contador a cada repetição.

Resolução:
```python
contador = 1

while contador <= 10:
    print(contador)
    contador += 1
```

## Exercício 2

Agora vamos inverter a lógica.

Crie um programa que imprima os números de 10 até 1, em ordem decrescente, utilizando `while`.

A saída esperada é:

```
10
9
8
7
6
5
4
3
2
1
```

Regras:

- Utilize uma variável chamada `contador`.
- Comece com o valor `10`.
- Use `while` para repetir.
- Diminua o contador a cada repetição.

Resolução:
```python
contador = 10

while contador >= 1:
    print(contador)
    contador -= 1
```

## Exercício 3

Agora vamos combinar o `while` com os operadores matemáticos que você já conhece.

Crie um programa que imprima todos os números pares de 2 até 20, em ordem crescente.

Saída esperada:

```
2
4
6
8
10
12
14
16
18
20
```

Regras:

- Utilize uma variável chamada `contador`.
- Use `while` para repetir.
- O programa deve avançar de dois em dois números.

Resolução:
```python
contador = 2

while contador <= 20:
    print(contador)
    contador += 2
```

## Exercício 4

Agora vamos usar o `while` para realizar um cálculo, em vez de apenas imprimir números.

Crie um programa que calcule a soma de todos os números inteiros de 1 até 100.

O resultado esperado é:

```
Soma: 5050
```

Regras:

- Crie uma variável `contador` começando em `1`.
- Crie uma variável `soma` começando em `0`.
- Utilize `while` para percorrer os números de 1 até 100.
- Em cada repetição, adicione o valor do contador à variável `soma`.
- Ao final, exiba o resultado.

Dica: para acumular um valor, você pode usar `soma += contador`.

Resolução:
```python
contador = 1
soma = 0

while contador <= 100:
    soma += contador
    contador += 1

print(f'Soma: {soma}')   
```

## Exercício 5

Agora vamos usar o `while` para gerar uma tabuada.

Crie um programa que solicite um número inteiro ao usuário e exiba a tabuada desse número, de 1 a 10.

Exemplo, se o usuário digitar `7`:

```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

Regras:

- Utilize `input()` e `int()` para receber o número.
- Crie uma variável `contador` começando em `1`.
- Utilize `while` para repetir até `10`.
- Calcule e exiba o resultado de cada multiplicação.

Resolução:
```python
cont = 1

num = int(input('Digite um número entre 1 e 10 para ver sua tabuada: '))

while cont <= 10:
    print(f'{num} x {cont} = {num * cont}')
    cont += 1  
```

## Exercício 6

Agora vamos trabalhar com uma situação em que não sabemos antecipadamente quantas vezes o laço precisará se repetir.

Crie um programa que solicite números inteiros ao usuário. O programa deve continuar recebendo números enquanto eles forem positivos. Quando o usuário digitar `0` ou um número negativo, a entrada deve terminar.

Ao final, exiba a quantidade de números positivos digitados. O número que encerra a entrada não deve ser contado.

Exemplo de execução:

```
Digite um número: 5
Digite um número: 8
Digite um número: 3
Digite um número: 0

Quantidade de números positivos: 3
```

Regras:

- Utilize `while`.
- Crie uma variável para contar os números positivos.
- O programa deve parar quando o usuário digitar `0` ou um número negativo.
- Não conte o número que encerrou a repetição.

Resolução:
```python
num = 1
cont = 0

while num > 0:
    num = int(input('Digite um número: '))
    if num > 0:
        cont += 1

print(f'Quantidade de números positivos: {cont}')
```

## Exercício 7

Agora vamos combinar repetição, acumulação e cálculo de média.

Crie um programa que solicite 5 notas ao usuário e, ao final, calcule e exiba a média aritmética delas.

Exemplo de execução:

```
Digite a nota 1: 7
Digite a nota 2: 8
Digite a nota 3: 6
Digite a nota 4: 9
Digite a nota 5: 10

Média: 8.0
```

Regras:

- Utilize `while` para solicitar as cinco notas.
- Crie uma variável para acumular a soma das notas.
- Calcule a média dividindo a soma por `5`.
- Exiba a média somente depois que as cinco notas forem informadas.

Resolução:
```python
cont = 1
soma = 0

while cont <= 5:
    nota = int(input(f'Digite a nota {cont}: '))
    soma += nota
    cont += 1

media = soma / (cont - 1)
print(f'Média: {media}')
```

## Exercício 8

Agora vamos praticar algo novo: acompanhar o maior valor encontrado durante um laço.

Crie um programa que solicite 5 números inteiros ao usuário e, ao final, mostre qual foi o maior número digitado.

Exemplo de execução:

```
Digite o número 1: 12
Digite o número 2: 7
Digite o número 3: 25
Digite o número 4: 9
Digite o número 5: 18

Maior número: 25
```

Regras:

- Utilize `while` para solicitar os cinco números.
- Crie uma variável para contar as entradas.
- Identifique o maior número sem precisar guardar todos os números em uma lista.
- Exiba o maior valor somente depois das cinco entradas.

Resolução:
```python
maior = 0
cont = 1

while cont <= 5:
    num = int(input(f'Digite o número {cont}: '))
    if num > maior:
        maior = num
    cont += 1

print(f'Maior número: {maior}')
```

## Exercício 9

Agora vamos combinar `while`, condicionais e operações matemáticas.

Crie um programa que apresente este menu:

```
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Sair
```

O programa deve:

1. Exibir o menu e solicitar uma opção.
2. Se escolher `1`, solicitar dois números e exibir a soma.
3. Se escolher `2`, solicitar dois números e exibir a subtração.
4. Se escolher `3`, solicitar dois números e exibir a multiplicação.
5. Se escolher `4`, encerrar o programa.
6. Se escolher qualquer outra opção, exibir `Opção inválida`.
7. Continuar mostrando o menu até o usuário escolher `4`.

Exemplo de execução:

```
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Sair
Escolha uma opção: 1
Digite o primeiro número: 10
Digite o segundo número: 5
Resultado: 15

1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Sair
Escolha uma opção: 4
Programa encerrado.
```

Resolução:
```python
opcao = 1

while opcao > 0 and opcao < 4:
    print('''1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Sair''')

    opcao = int(input('Escolha uma opção: '))
    if opcao > 0 and opcao < 4: 
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))

        if opcao == 1:
            resultado = num1 + num2
        elif opcao == 2:
            resultado = num1 - num2
        elif opcao == 3:
            resultado = num1 * num2

        print(f'Resultado: {resultado}\n')
    else:
        print('Programa encerrado.')
```

## Exercício 10

Crie um programa que solicite números inteiros ao usuário até que ele digite `0`. Ao final, o programa deve exibir o maior número digitado, sem considerar o zero que encerra a entrada.

### Exemplo de execução

```
Digite um número: -4
Digite um número: -8
Digite um número: -2
Digite um número: -10
Digite um número: 0

Maior número: -2
```

### Regras

- Utilize `while` para receber os números.
- O programa deve parar quando o usuário digitar `0`.
- Não conte o zero como um número participante da comparação.
- O programa precisa funcionar mesmo quando todos os números digitados forem negativos.
- Ao final, exiba o maior número.

Resolução:
```python
num = int(input('Digite um número: '))
if num != 0:
    maior = num

    while num != 0:
        num = int(input('Digite um número: '))
        if num != 0:
            if num > maior:
                maior = num

    print(f'Maior número: {maior}')

else:
    print('Nenhum número encontrado')
```
