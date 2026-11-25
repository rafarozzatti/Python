## **Função&#x20;**`input()`

A função `input()` permite que o programa receba informações digitadas pelo usuário durante sua execução.

Diferentemente de valores definidos diretamente no código, com `input()` podemos solicitar informações enquanto o programa está rodando.

### **1. Utilizando&#x20;**`input()`

Para receber uma informação, utilizamos `input()` e podemos colocar uma mensagem dentro dos parênteses.

```
nome = input('Digite seu nome: ')

print(nome)
```

**Exemplo de execução:**

```
Digite seu nome: Rafael
Rafael
```

Nesse exemplo:

1. O programa exibe a mensagem `Digite seu nome:`.
2. O usuário digita `Rafael`.
3. O valor digitado é armazenado na variável `nome`.
4. O `print()` exibe o conteúdo da variável.

### **2. Armazenando diferentes informações**

Podemos utilizar vários `input()` no mesmo programa.

```
nome = input('Digite seu nome: ')
cidade = input('Digite sua cidade: ')
profissao = input('Digite sua profissão: ')

print(nome)
print(cidade)
print(profissao)
```

**Exemplo de execução:**

```
Digite seu nome: Rafael
Digite sua cidade: São Paulo
Digite sua profissão: Engenheiro

Rafael
São Paulo
Engenheiro
```

Cada informação digitada é armazenada em sua respectiva variável.

### **3. Importante:&#x20;**`input()`**&#x20;sempre retorna&#x20;**`str`

Independentemente do que o usuário digitar, a função `input()` retorna um valor do tipo `str` (texto).

Observe:

```
idade = input('Digite sua idade: ')

print(idade)
print(type(idade))
```

**Exemplo de execução:**

```
Digite sua idade: 27
27
<class 'str'>
```

Mesmo digitando `27`, o Python armazena o valor como texto.

Se quisermos utilizar essa informação em cálculos matemáticos, precisaremos converter o tipo de dado.

Por exemplo:

```
idade = int(input('Digite sua idade: '))

print(idade)
print(type(idade))
```

**Exemplo de execução:**

```
Digite sua idade: 27
27
<class 'int'>
```

Nesse caso, utilizamos `int()` para converter o valor recebido para inteiro.

Também podemos utilizar `float()` quando esperamos receber números decimais:

```
preco = float(input('Digite o preço: '))

print(preco)
print(type(preco))
```

**Exemplo de execução:**

```
Digite o preço: 29.90
29.9
<class 'float'>
```

### **Resumo**

- `input()` recebe informações digitadas pelo usuário.
- Podemos armazenar o conteúdo recebido em variáveis.
- A função sempre retorna um valor do tipo `str`.
- Para realizar cálculos com os valores recebidos, podemos utilizar `int()` ou `float()`, conforme necessário.
