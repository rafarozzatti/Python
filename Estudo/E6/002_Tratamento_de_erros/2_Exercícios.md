# Exercícios de Tratamento de Erros

## Exercício 1

Crie um programa que:

1. Solicite ao usuário que digite um número inteiro.
2. Utilize `try` para tentar converter a entrada com `int()`.
3. Utilize `except ValueError` para tratar uma entrada inválida.
4. Se ocorrer um erro, exiba a mensagem: `"Digite um número inteiro válido."`
5. Se não ocorrer erro, exiba o número digitado.

[Resolucão](3_Resolução_dos_Exercícios.md#exercício-1)

## Exercício 2

Crie um programa que:

1. Solicite ao usuário dois números inteiros.
2. Utilize `try` para realizar a divisão do primeiro pelo segundo.
3. Utilize `except ZeroDivisionError` para tratar a divisão por zero.
4. Se ocorrer esse erro, exiba: `"Não é possível dividir por zero."`
5. Se não ocorrer erro, utilize `else` para exibir o resultado da divisão.

[Resolucão](3_Resolução_dos_Exercícios.md#exercício-2)

## Exercício 3

Crie um programa que:

1. Solicite ao usuário que digite um número.
2. Tente converter esse valor para inteiro.
3. Utilize `except ValueError as erro` para capturar o erro.
4. Exiba a mensagem original da exceção utilizando a variável `erro`.
5. Se não ocorrer erro, exiba o número convertido.

[Resolucão](3_Resolução_dos_Exercícios.md#exercício-3)

## Exercício 4

Crie um programa que:

1. Crie uma lista com os números `[10, 20, 30]`.
2. Solicite ao usuário um índice.
3. Utilize `try` para tentar acessar e exibir o elemento da lista nessa posição.
4. Utilize `except IndexError` para tratar índices inexistentes.
5. Se ocorrer o erro, exiba: `"Índice inexistente."`

[Resolucão](3_Resolução_dos_Exercícios.md#exercício-4)

## Exercício 5

Crie um programa que:

1. Crie um dicionário chamado `pessoa` com as seguintes informações:
   - `"nome": "Carlos"`
   - `"idade": 25`
2. Solicite ao usuário o nome de uma chave que deseja consultar.
3. Utilize `try` para acessar o valor dessa chave.
4. Utilize `except KeyError` para tratar chaves inexistentes.
5. Se ocorrer o erro, exiba: `"Essa chave não existe no dicionário."`
6. Se não ocorrer erro, utilize `else` para exibir o valor encontrado.

[Resolucão](3_Resolução_dos_Exercícios.md#exercício-5)

## Exercício 6

Crie um programa que:

1. Utilize `try` para tentar abrir um arquivo chamado `"dados.txt"` no modo de leitura (`"r"`).
2. Utilize `except FileNotFoundError` para tratar a situação em que o arquivo não existe.
3. Se ocorrer o erro, exiba: `"Arquivo não encontrado."`
4. Se não ocorrer erro, utilize `else` para exibir: `"Arquivo encontrado com sucesso."`

[Resolucão](3_Resolução_dos_Exercícios.md#exercício-6)

## Exercício 7

Agora vamos praticar o `finally`.

Crie um programa que:

1. Solicite ao usuário um número inteiro dentro de um bloco `try`.
2. Utilize `except ValueError` para tratar entradas inválidas, exibindo `"Digite um número inteiro válido."`
3. Utilize `else` para exibir o número digitado, caso não ocorra erro.
4. Utilize `finally` para exibir a mensagem `"Programa finalizado."`, independentemente de ocorrer erro ou não.

[Resolucão](3_Resolução_dos_Exercícios.md#exercício-7)

## Exercício 8

Vamos combinar múltiplas exceções.

Crie um programa que:

1. Solicite dois números ao usuário.
2. Converta ambos para inteiros.
3. Realize a divisão do primeiro pelo segundo.
4. Utilize `except ValueError` para tratar entradas que não sejam números inteiros, exibindo `"Digite apenas números inteiros."`
5. Utilize `except ZeroDivisionError` para tratar divisões por zero, exibindo `"Não é possível dividir por zero."`
6. Utilize `else` para exibir o resultado quando não ocorrer nenhum erro.

[Resolucão](3_Resolução_dos_Exercícios.md#exercício-8)

## Exercício 9

Crie um programa que:

1. Crie um dicionário chamado `produtos` com:
   - `"Notebook": 3500`
   - `"Mouse": 80`
   - `"Teclado": 150`
2. Solicite ao usuário o nome de um produto.
3. Utilize `try` para consultar o preço no dicionário.
4. Utilize `except KeyError as erro` para capturar a exceção e exibir a mensagem original.
5. Utilize `else` para exibir o preço encontrado.
6. Utilize `finally` para exibir `"Consulta finalizada."`

[Resolucão](3_Resolução_dos_Exercícios.md#exercício-9)

## Exercício 10

Último exercício deste assunto! Vamos fazer um cenário um pouco mais completo.

Crie um programa de cálculo de média que:

1. Solicite ao usuário três notas.
2. Converta as notas para `float`.
3. Calcule a média das três notas.
4. Utilize `except ValueError` para tratar entradas inválidas, exibindo `"Digite apenas valores numéricos."`
5. Utilize `else` para exibir a média calculada.
6. Utilize `finally` para exibir `"Cálculo finalizado."`

[Resolucão](3_Resolução_dos_Exercícios.md#exercício-10)
