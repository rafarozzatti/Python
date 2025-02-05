# Funções em Python

## **O que são funções?**
Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas ajudam a organizar e reutilizar código de maneira eficiente.

---

## **Criando uma função**
Podemos criar uma função em Python usando a palavra-chave `def`.

### **Exemplo de função simples:**
```python
# Definição da função que exibe uma mensagem
def saudacao():
    print("Olá! Bem-vindo ao Python!")

# Chamando a função
saudacao()
```
**Saída:**
```
Olá! Bem-vindo ao Python!
```

---

## **Parâmetros e Argumentos**
As funções podem receber valores chamados **parâmetros**.

### **Exemplo com um parâmetro:**
```python
# Função que recebe um nome e exibe uma mensagem personalizada
def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo ao Python!")

# Chamando a função com um argumento
saudacao("Lucas")
```
**Saída:**
```
Olá, Lucas! Bem-vindo ao Python!
```

### **Exemplo com dois parâmetros:**
```python
# Função que soma dois números
def soma(a, b):
    return a + b  # Retorna a soma dos dois valores

# Chamando a função e armazenando o resultado
resultado = soma(3, 5)
print(resultado)
```
**Saída:**
```
8
```

---

## **Parâmetros com valor padrão**
Podemos definir valores padrão para parâmetros, tornando-os opcionais ao chamar a função.

### **Exemplo com parâmetro padrão:**
```python
# Função que exibe uma mensagem com um nome padrão
def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")

# Chamadas da função
saudacao()  # Usa o valor padrão
saudacao("Ana")  # Substitui o valor padrão
```
**Saída:**
```
Olá, Visitante!
Olá, Ana!
```

---

## **Funções com número variável de argumentos**
Em algumas situações, não sabemos quantos argumentos serão passados. Podemos usar `*args` para aceitar um número variável de argumentos posicionais.

### **Exemplo usando `*args`:**
```python
# Função que soma vários números
def soma(*numeros):
    return sum(numeros)  # Retorna a soma de todos os argumentos

# Chamando a função com diferentes quantidades de argumentos
print(soma(1, 2, 3))      # 6
print(soma(10, 20, 30, 40))  # 100
```

Podemos também usar `**kwargs` para aceitar um número variável de argumentos nomeados.

### **Exemplo usando `**kwargs`:**
```python
# Função que exibe informações sobre uma pessoa
def exibir_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

# Chamando a função com argumentos nomeados
exibir_info(nome="Carlos", idade=30, cidade="São Paulo")
```
**Saída:**
```
nome: Carlos
idade: 30
cidade: São Paulo
```

---

## **Funções Anônimas (`lambda`)**
Funções `lambda` são funções anônimas que são definidas em uma única linha.

### **Exemplo de `lambda`:**
```python
# Função lambda que multiplica um número por 2
multiplicar = lambda x: x * 2

# Chamando a função lambda
print(multiplicar(5))
```
**Saída:**
```
10
```

Funções `lambda` são úteis para operações simples, como argumentos para `map()`, `filter()` e `sorted()`.

### **Exemplo usando `lambda` com `sorted()`:**
```python
# Lista de tuplas (produto, preço)
produtos = [("Celular", 1500), ("Notebook", 3500), ("Fone de Ouvido", 200)]

# Ordena os produtos pelo preço usando lambda
produtos_ordenados = sorted(produtos, key=lambda produto: produto[1])

# Impressão dos produtos ordenados
print(produtos_ordenados)
```
**Saída:**
```
[("Fone de Ouvido", 200), ("Celular", 1500), ("Notebook", 3500)]
```

---

## **Conclusão**
Funções são essenciais para organizar e reutilizar código em Python. Dependendo da necessidade, podemos usar:

- **Funções normais (`def`)** para código reutilizável e estruturado.
- **Parâmetros e argumentos** para tornar funções flexíveis.
- **`*args` e `**kwargs`** para aceitar um número variável de argumentos.
- **Funções `lambda`** para operações curtas e diretas.
