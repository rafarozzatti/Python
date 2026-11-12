# Exercícios de Tuplas

## Exercício 1

Crie uma tupla chamada `cores` contendo:

```
"Azul", "Verde", "Vermelho", "Amarelo", "Preto"
```

Depois, escreva um programa que exiba exatamente:

```
Azul
Vermelho
Preto
```

Regras:

1. Utilize a tupla `cores`.
2. O primeiro elemento deve ser acessado com índice positivo.
3. O segundo elemento solicitado deve ser acessado com índice positivo.
4. O terceiro elemento solicitado deve ser acessado com índice negativo.
5. Utilize três comandos `print()`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-1)

Correto!

Seu código está correto e atende a todas as regras.

Saída:

```
Azul
Vermelho
Preto
```

Você utilizou:

- `cores[0]`: primeiro elemento.
- `cores[2]`: terceiro elemento.
- `cores[-1]`: último elemento.

Exercício 1/10 concluído.

## Exercício 2

Considere:

```
numeros = (10, 20, 30, 40, 50, 60, 70)
```

Escreva um programa que exiba exatamente:

```
(10, 20, 30)
(40, 50, 60, 70)
(70, 60, 50, 40, 30, 20, 10)
```

Regras:

1. Utilize a tupla `numeros`.
2. Utilize fatiamento nos três comandos `print()`.
3. O terceiro comando deve utilizar passo negativo para inverter a tupla.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-2)

## Exercício 3

Considere:

```
numeros = (5, 10, 5, 20, 5, 30, 10, 5)
```

Utilize o método `count()` para descobrir quantas vezes aparecem na tupla:

- O número `5`.
- O número `10`.
- O número `30`.

Saída esperada:

```
4
2
1
```

Regras:

1. Utilize a tupla `numeros`.
2. Utilize três comandos `print()`.
3. Utilize `count()` nos três comandos.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-3)

## Exercício 4

Considere:

```
frutas = ("Maçã", "Banana", "Uva", "Laranja", "Morango")
```

Utilize o método `index()` para descobrir a posição dos seguintes elementos:

- `"Banana"`
- `"Laranja"`
- `"Morango"`

Saída esperada:

```
1
3
4
```

Regras:

1. Utilize a tupla `frutas`.
2. Utilize três comandos `print()`.
3. Utilize `index()` nos três comandos.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-4)

## Exercício 5

Considere:

```
numeros = (10, 20, 30, 20, 40, 20, 50)
```

Utilize `index()` para descobrir a posição da primeira ocorrência do número `20`.

Depois, utilize `count()` para descobrir quantas vezes o número `20` aparece.

Saída esperada:

```
1
3
```

Regras:

1. Utilize a tupla `numeros`.
2. Utilize dois comandos `print()`.
3. Utilize `index()` no primeiro e `count()` no segundo.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-5)

## Exercício 6

Considere:

```
cores = ("Azul", "Verde", "Vermelho")
```

Agora, responda:

O que acontece se executarmos o seguinte comando?

```
cores[1] = "Amarelo"
```

Escreva um pequeno código que tente realizar essa alteração e explique, com suas palavras, por que o Python apresenta esse resultado.

Não se preocupe se ocorrer um erro: neste exercício, queremos justamente entender a imutabilidade das tuplas.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-6)

## Exercício 7

Considere:

```
frutas = ["Maçã", "Banana", "Uva"]
```

e

```
cores = ("Azul", "Verde", "Vermelho")
```

Faça o seguinte:

1. Altere `"Banana"` para `"Morango"` na lista `frutas`.
2. Exiba a lista modificada.
3. Tente alterar `"Verde"` para `"Amarelo"` na tupla `cores`.

Pergunta: O que acontece quando você tenta realizar a terceira operação?

[Resolução](3_Resolução_dos_Exercícios.md#exercício-7)

## Exercício 8

Crie uma tupla chamada `numeros` contendo apenas o número `10`.

Depois, utilize `type()` para verificar o tipo da variável.

Saída esperada:

```
<class 'tuple'>
```

Regra: lembre-se da particularidade que estudamos sobre tuplas com apenas um elemento.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-8)

## Exercício 9

Considere:

```
dados = ("Rafael", 27, 1.69, True)
```

Escreva um programa que exiba:

1. O primeiro elemento da tupla.
2. O segundo elemento da tupla.
3. O tipo de dado do terceiro elemento.
4. O tipo de dado do quarto elemento.
5. O tipo de dado da própria variável `dados`.

Saída esperada:

```
Rafael
27
<class 'float'>
<class 'bool'>
<class 'tuple'>
```

Regras:

- Utilize a tupla `dados`.
- Utilize cinco comandos `print()`.
- Utilize `type()` nos três últimos comandos.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-9)

## Exercício 10

Considere:

```
numeros = (15, 10, 25, 10, 30, 5, 10)
```

Escreva um programa que exiba exatamente:

```
15
10
(25, 10, 30)
(10, 5, 10)
3
1
```

Regras:

1. Exiba o primeiro elemento utilizando índice positivo.
2. Exiba o último elemento utilizando índice negativo.
3. Utilize fatiamento para obter `(25, 10, 30)`.
4. Utilize fatiamento para obter `(30, 5, 10)`.
5. Utilize `count()` para contar quantas vezes o número `10` aparece.
6. Utilize `index()` para encontrar a primeira ocorrência do número `10`.
7. Utilize seis comandos `print()`.

[Resolução](3_Resolução_dos_Exercícios.md#exercício-9)
