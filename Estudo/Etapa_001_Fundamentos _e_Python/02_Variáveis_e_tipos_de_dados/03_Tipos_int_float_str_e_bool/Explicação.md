## **Tipos&#x20;**`int`**,&#x20;**`float`**,&#x20;**`str`**&#x20;e&#x20;**`bool`

Em Python, toda variável armazena um valor que possui um determinado tipo de dado.

Os quatro tipos básicos que estamos estudando são:

| Tipo    | Representa       | Exemplos               |
| ------- | ---------------- | ---------------------- |
| `int`   | Números inteiros | `10`, `25`, `-5`       |
| `float` | Números decimais | `10.5`, `3.14`, `-2.7` |
| `str`   | Textos           | `'Rafael'`, `'Python'` |
| `bool`  | Valores lógicos  | `True`, `False`        |

### **1. Tipo&#x20;**`int`**&#x20;— Números inteiros**

Representa números sem casas decimais, incluindo positivos, negativos e zero.

```
idade = 27
quantidade = 150
temperatura = -5

print(idade)
print(quantidade)
print(temperatura)
```

**Resultado:**

```
27
150
-5
```

É bastante utilizado para representar quantidades, contagens e números de registros.

### **2. Tipo&#x20;**`float`**&#x20;— Números decimais**

Representa números que possuem casas decimais.

Em Python, utilizamos o ponto (`.`) como separador decimal, e não a vírgula.

```
preco = 29.90
altura = 1.75
media = 8.5

print(preco)
print(altura)
print(media)
```

**Resultado:**

```
29.9
1.75
8.5
```

Observe que Python não necessariamente mantém zeros à direita. Por isso, `29.90` é exibido como `29.9`, mas o valor numérico é equivalente.

É utilizado para representar preços, médias, medidas, percentuais e outras informações decimais.

### **3. Tipo&#x20;**`str`**&#x20;— Textos**

Representa sequências de caracteres, como palavras, frases, nomes e códigos.

Para criar uma string, utilizamos aspas simples (`' '`) ou duplas (`" "`).

```
nome = 'Rafael'
cidade = "São Paulo"
mensagem = 'Estou aprendendo Python'

print(nome)
print(cidade)
print(mensagem)
```

**Resultado:**

```
Rafael
São Paulo
Estou aprendendo Python
```

Uma observação importante: mesmo que um valor contenha apenas números, ele será considerado texto se estiver entre aspas.

```
numero = 100
codigo = '100'

print(numero)
print(codigo)
```

**Resultado:**

```
100
100
```

Apesar de apresentarem o mesmo resultado visual, os valores possuem tipos diferentes:

- `numero` é um inteiro (`int`).
- `codigo` é um texto (`str`).

Isso faz diferença porque podemos realizar operações matemáticas com números, mas não da mesma maneira com textos.

### **4. Tipo&#x20;**`bool`**&#x20;— Valores lógicos**

O tipo `bool` representa apenas dois valores:

- `True`: verdadeiro.
- `False`: falso.

Observe que as iniciais são maiúsculas.

```
aprovado = True
reprovado = False

print(aprovado)
print(reprovado)
```

**Resultado:**

```
True
False
```

Esse tipo é muito utilizado para representar condições e situações que podem ser verdadeiras ou falsas.

Por exemplo:

```
idade = 27

maior_de_idade = idade >= 18

print(maior_de_idade)
```

**Resultado:**

```
True
```

A expressão `idade >= 18` verifica se a idade é maior ou igual a 18. Como a condição é verdadeira, a variável recebe `True`.

### **5. Comparando os quatro tipos**

Observe este exemplo com os quatro tipos de dados:

```
nome = 'Rafael'
idade = 27
altura = 1.75
estudando = True

print(nome)
print(idade)
print(altura)
print(estudando)
```

**Resultado:**

```
Rafael
27
1.75
True
```

Embora todas sejam variáveis, cada uma armazena um tipo diferente de informação.

### **6. Aplicação em Análise de Dados**

Imagine uma tabela de vendas:

| Produto  | Quantidade | Preço   | Disponível |
| -------- | ---------- | ------- | ---------- |
| Notebook | 10         | 3500.00 | True       |
| Mouse    | 25         | 89.90   | True       |
| Teclado  | 0          | 150.00  | False      |

Em Python, poderíamos representar um registro dessa tabela assim:

```
produto = 'Notebook'
quantidade = 10
preco = 3500.00
disponivel = True
```

Cada informação utiliza um tipo adequado ao seu conteúdo.

### **Resumo geral**

`int`

Inteiro

Números sem casas decimais: `10`, `25`, `-5`.

`float`

Decimal

Números com casas decimais: `10.5`, `3.14`.

`str`

Texto

Palavras, frases e caracteres: `'Python'`, `'Rafael'`.

`bool`

Lógico

Valores verdadeiros ou falsos: `True`, `False`.
l.