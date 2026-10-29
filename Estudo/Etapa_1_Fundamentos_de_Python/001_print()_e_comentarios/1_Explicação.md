**# Aula 1 — `print()` e comentários**

**## 1. A função `print()`**

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

**### Exibir várias informações**

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

**### O parâmetro `end`**

Por padrão, o `print()` termina com uma quebra de linha. Entretanto, podemos utilizar o parâmetro `end` para definir o que será colocado depois do valor exibido.

**1. `end=' '` — espaço**

O `end=' '` coloca um espaço depois do valor e impede a quebra de linha automática. Assim, os próximos valores podem aparecer na mesma linha.

Exemplo:

```
print(1, end=' ')
print(2, end=' ')
print(3)
```

Saída:

```
1 2 3
```

Observe que os dois primeiros comandos não pularam para a próxima linha. O último `print(3)` utiliza o comportamento padrão e termina com uma quebra de linha.

**2. `end='-'` — hífen**

O `end='-'` coloca um hífen depois do valor, sem pular automaticamente para a próxima linha.

Exemplo:

```
print(1, end='-')
print(2, end='-')
print(3)
```

Saída:

```
1-2-3
```

Nesse caso, o hífen é utilizado como separador entre os valores.

**3. `end=''` — sem separador**

O `end=''` não acrescenta nenhum caractere depois do valor e também impede a quebra de linha automática.

Exemplo:

```
print(1, end='')
print(2, end='')
print(3)
```

Saída:

```
123
```

Como não foi acrescentado espaço, hífen ou outro caractere entre os valores, eles aparecem juntos.

**### Resumo do parâmetro `end`**

| Código              | Comportamento             | Exemplo de saída            |
| ------------------- | ------------------------- | --------------------------- |
| `print(1)`          | Pula para a próxima linha | `1` e depois quebra a linha |
| `print(1, end=' ')` | Acrescenta um espaço      | `1 `                        |
| `print(1, end='-')` | Acrescenta um hífen       | `1-`                        |
| `print(1, end='')`  | Não acrescenta nada       | `1` sem quebra de linha     |

Lembre-se: o parâmetro `end` controla o que acontece **depois que o valor é exibido**. Ele é útil para organizar a saída do programa, colocar valores na mesma linha e montar tabelas ou matrizes.

**## 2. Comentários em Python**

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
