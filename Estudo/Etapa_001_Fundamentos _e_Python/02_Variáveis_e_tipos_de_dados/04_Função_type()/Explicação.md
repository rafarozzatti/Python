## **Função&#x20;**`type()`

A função `type()` permite identificar o tipo de dado armazenado em uma variável ou utilizado em um valor.

Ela é bastante útil para verificar se uma informação é um número inteiro, decimal, texto ou valor lógico.

### **1. Utilizando&#x20;**`type()`

Para utilizar a função, escrevemos `type()` e colocamos dentro dos parênteses a variável ou o valor que queremos verificar.

```
idade = 27

print(type(idade))
```

**Resultado:**

```
<class 'int'>
```

O resultado indica que a variável `idade` armazena um valor do tipo `int`.

### **2. Identificando os quatro tipos de dados**

Vamos verificar os tipos que estudamos anteriormente:

```
nome = 'Rafael'
idade = 27
altura = 1.75
estudando = True

print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudando))
```

**Resultado:**

```
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

Observe a correspondência:

| Variável    | Resultado | Tipo    |
| ----------- | --------- | ------- |
| `nome`      | `str`     | Texto   |
| `idade`     | `int`     | Inteiro |
| `altura`    | `float`   | Decimal |
| `estudando` | `bool`    | Lógico  |

### **3. Verificando valores diretamente**

Não precisamos necessariamente criar uma variável para utilizar `type()`.

Também podemos verificar um valor diretamente:

```
print(type(100))
print(type(15.5))
print(type('Python'))
print(type(False))
```

**Resultado:**

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

### **4. Verificando se uma variável mudou de tipo**

Lembre-se de que uma variável pode receber um novo valor durante a execução do programa.

Com isso, seu tipo também pode mudar.

```
valor = 100

print(type(valor))

valor = 'Cem'

print(type(valor))
```

**Resultado:**

```
<class 'int'>
<class 'str'>
```

Inicialmente, `valor` armazenava um número inteiro. Depois, passou a armazenar um texto.

### **Resumo**

- `type()` identifica o tipo de dado de um valor ou variável.
- O resultado apresenta a classe correspondente: `int`, `float`, `str` ou `bool`.
- Podemos utilizar `type()` diretamente com valores ou com variáveis.
- O tipo de uma variável pode mudar quando atribuímos um novo valor a ela.
