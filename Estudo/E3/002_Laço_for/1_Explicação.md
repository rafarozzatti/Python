# 1. Laço `for`

O `for` é uma estrutura de repetição. Ele permite executar um bloco de código várias vezes, mudando o valor de uma variável a cada repetição.

Por exemplo:

```
for i in range(5):    
    print(i)
```

Saída:

```
0
1
2
3
4
```

Nesse caso, o `for` executa cinco vezes. A variável `i` assume um valor diferente em cada repetição.

## 2. Como funciona o `range()`?

O `range()` pode ser utilizado de três maneiras:

| Formato                     | Significado                                               |
| --------------------------- | --------------------------------------------------------- |
| `range(fim)`                | Começa em 0 e vai até antes de `fim`.                     |
| `range(inicio, fim)`        | Começa em `inicio` e vai até antes de `fim`.              |
| `range(inicio, fim, passo)` | Define o início, o limite e o intervalo entre os números. |

Vamos entender cada um.

### A) `range(fim)`

```
for i in range(5):    
    print(i)
```

Saída: `0, 1, 2, 3, 4`

O Python começa em zero e para antes de chegar ao cinco.

### B) `range(inicio, fim)`

```
for i in range(1, 6):    
    print(i)
```

Saída: `1, 2, 3, 4, 5`

Aqui, você escolhe o número inicial. O limite final continua sendo exclusivo: o `6` não aparece.

### C) `range(inicio, fim, passo)`

Este é o caso que merece atenção especial.

O passo determina quanto o número aumenta ou diminui a cada repetição.

```
for i in range(1, 11, 2):    
    print(i)
```

Saída:

```
1
3
5
7
9
```

Veja como funciona:

- Começa em `1`.
- Soma `2` a cada repetição.
- Para antes de chegar a `11`.

Portanto, os valores são `1, 3, 5, 7, 9`.

## 3. Como fazer uma contagem regressiva?

Para contar de trás para frente, você precisa usar um passo negativo.

Por exemplo:

```
for i in range(10, 0, -1):    
    print(i)
```

Saída:

```
10
9
8
7
6
5
4
3
2
1
```

Vamos separar os três parâmetros:

- `10`: início da contagem.
- `0`: limite em que a contagem para antes de chegar.
- `-1`: diminui um a cada repetição.

Por que usamos `0` como limite, se queremos chegar até `1`?

Porque o limite final não é incluído. Quando a contagem chega a `1`, a próxima tentativa seria chegar a `0`. Como o limite é exclusivo, o `0` não é exibido.

Atenção à diferença:

```
range(10, 1, -1)
```

Gera `10, 9, 8, 7, 6, 5, 4, 3, 2`. Não inclui o `1`.

Já:

```
range(10, 0, -1)
```

Gera `10, 9, 8, 7, 6, 5, 4, 3, 2, 1`.

## 4. Como escolher o passo?

Passo positivo: aumenta a contagem

```
for i in range(1, 10, 2):    
    print(i)
```

Saída: 1, 3, 5, 7, 9

Passo negativo: diminui a contagem

```
for i in range(10, 0, -2):    
    print(i)
```

Saída: 10, 8, 6, 4, 2

Passo de 1: comportamento padrão da contagem

```
for i in range(1, 6, 1):    
    print(i)
```

Saída: 1, 2, 3, 4, 5

O `1` pode ser omitido: `range(1, 6)` produz a mesma sequência.

Uma regra importante: o sinal do passo precisa combinar com a direção da contagem. Por exemplo, `range(10, 0, 1)` não gera números, pois começa em `10`, tenta aumentar e já está além do limite final.

O passo também não pode ser zero: `range(1, 10, 0)` gera um erro.

## 5. Resumo para suas anotações

| Código             | Números gerados                |
| ------------------ | ------------------------------ |
| `range(5)`         | 0, 1, 2, 3, 4                  |
| `range(1, 6)`      | 1, 2, 3, 4, 5                  |
| `range(1, 10, 2)`  | 1, 3, 5, 7, 9                  |
| `range(2, 11, 2)`  | 2, 4, 6, 8, 10                 |
| `range(10, 0, -1)` | 10 até 1, em ordem decrescente |
| `range(10, 0, -2)` | 10, 8, 6, 4, 2                 |

A regra principal para lembrar: `range(inicio, fim, passo)` começa no valor inicial, avança de acordo com o passo e para antes de atingir o limite final.
