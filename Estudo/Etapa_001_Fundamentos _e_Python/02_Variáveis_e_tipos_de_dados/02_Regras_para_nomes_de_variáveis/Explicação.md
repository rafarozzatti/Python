## **Regras para nomes de variáveis**

Em Python, podemos escolher os nomes das variáveis, mas existem algumas regras que precisam ser respeitadas.

Além das regras obrigatórias, existem convenções que ajudam a deixar o código mais organizado e fácil de entender.

### **1. Regras obrigatórias**

**Regra 1 — Não começar com números**

```
# Incorreto
2nome = 'Rafael'

# Correto
nome2 = 'Rafael'
```

O nome pode conter números, mas nunca começar com eles.

**Regra 2 — Não utilizar espaços**

```
# Incorreto
nome completo = 'Rafael Rozzatti'

# Correto
nome_completo = 'Rafael Rozzatti'
```

Para separar palavras, utilizamos o caractere `_` (underline).

**Regra 3 — Não utilizar caracteres especiais**

Nomes de variáveis não podem conter caracteres como `@`, `!`, `#`, `%` e `-`.

```
# Incorreto
nome-completo = 'Rafael'

# Correto
nome_completo = 'Rafael'
```

**Regra 4 — Diferenciar letras maiúsculas e minúsculas**

Python diferencia letras maiúsculas de minúsculas. Portanto, os nomes abaixo representam variáveis diferentes:

```
nome = 'Rafael'
Nome = 'Carlos'
NOME = 'Mariana'

print(nome)
print(Nome)
print(NOME)
```

**Resultado:**

```
Rafael
Carlos
Mariana
```

### **2. Palavras reservadas**

Python possui palavras reservadas que já têm funções específicas na linguagem. Por isso, não podemos utilizá-las como nomes de variáveis.

Alguns exemplos:

- `if`
- `else`
- `for`
- `while`
- `class`
- `def`
- `return`
- `import`
- `True`
- `False`

Exemplo incorreto:

```
if = 10
```

O código gera um erro porque `if` é uma palavra reservada.

### **3. Convenções para bons nomes**

Além das regras obrigatórias, existem boas práticas para escolher nomes.

**Utilize nomes descritivos:**

```
# Pouco descritivo
x = 1500

# Mais descritivo
salario = 1500
```

**Utilize snake_case:**

Em Python, a convenção mais comum é escrever nomes com letras minúsculas e separar palavras com `_`.

```
nome_completo = 'Rafael Rozzatti'
data_nascimento = '15/08/1999'
total_vendas = 5000
```

**Evite nomes muito genéricos:**

```
# Pouco descritivo
a = 100
b = 200

# Mais descritivo
preco = 100
desconto = 200
```

### **Resumo**

| Regra                               | Exemplo                     |
| ----------------------------------- | --------------------------- |
| Não começar com números             | `nome2`                     |
| Não utilizar espaços                | `nome_completo`             |
| Não utilizar caracteres especiais   | `total_vendas`              |
| Diferenciar maiúsculas e minúsculas | `nome` e `Nome`             |
| Não utilizar palavras reservadas    | Evitar `if`, `for`, `class` |
| Preferir nomes descritivos          | `total_vendas`              |
