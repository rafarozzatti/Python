## **Concatenação**

Concatenação é o processo de juntar dois ou mais textos em uma única sequência.

Em Python, podemos realizar concatenação utilizando o operador `+`.

### **1. Concatenando textos**

Podemos juntar textos diretamente:

```
print('Olá' + ' ' + 'mundo!')
```

**Resultado:**

```
Olá mundo!
```

Observe que adicionamos um espaço entre os textos para que as palavras não fiquem juntas.

### **2. Concatenando variáveis**

Também podemos juntar variáveis que armazenam textos.

```
nome = 'Rafael'
sobrenome = 'Rozzatti'

nome_completo = nome + ' ' + sobrenome

print(nome_completo)
```

**Resultado:**

```
Rafael Rozzatti
```

Nesse exemplo, criamos uma nova variável chamada `nome_completo`, que recebe a junção das outras duas.

### **3. Concatenando textos com variáveis**

Podemos combinar textos fixos com variáveis.

```
nome = 'Rafael'
cidade = 'São Paulo'

print('Meu nome é ' + nome + ' e moro em ' + cidade + '.')
```

**Resultado:**

```
Meu nome é Rafael e moro em São Paulo.
```

### **4. Concatenando números com textos**

Aqui precisamos ter atenção.

O operador `+` pode juntar textos, mas não podemos utilizá-lo diretamente para juntar um texto com um número.

**Exemplo que gera erro:**

```
idade = 27

print('Minha idade é ' + idade)
```

**Resultado:**

```
TypeError: can only concatenate str (not "int") to str
```

Isso acontece porque `idade` é um número inteiro (`int`), enquanto o restante é texto (`str`).

Para resolver, podemos converter o número para texto utilizando `str()`:

```
idade = 27

print('Minha idade é ' + str(idade))
```

**Resultado:**

```
Minha idade é 27
```

### **5. Diferença entre concatenação e soma**

É importante entender que o operador `+` pode ter funções diferentes dependendo dos tipos de dados.

**Com números, realiza uma soma:**

```
print(10 + 20)
```

Resultado:

```
30
```

**Com textos, realiza uma concatenação:**

```
print('10' + '20')
```

Resultado:

```
1020
```

Observe que, no segundo exemplo, os valores estão entre aspas. Portanto, são textos, não números.

### **Resumo**

- Concatenação significa juntar textos.
- Utilizamos o operador `+` para concatenar.
- Podemos juntar textos diretamente ou por meio de variáveis.
- Para concatenar números com textos, precisamos converter os números para `str()`.
- O operador `+` realiza soma entre números e concatenação entre textos.
