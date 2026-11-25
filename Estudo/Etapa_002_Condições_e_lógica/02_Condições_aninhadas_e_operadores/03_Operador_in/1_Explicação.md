## **Operador&#x20;**`in`

O operador `in` é utilizado para verificar se determinado elemento está presente em uma sequência ou coleção de dados.

Ele retorna um valor booleano:

- `True`: quando o elemento está presente.
- `False`: quando o elemento não está presente.

### **1. Utilizando&#x20;**`in`**&#x20;com strings**

Podemos verificar se uma letra ou palavra está presente dentro de uma string.

**Exemplo:**

```
nome = 'Rafael'

if 'a' in nome:    
    print('A letra está presente')
else:    
    print('A letra não está presente')
```

**Resultado:**

```
A letra está presente
```

Nesse caso, o Python verifica se a letra `'a'` aparece em algum lugar da string `nome`.

Também podemos procurar uma palavra dentro de outra string:

```
frase = 'Estou estudando Python'

if 'Python' in frase:    
    print('Palavra encontrada')
else:    
    print('Palavra não encontrada')
```

**Resultado:**

```
Palavra encontrada
```

### **2. Utilizando&#x20;**`in`**&#x20;com listas**

Podemos verificar se determinado elemento existe em uma lista.

**Exemplo:**

```
frutas = ['maçã', 'banana', 'uva']

if 'banana' in frutas:    
    print('Fruta encontrada')
else:    
    print('Fruta não encontrada')
```

**Resultado:**

```
Fruta encontrada
```

O Python verifica se `'banana'` é um dos elementos da lista.

Também podemos verificar números:

```
numeros = [10, 20, 30, 40, 50]

if 30 in numeros:    
    print('Número encontrado')
else:    
    print('Número não encontrado')
```

**Resultado:**

```
Número encontrado
```

### **3. Utilizando&#x20;**`not in`

O operador `not in` faz o contrário do `in`.

Ele verifica se determinado elemento **não está presente** em uma sequência ou coleção.

**Exemplo:**

```
frutas = ['maçã', 'banana', 'uva']

if 'laranja' not in frutas:    
    print('Fruta não encontrada')
else:    
    print('Fruta encontrada')
```

**Resultado:**

```
Fruta não encontrada
```

Nesse caso, como `'laranja'` não está na lista, a condição é verdadeira.

### **4. Utilizando&#x20;**`in`**&#x20;em condições aninhadas**

Também podemos utilizar o operador `in` dentro de uma condição aninhada.

**Exemplo:**

Uma empresa verifica primeiro se o funcionário está ativo. Depois, verifica se ele pertence a um dos setores autorizados.

```
funcionario_ativo = True
setor = 'TI'

setores_autorizados = ['TI', 'Financeiro', 'RH']

if funcionario_ativo:    
    if setor in setores_autorizados:        
        print('Acesso permitido')    
    else:        
        print('Setor não autorizado')
else:   
    print('Funcionário inativo')
```

**Resultado:**

```
Acesso permitido
```

Observe que o operador `in` é utilizado dentro do segundo `if`, verificando se o setor está presente na lista.
