# 1. Estruturas condicionais: `if`, `elif` e `else`

As estruturas condicionais permitem que o Python tome decisões com base em condições.

Por exemplo, podemos criar um programa que verifique se uma pessoa é maior de idade ou não.

## 1.1. `if` — Se

O `if` executa um bloco de código se uma condição for verdadeira.

Exemplo:

```
idade = 20

if idade >= 18:    
    print('Maior de idade')
```

Saída:

```
Maior de idade
```

Como `idade` vale `20`, a condição `idade >= 18` é verdadeira, então o Python executa o `print()`.

Observe dois detalhes importantes:

- Os dois-pontos (`:`) indicam o início do bloco condicional.
- A indentação (espaços no início da linha) indica quais instruções pertencem ao `if`. Por convenção, usamos quatro espaços.

Veja outro exemplo:

```
idade = 15

if idade >= 18:    
    print('Maior de idade')
```

Nesse caso, nada será exibido, porque a condição é falsa.

## 1.2. `else` — Senão

O `else` permite executar um bloco alternativo quando a condição do `if` é falsa.

```
idade = 15

if idade >= 18:
    print('Maior de idade')
else:   
    print('Menor de idade')
```

Saída:

```
Menor de idade
```

O funcionamento é simples:

`if idade >= 18`

A condição é verdadeira?

Sim

`print('Maior de idade')`

Não

`print('Menor de idade')`

## 1.3. `elif` — Senão, se

O `elif` permite verificar outra condição quando a condição anterior é falsa.

Exemplo:

```
nota = 7

if nota >= 9:    
    print('Excelente')
elif nota >= 6:    
    print('Aprovado')
else:    
    print('Reprovado')
```

Saída:

```
Aprovado
```

O Python verifica as condições na ordem:

1. `if nota >= 9`: é falsa, porque a nota é `7`.
2. `elif nota >= 6`: é verdadeira, porque `7` é maior ou igual a `6`.
3. O Python exibe `Aprovado` e não verifica o `else`.

Podemos usar vários `elif` quando precisamos verificar várias possibilidades.

Importante: o Python executa apenas o primeiro bloco cuja condição seja verdadeira. Se nenhuma condição for verdadeira, executa o `else`, caso exista.

## 1.4. Resumo para suas anotações

| Estrutura | Função                                                   |
| --------- | -------------------------------------------------------- |
| `if`      | Verifica a primeira condição.                            |
| `elif`    | Verifica outra condição se as anteriores forem falsas.   |
| `else`    | Executa quando nenhuma condição anterior foi verdadeira. |
