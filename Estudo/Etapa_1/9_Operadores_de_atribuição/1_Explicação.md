# 9. Operadores de atribuição

Os operadores de atribuição servem para atribuir um valor a uma variável ou atualizar o valor que ela já possui.

Você já conhece o operador `=`, que usamos desde o começo:

```
saldo = 100
print(saldo)
```

Saída:

```
100
```

Nesse caso, o operador `=` atribui o valor `100` à variável `saldo`.

Agora vamos aprender outros operadores que permitem atualizar variáveis de maneira mais curta.

## 2. Principais operadores de atribuição

## `=`

Atribuição simples

```
numero = 10
```

A variável `numero` recebe o valor `10`.

## `+=`

Soma e atribuição

```
numero = 10
numero += 5

print(numero)
```

Saída: `15`

É equivalente a `numero = numero + 5`.

## `-=`

Subtração e atribuição

```
numero = 10
numero -= 3

print(numero)
```

Saída: `7`

É equivalente a `numero = numero - 3`.

## `*=`

Multiplicação e atribuição

```
numero = 10
numero *= 3

print(numero)
```

Saída: `30`

É equivalente a `numero = numero * 3`.

## `/=`

Divisão e atribuição

```
numero = 10
numero /= 2

print(numero)
```

Saída: `5.0`

É equivalente a `numero = numero / 2`. O resultado de `/` é do tipo `float`.

## 3. Outros operadores de atribuição

Também existem operadores para outras operações matemáticas que você já estudou.

| Operador | Equivalente            | Exemplo: começando com `numero = 10` | Resultado |
| -------- | ---------------------- | ------------------------------------ | --------- |
| `//=`    | `numero = numero // 3` | `numero //= 3`                       | `3`       |
| `%=`     | `numero = numero % 3`  | `numero %= 3`                        | `1`       |
| `**=`    | `numero = numero ** 3` | `numero **= 3`                       | `1000`    |

Esses operadores fazem, respectivamente, divisão inteira, resto da divisão e exponenciação, salvando o resultado na própria variável.

## 4. Entenda a diferença entre `=` e `+=`

Observe este exemplo:

```
saldo = 100
saldo = 50

print(saldo)
```

Saída: `50`

O segundo `=` substitui o valor anterior.

Agora veja:

```
saldo = 100
saldo += 50

print(saldo)
```

Saída: `150`

O `+=` soma `50` ao valor existente e atualiza a variável.

Regra importante: o operador de atribuição combinado sempre utiliza o valor atual da variável para calcular o novo valor.
