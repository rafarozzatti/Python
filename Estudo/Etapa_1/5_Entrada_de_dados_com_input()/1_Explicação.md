# 5. Entrada de dados com `input()`

## 1. O que é `input()`?

A função `input()` permite que o usuário digite uma informação enquanto o programa está sendo executado.

Até agora, você definiu os valores diretamente no código. Com `input()`, o programa pode receber os valores de quem está usando.

Veja a diferença:

Sem `input()`

```
nome = "Rafael"
print(nome)
```

Saída:

```
Rafael
```

Com `input()`

```
nome = input("Digite seu nome: ")
print(nome)
```

Exemplo de execução:

```
Digite seu nome: Rafael
Rafael
```

Nesse exemplo, Rafael é o valor digitado pelo usuário. O programa não define esse nome antecipadamente.

## 2. Como funciona o `input()`?

Observe este código:

```
idade = input("Digite sua idade: ")
print(idade)
```

A execução acontece nesta ordem:

1. O programa exibe `Digite sua idade:`.
2. O usuário digita um valor, por exemplo, `27`.
3. O valor digitado é armazenado na variável `idade`.
4. O `print()` exibe o conteúdo da variável.

## 3. Atenção: `input()` sempre retorna texto (`str`)

Esse é o ponto mais importante desta aula.

Mesmo que o usuário digite um número, o `input()` recebe o valor como texto.

```
idade = input("Digite sua idade: ")
print(idade)
print(type(idade))
```

Se o usuário digitar `27`, a saída será:

```
27
<class 'str'>
```

O valor parece um número, mas está armazenado como texto.

### Como resolver isso?

Você pode combinar `input()` com as funções de conversão que já estudamos.

Exemplo 1 — Receber um número inteiro

```
idade = int(input("Digite sua idade: "))
print(idade)
print(type(idade))
```

Se o usuário digitar `27`:

```
27
<class 'int'>
```

Exemplo 2 — Receber um número decimal

```
preco = float(input("Digite o preço: "))
print(preco)
print(type(preco))
```

Se o usuário digitar `49.90`:

```
49.9
<class 'float'>
```

Repare nesta estrutura:

```
int(input("Digite um número: "))
```

Primeiro, o `input()` recebe o valor digitado. Depois, o `int()` converte esse valor para inteiro.

## 4. Fazendo cálculos com dados digitados

Veja um exemplo que soma dois números informados pelo usuário:

```
numero1 = int(input("Digite o primeiro número: "))numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2
print(soma)
```

Exemplo de execução:

```
Digite o primeiro número: 10
Digite o segundo número: 5
15
```

Usamos `int()` porque queremos somar números inteiros. Se fossem valores decimais, poderíamos utilizar `float()`.

Importante: para converter um texto em `int` ou `float`, o conteúdo digitado precisa representar um número válido. Por exemplo, `int("abc")` gera um erro.
