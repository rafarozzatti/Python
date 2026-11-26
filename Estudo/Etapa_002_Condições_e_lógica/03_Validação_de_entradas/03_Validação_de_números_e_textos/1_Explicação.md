# **Validação de números e textos**

### **1. Validação de números inteiros (**`int`**)**

Números inteiros são aqueles que não possuem casas decimais.

Podemos verificar se um número está dentro de determinado intervalo ou atende a uma regra.

**Exemplo: quantidade de funcionários**

```python
quantidade = int(input('Digite a quantidade de funcionários: '))

if quantidade >= 1 and quantidade <= 100:    
    print('Quantidade aceita')
else:    
    print('Quantidade fora do limite')
```

Nesse exemplo, o programa aceita quantidades entre 1 e 100.

### **2. Validação de números decimais (**`float`**)**

Números decimais são utilizados em situações como preços, salários, notas e porcentagens.

**Exemplo: validação de preço**

```python
preco = float(input('Digite o preço: '))

if preco > 0:    
    print('Preço aceito')
else:    
    print('Preço inválido')
```

O programa verifica se o preço é maior que zero.

### **3. Validação de textos (**`str`**)**

Também podemos verificar características de textos utilizando operadores e métodos de strings.

**Exemplo 1: verificar se um texto está vazio**

```python
nome = input('Digite seu nome: ')

if nome == '':    
    print('Nome não informado')
else:    
    print('Nome informado')
```

**Exemplo 2: verificar se existem apenas espaços**

```python
nome = input('Digite seu nome: ')

if nome.strip() == '':    
    print('Nome não informado')
else:    
    print('Nome informado')
```

O método `strip()` remove os espaços existentes no início e no final do texto. Assim, conseguimos identificar uma entrada que contém somente espaços.

### **4. Verificação do tamanho de um texto com&#x20;**`len()`

A função `len()` retorna a quantidade de caracteres de um texto.

Podemos utilizá-la para verificar se uma informação possui o tamanho esperado.

**Exemplo: senha**

```python
senha = input('Digite sua senha: ')

if len(senha) >= 8:    
    print('Senha aceita')
else:    
    print('Senha muito curta')
```

Nesse exemplo, a senha precisa ter pelo menos oito caracteres.

Observe que os espaços também são considerados caracteres.

### **5. Verificação de conteúdo com&#x20;**`in`

Podemos verificar se determinado caractere ou texto está presente em uma string utilizando `in`.

**Exemplo: verificar se um e-mail contém&#x20;**`@`

```python
email = input('Digite seu e-mail: ')

if '@' in email:    
    print('E-mail contém o caractere @')
else:    
    print('E-mail não contém o caractere @')
```

O operador `in` verifica se um elemento está presente dentro de outro.

Essa verificação é simples e não garante que o e-mail seja válido, apenas que contém o caractere informado.

## **Resumo**

| Recurso   | Utilização                                      |
| --------- | ----------------------------------------------- |
| `int()`   | Trabalhar com números inteiros                  |
| `float()` | Trabalhar com números decimais                  |
| `strip()` | Remover espaços das extremidades de textos      |
| `len()`   | Contar caracteres                               |
| `in`      | Verificar se um conteúdo está presente em outro |
| `== ''`   | Verificar se um texto está vazio                |
