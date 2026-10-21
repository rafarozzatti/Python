# Aula 2 — Variáveis e atribuição de valores

## 1. O que é uma variável?

Uma variável é um nome que utilizamos para referenciar um valor durante a execução do programa.

Imagine que você está criando um relatório de vendas. Em vez de escrever o nome de um produto diretamente em vários lugares do código, pode armazená-lo em uma variável e reutilizá-lo.

Veja este exemplo:

```
produto = "Notebook"

print(produto)
```

Saída:

```
Notebook
```

Vamos entender cada parte:

- `produto` é o nome da variável.
- `=` é o operador de atribuição.
- `"Notebook"` é o valor armazenado.
- `print(produto)` exibe o valor associado à variável.

Atenção: quando você utiliza aspas, está indicando um texto. Quando escreve `produto` sem aspas dentro do `print()`, o Python procura a variável com esse nome.

Compare:

```
produto = "Notebook"

print(produto)
print("produto")
```

Saída:

```
Notebook
produto
```

No primeiro `print()`, aparece o valor da variável. No segundo, aparece literalmente a palavra `produto`.

## 2. Como atribuir valores?

Podemos armazenar diferentes tipos de valores em variáveis:

```
nome = "Rafael"
idade = 27
altura = 1.69
estudando = True
```

Neste momento, estamos apenas atribuindo os valores. Se executarmos o código, nada será exibido, porque ainda não utilizamos `print()`.

Para exibi-los:

```
nome = "Rafael"
idade = 27
altura = 1.69
estudando = True

print(nome)
print(idade)
print(altura)
print(estudando)
```

Saída:

```
Rafael
27
1.75
True
```

Observe que as variáveis podem armazenar textos, números inteiros, números decimais e valores booleanos. Vamos estudar os tipos de dados com mais profundidade em outro tópico.

## 3. Como alterar o valor de uma variável?

Uma variável pode receber um novo valor durante a execução do programa.

```
faturamento = 1000

print(faturamento)

faturamento = 1500

print(faturamento)
```

Saída:

```
1000
1500
```

Na primeira atribuição, `faturamento` recebe `1000`. Depois, recebe `1500`. A segunda atribuição substitui o valor anterior.

## 4. Regras para nomes de variáveis

Em Python, existem algumas regras importantes:

| Exemplo        | É válido? | Motivo                                |
| -------------- | --------- | ------------------------------------- |
| `nome`         | Sim       | Nome simples                          |
| `nome_cliente` | Sim       | Sublinhado permitido                  |
| `idade2`       | Sim       | Pode conter números depois do início  |
| `2idade`       | Não       | Não pode começar com número           |
| `nome-cliente` | Não       | O hífen é interpretado como subtração |
| `nome cliente` | Não       | Não pode conter espaço                |
| `class`        | Não       | Palavra reservada do Python           |

Uma boa prática é usar nomes descritivos e o padrão `snake_case`, no qual palavras são separadas por sublinhados.

Por exemplo:

```
total_vendas = 5000
quantidade_produtos = 12
nome_cliente = "Mariana"
```

Evite nomes genéricos como `a`, `b` ou `x` quando estiver trabalhando com dados reais, a menos que exista um motivo para usá-los.

## 5. Atribuindo um novo valor com base no anterior

Você também pode usar o valor atual de uma variável para calcular seu novo valor.

```
quantidade = 10

quantidade = quantidade + 5

print(quantidade)
```

Saída:

```
15
```

A expressão `quantidade = quantidade + 5` significa: pegue o valor atual de `quantidade`, some 5 e atribua o resultado novamente à variável.

Isso é diferente de uma igualdade matemática. Em Python, o sinal `=` representa atribuição.
