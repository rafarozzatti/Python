## **Comentários**

Comentários são trechos de texto escritos no código para explicar o que ele faz, registrar observações ou facilitar a leitura.

**O Python não executa os comentários.** Eles são ignorados durante a execução do programa.

### **1. Comentários de uma linha**

Para criar um comentário, utilizamos o símbolo `#`.

```
# Exibe uma mensagem na tela
print('Olá, mundo!')
```

**Resultado:**

```
Olá, mundo!
```

Tudo o que estiver depois de `#` na mesma linha será considerado comentário.

Também podemos escrever comentários ao lado de um comando:

```
idade = 27  # Armazena a idade
print(idade)
```

**Resultado:**

```
27
```

### **2. Comentários em várias linhas**

Não existe uma sintaxe específica de comentário de múltiplas linhas em Python. Uma forma comum é utilizar `#` em cada linha:

```
# Este programa calcula
# a soma de dois números
# e exibe o resultado.

numero1 = 10
numero2 = 20

print(numero1 + numero2)
```

**Resultado:**

```
30
```

### **3. Aspas triplas não são comentários propriamente ditos**

Você também pode encontrar textos escritos entre três aspas simples (`'''`) ou duplas (`"""`):

```
"""Este programa realizauma soma entre dois números."""
numero1 = 10
numero2 = 20

print(numero1 + numero2)
```

Esse trecho é, tecnicamente, uma string de várias linhas, não um comentário. Quando colocado no início de um módulo, função ou classe, pode funcionar como uma *docstring*, utilizada para documentar o código.

### **4. Boas práticas**

- Explique trechos que não sejam óbvios.
- Evite comentar cada linha desnecessariamente.
- Mantenha os comentários objetivos e atualizados.
- Não utilize comentários para substituir nomes claros de variáveis.
