# Exercícios de print() e comentários

## Exercício 1

Escreva um programa Python que exiba exatamente esta frase:

Estou aprendendo Python!

Resolução:
``` python
print('Estou aprendendo Python!')
```

## Exercício 2

Escreva um programa Python que exiba exatamente estas três linhas:

```
Nome: Rafael
Curso: Python
Objetivo: Analista de Dados
```

Regras:

- Cada informação deve aparecer em uma linha diferente.
- Utilize a função `print()`.
- Não precisa usar comentários neste exercício.

Resolução:
``` python
print('Nome: Rafael')
print('Curso: Python')
print('Objetivo: Analista de Dados')
```

## Exercício 3

Escreva um programa Python que exiba exatamente estas quatro linhas:

```
Python
2026
3.14
100
```

Regras:

- Cada valor deve aparecer em uma linha diferente.
- Utilize a função `print()`.
- Neste exercício, tente escrever os números sem aspas e o texto com aspas.

Resolução:
``` python
print('Python')
print('2026')
print(3.14)
print(100)
```

## Exercício 4

Agora vamos praticar o uso do símbolo `#`.

Escreva um programa que tenha:

1. Um comentário explicando o objetivo do programa.
2. Um comando `print()` que exiba `Meu primeiro programa`.
3. Outro comentário depois do comando `print()`, na mesma linha.

Atenção: os comentários não devem aparecer na saída do programa.

Resolução:
``` python
# praticando o uso do símbolo #
print('Meu primeiro programa') # exibe a 'frase Meu primeiro programa'
```

## Exercício 5

Escreva um programa que exiba exatamente estas quatro linhas:

```
=== MEU PERFIL ===
Nome: Rafael
Área: Dados
Meta: Aprender Python
```

Regras:

- Utilize `print()` para exibir cada linha.
- Inclua pelo menos dois comentários no código.
- Nenhum comentário pode aparecer na saída.

Resolução:
``` python
print('=== MEU PERFIL ===') # titulo
print('Nome: Rafael')
print('Área: Dados') # Área desejada
print('Meta: Aprender Python')
```

## Exercício 6

Escreva um programa Python que exiba exatamente esta saída:

```
CURSO DE PYTHON
Duração: 40 horas
Módulo: Fundamentos
Status: Em andamento
```

Regras:

- Utilize exatamente quatro comandos `print()`, um para cada linha.
- Inclua pelo menos um comentário no código.
- O comentário não pode aparecer na saída.
- Não copie a saída como um único texto em um único `print()`.

Resolução:
``` python
print('CURSO DE PYTHON')
print('Duração: 40 horas') # Duração do curso
print('Módulo: Fundamentos')
print('Status: Em andamento') # Status
```

## Exercício 7

Agora vamos testar sua capacidade de identificar erros.

O código abaixo deveria exibir três linhas, mas contém alguns problemas:

```
print('Relatório de vendas)# Exibe o faturamentoprint('Faturamento: R$ 1500)print('Status: Concluído'
```

Sua tarefa:

1. Identifique os erros no código.
2. Reescreva o programa corrigido.
3. Mantenha o comentário e as três linhas de saída esperadas:

```
Relatório de vendas
Faturamento: R$ 1500
Status: Concluído
```

Resolução:
``` python
print('Relatório de vendas')
print('Faturamento: R$ 1500') # Exibe o faturamento
print('Status: Concluído')
```

## Exercício 8

Escreva um programa que exiba exatamente esta saída:

```
====================
RELATÓRIO DE VENDAS
====================
Produto: Notebook
Quantidade: 5 unidades
Status: Finalizado
```

Regras:

- Utilize exatamente seis comandos `print()`.
- Inclua pelo menos dois comentários.
- Os comentários não podem aparecer na saída.
- Respeite as letras maiúsculas, os acentos e a ordem das linhas.

Resolução:
``` python
print('====================')
print('RELATÓRIO DE VENDAS')
print('====================')
print('Produto: Notebook') # Produto
print('Quantidade: 5 unidades')
print('Status: Finalizado') # Status
```

## Exercício 9

Agora vamos testar se você realmente entendeu a diferença entre código, comentários e saída do programa.

Considere o seguinte código:

```
print('Início')# print('Esta mensagem não aparece')print('Python')print('10') # print('Esta mensagem também não aparece')print('Fim')
```

Sua tarefa: escreva exatamente qual será a saída desse programa, respeitando as linhas e a ordem.

Não precisa executar o código. Tente responder com base no que aprendeu sobre `print()` e comentários.

Resolução:
```
Início
Python
10
Fim
```

## Exercício 10

Agora vamos juntar tudo o que você praticou nesta aula.

Escreva um programa Python que produza exatamente a seguinte saída:

```
==============================
RELATÓRIO DE ESTUDOS
==============================
Linguagem: Python
Exercícios concluídos: 9
Próxima etapa: Variáveis
Status: Em andamento
==============================
```

Regras:

1. Utilize exatamente sete comandos `print()`.
2. Inclua pelo menos três comentários no código.
3. Os comentários devem estar distribuídos em pelo menos duas linhas diferentes do código.
4. Nenhum comentário pode aparecer na saída.
5. Respeite exatamente o texto, as letras maiúsculas, os acentos e a ordem das linhas.

Resolução:
``` python
print('''==============================
RELATÓRIO DE ESTUDOS''') # 6 aspas(3 em cada linha) para utilizar varias linhas em um print só
print('==============================')
print('Linguagem: Python')
print('Exercícios concluídos: 9')
print('Próxima etapa: Variáveis')
print('Status: Em andamento') # Status
print('==============================') # Fim
```
