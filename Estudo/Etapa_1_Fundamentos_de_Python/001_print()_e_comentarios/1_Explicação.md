# Aula 1 — `print()` e comentários

## 1. A função `print()`

A função `print()` é utilizada para exibir informações na tela. Ela é uma das primeiras funções que aprendemos em Python.

Exemplo:

```
print("Olá, mundo!")
```

Saída:

```
Olá, mundo!
```

Tudo o que estiver entre aspas será exibido como texto.

Você também pode imprimir números sem aspas:

```
print(10)
print(25.5)
print(100 + 50)
```

Saída:

```
10
25.5
150
```

Observe que, no último exemplo, o Python calculou `100 + 50` antes de mostrar o resultado.

### Exibir várias informações

Você pode utilizar vários comandos `print()` no mesmo programa:

```
print("Meu nome é Rafael.")
print("Estou estudando Python.")
print("Quero trabalhar com análise de dados.")
```

Saída:

```
Meu nome é Rafael.
Estou estudando Python.
Quero trabalhar com análise de dados.
```

Por padrão, cada chamada de `print()` termina com uma quebra de linha. Por isso, cada informação aparece em uma linha diferente.

Também é possível imprimir vários valores em um único comando:

```
print("Python", "SQL", "Power BI")
```

Saída:

```
Python SQL Power BI
```

Por padrão, o Python separa os valores por um espaço.

## 2. Comentários em Python

Os comentários servem para escrever observações no código. Eles ajudam você ou outra pessoa a entender o que determinado trecho faz.

Para escrever um comentário de uma linha, utilizamos o símbolo `#`.

```
# Este programa exibe uma mensagem
print("Estou aprendendo Python!")
```

Saída:

```
Estou aprendendo Python!
```

Perceba que o comentário não aparece na saída. O Python ignora o conteúdo escrito depois do `#` naquela linha.

Você também pode colocar um comentário depois de um comando:

```
print("Olá!")  # Exibe uma saudação
```

Saída:

```
Olá!
```

Atenção: não confunda comentários com textos exibidos pelo programa.

```
# Isto é um comentário
print("Isto é uma mensagem")
```

O primeiro não aparece na tela; o segundo aparece.
