## **Condições dentro de outras condições**

As **condições aninhadas** acontecem quando colocamos uma estrutura condicional (`if`, `elif` ou `else`) dentro de outra estrutura condicional.

Elas permitem realizar verificações adicionais dependendo do resultado de uma condição anterior.

### **1. Estrutura básica**

```
if condição_1:    
    if condição_2:        
        print('As duas condições foram atendidas')    
    else:        
        print('A primeira condição foi atendida, mas a segunda não')
else:    
    print('A primeira condição não foi atendida')
```

Observe a identação: o segundo `if` está dentro do primeiro. Isso significa que ele só será executado se a primeira condição for verdadeira.

### **2. Exemplo prático**

Imagine um sistema que verifica se uma pessoa pode dirigir.

Para isso:

- Primeiro, verifica se a pessoa tem 18 anos ou mais.
- Depois, verifica se ela possui carteira de habilitação.

```
idade = 20
possui_carteira = True

if idade >= 18:    
    if possui_carteira:        
        print('Pode dirigir')    
    else:        
        print('Precisa de habilitação')
else:    
    print('Menor de idade')
```

**Resultado:**

```
Pode dirigir
```

Como a idade atende ao requisito, o programa realiza a segunda verificação.

### **3. Utilizando mais de uma condição aninhada**

Também podemos colocar várias verificações dentro de uma estrutura condicional.

```
nota = 8
frequencia = 85

if nota >= 7:    
    if frequencia >= 75:        
        print('Aprovado')    
    else:        
        print('Reprovado por frequência')
else:    
    print('Reprovado por nota')
```

**Resultado:**

```
Aprovado
```

Nesse caso:

1. O programa verifica se a nota é maior ou igual a 7.
2. Se for, verifica se a frequência é maior ou igual a 75.
3. Se ambas forem atendidas, o aluno será aprovado.
4. Caso a frequência não seja suficiente, será reprovado por frequência.
5. Caso a nota não seja suficiente, será reprovado por nota.

### **4. Diferença entre condições aninhadas e sequenciais**

**Condições aninhadas:** uma condição depende da outra para ser executada.

```
idade = 20

if idade >= 18:    
    if idade >= 21:        
        print('Pode entrar em qualquer área')    
    else:        
        print('Acesso permitido somente para maiores de 18')
```

**Condições sequenciais:** são verificações independentes, executadas uma após a outra.

```
idade = 20

if idade >= 18:    
    print('Maior de idade')
if idade >= 21:    
    print('Tem 21 anos ou mais')
```

A diferença principal é que, nas condições aninhadas, a segunda verificação está dentro do bloco da primeira. Nas sequenciais, cada `if` é independente.
