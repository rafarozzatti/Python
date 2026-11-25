## **Resto da divisão (**`%`**)**

O operador `%`, chamado de módulo, retorna o **resto de uma divisão**.

Enquanto o operador `//` retorna o resultado inteiro da divisão, o `%` retorna o valor que sobra.

### **1. Exemplo básico**

```
numero1 = 10
numero2 = 3

resultado = numero1 % numero2

print(resultado)
```

**Resultado:**

```
1
```

Isso acontece porque:

- 10 dividido por 3 resulta em 3.
- 3 × 3 = 9.
- 10 − 9 = 1.

Portanto, o resto da divisão é `1`.

### **2. Quando a divisão é exata**

Se a divisão não deixa resto, o resultado de `%` será zero.

```
print(10 % 2)
print(15 % 5)
print(20 % 4)
```

**Resultado:**

```
0
0
0
```

### **3. Comparando&#x20;**`//`**&#x20;e&#x20;**`%`

Podemos utilizar os dois operadores para entender melhor a divisão.

```
numero1 = 17
numero2 = 5

quociente = numero1 // numero2
resto = numero1 % numero2

print(quociente)
print(resto)
```

**Resultado:**

```
3
2
```

Nesse exemplo:

- `//` retorna quantas vezes o número 5 cabe em 17 sem ultrapassar: 3.
- `%` retorna o que sobra: 2.

### **4. Identificando números pares e ímpares**

Uma aplicação muito comum do operador `%` é verificar se um número é par ou ímpar.

Um número é par quando sua divisão por 2 tem resto zero.

Um número é ímpar quando sua divisão por 2 tem resto diferente de zero.

```
print(10 % 2)
print(7 % 2)
```

**Resultado:**

```
0
1
```

Portanto:

- 10 é par, pois o resto é 0.
- 7 é ímpar, pois o resto é 1.

### **5. Trabalhando com quantidades**

Imagine que temos 23 produtos e queremos organizá-los em caixas com 5 unidades.

```
produtos = 23
por_caixa = 5

caixas_completas = produtos // por_caixa
produtos_restantes = produtos % por_caixa

print(caixas_completas)
print(produtos_restantes)
```

**Resultado:**

```
4
3
```

Conseguimos montar 4 caixas completas e sobraram 3 produtos.

### **Resumo**

| Operador | Função           | Exemplo   | Resultado |
| -------- | ---------------- | --------- | --------- |
| `//`     | Divisão inteira  | `17 // 5` | `3`       |
| `%`      | Resto da divisão | `17 % 5`  | `2`       |
