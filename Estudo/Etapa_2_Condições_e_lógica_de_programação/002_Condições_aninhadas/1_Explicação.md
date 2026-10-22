# 2. Condições aninhadas

Condições aninhadas são estruturas condicionais colocadas dentro de outras estruturas condicionais.

Ou seja, você utiliza um `if` dentro de outro `if`, por exemplo, para verificar uma segunda condição somente depois que a primeira for verdadeira.

## 1.1. Exemplo básico

Imagine que queremos verificar se uma pessoa pode entrar em um evento. Primeiro, ela precisa ter 18 anos ou mais. Depois, precisamos verificar se possui ingresso.

```
idade = 20
tem_ingresso = True

if idade >= 18:    
    if tem_ingresso:       
        print('Entrada permitida')
```

Saída:

```
Entrada permitida
```

Vamos entender a execução:

1. `if idade >= 18:` verifica se a pessoa tem pelo menos 18 anos.
2. Como a condição é verdadeira, o Python entra nesse bloco.
3. `if tem_ingresso:` verifica se a pessoa possui ingresso.
4. Como `tem_ingresso` é `True`, a mensagem é exibida.

Observe a indentação: o segundo `if` está dentro do primeiro, com mais quatro espaços.

## 1.2. E se a primeira condição for falsa?

Veja este exemplo:

```
idade = 16
tem_ingresso = True

if idade >= 18:    
    if tem_ingresso:        
        print('Entrada permitida')
```

Saída: nenhuma mensagem.

Mesmo tendo ingresso, a pessoa não passa pela primeira condição. Por isso, o segundo `if` nem chega a ser executado.

## 1.3. Condições aninhadas com `else`

Também podemos usar `else` dentro de um `if` aninhado.

```
idade = 20
tem_ingresso = False

if idade >= 18:    
    if tem_ingresso:        
        print('Entrada permitida')    
    else:        
        print('Você precisa de um ingresso')
else:    
    print('Você precisa ter pelo menos 18 anos')
```

Saída:

```
Você precisa de um ingresso
```

O `else` mais interno corresponde ao `if tem_ingresso`. Já o `else` mais externo corresponde ao `if idade >= 18`.

Essa relação depende da indentação: o `else` pertence ao `if` que está alinhado com ele.
