## **Utilizando operadores lógicos em condições aninhadas**

Podemos utilizar `and`, `or` e `not` dentro de um `if` que já está dentro de outro `if`.

### **1. Condição aninhada com&#x20;**`and`

Imagine que uma empresa exige que o funcionário tenha pelo menos 18 anos e renda de R$ 3.000 para solicitar crédito.

```
idade = 25
renda = 4000

if idade >= 18:    
    if renda >= 3000 and renda <= 10000:        
        print('Crédito aprovado')    
    else:        
        print('Renda fora dos critérios')
else:    
    print('Idade insuficiente')
```

**Resultado:**

```
Crédito aprovado
```

O primeiro `if` verifica a idade. Dentro dele, o segundo `if` utiliza `and` para verificar se a renda está dentro do intervalo exigido.

As duas condições da segunda verificação precisam ser verdadeiras.

### **2. Condição aninhada com&#x20;**`or`

Imagine que um aluno precisa ter nota mínima 7 ou possuir uma aprovação especial para ser aprovado.

```
nota = 6
aprovacao_especial = True

if nota >= 5:    
    if nota >= 7 or aprovacao_especial:        
        print('Aprovado')    
    else:        
        print('Em recuperação')
else:    
    print('Reprovado')
```

**Resultado:**

```
Aprovado
```

O primeiro `if` verifica se a nota é pelo menos 5. Dentro dele, o `or` permite a aprovação se pelo menos uma das condições for verdadeira.

### **3. Condição aninhada com&#x20;**`not`

Imagine que um usuário precisa ser maior de idade e não pode estar bloqueado para acessar um sistema.

```
idade = 25
bloqueado = False

if idade >= 18:    
    if not bloqueado:        
        print('Acesso permitido')    
    else:        
        print('Usuário bloqueado')
else:    
    print('Idade insuficiente')
```

**Resultado:**

```
Acesso permitido
```

O primeiro `if` verifica a idade. O segundo utiliza `not` para verificar se o usuário não está bloqueado.

### **4. Combinação dos operadores em condições aninhadas**

Podemos utilizar mais de um operador lógico na mesma condição.

```
idade = 25
renda = 4000
bloqueado = False

if idade >= 18:    
    if renda >= 3000 and not bloqueado:        
        print('Crédito aprovado')    
    else:        
        print('Crédito negado')
else:    
    print('Idade insuficiente')
```

**Resultado:**

```
Crédito aprovado
```

Nesse exemplo:

1. O primeiro `if` verifica a idade.
2. O segundo verifica se a renda é suficiente **e** se o usuário não está bloqueado.
3. Somente se as duas condições forem verdadeiras, o crédito será aprovado.
