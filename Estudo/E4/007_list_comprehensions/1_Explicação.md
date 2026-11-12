# 1. Criando listas com `for`

Antes de entender List Comprehension, vamos relembrar uma maneira tradicional de criar listas.

Imagine que queremos criar uma lista com os números de 1 a 5.

Podemos fazer assim:

```
numeros = []

for i in range(1, 6):    
    numeros.append(i)
    
print(numeros)
```

Saída:

```
[1, 2, 3, 4, 5]
```

Observe o processo:

1. Criamos uma lista vazia.
2. Utilizamos `for` para percorrer os números.
3. Utilizamos `append()` para adicionar cada número à lista.

# 2. Criando a mesma lista com List Comprehension

Podemos escrever exatamente o mesmo código em uma única linha:

```
numeros = [i for i in range(1, 6)]

print(numeros)
```

Saída:

```
[1, 2, 3, 4, 5]
```

Essa é a estrutura básica:

## Estrutura da List Comprehension

# [ expressão for variável in sequência ]

- Expressão: o que será adicionado à lista.
- for: percorre os elementos.
- Variável: recebe cada elemento.
- Sequência: de onde vêm os elementos.

Vamos entender outro exemplo:

```
dobros = [numero * 2 for numero in range(1, 6)]

print(dobros)
```

Saída:

```
[2, 4, 6, 8, 10]
```

A cada repetição, o Python multiplica o número atual por 2 e adiciona o resultado à nova lista.

| Repetição | Expressão | Resultado |
| --------- | --------- | --------- |
| 1         | 1 \* 2    | 2         |
| 2         | 2 \* 2    | 4         |
| 3         | 3 \* 2    | 6         |
| 4         | 4 \* 2    | 8         |
| 5         | 5 \* 2    | 10        |

# 3. Utilizando condições com `if`

Também podemos adicionar condições para decidir quais elementos entrarão na lista.

Imagine que queremos criar uma lista contendo somente números pares de 1 a 10.

Forma tradicional:

```
pares = []

for numero in range(1, 11):    
    if numero % 2 == 0:        
        pares.append(numero)
        
print(pares)
```

Saída:

```
[2, 4, 6, 8, 10]
```

Com List Comprehension:

```
pares = [numero for numero in range(1, 11) if numero % 2 == 0]

print(pares)
```

A estrutura agora é:

## List Comprehension com condição

# [ expressão for variável in sequência if condição ]

- Expressão: valor que será adicionado.
- For: percorre a sequência.
- If: determina quais elementos serão incluídos.

Nesse exemplo, somente os números que satisfazem `numero % 2 == 0` são adicionados.

# 4. Aplicando operações aos elementos

Podemos utilizar operações matemáticas e também trabalhar com textos.

Exemplo com números:

```
numeros = [1, 2, 3, 4, 5]

quadrados = [numero ** 2 for numero in numeros]

print(quadrados)
```

Saída:

```
[1, 4, 9, 16, 25]
```

Exemplo com strings:

```
nomes = ["carlos", "mariana", "pedro"]

nomes_maiusculos = [nome.upper() for nome in nomes]

print(nomes_maiusculos)
```

Saída:

```
['CARLOS', 'MARIANA', 'PEDRO']
```

Aqui utilizamos `upper()`, que transforma os caracteres de uma string em letras maiúsculas.

# 5. Utilizando `if` e `else`

Existe outra possibilidade: utilizar uma condição para definir qual valor será adicionado à lista.

Imagine que queremos classificar números como "Par" ou "Ímpar".

```
numeros = [1, 2, 3, 4, 5]

classificacao = [    
    "Par" if numero % 2 == 0 else "Ímpar"    
    for numero in numeros
]
    
print(classificacao)
```

Saída:

```
['Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar']
```

Observe que agora temos uma diferença importante:

- O `if` e o `else` ficam antes do `for`.
- A condição determina o valor que será colocado na lista.
- Todos os elementos são incluídos, mas recebem valores diferentes dependendo da condição.

Estrutura:

```
[valor_se_verdadeiro if condição else valor_se_falso for variável in sequência]
```

# Resumo do conteúdo

| Tipo          | Estrutura                                             |
| ------------- | ----------------------------------------------------- |
| Básica        | `[expressão for x in sequência]`                      |
| Com `if`      | `[expressão for x in sequência if condição]`          |
| Com `if/else` | `[valor1 if condição else valor2 for x in sequência]` |

Uma recomendação: apesar de ser possível escrever expressões bastante complexas com List Comprehension, prefira utilizá-la quando o código continuar fácil de entender. Nem sempre substituir um `for` tradicional por uma linha é a melhor escolha.
