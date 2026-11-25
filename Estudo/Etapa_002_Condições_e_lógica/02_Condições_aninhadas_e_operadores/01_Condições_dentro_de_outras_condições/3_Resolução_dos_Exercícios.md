## **Resolução dos Exercícios — Condições aninhadas**

### **Exercício 1**

```python
idade = 20

if idade >= 18:
    if idade >= 21:
        print('Tem 21 anos ou mais')
    else:
        print('É maior de idade, mas tem menos de 21 anos')
else:
    print('Menor de idade')
```

### **Exercício 2**

```python
nota = 8

if nota >= 7:
    if nota >= 9:
        print('Aprovado com nota excelente')
    else:
        print('Aprovado')
else:
    print('Reprovado')
```

### **Exercício 3**

```python
saldo = 1000
compra = 300

if saldo >= compra:
    if saldo > compra:
        print('Compra autorizada e há saldo restante')
    else:
        print('Compra autorizada, sem saldo restante')
else:
    print('Saldo insuficiente')
```

### **Exercício 4**

```python
temperatura = 30

if temperatura > 25:
    if temperatura > 35:
        print('Temperatura muito elevada')
    else:
        print('Temperatura elevada')
else:
    print('Temperatura normal')
```

### **Exercício 5**

```python
idade = 17

if idade >= 18:
    if idade >= 60:
        print('Pessoa idosa')
    else:
        print('Pessoa adulta')
else:
    print('Menor de idade')
```

### **Exercício 6**

```python
nota = 6
frequencia = 80

if nota >= 5:
    if frequencia >= 75:
        print('Aluno aprovado')
    else:
        print('Reprovado por frequência')
else:
    print('Reprovado por nota')
```

### **Exercício 7**

```python
idade = 25
renda = 3500

if idade >= 18:
    if renda >= 3000:
        print('Crédito aprovado')
    else:
        print('Renda insuficiente')
else:
    print('Não atende ao requisito de idade')
```

### **Exercício 8**

```python
numero = 10

if numero > 0:
    if numero > 5:
        print('Número positivo e maior que 5')
    else:
        print('Número positivo, mas menor ou igual a 5')
else:
    print('Número não positivo')
```

### **Exercício 9**

```python
idade = 22
possui_ingresso = True

if idade >= 18:
    if possui_ingresso:
        print('Entrada permitida')
    else:
        print('Precisa de ingresso')
else:
    print('Entrada não permitida')
```

### **Exercício 10**

```python
salario = 4000
tempo_empresa = 3

if salario >= 3000:
    if tempo_empresa >= 2:
        print('Funcionário atende aos dois requisitos')
    else:
        print('Tempo de empresa insuficiente')
else:
    print('Salário abaixo do requisito')
```
