# **. O que são funções?**

Uma função é um bloco de código que executa uma tarefa específica.

Imagine que precisamos exibir uma mensagem várias vezes.

Sem função:

```
print("Bem-vindo ao curso de Python!")print("Bem-vindo ao curso de Python!")print("Bem-vindo ao curso de Python!")
```

Podemos evitar essa repetição criando uma função:

```
def saudacao():    print("Bem-vindo ao curso de Python!")
```

Agora, para executar esse código, basta chamar a função:

```
saudacao()
```

Saída:

```
Bem-vindo ao curso de Python!
```

**Entenda cada parte:**

- `def`: palavra reservada utilizada para definir uma função.
- `saudacao`: nome que escolhemos para a função.
- `()`: indicam onde podemos colocar os parâmetros.
- `:`: indica o início do bloco de código.
- Indentação: identifica as instruções que pertencem à função.

Uma observação importante: **definir uma função não significa executá-la**. O código dentro dela só será executado quando fizermos a chamada, como `saudacao()`.

# **2. Funções com parâmetros**

Podemos criar funções que recebem informações para trabalhar.

Exemplo:

```
def saudacao(nome):    print(f"Olá, {nome}!")saudacao("Carlos")saudacao("Mariana")saudacao("Pedro")
```

Saída:

```
Olá, Carlos!
Olá, Mariana!
Olá, Pedro!
```

Nesse exemplo:

- `nome` é o parâmetro da função.
- `"Carlos"`, `"Mariana"` e `"Pedro"` são argumentos enviados nas chamadas.

**Diferença:**

- Parâmetro: variável definida na criação da função.
- Argumento: valor enviado quando chamamos a função.

# **3. Funções com mais de um parâmetro**

Uma função também pode receber várias informações.

```
def apresentar(nome, idade):    print(f"Nome: {nome}")    print(f"Idade: {idade}")apresentar("Rafael", 27)
```

Saída:

```
Nome: Rafael
Idade: 27
```

A ordem dos argumentos importa nesse exemplo: o primeiro valor é atribuído a `nome` e o segundo a `idade`.

Podemos ter quantos parâmetros forem necessários.

# **4. Utilizando&#x20;**`return`

Até agora, nossas funções executaram instruções com `print()`.

Mas e se quisermos que uma função faça um cálculo e devolva o resultado para utilizarmos em outra parte do programa?

Para isso, utilizamos `return`.

Exemplo:

```
def somar(a, b):    resultado = a + b    return resultadototal = somar(10, 20)print(total)
```

Saída:

```
30
```

Observe o funcionamento:

1. Chamamos `somar(10, 20)`.
2. Os valores são recebidos pelos parâmetros `a` e `b`.
3. A função calcula `10 + 20`.
4. `return` devolve o resultado.
5. O resultado é armazenado na variável `total`.

**Diferença entre&#x20;**`print()`**&#x20;e&#x20;**`return`**:**

- `print()`: mostra uma informação na tela.
- `return`: devolve um valor para quem chamou a função.

Essa diferença é fundamental para trabalhar com funções.

# **5. Parâmetros com valores padrão**

Podemos definir um valor padrão para um parâmetro. Assim, se não enviarmos um argumento, a função utilizará esse valor automaticamente.

Exemplo:

```
def saudacao(nome="Visitante"):    print(f"Olá, {nome}!")saudacao()saudacao("Carlos")
```

Saída:

```
Olá, Visitante!
Olá, Carlos!
```

No primeiro caso, nenhum argumento foi enviado, então a função utilizou `"Visitante"`.

No segundo, o argumento `"Carlos"` substituiu o valor padrão.

# **6. Argumentos nomeados**

Também podemos informar o nome do parâmetro ao chamar uma função.

```
def apresentar(nome, idade):    print(f"Nome: {nome}")    print(f"Idade: {idade}")apresentar(idade=25, nome="Mariana")
```

Saída:

```
Nome: Mariana
Idade: 25
```

Observe que, utilizando argumentos nomeados, podemos mudar a ordem dos argumentos na chamada.

# **7. Variáveis locais**

Uma variável criada dentro de uma função é chamada de variável local. Ela existe dentro daquela função e não pode ser acessada diretamente fora dela.

Exemplo:

```
def calcular():    resultado = 10 + 20    print(resultado)calcular()
```

Saída:

```
30
```

A variável `resultado` foi criada dentro da função. Se tentarmos executar `print(resultado)` fora dela, teremos um erro, pois essa variável não está disponível nesse escopo.

# **8. Funções sem&#x20;**`return`

Uma função não precisa obrigatoriamente utilizar `return`.

Quando uma função não possui um `return` explícito, o Python devolve automaticamente o valor `None`.

Exemplo:

```
def mostrar_mensagem():    print("Olá!")resultado = mostrar_mensagem()print(resultado)
```

Saída:

```
Olá!
None
```

Isso acontece porque a função exibe a mensagem, mas não devolve nenhum resultado.

## **Resumo para suas anotações**

| Conceito          | Utilidade                                                   |
| ----------------- | ----------------------------------------------------------- |
| `def`             | Cria uma função                                             |
| Chamada da função | Executa a função                                            |
| Parâmetro         | Recebe uma informação                                       |
| Argumento         | Valor enviado à função                                      |
| `return`          | Devolve um resultado                                        |
| Valor padrão      | Define um argumento utilizado quando nenhum valor é enviado |
| Argumento nomeado | Informa o nome do parâmetro na chamada                      |
| Variável local    | Existe dentro da função                                     |

**Uma diferença que você precisa guardar:**

```
# Exibe o resultadodef somar(a, b):    print(a + b)# Devolve o resultadodef somar(a, b):    return a + b
```

A segunda versão permite armazenar o resultado, utilizá-lo em cálculos e passá-lo para outras funções.
