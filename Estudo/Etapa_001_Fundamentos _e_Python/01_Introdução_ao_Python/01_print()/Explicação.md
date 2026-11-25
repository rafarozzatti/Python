## **Função&#x20;**`print()`

A função `print()` é utilizada para **exibir informações na tela**, como textos, números, variáveis e resultados de operações.

É uma das funções mais utilizadas em Python.

### **1. Exibindo textos**

Para exibir textos, utilizamos aspas simples (`' '`) ou duplas (`" "`).

```
print('Olá, mundo!')
print("Estou aprendendo Python.")
```

Resultado:

```
Olá, mundo!
Estou aprendendo Python.
```

As duas formas funcionam da mesma maneira.

### **2. Exibindo números**

Podemos utilizar `print()` para apresentar números inteiros e decimais sem precisar colocá-los entre aspas.

```
print(10)
print(25.5)
```

Resultado:

```
10
25.5
```

**Atenção à diferença:**

```
print(10)
print('10')
```

Resultado:

```
10
10
```

Visualmente, o resultado é igual, mas os tipos são diferentes:

- `10` é um número inteiro.
- `'10'` é um texto.

### **3. Exibindo variáveis**

Também podemos utilizar `print()` para apresentar o conteúdo armazenado em variáveis.

```
nome = 'Rafael'
idade = 27

print(nome)
print(idade)
```

Resultado:

```
Rafael
27
```

### **4. Exibindo vários valores**

Podemos utilizar vírgulas para apresentar diferentes valores em uma mesma chamada de `print()`.

```
nome = 'Rafael'
idade = 27

print('Nome:', nome, 'Idade:', idade)
```

Resultado:

```
Nome: Rafael Idade: 27
```

Por padrão, o `print()` separa os valores com um espaço.

### **5. Parâmetro&#x20;**`sep`

O parâmetro `sep` permite definir qual separador será utilizado entre os valores apresentados.

Por padrão, ele utiliza um espaço (`' '`).

Exemplo:

```
print('2026', '11', '25', sep='/')
```

Resultado:

```
2026/11/25
```

Outro exemplo:

```
print('Python', 'SQL', 'Power BI', sep=' | ')
```

Resultado:

```
Python | SQL | Power BI
```

### **6. Parâmetro&#x20;**`end`

Por padrão, cada chamada de `print()` termina com uma quebra de linha.

O parâmetro `end` permite alterar esse comportamento.

Exemplo:

```
print('Olá', end=' ')
print('mundo!')
```

Resultado:

```
Olá mundo!
```

Outro exemplo:

```
print('Python', end=' - ')
print('Análise de Dados')
```

Resultado:

```
Python - Análise de Dados
```

Também podemos utilizar `end=''` para não adicionar nenhum caractere ao final.

### **7. Quebras de linha com&#x20;**`\n`

O caractere especial `\n` permite inserir uma quebra de linha dentro de um texto.

Exemplo:

```
print('Nome: Rafael\nIdade: 27\nProfissão: Analista de Dados')
```

Resultado:

```
Nome: Rafael
Idade: 27
Profissão: Analista de Dados
```

### **Resumo**

| Recurso   | Utilização                          |
| --------- | ----------------------------------- |
| `print()` | Exibe informações                   |
| `sep`     | Define o separador entre valores    |
| `end`     | Define o que será colocado ao final |
| `\n`      | Insere uma quebra de linha          |
