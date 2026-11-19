# **1. O que são funções lambda?**

Uma função `lambda` é uma forma mais curta de criar funções em Python.

Até agora, utilizamos `def` para criar nossas funções:

```
def somar(a, b):    
    return a + b

resultado = somar(10, 5)

print(resultado)
```

Saída:

```
15
```

Com `lambda`, podemos escrever a mesma função em apenas uma linha:

```
somar = lambda a, b: a + b

resultado = somar(10, 5)

print(resultado)
```

Saída:

```
15
```

Observe a estrutura:

```
lambda parametros: expressão
```

- `lambda`: palavra-chave que cria a função.
- `parametros`: informações que a função recebe.
- `:` separa os parâmetros da expressão.
- `expressão`: operação que será executada e retornada automaticamente.

**Importante:** Diferentemente de uma função criada com `def`, uma função lambda não precisa utilizar `return`. O resultado da expressão é retornado automaticamente.

# **2. Lambda com um parâmetro**

Podemos criar uma função que recebe apenas um parâmetro:

```
dobro = lambda numero: numero * 2

print(dobro(5))
```

Saída:

```
10
```

Nesse exemplo:

- `numero` é o parâmetro.
- `numero * 2` é a expressão.
- `dobro(5)` chama a função passando o valor 5.

# **3. Lambda com vários parâmetros**

Também podemos receber dois ou mais parâmetros:

```
multiplicar = lambda a, b: a * b

print(multiplicar(4, 3))
```

Saída:

```
12
```

A quantidade de parâmetros não é limitada a um.

# **4. Lambda com condições**

Podemos utilizar `if` e `else` dentro de uma função lambda.

Exemplo:

```
verificar = lambda idade: 'Maior de idade' if idade >= 18 else 'Menor de idade'

print(verificar(20))
print(verificar(15))
```

Saída:

```
Maior de idade
Menor de idade
```

Observe a estrutura:

```
lambda parametro: valor_se_verdadeiro if condição else valor_se_falso
```

Atenção: nesse formato, utilizamos `if` e `else`, mas não `elif`.

# **5. Diferenças entre def e lambda**

| Característica | def                          | lambda           |
| -------------- | ---------------------------- | ---------------- |
| Criação        | Mais extensa                 | Mais curta       |
| Nome           | Pode ter nome                | Pode ser anônima |
| Parâmetros     | Sim                          | Sim              |
| `return`       | Explícito, quando necessário | Automático       |
| Operações      | Várias instruções            | Uma expressão    |

**Quando utilizar?**

- `def`: quando a função possui várias operações ou precisa de uma estrutura mais elaborada.
- `lambda`: quando precisamos de uma função pequena, simples e de uma única expressão.

Não significa que lambda seja melhor. Cada uma tem sua utilidade.

# **6. Exemplos adicionais**

**Exemplo 1 — Calcular desconto:**

```
desconto = lambda preco: preco * 0.10

print(desconto(200))
```

Saída:

```
20.0
```

**Exemplo 2 — Converter temperatura:**

```
celsius_para_fahrenheit = lambda c: (c * 9/5) + 32

print(celsius_para_fahrenheit(30))
```

Saída:

```
86.0
```

**Exemplo 3 — Verificar número positivo ou negativo:**

```
verificar = lambda numero: 'Positivo' if numero >= 0 else 'Negativo'

print(verificar(-5))
```

Saída:

```
Negativo
```

## **Resumo para suas anotações**

A função lambda permite criar funções pequenas em uma única linha.

Estrutura:

```
nome = lambda parametros: expressão
```

Principais características:

- Pode receber um ou vários parâmetros.
- Não utiliza `return` explicitamente.
- Retorna automaticamente o resultado da expressão.
- Pode utilizar condições com `if` e `else`.
- É indicada para operações simples.
