## **Operadores&#x20;**`=`**,&#x20;**`+=`**,&#x20;**`-=`**,&#x20;**`*=`**&#x20;e&#x20;**`/=`

Os **operadores de atribuição** são utilizados para atribuir valores a variáveis ou atualizar valores que elas já possuem.

### **1. Atribuição simples (**`=`**)**

O operador `=` atribui um valor a uma variável.

```
numero = 10

print(numero)
```

Resultado:

```
10
```

### **2. Adição com atribuição (**`+=`**)**

Soma um valor ao conteúdo atual da variável e armazena o resultado nela.

```
numero = 10

numero += 5

print(numero)
```

Resultado:

```
15
```

É equivalente a:

```
numero = numero + 5
```

### **3. Subtração com atribuição (**`-=`**)**

Subtrai um valor do conteúdo atual da variável.

```
numero = 10

numero -= 3

print(numero)
```

Resultado:

```
7
```

Equivalente a `numero = numero - 3`.

### **4. Multiplicação com atribuição (**`*=`**)**

Multiplica o conteúdo atual da variável por um valor.

```
numero = 10

numero *= 3

print(numero)
```

Resultado:

```
30
```

Equivalente a `numero = numero * 3`.

### **5. Divisão com atribuição (**`/=`**)**

Divide o conteúdo atual da variável por um valor.

```
numero = 10

numero /= 2

print(numero)
```

Resultado:

```
5.0
```

Equivalente a `numero = numero / 2`.

Observe que a divisão `/` retorna um resultado do tipo `float`, mesmo quando o resultado é inteiro.

### **Resumo**

| Operador | Equivalente           | Exemplo (`numero = 10`) | Resultado |
| -------- | --------------------- | ----------------------- | --------- |
| `=`      | Atribuição            | `numero = 10`           | 10        |
| `+=`     | `numero = numero + 5` | `numero += 5`           | 15        |
| `-=`     | `numero = numero - 3` | `numero -= 3`           | 7         |
| `*=`     | `numero = numero * 3` | `numero *= 3`           | 30        |
| `/=`     | `numero = numero / 2` | `numero /= 2`           | 5.0       |
