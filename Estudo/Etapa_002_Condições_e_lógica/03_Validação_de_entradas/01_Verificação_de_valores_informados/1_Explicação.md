# **Verificação de valores informados**

A verificação de valores consiste em **conferir se uma informação fornecida pelo usuário atende a uma determinada condição**.

Em Python, fazemos isso utilizando principalmente as estruturas condicionais `if`, `elif` e `else`, que já estudamos.

### **1. Verificando um valor numérico**

Imagine que um sistema solicite a idade de uma pessoa e precise verificar se ela tem pelo menos 18 anos.

```python
idade = int(input('Digite sua idade: '))

if idade >= 18:    
    print('Idade igual ou superior a 18 anos')
else:    
    print('Idade inferior a 18 anos')
```

Se o usuário informar `25`, a condição `idade >= 18` será verdadeira.

Se informar `15`, será falsa.

### **2. Verificando igualdade**

Também podemos conferir se o valor informado corresponde exatamente ao esperado.

Imagine um sistema que solicita um código de acesso:

```python
codigo = int(input('Digite o código: '))

if codigo == 1234:    
    print('Código correto')
else:    
    print('Código incorreto')
```

Nesse caso, o programa compara o código informado com o número `1234`.

### **3. Verificando intervalos de valores**

Podemos verificar se um valor está dentro de uma determinada faixa utilizando duas condições combinadas com `and`.

Imagine que uma empresa considere válida uma idade entre 18 e 60 anos.

```python
idade = int(input('Digite sua idade: '))

if idade >= 18 and idade <= 60:    
    print('Idade dentro do intervalo')
else:    
    print('Idade fora do intervalo')
```

A condição só será verdadeira quando as duas comparações forem verdadeiras.

Uma alternativa seria:

```python
if 18 <= idade <= 60:    
    print('Idade dentro do intervalo')
else:    
    print('Idade fora do intervalo')
```

As duas formas produzem o mesmo resultado.

### **4. Verificando valores armazenados em variáveis**

A verificação também pode ser feita sem solicitar informações ao usuário.

```python
estoque = 15

if estoque > 0:    
    print('Produto disponível')
else:    
    print('Produto indisponível')
```

Aqui, o programa verifica diretamente o valor armazenado na variável `estoque`.
