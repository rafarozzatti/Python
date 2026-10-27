# Exercícios de Laço for

## Exercício 1

Crie um programa que imprima os números de 1 até 10, utilizando `for` e `range()`.

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

- Use `for`.
- Use `range()`.
- Não utilize `while` nem atualize um contador manualmente.

## Exercício 2

Crie um programa que imprima os números de 10 até 1, em ordem decrescente, utilizando `for` e `range()`.

Saída esperada:

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

## Exercício 3

Crie um programa que imprima todos os números pares de 2 até 20, em ordem crescente, utilizando `for` e `range()`.

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

## Exercício 4

Crie um programa que calcule a soma de todos os números inteiros de 1 até 100.

Resultado esperado:

```
Soma: 5050
```

Regras:

- Crie uma variável `soma` começando em `0`.
- Utilize `for` e `range()` para percorrer os números de `1` até `100`.
- Acumule cada número na variável `soma`.
- Exiba o resultado ao final.

## Exercício 5

Crie um programa que peça ao usuário um número inteiro e mostre a tabuada desse número, de 1 a 10.

Exemplo de execução:

```
Digite um número: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

Regras:

- Use `input()` para receber o número.
- Converta a entrada para inteiro com `int()`.
- Use `for` e `range()` para repetir de 1 a 10.
- Use uma f-string para exibir cada multiplicação.

## Exercício 6

Crie um programa que peça ao usuário 5 números inteiros e, ao final, informe quantos deles são positivos (maiores que zero).

Exemplo de execução:

```
Digite um número: 4
Digite um número: -2
Digite um número: 0
Digite um número: 7
Digite um número: -5

Quantidade de positivos: 2
```

Regras:

- Use `for` e `range()` para repetir 5 vezes.
- Use `input()` para receber cada número.
- Utilize `if` para verificar se o número é maior que zero.
- Crie uma variável contadora para registrar a quantidade de positivos.

Atenção: o número `0` não é positivo.

## Exercício 7

Crie um programa que solicite 4 notas de um aluno e calcule a média aritmética delas.

Exemplo de execução:

```
Digite a nota: 7
Digite a nota: 8
Digite a nota: 6
Digite a nota: 9

Média: 7.5
```

Regras:

- Use `for` e `range()` para solicitar as 4 notas.
- Utilize uma variável para acumular a soma das notas.
- Ao terminar o laço, divida a soma por 4.
- Exiba a média com uma f-string.

## Exercício 8

Crie um programa que solicite 5 números inteiros e, ao final, mostre o maior número digitado.

Exemplo de execução:

```
Digite um número: 12
Digite um número: 5
Digite um número: 28
Digite um número: 9
Digite um número: 17

Maior número: 28
```

Regras:

- Use `for` e `range()` para receber os 5 números.
- Crie uma variável para guardar o maior número encontrado.
- Compare cada novo número com o maior registrado até aquele momento.
- Ao final, exiba o maior número.

## Exercício 9

Crie um programa que solicite 10 números inteiros e, ao final, informe quantos são pares e quantos são ímpares.

Exemplo de execução:

```
Digite um número: 2
Digite um número: 7
Digite um número: 4
Digite um número: 9
Digite um número: 10
Digite um número: 3
Digite um número: 6
Digite um número: 1
Digite um número: 8
Digite um número: 5

Quantidade de pares: 5
Quantidade de ímpares: 5
```

Regras:

- Use `for` e `range()` para receber os 10 números.
- Crie um contador para os pares e outro para os ímpares.
- Utilize `if` e `else` para verificar cada número.
- Lembre-se: `num % 2 == 0` indica que o número é par.

## Exercício 10

Vamos fechar esta sequência com um exercício aplicado a uma situação de negócio.

Uma loja registra o valor de 5 vendas. Crie um programa que receba o valor de cada venda e, ao final, mostre:

1. O faturamento total.
2. A quantidade de vendas acima de R$ 100,00.
3. O valor médio das vendas.

Exemplo de execução:

```
Digite o valor da venda: 80
Digite o valor da venda: 150
Digite o valor da venda: 200
Digite o valor da venda: 50
Digite o valor da venda: 120

Faturamento total: R$ 600.00
Vendas acima de R$ 100: 3
Valor médio das vendas: R$ 120.00
```

### Regras

- Use `for` e `range()` para receber as 5 vendas.
- Utilize `float()` para aceitar valores decimais.
- Acumule o faturamento total.
- Conte quantas vendas foram estritamente maiores que 100.
- Calcule a média depois que o laço terminar.
- Exiba os resultados usando f-strings.
