## **Identação e blocos condicionais**

### **1. O que é identação?**

A **identação** é o espaço utilizado no início de uma linha de código para indicar que ela pertence a um determinado bloco.

Em Python, a identação é obrigatória para definir a organização e a hierarquia do código.

Normalmente, utilizamos **4 espaços** para cada nível de identação.

Exemplo:

```
idade = 20

if idade >= 18:    
    print('Maior de idade')    
    print('Acesso permitido')

print('Programa finalizado')
```

Resultado:

```
Maior de idade
Acesso permitido
Programa finalizado
```

Observe que os dois primeiros `print()` possuem 4 espaços no início. Isso indica que pertencem ao bloco do `if`.

O último `print()` não possui identação, portanto está fora do bloco condicional.

### **2. Organização dos blocos condicionais**

As estruturas `if`, `elif` e `else` utilizam dois pontos (`:`) para indicar o início de um bloco.

As instruções pertencentes a esse bloco precisam ter a mesma identação.

Exemplo:

```
nota = 8

if nota >= 7:    
    print('Aprovado')    
    print('Parabéns!')
else:    
    print('Reprovado')    
    print('Estude mais')
```

Resultado:

```
Aprovado
Parabéns!
```

Nesse exemplo:

- Os dois `print()` dentro do `if` possuem a mesma identação.
- Os dois `print()` dentro do `else` também possuem a mesma identação.
- `if` e `else` começam no mesmo nível, pois pertencem à mesma estrutura condicional.

### **3. Blocos condicionais aninhados**

Também podemos colocar uma estrutura condicional dentro de outra.

Isso é chamado de **condicional aninhada**.

Exemplo:

```
idade = 20
possui_carteira = True

if idade >= 18:    
    if possui_carteira:        
        print('Pode dirigir') 
    else:        
        print('Precisa tirar a habilitação')
else:    
    print('Menor de idade')
```

Resultado:

```
Pode dirigir
```

Observe os níveis de identação:

- Primeiro nível: `if idade >= 18`.
- Segundo nível: `if possui_carteira` e seu `else`.
- O último `else` pertence ao primeiro `if`.

A identação permite identificar exatamente a qual estrutura cada bloco pertence.

### **4. Erros comuns de identação**

**Erro 1 — Não utilizar identação**

```
idade = 20

if idade >= 18:
print('Maior de idade')
```

Resultado:

```
IndentationError
```

O `print()` deveria estar identado porque pertence ao bloco do `if`.

**Erro 2 — Utilizar identações diferentes no mesmo bloco**

```
idade = 20

if idade >= 18:    
    print('Maior de idade')        
        print('Acesso permitido')
```

Resultado:

```
IndentationError
```

As duas instruções deveriam possuir o mesmo nível de identação.

**Erro 3 — Misturar espaços e tabulações**

Python pode apresentar erros quando utilizamos espaços e tabulações de maneira inconsistente.

Por isso, o recomendado é utilizar sempre 4 espaços por nível de identação.

### **Resumo**

- Identação define a organização e a hierarquia dos blocos de código.
- Python utiliza identação para identificar quais instruções pertencem a cada estrutura.
- O padrão recomendado é utilizar 4 espaços.
- Instruções do mesmo bloco devem possuir a mesma identação.
- Condicionais aninhadas possuem diferentes níveis de identação.
