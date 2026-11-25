## **Criação e atribuição de variáveis**

Uma **variável** é um nome utilizado para armazenar um valor na memória durante a execução de um programa.

Ela permite guardar informações para utilizá-las posteriormente, sem precisar escrever o mesmo valor várias vezes.

### **1. Criando uma variável**

Em Python, criamos uma variável utilizando o sinal de igualdade (`=`).

```
nome = 'Rafael'
idade = 27
altura = 1.75
```

Nesse exemplo, criamos três variáveis:

- `nome` armazena o valor `'Rafael'`.
- `idade` armazena o valor `27`.
- `altura` armazena o valor `1.75`.

O sinal `=` é chamado de **operador de atribuição**. Ele atribui o valor que está à direita à variável que está à esquerda.

### **2. Utilizando variáveis**

Depois de criar uma variável, podemos utilizar seu nome para acessar o valor armazenado.

```
nome = 'Rafael'
idade = 27

print(nome)
print(idade)
```

**Resultado:**

```
Rafael
27
```

Também podemos utilizar variáveis em operações:

```
numero1 = 10
numero2 = 20

soma = numero1 + numero2

print(soma)
```

**Resultado:**

```
30
```

Observe que criamos uma terceira variável, `soma`, para armazenar o resultado da operação.

### **3. Alterando o valor de uma variável**

Uma variável pode receber um novo valor durante a execução do programa.

```
idade = 25

print(idade)

idade = 27

print(idade)
```

**Resultado:**

```
25
27
```

Quando atribuímos `27` à variável `idade`, o valor anterior, `25`, deixa de ser o valor armazenado nela.

### **4. Atribuindo valores a partir de outras variáveis**

Também podemos utilizar uma variável para atribuir seu valor a outra.

```
nome = 'Rafael'

nome_completo = nome

print(nome_completo)
```

**Resultado:**

```
Rafael
```

Nesse caso, `nome_completo` recebe o valor que estava armazenado em `nome`.

### **5. Atribuição de múltiplas variáveis**

Python permite atribuir valores a várias variáveis em uma única linha:

```
nome, idade, cidade = 'Rafael', 27, 'São Paulo'

print(nome)
print(idade)
print(cidade)
```

**Resultado:**

```
Rafael
27
São Paulo
```

Também podemos atribuir o mesmo valor a várias variáveis:

```
a = b = c = 10

print(a)
print(b)
print(c)
```

**Resultado:**

```
10
10
10
```

**Resumo:** variáveis armazenam valores, são criadas por meio de atribuições com `=` e podem ser utilizadas em operações, impressões e outras atribuições.
