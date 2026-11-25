## **F-strings**

F-strings são uma forma de inserir variáveis e expressões diretamente dentro de textos.

Elas facilitam a construção de mensagens, evitando a necessidade de utilizar concatenação com `+` ou converter números manualmente com `str()`.

Para utilizar uma f-string, colocamos a letra `f` antes das aspas e inserimos as variáveis entre chaves `{}`.

### **1. Inserindo variáveis em textos**

```
nome = 'Rafael'
idade = 27

print(f'Meu nome é {nome} e tenho {idade} anos.')
```

**Resultado:**

```
Meu nome é Rafael e tenho 27 anos.
```

Observe que:

- A letra `f` aparece antes das aspas.
- As variáveis ficam dentro de `{}`.
- O Python substitui as variáveis pelos valores armazenados.

### **2. Inserindo várias variáveis**

Podemos inserir quantas variáveis forem necessárias dentro de uma f-string.

```
produto = 'Notebook'
quantidade = 5
preco = 3500.00

print(f'Produto: {produto}')
print(f'Quantidade: {quantidade}')
print(f'Preço: R$ {preco}')
```

**Resultado:**

```
Produto: Notebook
Quantidade: 5
Preço: R$ 3500.0
```

### **3. Utilizando expressões matemáticas**

Também podemos realizar operações diretamente dentro das chaves.

```
numero1 = 10
numero2 = 20

print(f'A soma é {numero1 + numero2}.')
```

**Resultado:**

```
A soma é 30.
```

Outro exemplo:

```
preco = 100
desconto = 20

print(f'Preço final: R$ {preco - desconto}')
```

**Resultado:**

```
Preço final: R$ 80
```

### **4. Formatando números decimais**

As f-strings também permitem controlar a quantidade de casas decimais exibidas.

Utilizamos `:.2f` para apresentar um número com duas casas decimais.

```
preco = 29.9

print(f'Preço: R$ {preco:.2f}')
```

**Resultado:**

```
Preço: R$ 29.90
```

Outros exemplos:

```
numero = 10.56789

print(f'{numero:.1f}')
print(f'{numero:.2f}')
print(f'{numero:.3f}')
```

**Resultado:**

```
10.6
10.57
10.568
```

O Python arredonda o valor exibido de acordo com a quantidade de casas decimais solicitada. A variável original não é alterada.

### **5. Comparando concatenação e f-strings**

Observe como podemos produzir a mesma mensagem das duas maneiras:

**Utilizando concatenação:**

```
nome = 'Rafael'
idade = 27

print('Meu nome é ' + nome + ' e tenho ' + str(idade) + ' anos.')
```

**Utilizando f-string:**

```
nome = 'Rafael'
idade = 27

print(f'Meu nome é {nome} e tenho {idade} anos.')
```

**Resultado dos dois exemplos:**

```
Meu nome é Rafael e tenho 27 anos.
```

A f-string deixa o código mais simples e legível, principalmente quando trabalhamos com várias variáveis.

### **Resumo**

| Recurso        | Utilização                     |
| -------------- | ------------------------------ |
| `f'...'`       | Cria uma f-string              |
| `{variavel}`   | Insere o valor de uma variável |
| `{expressao}`  | Executa uma expressão          |
| `{numero:.2f}` | Exibe duas casas decimais      |
