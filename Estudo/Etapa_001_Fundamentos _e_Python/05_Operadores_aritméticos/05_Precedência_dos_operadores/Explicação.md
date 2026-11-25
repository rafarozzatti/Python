## **Precedência dos operadores**

A **precedência dos operadores** define a ordem em que o Python realiza as operações dentro de uma expressão matemática.

Assim como na matemática, algumas operações são executadas antes de outras.

### **1. Ordem de precedência**

Para os operadores aritméticos que estudamos, a ordem é:

| Prioridade | Operadores          | Operação                        |
| ---------- | ------------------- | ------------------------------- |
| 1º         | `()`                | Parênteses                      |
| 2º         | `**`                | Potenciação                     |
| 3º         | `*`, `/`, `//`, `%` | Multiplicação, divisões e resto |
| 4º         | `+`, `-`            | Adição e subtração              |

Quando operadores estão no mesmo nível de prioridade, normalmente são avaliados da esquerda para a direita. A potenciação é uma exceção: é avaliada da direita para a esquerda.

### **2. Exemplos práticos**

**Exemplo 1 — Multiplicação antes da adição**

```
resultado = 2 + 3 * 4

print(resultado)
```

Resultado:

```
14
```

Primeiro, Python realiza `3 * 4`, depois soma `2`.

**Exemplo 2 — Parênteses alteram a ordem**

```
resultado = (2 + 3) * 4

print(resultado)
```

Resultado:

```
20
```

Primeiro, Python resolve o que está entre parênteses: `2 + 3`. Depois multiplica por `4`.

**Exemplo 3 — Potenciação antes da multiplicação**

```
resultado = 2 * 3 ** 2

print(resultado)
```

Resultado:

```
18
```

Primeiro, `3 ** 2 = 9`. Depois, `2 * 9 = 18`.

**Exemplo 4 — Operadores com a mesma prioridade**

```
resultado = 20 / 5 * 2

print(resultado)
```

Resultado:

```
8.0
```

A divisão e a multiplicação possuem a mesma prioridade. Portanto, Python executa da esquerda para a direita:

1. `20 / 5 = 4.0`
2. `4.0 * 2 = 8.0`

**Exemplo 5 — Potenciação da direita para a esquerda**

```
resultado = 2 ** 3 ** 2

print(resultado)
```

Resultado:

```
512
```

Python interpreta a expressão como:

```
2 ** (3 ** 2)
```

Primeiro, `3 ** 2 = 9`. Depois, `2 ** 9 = 512`.

**Resumo:** os parênteses permitem controlar a ordem das operações. Quando tiver dúvida sobre uma expressão, você pode utilizá-los para deixar a intenção mais clara.
