# **. Retorno de múltiplos valores**

Até agora, aprendemos que uma função pode utilizar `return` para devolver um resultado.

Mas você sabia que uma função também pode devolver **mais de um valor ao mesmo tempo**?

## **1. Como funciona?**

Imagine uma função que recebe dois números e precisa devolver a soma e a multiplicação deles.

```
def calcular(a, b):    soma = a + b    multiplicacao = a * b    return soma, multiplicacao
```

Observe que utilizamos apenas um `return`, mas colocamos duas variáveis separadas por vírgula.

## **2. Armazenando os valores retornados**

Podemos receber os dois resultados em variáveis diferentes:

```
resultado_soma, resultado_multiplicacao = calcular(10, 5)print(resultado_soma)print(resultado_multiplicacao)
```

Saída:

```
15
50
```

O Python distribui automaticamente cada valor retornado para sua respectiva variável.

## **3. O que acontece por trás?**

Quando retornamos vários valores separados por vírgula, o Python agrupa esses valores em uma estrutura chamada **tupla**.

Por exemplo:

```
def calcular(a, b):    return a + b, a * bresultado = calcular(10, 5)print(resultado)print(type(resultado))
```

Saída:

```
(15, 50)
<class 'tuple'>
```

Portanto, podemos receber os valores individualmente ou armazenar todos em uma única variável.

## **4. Exemplo prático**

Imagine uma análise de vendas em que precisamos obter o total vendido e a quantidade de vendas.

```
def analisar_vendas(vendas):    total = sum(vendas)    quantidade = len(vendas)    return total, quantidadetotal_vendido, quantidade_vendas = analisar_vendas([100, 200, 150, 50])print(f'Total vendido: R$ {total_vendido}')print(f'Quantidade de vendas: {quantidade_vendas}')
```

Saída:

```
Total vendido: R$ 500
Quantidade de vendas: 4
```

Aqui, a função devolve duas informações diferentes a partir de uma única lista.

